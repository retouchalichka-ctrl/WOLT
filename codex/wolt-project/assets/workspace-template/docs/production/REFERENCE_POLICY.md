# Reference Policy

## Numbering

| Вход | Нумерация |
|---|---|
| Storyboard + image refs | storyboard `@Image1`, остальные `@Image2+` по порядку вложения |
| Storyboard only | storyboard `@Image1` |
| Image refs only | первая реальная image `@Image1`, затем по порядку |
| Video | отдельная последовательность `@Video1+` |
| Audio | отдельная последовательность `@Audio1+` |

Если новый storyboard создаётся позже и реально будет приложен, он становится `@Image1`, а существующие image refs сдвигаются на один без изменения относительного порядка.

## Narrow-job contract

Для каждого asset обязательно записать:

- `USE FOR`: одна-две конкретные задачи;
- `DO NOT COPY/CHANGE`: фон, свет, style, identity, text, unrelated branding и другие exclusions;
- `PRIORITY`: critical/supporting/optional;
- `APPLIES TO`: весь spot или конкретный time range.

Нельзя писать `copy the reference`. Для video ref указывать уровень абстракции: literal performance, camera grammar, rhythm only, cinematic intention, edit structure или sound relationship.

## Canonical local refs

- `assets/brand/core/wolt-kraft-bag.jpeg`: bag geometry, kraft material, handles, food-icon print, logo placement only.
- `assets/brand/core/wolt-colors.png`: exact brand colors; не прикладывать к Seedance без риска color drift.
- `assets/brand/core/wolt-blue-background.jpg`: flat Wolt Blue plate only.
- `assets/brand/courier/courier-01.webp` и `courier-02.jpg`: clothing silhouette, Wolt Blue и delivery-gear geometry only. Не копировать лица, локацию, photographic style, logos/text; все courier logos/text подавлять.
- `assets/brand/archive/logos/`: не использовать в generation или post без отдельного client approval.

## Storyboard precedence

Если visual reference уже приложен, использовать его в рамках реальной задачи: single frame — appearance/composition или явно выбранное начальное/финальное состояние; grid — depicted action/spatial anchors. Intended shot order допустим только если каждому shot соответствует отдельная панель; timed video prompt остаётся главным, точное исполнение не гарантируется. Сетка/gutters не воспроизводятся в видео. Новый формат выбирать по OUTPUT_CONTRACT.md: single frame, 2×1, 2×2, 3×2 или 3×3, минимально достаточный для сценария. Не генерировать replacement plan/prompt без явного запроса. Если новая концепция конфликтует с board, кратко указать mismatch и запросить разрешение на revision только при материальном конфликте.

## Courier scene rule

Courier refs можно прикладывать к storyboard generation и Seedance, когда в сцене нужна экипировка. Во всех таких кадрах лицо исключено композицией: верхняя рамка ниже подбородка, без eyes/mouth/full chin/identity. Storyboard `@Image1` сохраняет приоритет; bag и courier refs нумеруются далее только если реально используются. Не резервировать tag для отсутствующего bag или courier.
