# Project Package

Файлы создаются сразу, но заполняются только по текущему gate:

1. `00-idea.md`
2. `01-scenario.md`
3. `02-reference-map.md`
4. `03-storyboard.md`
5. `04-seedance-prompts.md`
6. `05-client-review.md`
7. `06-generation-log.md` — только после client approval
8. `07-upscale-delivery.md` — только после master selection
9. `08-qa.md` — только по активной QA-стадии
10. `09-retrospective.md` — после закрытия или получения результата

На `INTERNAL_READY` файлы `06–09` остаются нетронутыми шаблонами: не заполнять их `TBD`, `unknown` или пустыми логами.

Idea-specific inputs лежат в `assets/`; client submissions/feedback — в `client/`; storyboard versions — в `storyboard/drafts/` и `storyboard/approved/`; генерации — в `outputs/generations/`; masters — в `outputs/approved/`; 4K и финалы — в `outputs/upscaled/` и `outputs/delivery/`. После закрытия проекта выводы возвращаются в idea record, затем идея уходит в локальный архив.
