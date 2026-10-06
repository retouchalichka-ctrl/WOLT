#!/usr/bin/env python3
"""Build reusable SVG color cards; --png also renders previews using Pillow.

Reads project-authored schemes, never samples or modifies reference photographs.
This maintenance helper is not required to use the skill or write prompts.
"""
from pathlib import Path
import argparse
import html
import json
import textwrap


INK = '#021738'
PAPER = '#F8F8F8'


class Canvas:
    def __init__(self, width, height, png=False):
        self.width, self.height = width, height
        self.elements = []
        self.im = self.draw = None
        if png:
            from PIL import Image, ImageDraw
            self.im = Image.new('RGB', (width, height), PAPER)
            self.draw = ImageDraw.Draw(self.im)
        self.rect(0, 0, width, height, PAPER)

    def rect(self, x, y, width, height, fill, radius=0):
        self.elements.append(f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="{radius}" fill="{fill}"/>')
        if self.draw:
            self.draw.rounded_rectangle((x, y, x + width, y + height), radius=radius, fill=fill)

    def text(self, x, y, value, size=20, bold=False, fill=INK):
        weight = '700' if bold else '400'
        self.elements.append(f'<text x="{x}" y="{y + size}" font-family="Arial, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}">{html.escape(value)}</text>')
        if self.draw:
            from PIL import ImageFont
            candidates = ([Path('/System/Library/Fonts/Supplemental/Arial Bold.ttf'),
                           Path('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf')] if bold else
                          [Path('/System/Library/Fonts/Supplemental/Arial.ttf'),
                           Path('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')])
            font_path = next((p for p in candidates if p.exists()), None)
            if not font_path:
                raise RuntimeError('PNG rendering needs Arial or DejaVu Sans; SVG output needs no font installation.')
            font = ImageFont.truetype(str(font_path), size)
            self.draw.text((x, y), value, font=font, fill=fill, anchor='lt')

    def save(self, directory, name, description):
        title = html.escape(description)
        svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.width}" height="{self.height}" viewBox="0 0 {self.width} {self.height}" role="img"><title>{title}</title>' + ''.join(self.elements) + '</svg>\n'
        (directory / (name + '.svg')).write_text(svg)
        if self.im:
            self.im.save(directory / (name + '.png'))


def card(canvas, item, x=0, y=0, width=740):
    canvas.rect(x, y, width, 430, '#FFFFFF', 16)
    canvas.text(x+26, y+22, item['id'] + '  /  ' + item['title_en'], 19)
    canvas.text(x+26, y+58, item['title_ru'], 32, True)
    canvas.text(x+26, y+109, item['use_ru'], 18)
    sw = 160
    for index, color in enumerate(item['colors']):
        sx = x+26+index*176
        canvas.rect(sx, y+150, sw, 126, color['hex'], 8)
        # A fine ink rule makes near-white official swatches visible without changing them.
        canvas.rect(sx, y+275, sw, 1, INK)
        for row, line in enumerate(textwrap.wrap(color['name'], width=16)):
            canvas.text(sx, y+293+row*22, line, 18)
        canvas.text(sx, y+340, color['hex'], 19, True)
        for row, line in enumerate(textwrap.wrap(color['role_ru'], width=17)):
            canvas.text(sx, y+376+row*21, line, 16)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--png', action='store_true')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    skill = Path(__file__).resolve().parent.parent
    data = json.loads((skill/'references/color-schemes.json').read_text())
    out = args.output or skill/'assets/color-maps'
    out.mkdir(parents=True, exist_ok=True)
    for item in data['schemes']:
        for color in item['colors']:
            assert data['palette'][color['name']] == color['hex'], color
        canvas = Canvas(740, 430, args.png)
        card(canvas, item)
        canvas.save(out, item['id'].lower(), item['id'] + ': ' + item['title_ru'])
    atlas = Canvas(1600, 2000, args.png)
    atlas.text(40, 24, 'Цветовые карты для рекламы Wolt', 42, True)
    atlas.text(40, 85, '6 рабочих сочетаний + отдельный финал · только официальные цвета · 09.09.2026', 23)
    for index, item in enumerate(data['schemes'][:6]):
        card(atlas, item, 40+(index % 2)*780, 150+(index//2)*458)
    final = data['schemes'][6]
    card(atlas, final, 40, 1524)
    atlas.text(830, 1550, 'Один кадр — одна выбранная схема', 28, True)
    lines = ['Референсы задают характер, а не чужую палитру.',
             'В интерьере — лёгкие акценты, без квот.',
             'Еда, кожа и крафт сохраняют натуральный цвет.',
             'Логотип — только печать на пакете.',
             'Равные плашки не означают доли цвета в кадре.',
             'Это наши сочетания официальных цветов,',
             'а не отдельные утверждённые схемы Wolt.']
    for row, line in enumerate(lines):
        atlas.text(830, 1608+row*37, line, 22)
    atlas.save(out, 'wolt-color-atlas', 'Wolt: six working color schemes and a final pack-shot palette; swatch sizes do not prescribe area percentages.')
    print(f'7 color cards and atlas written to {out}')


if __name__ == '__main__':
    main()
