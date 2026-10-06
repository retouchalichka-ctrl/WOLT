#!/usr/bin/env python3
"""Regression checks in disposable workspaces; never writes real client projects."""
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent.parent


class MechanismTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='wolt-mechanism-')
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        shutil.copytree(ROOT / 'scripts', self.root / 'scripts', ignore=shutil.ignore_patterns('__pycache__'))
        shutil.copytree(ROOT / 'templates', self.root / 'templates')
        self.project = self.root / 'projects' / 'fixture'
        shutil.copytree(self.root / 'templates/project', self.project)
        (self.project / '00-idea.md').write_text('Fixture concept\n')
        self.en = 'One bag. @Image1 defines its geometry.\n0–3s: A hand lowers the bag.\n3–6.8s: Reveal apples.\n6.8–15s: Settle the bag upright.\n'
        self.zh = '@Image1控制纸袋形状。\n0–3秒：手放下纸袋。\n3–6.8秒：展示苹果。\n6.8–15秒：纸袋直立稳定。\n'

    def prompt(self, en=None, zh=None):
        value = '# Prompt\n- Duration: 15s\n\n```text\n' + (self.en if en is None else en) + '```\n'
        if zh is not None:
            value += '\n```text\n' + zh + '```\n'
        (self.project / '04-seedance-prompts.md').write_text(value)

    def validate(self, ok, diagnostic=''):
        result = subprocess.run([sys.executable, str(self.root / 'scripts/validate-project.py'), str(self.project)], text=True, capture_output=True)
        self.assertEqual(result.returncode, 0 if ok else 1, result.stdout + result.stderr)
        self.assertIn(diagnostic, result.stdout)

    def test_english_only_and_decimal_timeline(self):
        self.prompt()
        self.validate(True)

    def test_optional_chinese(self):
        self.prompt(zh=self.zh)
        self.validate(True)

    def test_gap_and_overlap(self):
        for altered in ('3–7s', '3–6s'):
            with self.subTest(altered=altered):
                self.prompt(en=self.en.replace('3–6.8s', altered))
                self.validate(False, 'timeline gap/overlap')

    def test_stale_chinese_timeline(self):
        self.prompt(zh=self.zh.replace('6.8', '7'))
        self.validate(False, 'EN/ZH timelines differ')

    def test_stale_chinese_references(self):
        self.prompt(zh=self.zh.replace('@Image1', '@Image2'))
        self.validate(False, 'reference tags differ')

    def test_unfinished_template_rejected(self):
        shutil.copy2(self.root / 'templates/project/04-seedance-prompts.md', self.project / '04-seedance-prompts.md')
        self.validate(False, 'unresolved prompt placeholder')

    def test_incomplete_approval_rejected(self):
        self.prompt()
        review = self.project / '05-client-review.md'
        review.write_text(review.read_text().replace('APPROVED_FOR_GENERATION: NO', 'APPROVED_FOR_GENERATION: YES'))
        self.validate(False, 'Approved scenario version is missing')

    def test_closed_fences_required(self):
        self.prompt()
        prompt = self.project / '04-seedance-prompts.md'
        prompt.write_text(prompt.read_text().rstrip()[:-3])
        self.validate(False, 'closed fences')

    def test_search_skip_and_name_collision(self):
        script = self.root / 'scripts/new-idea.sh'
        first = subprocess.run(['bash', str(script), 'Fixture', '--skip-search'], capture_output=True, text=True, check=True)
        self.assertNotIn('Similar idea candidates', first.stdout)
        files = list((self.root / 'ideas/inbox').glob('*.md'))
        original = files[0].read_bytes()
        subprocess.run(['bash', str(script), 'Fixture', '--skip-search'], capture_output=True, text=True, check=True)
        self.assertEqual(len(list((self.root / 'ideas/inbox').glob('*.md'))), 2)
        self.assertEqual(files[0].read_bytes(), original)


if __name__ == '__main__':
    unittest.main()
