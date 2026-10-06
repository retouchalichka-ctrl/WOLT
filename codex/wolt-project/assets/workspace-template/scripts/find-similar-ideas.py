#!/usr/bin/env python3
"""Find lexical candidate neighbours in the local Wolt idea library."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


STOPWORDS = {
    "about", "after", "again", "also", "before", "from", "have", "into", "only",
    "that", "the", "their", "then", "this", "through", "with", "wolt", "идея",
    "как", "для", "или", "над", "она", "они", "при", "про", "так", "это",
}


def tokens(value: str) -> set[str]:
    found = re.findall(r"[^\W_]+", value.casefold(), flags=re.UNICODE)
    return {token for token in found if len(token) >= 3 and token not in STOPWORDS}


def field(text: str, name: str) -> str:
    match = re.search(rf"^- {re.escape(name)}:\s*(.*)$", text, flags=re.MULTILINE)
    return match.group(1).strip() if match else ""


def searchable(value: str) -> str:
    placeholders = {
        "TBD",
        "none / duplicate-of / variant-of / adjacent-to + idea ID",
        "`vertical | audience/job | hook device | core action/transformation | payoff | Wolt role`",
    }
    return "" if value in placeholders else value


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("query", help="idea title, raw wording, or fingerprint")
    parser.add_argument("--limit", type=int, default=8)
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parent.parent
    idea_root = project_root / "ideas"
    query_tokens = tokens(args.query)
    if not query_tokens:
        print("No searchable idea terms supplied.")
        return 0

    results: list[tuple[float, Path, str, str, str]] = []
    for path in idea_root.glob("*/*.md"):
        text = path.read_text(encoding="utf-8", errors="replace")
        identity = " ".join(
            searchable(value) for value in [
                field(text, "Title"), field(text, "Fingerprint"), field(text, "Search tags"),
                field(text, "Hook device"), field(text, "Core action or transformation"),
                field(text, "Payoff"), field(text, "Wolt role"),
            ]
        )
        candidate_tokens = tokens(identity)
        if not candidate_tokens:
            continue
        overlap = query_tokens & candidate_tokens
        if not overlap:
            continue
        score = len(overlap) / len(query_tokens | candidate_tokens)
        results.append((score, path, field(text, "Title") or path.stem,
                        field(text, "Lifecycle") or path.parent.name,
                        field(text, "Fingerprint")))

    results.sort(key=lambda item: (-item[0], str(item[1])))
    if not results:
        print("Similar idea candidates: none found")
        return 0

    print("Similar idea candidates (review before creating a new record):")
    for score, path, title, lifecycle, fingerprint in results[: max(1, args.limit)]:
        relative = path.relative_to(project_root)
        print(f"- {score:.0%} | {lifecycle} | {title} | {relative}")
        if fingerprint:
            print(f"  fingerprint: {fingerprint}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
