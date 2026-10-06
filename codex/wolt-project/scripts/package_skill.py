#!/usr/bin/env python3
"""Build a deterministic transferable ZIP of the Wolt Project skill."""

from __future__ import annotations

import argparse
from datetime import date
import hashlib
import re
import stat
import zipfile
from pathlib import Path


EXCLUDED_PARTS = {"__pycache__", ".DS_Store"}
EXCLUDED_SUFFIXES = {".pyc", ".pyo"}
FIXED_TIME = (2026, 1, 1, 0, 0, 0)
MONTH_PREFIX = re.compile(r"^(0[1-9]|1[0-2])(?:\D|$)")
YEAR_PREFIX = re.compile(r"^(20\d{2})-")


def include(path: Path) -> bool:
    return not (set(path.parts) & EXCLUDED_PARTS or path.suffix in EXCLUDED_SUFFIXES)


def add_file(bundle: zipfile.ZipFile, source: Path, relative: Path) -> None:
    info = zipfile.ZipInfo(str(Path("wolt-project") / relative), FIXED_TIME)
    mode = source.stat().st_mode
    permissions = 0o755 if mode & stat.S_IXUSR else 0o644
    info.external_attr = (permissions & 0xFFFF) << 16
    info.compress_type = zipfile.ZIP_DEFLATED
    bundle.writestr(info, source.read_bytes(), compresslevel=9)


def add_bytes(bundle: zipfile.ZipFile, data: bytes, relative: Path) -> None:
    info = zipfile.ZipInfo(str(Path("wolt-project") / relative), FIXED_TIME)
    info.external_attr = (0o644 & 0xFFFF) << 16
    info.compress_type = zipfile.ZIP_DEFLATED
    bundle.writestr(info, data, compresslevel=9)


def infer_brief_label(briefs: list[Path]) -> str | None:
    if len(briefs) != 1:
        return None
    brief = briefs[0]
    if brief.is_file():
        candidates = [brief]
    else:
        source_root = brief / "source"
        search_root = source_root if source_root.is_dir() else brief
        candidates = sorted(path for path in search_root.rglob("*") if path.is_file())
    months = {match.group(1) for path in candidates if (match := MONTH_PREFIX.match(path.name))}
    if len(months) != 1:
        return None
    year = next(
        (match.group(1) for node in (brief, *brief.parents) if (match := YEAR_PREFIX.match(node.name))),
        str(date.today().year),
    )
    return f"brief-{months.pop()}-{year}"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("output_directory", help="directory that will receive ZIP and checksum")
    parser.add_argument(
        "--brief",
        action="append",
        default=[],
        help="internal-only brief file or directory to embed; may be repeated",
    )
    parser.add_argument(
        "--label",
        help="optional release label; inferred from one MM-prefixed brief when unambiguous",
    )
    args = parser.parse_args()

    skill_root = Path(__file__).resolve().parent.parent
    version = (skill_root / "VERSION").read_text(encoding="utf-8").strip()
    if not version:
        raise SystemExit("VERSION is empty")

    brief_paths = [Path(raw).expanduser().resolve() for raw in args.brief]
    for brief in brief_paths:
        if not brief.exists():
            raise SystemExit(f"Brief path does not exist: {brief}")
    label = args.label or infer_brief_label(brief_paths)
    if brief_paths and not label:
        raise SystemExit("Could not infer one brief month. Pass --label explicitly.")
    if label and not re.fullmatch(r"[a-z0-9][a-z0-9._-]*", label):
        raise SystemExit("--label must use lowercase letters, digits, dots, underscores or hyphens.")

    output_dir = Path(args.output_directory).expanduser().resolve()
    if output_dir == Path(output_dir.anchor) or output_dir == Path.home().resolve():
        raise SystemExit("Refusing to write a package directly into a filesystem root or home directory.")
    output_dir.mkdir(parents=True, exist_ok=True)
    label_suffix = f"-{label}" if label else ""
    archive = output_dir / f"wolt-project-{version}{label_suffix}.zip"
    checksum = archive.with_suffix(archive.suffix + ".sha256")
    if archive.exists() or checksum.exists():
        raise SystemExit("Release already exists; use a new version or --label. Existing releases are never overwritten.")

    files = sorted(path for path in skill_root.rglob("*") if path.is_file() and include(path.relative_to(skill_root)))
    entries: list[tuple[Path, Path]] = [(path, path.relative_to(skill_root)) for path in files]
    included_briefs: list[str] = []
    for brief in brief_paths:
        included_briefs.append(brief.name)
        brief_files = [brief] if brief.is_file() else sorted(path for path in brief.rglob("*") if path.is_file())
        for path in brief_files:
            local = Path(brief.name) if brief.is_file() else Path(brief.name) / path.relative_to(brief)
            if include(local):
                entries.append((path, Path("assets") / "internal-briefs" / local))

    names = [str(relative) for _, relative in entries]
    if len(names) != len(set(names)):
        raise SystemExit("Package inputs create duplicate archive paths; rename or select fewer briefs.")

    entries.sort(key=lambda item: str(item[1]))
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as bundle:
        for path, relative in entries:
            add_file(bundle, path, relative)
        if included_briefs:
            manifest = "# Internal Brief Bundle\n\n" + "".join(f"- {name}\n" for name in included_briefs)
            add_bytes(bundle, manifest.encode("utf-8"), Path("assets") / "internal-briefs" / "CONTENTS.md")

    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    checksum.write_text(f"{digest}  {archive.name}\n", encoding="utf-8")
    print(archive)
    print(checksum)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
