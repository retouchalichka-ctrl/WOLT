#!/usr/bin/env python3
"""Move an idea between inbox/active/archive without overwriting records."""

from __future__ import annotations

import argparse
import re
from datetime import date
from pathlib import Path


LIFECYCLES = {"inbox", "active", "archive"}


def replace_field(text: str, name: str, value: str) -> str:
    pattern = rf"(^- {re.escape(name)}:\s*).*$"
    if re.search(pattern, text, flags=re.MULTILINE):
        return re.sub(pattern, rf"\g<1>{value}", text, flags=re.MULTILINE)
    return text


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("idea_file")
    parser.add_argument("lifecycle", choices=sorted(LIFECYCLES))
    parser.add_argument("--reason", default="")
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parent.parent
    idea_root = (project_root / "ideas").resolve()
    source = Path(args.idea_file)
    if not source.is_absolute():
        source = (project_root / source).resolve()
    if not source.is_file() or idea_root not in source.parents:
        raise SystemExit("Idea file must exist under this workspace's ideas/ directory.")
    if source.parent.name not in LIFECYCLES:
        raise SystemExit("Idea file must be in ideas/inbox, ideas/active, or ideas/archive.")
    if args.lifecycle == "archive" and not args.reason.strip():
        raise SystemExit("Archiving requires --reason (delivered, rejected, merged duplicate, paused, etc.).")

    target_dir = idea_root / args.lifecycle
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / source.name
    if target != source and target.exists():
        raise SystemExit(f"Refusing to overwrite existing record: {target}")

    text = source.read_text(encoding="utf-8")
    text = replace_field(text, "Lifecycle", args.lifecycle)
    text = replace_field(text, "Updated", date.today().isoformat())
    if args.reason.strip():
        text = replace_field(text, "Archive reason", args.reason.strip())

    if target == source:
        source.write_text(text, encoding="utf-8")
    else:
        target.write_text(text, encoding="utf-8")
        source.unlink()
    print(target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
