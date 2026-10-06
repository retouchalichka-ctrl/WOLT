#!/usr/bin/env python3
"""Rebuild ideas/INDEX.md from local idea records."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


FIELDS = ["Idea ID", "Title", "Lifecycle", "Stage", "Outcome", "Vertical",
          "Fingerprint", "Duplicate relation", "Project path", "Updated"]


def field(text: str, name: str) -> str:
    match = re.search(rf"^- {re.escape(name)}:\s*(.*)$", text, flags=re.MULTILINE)
    return match.group(1).strip() if match else ""


def clean(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ") or "—"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="write ideas/INDEX.md")
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parent.parent
    idea_root = project_root / "ideas"
    rows = []
    for path in sorted(idea_root.glob("*/*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        data = {name: field(text, name) for name in FIELDS}
        data["Path"] = str(path.relative_to(project_root))
        rows.append(data)

    lines = [
        "# Idea Library Index", "",
        "Generated from local idea records. Each record remains the source of truth.", "",
        "| Idea ID | Title | Lifecycle | Stage | Outcome | Vertical | Fingerprint | Relation | Project | Updated | Path |",
        "|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for data in rows:
        values = [data["Idea ID"], data["Title"], data["Lifecycle"], data["Stage"],
                  data["Outcome"], data["Vertical"], data["Fingerprint"],
                  data["Duplicate relation"], data["Project path"], data["Updated"], data["Path"]]
        lines.append("| " + " | ".join(clean(value) for value in values) + " |")
    if not rows:
        lines.append("| — | No ideas recorded yet | — | — | — | — | — | — | — | — | — |")
    lines += ["", "Archive is not synonymous with failure. Check each record's evidence-based outcome review.", ""]
    output = "\n".join(lines)
    if args.write:
        idea_root.mkdir(parents=True, exist_ok=True)
        (idea_root / "INDEX.md").write_text(output, encoding="utf-8")
        print(idea_root / "INDEX.md")
    else:
        print(output, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
