# Brief-to-4K Delivery Pipeline

## 1. Client brief intake

Создать `briefs/YYYY-MM-DD-<slug>/`, сохранить оригиналы без изменения в `source/`, извлечь objective, audience, market, vertical, deliverable matrix, references, mandatory/forbidden details, rights, claims, deadlines и open questions. Сохранять начальный двухзначный номер месяца/выпуска из имени файла. Явно отмечать, является ли новый файл cumulative и заменяет ли предыдущие monthly briefs; cumulative latest используется как current source, а старые файлы не складываются повторно в team package. Отделить direct client facts от inference.

## 2. Ideation

Создать несколько brief-derived directions и, когда полезно, self-initiated направления вне brief. Brainstorm candidates не сохранять до выбора. Выбранную или явно запрошенную к сохранению задумку сначала записать как `ideas/inbox/YYYY-MM-DD-<slug>.md` со source brief или `self-initiated`, hook, product role, compliance risk и reason to pursue; при активной разработке перевести её в `ideas/active/`.

## 3. Selection & project folder

После внутреннего выбора создать `projects/YYYY-MM-DD-<slug>/` из `templates/project/`, связать brief/idea/project, сохранить исходную идею в `00-idea.md`, а относящиеся refs — в `assets/`.

## 4. Attachment classification

Классифицировать файлы до присвоения tags. Отделять наблюдаемые факты от creative inference. Если роль реально меняет нумерацию и неясна, задать один короткий вопрос; в остальных случаях продолжить.

## 5. Compliance before concept

До разработки сцены выбрать безопасный vertical/dish/product set. Проверить halal, bag-only branding, generic textless packaging, no generated copy и Pharmacy rules.

## 6. Scenario & timing

Зафиксировать:

- strongest element;
- главную retention/generation/compliance проблему, если она есть;
- одно decisive improvement.

Концепт строится как cause-and-effect: first-frame hook → escalation → payoff → Wolt memory. `0–3s` содержит hook и желательно early bag/logo exposure; к `6s` main story/reveal уже понятен; `6–15s` — consequence, resolution, beauty или pack shot; продолжать менять видимую информацию, не растягивать статичный финал на 9 секунд.

Смысл должен читаться визуально без речи и инфографики. Default soundtrack: instrumental music bed plus precise synchronized SFX/Foley. Dialogue, VO, vocals/lyrics и explainer graphics добавляются только по explicit user request.

## 7. Shot-size and angle grammar

Использовать ladder: `detail/ECU → CU → MCU → MS → MLS → WS → EWS`. На обычной склейке новая крупность обычно должна отличаться минимум на две позиции, а угол/высота/ось камеры — заметно меняться (ориентир, а не закон: примерно 30°+ или очевидно иная перспектива). Оценивать не арифметику, а цельность: кадр должен добавлять информацию и не создавать accidental jump cut. Нарушение допустимо, если художественно сильнее; записать motivation.

## 8. Mode

Выбрать один primary mode: text-to-video, image-to-video, reference-to-video, edit, extend, white-model или green-screen. Standard spot — one 15s generation. Временные диапазоны целые, непрерывные, без gaps/overlaps.

## 9. Reference map

Использовать минимальное количество refs. Каждому дать одну-две функции, exclusions, priority и time applicability. Если storyboard будет приложен, он `@Image1`; иначе phantom storyboard tag не создаётся.

## 10. Storyboard & prompt development

Тип visual reference выбирается по сценарию автоматически: один кадр, `2×1`, `2×2`, `3×2` или `3×3` (столбцы × строки). Брать минимальное достаточное число различных состояний для контроля appearance/composition, action/contact, geography или loop; не приравнивать число панелей числу shots. Коротко объяснить выбор. Подробная decision guide — в OUTPUT_CONTRACT.md. Никакого текста, labels, timecodes или декоративной типографики внутри sheet. Сначала подготовить prompt и asset list. Обычно пользователь переносит prompt и assets в ChatGPT или Gemini/Nano Banana Pro. Render здесь выполнять только после отдельной явной команды через `imagegen`, используя текущую версию prompt. При возврате изображения проверить фактические anchors/continuity и source version; существование board не означает approval. Параллельно можно подготовить полный Seedance prompt, но не запускать video generation.

На `INTERNAL_READY` заполняются только project files `00–05`. Журнал generation, upscale/delivery, final QA и retrospective остаются нетронутыми до своего gate.

## 11. Client review gate

Клиент получает storyboard и короткий описывающий сценарий, а не внутренний production dump. Записывать submission version, дату, feedback и решение. Все правки обновляют связанные scenario/storyboard/video-prompt versions. Generation разрешена только после явного `APPROVED_FOR_GENERATION: YES`.

## 12. Final prompt & generation

Один complete multi-shot prompt на весь spot. Архитектура: deliverable → idea → refs → timeline → performance/blocking → camera/focus → lighting → production design → edit/VFX → sound → continuity → 3–7 relevant failure protections → exact final frame.

Полнота не требует многословия: каждое global rule писать один раз, а в timed beats оставлять только action-specific instructions. Ориентиры для обычного spot: EN `350–600` words, RU описание 2–4 предложения, ZH только по запросу с приоритетом точности.

По умолчанию один полный English fenced video prompt; русский Client Story — только краткое описание, без технического перевода. Native Simplified Chinese — отдельным блоком только по запросу. Перед generation зафиксировать exact prompt version и attach list; чаще всего storyboard `@Image1` + Wolt kraft bag `@Image2`.

## 13. Generation QA & iteration

Перед выдачей один раз проверить смысл, причинность, Wolt role, continuity и compliance; исправить конкретные дефекты без ритуальных self-scores. Для первой ревизии менять одну major variable: contradiction → ref assignment → simplify choreography/camera/VFX → timing/cut.

## 14. Upscale & delivery

После выбора approved master выполнить отдельный UHD 4K upscale до `3840×2160`, сохраняя 16:9, frame rate, duration, audio sync и цвет. Проверить bag/logo edges, faces/hands, food texture, flicker, halos, sharpening, banding и audio. Записать tool/model/version/settings и не утверждать, что Seedance сгенерировал native 4K. Контейнер/codec/bitrate/colorspace уточняются по client delivery spec.
