# Storyboard

Status: `not needed / existing attached / prompt ready / render requested / draft rendered / approved`

Если storyboard уже приложен, не создавать новый plan/prompt; записать путь к existing sheet и перейти к reference map.

## Existing storyboard

- File/path:
- Attached with: original idea / later addition / none
- Use as future Seedance `@Image1`: YES/NO

Если поле содержит реальный storyboard, удалить следующие sections для нового board.

## Reference choice

- Type: single frame / 2×1 / 2×2 / 3×2 / 3×3 / existing sufficient reference / not needed
- Grid notation: columns × rows
- Job: look/composition / opening state / final state / action-state anchors / geography / shot order when one panel per shot
- Why this is the smallest sufficient reference: one sentence naming the scenario uncertainty.
- Necessary distinct states: list only what needs visual control; do not add filler panels or equate panel count with shot count.
- Single-frame time/state, if applicable:
- Individual frame/panel aspect ratio: deliverable ratio, default 16:9

Single frame is sufficient when text already explains the motion. Use 2×1 for two states, 2×2 for a short state chain, 3×2 for essential intermediate states, 3×3 for dense continuity. These are options, not quotas. A single frame is not automatically an opening-frame constraint.

## Frame or anchor plan

For a single frame use one row. For a grid, each panel resolves a distinct visual state; reading order is left-to-right then top-to-bottom.

| Panel | Time | Composition/action | Size code | Angle/height/axis | Change from previous | Light | Reference job |
|---|---:|---|---|---|---|---|---|

## Storyboard image prompt

Visual finish: photoreal premium advertising stills, bright juicy high-key light, believable food/kraft texture and contact shadows; no plastic CGI look.

Copy-ready English prompt for ChatGPT or Gemini/Nano Banana Pro; one shared prompt unless a provider-specific variant is requested. External generation is performed by the user. On return, record the actual file and source prompt version; image existence does not imply approval.

Render gate: `CLOSED`. Изменить на `OPEN — explicit user request received` только после отдельной команды пользователя сгенерировать storyboard.

### Attach for storyboard creation

- Attach only scene-relevant refs. If bag is used: its image controls geometry/material/print/logo only. If courier is used: courier refs control clothing silhouette, Wolt Blue and gear geometry only.
- For courier panels, keep every frame below the chin with no face/eyes/mouth/full chin or identity; make the crop intentional and natural.
- No phantom tags.

Один fenced block. Для single frame описать только выбранный кадр, без grid/gutters и выдуманных стадий движения. Для grid указать columns × rows, reading order, panel aspect (не путать с общей пропорцией sheet), recurring anchors, panel-by-panel action/shot-size/angle/light, same bag/product/hero across panels, halal/generic-packaging rules, courier below-chin framing when applicable, `no text, captions, labels, frame numbers, timecodes, infographic, charts, diagrams, arrows, UI panels, callouts, explanatory icons or decorative typography`. Смена крупности/угла нужна между panels, представляющими разные монтажные shots. Для последовательных состояний одного действия или continuous take сохранять нужные axis/framing — не имитировать несуществующие склейки.

Typical length: `120–220` words, not a minimum. State sheet-wide rules once; keep panel descriptions specific.

Перед блоком в готовом выводе: кратко по-русски что создаётся, затем нумерованный список реальных файлов/кадров в порядке загрузки с ролью каждого. Если вложения не нужны, явно написать это. Каждый отдельный image prompt — отдельный text block; один prompt сетки остаётся одним блоком.

```text
TBD only when a new storyboard is required.
```

## Output

- Prompt version:
- Render requested by/date:
- Rendered with exact prompt version:
- Rendered with exact asset list:
- Approved sheet:
- Will be attached to Seedance as: `@Image1 / no`
- Note: storyboard-creation tags end here; Seedance uses a new independent attach list.

Food lock inside this prompt: specify each permitted dish and ingredients; no pork/derivatives, pepperoni, cheeseburgers, molluscs/shellfish, alcohol or meat+dairy. Meat-free pizza only; meat burgers with dairy-free buns/sauce, no cheese. Covers background, bag contents and final pack shot; do not copy prohibited reference food.
