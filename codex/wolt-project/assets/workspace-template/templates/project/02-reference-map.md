# Reference Map

Заполнять только реальными или явно запланированными вложениями. Если refs нет, написать `No attachments` и не создавать tags в prompt.

## Attach order

`No attachments` until an exact real or explicitly planned file is identified. A planned file is marked `not yet attached` and receives no operation tag until it will actually be supplied.

## Map

| Label | Asset | Use for | Do not copy/change | Priority | Applies to |
|---|---|---|---|---|---|

## Canonical wording

- Bag ref: `defines only the Wolt kraft bag geometry, kraft paper material, handles, food-icon print and logo placement; do not copy its background, lighting, camera or unrelated styling.`
- Courier ref: `defines only courier clothing silhouette, Wolt Blue and delivery-gear geometry; do not copy face identity, location, photographic style, visible logos or text; suppress all courier logos/text; frame every courier shot below the chin with no face, eyes, mouth, full chin or recognizable identity.`
- Storyboard ref: `single still controls its assigned look/composition/start or end state only; grid controls depicted action/spatial anchors, with intended shot order only when one panel per shot. Timed video prompt remains authoritative. Never reproduce grid/gutters in video. Real object geometry/color comes from dedicated object references.`
- Video ref: назвать ровно один abstraction level — literal performance / camera grammar / rhythm only / cinematic intention / edit structure / sound relationship — и явно исключить content/identity/style, которые копировать нельзя.

## Numbering check

- [ ] Existing storyboard, если приложен, является `@Image1`.
- [ ] Если storyboard нет, первая реальная image является `@Image1`.
- [ ] Video/audio sequences нумеруются независимо.
- [ ] Каждый tag соответствует файлу, который пользователь действительно приложит.
- [ ] Ни одного phantom tag.
