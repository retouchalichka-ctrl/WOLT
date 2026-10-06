# Wolt color schemes — project art direction

These are project-authored combinations of the verified official palette, not separately approved Wolt layouts. Color facts and source: brand-colors.md (verified 2026-09-09).

## Use

User references show desired energy, playful forms, color contrast and styling only. Never copy their non-Wolt palettes, prints, logos or costumes. Keep the Wolt brand look: clear hierarchy, restrained official-color accents, appetizing natural food, photoreal materials and bright controlled light. Dopamine decor/Memphis/color blocking are optional descriptive influences, not a required maximalist set.

Choose one relevant C01–C06 scheme when useful; maintain it across the same scene. Neutral walls, wood and natural materials remain valid. Light accents means limited objects/area, not diluting the official HEX. No interior percentage quota or blue-room requirement. Avoid visual clutter and competing multicolored patterns. Equal swatch sizes do not prescribe color proportions. Food, skin and kraft retain natural colors; never recolor them into the palette.

P01 is the separate final pack shot: loaded Wolt bag on Wolt Blue #00C2E8 surrounded by the actual scenario's delivered products. Only the bag bears its authentic printed logo; no floating logo, title card or other branded props. Generic packaging stays textless. Food/Pharmacy/courier rules still apply.

Translate the chosen scheme into concrete object/background colors inside each image/video prompt; an ID alone is insufficient. Do not add a separate palette section to the four-part production response. Cards live in the skill at assets/color-maps/ (individual c01.png through c06.png, p01.png, SVG equivalents and wolt-color-atlas.png/.svg). Attach only an actually available relevant card if helpful; scope it to colors, never its text, swatches or diagram layout. Storyboards remain clean scene images without captions. JSON source: color-schemes.json; optional rebuild: scripts/build_color_maps.py --png.

## C01 — Лёгкий дом / Home / light & playful

Интерьеры · спокойная база, живые детали

Milk White `#F8F8F8` — Светлая база | Light Pumpkin Orange `#FFF6F1` — Мягкая деталь | Wolt Blue `#00C2E8` — Фирменный акцент | Raspberry Pink `#F294CD` — Малый акцент

Светлая гостиная или кухня: нейтральные стены и дерево; голубая лампа либо небольшой текстиль, одна розовая деталь. Цветная мебель допустима, но не весь комплект одновременно.

Избегать: Не красить всю комнату в фирменные цвета и не собирать пёстрые узоры.

Prompt cue (adapt to actual scene):

```text
Light home interior with Milk White #F8F8F8 neutrals, a small Light Pumpkin Orange #FFF6F1 detail, one Wolt Blue #00C2E8 prop and a restrained Raspberry Pink #F294CD accent.
```

## C02 — Тёплая еда / Food / warm contrast

Пицца · выпечка · тёплая золотистая еда

Milk White `#F8F8F8` — Тарелка / база | Wolt Blue `#00C2E8` — Прохладный акцент | Banana Yellow `#FCC34C` — Малый тёплый акцент | Blueberry Blue `#021738` — Тёмная деталь

Для золотистой корочки и красного соуса: светлая тарелка, маленький голубой реквизит, жёлтый штрих подальше от еды; тёмный оттенок в небольшой детали. Фактура еды — главный контраст.

Избегать: Не делать жёлтое блюдо на жёлтом фоне; не окрашивать еду ради палитры.

Prompt cue (adapt to actual scene):

```text
Milk White #F8F8F8 tableware separates warm food from a small Wolt Blue #00C2E8 prop; restrained Banana Yellow #FCC34C and Blueberry Blue #021738 details stay away from the food silhouette.
```

## C03 — Свежесть / Fresh / garden accent

Овощи · groceries · свежие продукты

Milk White `#F8F8F8` — Чистая база | Light Lime Green `#ECFED2` — Мягкая деталь | Lime Green `#A1CE47` — Свежий акцент | Wolt Blue `#00C2E8` — Фирменный акцент

Овощи, фрукты и свежие продукты на светлой базе; небольшая зелёная деталь и голубой предмет разделены в композиции. Натуральная зелень остаётся естественной.

Избегать: Не сливать зелёную еду с зелёной опорой: под героем оставить нейтральный участок.

Prompt cue (adapt to actual scene):

```text
Milk White #F8F8F8 around the food, one Light Lime Green #ECFED2 detail, sparse Lime Green #A1CE47 and Wolt Blue #00C2E8 props; preserve separation from natural greens.
```

## C04 — Ягодный акцент / Sweet / berry accent

Десерты · ягоды · напитки

Milk White `#F8F8F8` — Нейтральная база | Light Raspberry Pink `#FEF5FA` — Мягкая деталь | Raspberry Pink `#F294CD` — Ягодный акцент | Wolt Blue `#00C2E8` — Прохладный акцент

Светлая посуда для десертов; розовый текстиль или один предмет, голубой акцент для контраста. Под розовыми ягодами или кремом — нейтральный фон.

Избегать: Не превращать весь кадр в пастельную дымку, не усиливать цвет крема искусственно.

Prompt cue (adapt to actual scene):

```text
Milk White #F8F8F8 tableware, a small Light Raspberry Pink #FEF5FA textile detail, restrained Raspberry Pink #F294CD and Wolt Blue #00C2E8 props; natural dessert colors stay dominant.
```

## C05 — Солнечное утро / Morning / sunny accent

Завтрак · цитрусы · дневные сцены

Milk White `#F8F8F8` — Светлая база | Light Banana Yellow `#FFF8DE` — Мягкая деталь | Pumpkin Orange `#FF834F` — Солнечный акцент | Wolt Blue `#00C2E8` — Прохладный акцент

Открытый дневной свет; маленькая светло-жёлтая деталь, оранжевая керамика вдали от цитрусов или выпечки, голубой акцент. Цвет не заменяет правдоподобный солнечный свет.

Избегать: Не ставить оранжевую еду на оранжевый фон; не использовать цветные световые заливки.

Prompt cue (adapt to actual scene):

```text
Bright daylight with Milk White #F8F8F8 neutrals, a Light Banana Yellow #FFF8DE detail, one Pumpkin Orange #FF834F ceramic prop and a small Wolt Blue #00C2E8 accent.
```

## C06 — Игривый образ / Styling / playful detail

Одежда · lifestyle · персонаж в кадре

Milk White `#F8F8F8` — Светлое окружение | Wolt Blue `#00C2E8` — Один цветной элемент | Raspberry Pink `#F294CD` — Небольшая деталь | Blueberry Blue `#021738` — Контрастная деталь

Один выразительный цветной элемент одежды или мебели, спокойное окружение, один небольшой контрастный аксессуар. Для курьера сохраняются утверждённый силуэт и кадрирование ниже подбородка.

Избегать: Не копировать принты, бренды и костюмы референсов; не добавлять логотипы на одежду.

Prompt cue (adapt to actual scene):

```text
Milk White #F8F8F8 surroundings, one Wolt Blue #00C2E8 garment or furnishing, a small Raspberry Pink #F294CD detail and limited Blueberry Blue #021738 contrast; generic unbranded styling.
```

## P01 — Финальный пакшот / Final / brand finish

Отдельный финал · тот же доставленный заказ

Wolt Blue `#00C2E8` — Фон финала | Milk White `#F8F8F8` — Посуда, если нужна | Blueberry Blue `#021738` — Малая деталь, опция

Голубой фон, наполненный kraft-пакет и тот же набор товаров из сюжета. Еда, кожа, крафт и товары сохраняют натуральные цвета; посуда и детали необязательны.

Избегать: Не одинокий пакет, не новый ассортимент, не отдельная logo-заставка. Цветовые доли интерьеру не задаются.

Prompt cue (adapt to actual scene):

```text
Final pack shot on Wolt Blue #00C2E8 with the loaded kraft bag and the same delivered items; optional Milk White #F8F8F8 tableware, natural product colors and clear copy space.
```
