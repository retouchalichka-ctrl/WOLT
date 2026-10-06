#!/usr/bin/env python3
"""Check the actual four-part Markdown reply, not internal project records.

Read-only. Checks structure, copy fences, attachment maps, word budgets and
scene/video timing. Does not establish creative quality, asset availability,
brand compliance, or whether a remote chat loaded a skill.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path


TITLES = ("Название и описание для заказчика", "Сцены", "Storyboard", "Seedance 2.5")
TAG = re.compile(r"@(Image|Video|Audio)(\d+)\b")
RANGE = r"(\d+(?:\.\d+)?)\s*[–—-]\s*(\d+(?:\.\d+)?)\s*(?:s|с|сек)?"
SCENE = re.compile(r"^(\d+)\.\s+" + RANGE + r"\s*[—–:-]\s+(.+)$")
BEAT = re.compile(r"^" + RANGE + r"\s*[:—–-]\s*\S", re.MULTILINE)


def words(text: str) -> int:
    # A Markdown URL is a reference, not dozens of words in its path.
    text = re.sub(r"\[([^]]+)\]\([^\n]+?\)", r"\1", text)
    return sum(any(char.isalnum() for char in token) for token in text.split())


def heading(line: str) -> tuple[int, str] | None:
    clean = re.sub(r"^#{1,6}\s+", "", line).strip()
    if clean.startswith("**") and clean.endswith("**"):
        clean = clean[2:-2]
    match = re.fullmatch(r"([1-4])\.\s+(.+)", clean)
    if match and match[2].startswith(TITLES[int(match[1]) - 1]):
        return int(match[1]), match[2]
    return None


def validate(text: str, *, duration: float = 15, outside_limit: int = 180,
             storyboard_limit: int = 220, video_limit: int = 450) -> tuple[list[str], dict]:
    errors: list[str] = []
    sections = {i: {"lines": [], "blocks": []} for i in range(1, 5)}
    order, outside = [], []
    current = 0
    block: list[str] | None = None
    for line_no, raw in enumerate(text.splitlines(), 1):
        line = raw.strip()
        if block is not None:
            if line == "```":
                if current in sections:
                    sections[current]["blocks"].append("\n".join(block))
                block = None
            elif line.startswith("```"):
                errors.append(f"line {line_no}: invalid nested/closing fence")
            else:
                block.append(raw)
            continue
        if line.startswith("```"):
            if line != "```text":
                errors.append(f"line {line_no}: prompt must open with literal ```text")
            if current not in (3, 4):
                errors.append(f"line {line_no}: prompt outside section 3 or 4")
            block = []
            continue
        if not line:
            continue
        outside.append(line)
        found = heading(line)
        if found:
            current = found[0]
            order.append(current)
            continue
        if current not in sections:
            if "text before section 1" not in errors:
                errors.append("text before section 1")
            continue
        if sections[current]["blocks"]:
            errors.append(f"line {line_no}: extra text after prompt")
        sections[current]["lines"].append(line)
    if block is not None:
        errors.append("unclosed prompt fence")
    if order != [1, 2, 3, 4]:
        errors.append(f"expected exactly sections 1,2,3,4; got {order}")
    if ":::writing" in text or "<canvas" in text.lower():
        errors.append("document/canvas wrapper: return ordinary Markdown")

    story = sections[1]["lines"]
    if len(story) != 2 or not story[0].startswith("EN:") or not story[1].startswith("RU:"):
        errors.append("section 1 needs only EN: and RU: title/story lines")
    scene_times = []
    for n, line in enumerate(sections[2]["lines"], 1):
        match = SCENE.fullmatch(line.replace("**", ""))
        if not match or int(match[1]) != n:
            errors.append(f"section 2: expected numbered one-line timed scene, got {line[:65]}")
        else:
            scene_times.append((float(match[2]), float(match[3])))
    if not scene_times:
        errors.append("missing timed scenes")

    prompt_counts = {}
    for number, limit in ((3, storyboard_limit), (4, video_limit)):
        data = sections[number]
        lines, blocks = data["lines"], data["blocks"]
        if number == 3 and not blocks:
            if len(lines) != 1 or not (lines[0] == "Не нужен." or lines[0].startswith("Готовый storyboard:")):
                errors.append("section 3 requires one prompt or one explicit existing/not-needed line")
            continue
        if len(blocks) != 1:
            errors.append(f"section {number}: expected one separate closed text block")
            continue
        prompt = blocks[0]
        prompt_counts[str(number)] = words(prompt)
        if not prompt.strip():
            errors.append(f"section {number}: empty prompt")
        if words(prompt) > limit:
            errors.append(f"section {number}: {words(prompt)} prompt words exceed {limit}")
        declared = []
        no_refs = len(lines) == 1 and lines[0].startswith("Референсы:")
        if not lines:
            errors.append(f"section {number}: missing attachment list above prompt")
        elif not no_refs:
            for line in lines:
                match = re.fullmatch(r"(@(?:Image|Video|Audio)\d+)\s+—\s+(.+?)\s+—\s+(.+)", line)
                if not match:
                    errors.append(f"section {number}: unexpected text instead of attachment line: {line[:65]}")
                else:
                    declared.append(match[1])
            if len(declared) != len(set(declared)):
                errors.append(f"section {number}: duplicate attachment slots")
            for kind in ("Image", "Video", "Audio"):
                slots = [int(t[len(kind) + 1:]) for t in declared if t.startswith("@" + kind)]
                if slots != list(range(1, len(slots) + 1)):
                    errors.append(f"section {number}: {kind} slots must start at 1 in upload order")
        used = {m[0] for m in TAG.finditer(prompt)}
        if not used.issubset(set(declared)):
            errors.append(f"section {number}: undeclared prompt tags {sorted(used - set(declared))}")
        if number == 4 and set(declared) - used:
            errors.append("section 4: attachment tags have no job in the video prompt")

    video = sections[4]["blocks"]
    beats = [(float(a), float(b)) for a, b in BEAT.findall(video[0])] if len(video) == 1 else []
    if beats != scene_times or not beats:
        errors.append("scene list and video beat times must match")
    cursor = 0.0
    for start, end in scene_times:
        if abs(start - cursor) > 0.001 or end <= start:
            errors.append(f"scene timeline gap/overlap at {start:g}–{end:g}")
        cursor = end
    if abs(cursor - duration) > 0.001:
        errors.append(f"scene timeline must cover 0–{duration:g}s")
    count = words("\n".join(outside))
    if count > outside_limit:
        errors.append(f"{count} outside-prompt words exceed {outside_limit}")
    return errors, {"outside_words": count, "prompt_words": prompt_counts,
                    "sections": order, "prompt_blocks": sum(len(s["blocks"]) for s in sections.values())}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("markdown", type=Path)
    parser.add_argument("--duration", type=float, default=15)
    parser.add_argument("--outside-limit", type=int, default=180)
    parser.add_argument("--storyboard-limit", type=int, default=220)
    parser.add_argument("--video-limit", type=int, default=450)
    args = parser.parse_args()
    errors, stats = validate(args.markdown.read_text(), duration=args.duration,
        outside_limit=args.outside_limit, storyboard_limit=args.storyboard_limit,
        video_limit=args.video_limit)
    for error in errors[:12]:
        print("ERROR:", error)
    if len(errors) > 12:
        print(f"ERROR: {len(errors) - 12} additional issues")
    print("FAIL" if errors else "PASS", stats)
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())
