#!/usr/bin/env python3
"""Fast deterministic checks for a Wolt project package."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


CORE_FILES = [
    "00-idea.md",
    "01-scenario.md",
    "02-reference-map.md",
    "03-storyboard.md",
    "04-seedance-prompts.md",
    "05-client-review.md",
]
FUTURE_FILES = [
    "06-generation-log.md",
    "07-upscale-delivery.md",
    "08-qa.md",
    "09-retrospective.md",
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


BEAT = re.compile(
    r"^\s*(?:\*\*)?(\d+(?:\.\d+)?)\s*[–—-]\s*(\d+(?:\.\d+)?)\s*(?:s|秒)(?=[\s:：—–*]|$)",
    re.MULTILINE,
)


def timeline_errors(block: str, duration: float, label: str) -> tuple[list[str], list[tuple[float, float]]]:
    beats = [(float(a), float(b)) for a, b in BEAT.findall(block)]
    errors = []
    if not beats:
        return [f"{label}: no explicit timestamped beat lines (e.g. 0–3s: action)"], beats
    cursor = 0.0
    for start, end in beats:
        if abs(start - cursor) > 0.001:
            errors.append(f"{label}: timeline gap/overlap at {cursor:g} → {start:g}s")
        if end <= start:
            errors.append(f"{label}: non-positive beat {start:g}–{end:g}s")
        cursor = end
    if abs(cursor - duration) > 0.001:
        errors.append(f"{label}: ends at {cursor:g}s, expected {duration:g}s")
    return errors, beats


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("project_folder")
    args = parser.parse_args()

    workspace = Path(__file__).resolve().parent.parent
    projects_root = (workspace / "projects").resolve()
    project = Path(args.project_folder)
    if not project.is_absolute():
        project = workspace / project
    project = project.resolve()
    if not project.is_dir() or projects_root not in project.parents:
        raise SystemExit("Project folder must exist under this workspace's projects/ directory.")

    errors: list[str] = []
    warnings: list[str] = []
    for name in CORE_FILES:
        if not (project / name).is_file():
            errors.append(f"missing core file: {name}")

    if errors:
        for message in errors:
            print(f"ERROR: {message}")
        return 1

    idea = read(project / "00-idea.md")
    scenario = read(project / "01-scenario.md")
    storyboard = read(project / "03-storyboard.md")
    prompt = read(project / "04-seedance-prompts.md")
    review = read(project / "05-client-review.md")

    if "TBD" in idea:
        warnings.append("00-idea.md still contains TBD")
    if len(scenario.encode()) > 6000:
        warnings.append("01-scenario.md exceeds compact target (6 KB)")
    if len(storyboard.encode()) > 6000:
        warnings.append("03-storyboard.md exceeds compact target (6 KB)")
    if len(prompt.encode()) > 18000:
        warnings.append("04-seedance-prompts.md exceeds compact target (18 KB)")

    fence_count = len(re.findall(r"^```", prompt, flags=re.MULTILINE))
    blocks = re.findall(r"^```[^\n]*\n(.*?)^```[ \t]*$", prompt, re.MULTILINE | re.DOTALL)
    if len(blocks) not in (1, 2) or fence_count != 2 * len(blocks):
        errors.append("04-seedance-prompts.md needs one EN video block, optionally a second ZH block, with closed fences")
    duration_match = re.search(r"^- Duration:\s*(\d+(?:\.\d+)?)\s*s", prompt, re.MULTILINE)
    duration = float(duration_match.group(1)) if duration_match else 15.0
    timelines = []
    for index, block in enumerate(blocks):
        label = "EN" if index == 0 else "ZH"
        if re.search(r"\bTBD\b|\.{3}|…|\[primary mode\]", block):
            errors.append(f"{label}: unresolved prompt placeholder")
        issues, beats = timeline_errors(block, duration, label)
        errors.extend(issues)
        timelines.append(beats)
    if len(timelines) == 2 and timelines[0] != timelines[1]:
        errors.append("EN/ZH timelines differ; update the translation from the current EN version")
    if len(blocks) == 2:
        for kind in ("Image", "Video", "Audio"):
            left, right = [set(re.findall(rf"@{kind}\d+", block)) for block in blocks]
            if left != right:
                errors.append(f"EN/ZH {kind} reference tags differ")

    approval = re.search(r"^- APPROVED_FOR_GENERATION:\s*(\S+)", review, re.MULTILINE)
    approved = bool(approval and approval.group(1).upper() == "YES")
    if approved:
        for field in ("Approval date", "Approval source/evidence", "Approved scenario version", "Approved storyboard version", "Approved video-prompt version"):
            match = re.search(rf"^- {re.escape(field)}:\s*(.*)$", review, re.MULTILINE)
            if not match or match.group(1).strip().lower() in {"", "none", "tbd"}:
                errors.append(f"approval is YES but {field} is missing")
    else:
        template_root = workspace / "templates" / "project"
        for name in FUTURE_FILES:
            current = project / name
            template = template_root / name
            if current.is_file() and template.is_file() and current.read_bytes() != template.read_bytes():
                warnings.append(f"{name} changed before client approval; leave future-stage files untouched")

    for kind in ("Image", "Video", "Audio"):
        tags = sorted({int(value) for value in re.findall(rf"@{kind}(\d+)", prompt)})
        if tags and tags != list(range(1, max(tags) + 1)):
            errors.append(f"non-contiguous {kind} tags: {tags}")

    for message in errors:
        print(f"ERROR: {message}")
    for message in warnings:
        print(f"WARN: {message}")
    print(f"SUMMARY: {len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
