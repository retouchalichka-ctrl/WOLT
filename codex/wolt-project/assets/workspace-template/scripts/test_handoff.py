#!/usr/bin/env python3
"""Regression tests of user-visible Markdown structure, using synthetic content."""
import unittest
from validate_handoff import validate


VALID = """**1. Название и описание для заказчика**
EN: **Fixture** — A meal arrives.
RU: **Пример** — Приезжает заказ.

**2. Сцены**
1. 0–5s — Рука ставит пакет.
2. 5–15s — Пакет окружён продуктами.

**3. Storyboard — 2×1**
@Image1 — bag.jpeg — дизайн пакета.
```text
Use @Image1 for the bag. Two clean photographic panels.
```

**4. Seedance 2.5**
@Image1 — bag.jpeg — дизайн пакета.
```text
Use @Image1 for bag identity. One 15s film.
0–5s: A hand places the bag.
5–15s: Reveal the delivered items around it.
```
"""


class HandoffTests(unittest.TestCase):
    def rejects(self, candidate, diagnostic):
        issues, _ = validate(candidate)
        self.assertTrue(any(diagnostic in issue for issue in issues), issues)

    def test_two_independent_copyable_prompts(self):
        errors, stats = validate(VALID)
        self.assertEqual(errors, [])
        self.assertEqual(stats["prompt_blocks"], 2)

    def test_missing_fences(self):
        self.rejects(VALID.replace("```text\n", "").replace("```\n", ""), "closed text block")

    def test_unclosed_video(self):
        self.rejects(VALID.rstrip()[:-3], "unclosed")

    def test_document_wrapper_and_footer(self):
        self.rejects(':::writing{variant="document"}\n' + VALID + '\n:::', "document/canvas")
        self.rejects(VALID + "Why it works: delicious food.\n", "extra text after prompt")

    def test_detailed_scene_chapter(self):
        self.rejects(VALID.replace("**3. Storyboard", "### Camera\nTrack right.\n**3. Storyboard"), "one-line timed scene")

    def test_multiple_or_combined_prompt_blocks(self):
        self.rejects(VALID.replace("Two clean photographic panels.\n", "Two panels.\n```\n```text\nMore panels.\n"), "one separate")
        self.rejects(VALID.replace("```\n\n**4.", "\n**4.", 1), "sections 1,2,3,4")

    def test_missing_or_phantom_references(self):
        self.rejects(VALID.replace("@Image1 — bag.jpeg — дизайн пакета.\n", "", 1), "missing attachment")
        self.rejects(VALID.replace("Use @Image1 for bag identity", "Use @Image2 for bag identity"), "undeclared")

    def test_slot_order_restarts_per_prompt(self):
        self.rejects(VALID.replace("@Image1", "@Image2"), "start at 1")

    def test_no_board_and_no_references_are_valid(self):
        text = VALID.replace("@Image1 — bag.jpeg — дизайн пакета.\n```text\nUse @Image1 for the bag. Two clean photographic panels.\n```", "Не нужен.")
        text = text.replace("@Image1 — bag.jpeg — дизайн пакета.", "Референсы: не нужны.").replace("Use @Image1 for bag identity. ", "")
        self.assertEqual(validate(text)[0], [])

    def test_existing_board_status(self):
        text = VALID.replace("@Image1 — bag.jpeg — дизайн пакета.\n```text\nUse @Image1 for the bag. Two clean photographic panels.\n```", "Готовый storyboard: board-v2.png.")
        self.assertEqual(validate(text)[0], [])

    def test_timing_mismatch_and_gap(self):
        self.rejects(VALID.replace("0–5s: A hand", "0–6s: A hand"), "times must match")
        self.rejects(VALID.replace("5–15s", "6–15s"), "gap/overlap")

    def test_bold_scene_times_and_decimal_times(self):
        text = VALID.replace("1. 0–5s", "1. **0–5s**").replace("5s", "5.0s").replace("5–15s", "5.0–15s")
        self.assertEqual(validate(text)[0], [])

    def test_budget_is_enforced_and_explicit_override_supported(self):
        text = VALID.replace("Two clean photographic panels.", "detail " * 221)
        self.rejects(text, "prompt words exceed")
        self.assertEqual(validate(text, storyboard_limit=300)[0], [])
        text = VALID.replace("A meal arrives.", "word " * 181)
        self.rejects(text, "outside-prompt words exceed")


if __name__ == "__main__":
    unittest.main()
