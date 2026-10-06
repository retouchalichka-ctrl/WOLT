#!/usr/bin/env python3
"""Initialize a managed Wolt workspace from the portable skill bundle."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


def files_under(root: Path) -> list[Path]:
    return sorted(path for path in root.rglob("*") if path.is_file())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("target", help="new or existing directory to initialize")
    parser.add_argument(
        "--merge",
        action="store_true",
        help="copy only missing files into a non-empty target; never overwrite",
    )
    args = parser.parse_args()

    skill_root = Path(__file__).resolve().parent.parent
    source = skill_root / "assets" / "workspace-template"
    if not source.is_dir():
        raise SystemExit(f"Portable workspace template is missing: {source}")

    target = Path(args.target).expanduser().resolve()
    if target == Path(target.anchor) or target == Path.home().resolve():
        raise SystemExit("Refusing to initialize a filesystem root or home directory.")
    if target.exists() and not target.is_dir():
        raise SystemExit(f"Target exists and is not a directory: {target}")

    copy_plan = [(path, path.relative_to(source)) for path in files_under(source)]
    internal_briefs = skill_root / "assets" / "internal-briefs"
    if internal_briefs.is_dir():
        copy_plan.extend(
            (path, Path("briefs") / "imported" / path.relative_to(internal_briefs))
            for path in files_under(internal_briefs)
        )

    existing = [relative for _, relative in copy_plan if (target / relative).exists()]
    target_nonempty = target.exists() and any(target.iterdir())
    if target_nonempty and not args.merge:
        raise SystemExit("Target is not empty. Re-run with --merge to copy missing files without overwriting.")
    if existing and not args.merge:
        raise SystemExit("Target contains files from the workspace template; refusing to overwrite.")

    created = 0
    skipped = 0
    target.mkdir(parents=True, exist_ok=True)
    for source_file, relative in copy_plan:
        destination = target / relative
        if destination.exists():
            skipped += 1
            continue
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_file, destination)
        created += 1

    print(f"Initialized managed Wolt workspace: {target}")
    print(f"Created {created} file(s); skipped {skipped} existing file(s); overwrote 0 file(s).")
    if internal_briefs.is_dir():
        print("Imported the packaged team brief bundle into briefs/imported/.")
    print("Next: open this directory in Codex and invoke $wolt-project with a brief, idea, or brainstorm request.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
