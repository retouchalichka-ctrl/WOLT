# Client Review & Approval Gate

## Что отправляем клиенту

- approved internal storyboard sheet;
- короткий сценарий на 2–4 предложения: hook 0–3s, main action by 6s, resolution/pack shot 6–15s;
- при необходимости — один sentence о visual direction без имитации конкретного автора.

Не отправлять клиенту внутренние negative prompts, длинный technical breakdown, hidden QA или весь reference-control contract, если это не запрошено.

## Статусы

`DRAFT → INTERNAL_READY → SENT_V01 → CHANGES_REQUESTED → SENT_V02+ → APPROVED_FOR_GENERATION → GENERATED → MASTER_SELECTED → UPSCALED → DELIVERED`.

## Gate

Generation запрещена, пока в `05-client-review.md` нет:

- `APPROVED_FOR_GENERATION: YES`;
- даты approval;
- источника подтверждения: email/message/meeting note;
- точных approved versions scenario + storyboard + video prompt.

Feedback не считается approval. Фразы вроде «нравится, но поправьте…» означают `CHANGES_REQUESTED`.

## Revision discipline

- Каждая отправка получает `v01`, `v02`, ...
- Сохранять original client wording и отдельно interpretation/action.
- После правок заново проверять timing, shot-size/angle harmony, Wolt compliance, reference numbering и соответствие EN краткому RU Client Story; parity ZH — только если ZH запрошен.
- Не перезаписывать approved storyboard; новая правка создаёт новую version.
