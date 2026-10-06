# Wolt Brand & Compliance Rules

Этот файл — локальный digest актуальных правил проекта. При конфликте с новым прямым client brief побеждает client brief, а изменение фиксируется в `memory/DECISIONS.md`.

## Brand

- Main color: Wolt Blue `#00C2E8`.
- Secondary: Blueberry Blue `#021738`, Milk White `#F8F8F8`.
- Полная официальная палитра (11 цветов, HEX, print specs и правила применения): [WOLT_COLORS.md](WOLT_COLORS.md), сверено по Wolt Bynder 2026-09-09. В интерьере — только лёгкие акценты по сценарию, без квот/обязательного голубого доминирования; правило 80% Wolt Blue относится к графической площади без photography/3D, не к площади интерьера.
- Wolt Blue должен присутствовать естественно: поверхность, фон, prop, деталь courier wardrobe или акцент.
- Единственный branded object в generated footage — Wolt kraft paper bag с исходным food-icon print и Wolt logo.
- Нельзя генерировать отдельный logo lockup, floating logo, partner logo, end-card logo или второй Wolt mark без прямого client override.
- Standalone logo assets хранятся только в `assets/brand/archive/logos/`.
- Все остальные продукты и упаковки: generic, textless, unbranded, без имитации узнаваемого third-party design system.
- Generated copy запрещён: captions, prices, promos, CTA, claims, disclaimers, legal, decorative words и watermarks добавляются в post.
- Default audio: instrumental music and synchronized SFX/Foley only. No dialogue, VO, spoken words, vocal phrases or lyrics unless the user explicitly requests them.
- Default visual communication: no infographic, charts, diagrams, arrows, UI panels, callouts, labels, explanatory icons or data overlays unless explicitly requested. Artistic VFX remains allowed when it is part of the scene/action rather than an information layer.

## Hero bag

- Wolt bag никогда не пустой: внутри всегда есть продукты по сценарию, в том числе после извлечения части заказа. Если внутренность попадает в кадр, видны оставшиеся продукты или их generic textless containers, не пустая полость/голое дно. Закрытый пакет имеет правдоподобные наполненный объём, вес, контакт с опорой и натяжение ручек; открывать или переполнять его специально не нужно. Содержимое согласовано между кадрами; пустоту исходного bag reference не копировать.

- Сохранять geometry, kraft color/material, handles, food-icon print density и logo placement.
- Обеспечивать believable weight, paper flex, contact shadow, occlusion и контакт с руками/поверхностями.
- Не допускать morph, duplication, extra logo или случайную смену дизайна.
- Финальный кадр — pack shot наполненного kraft-пакета Wolt на фирменном голубом фоне Wolt Blue `#00C2E8`, в окружении доставляемой еды, продуктов или товаров, подходящих сценарию. Конкретный состав назвать в промпте и согласовать с сюжетом; пакет не должен стоять один, без товаров вокруг. Композиция привлекательная, logo читаемый, контакты/тени реалистичные, фактуры сохранены, есть чистое место под post copy. Остальная упаковка generic/textless; food/Pharmacy rules сохраняются. Этот финал отражается в соответствующем storyboard-кадре и последнем beat Seedance, если пользователь/клиент явно не задал другой финал.

## Courier privacy & framing

- Approved courier references могут управлять clothing silhouette, Wolt Blue accents и geometry of jacket, thermal backpack, helmet, gloves, bike/scooter gear.
- Они не управляют face identity, casting, location, photographic style, visible logos или text.
- В сценах с курьером лицо никогда не показывать. Верхняя граница кадра остаётся ниже подбородка; eyes, mouth, full chin и любые узнаваемые facial features находятся вне кадра во всех storyboard panels и video shots.
- Кадрировать естественно: chest/shoulders, hands, torso, legs и gear должны выглядеть намеренно, без awkward neck crop.
- Courier clothing/gear остаются без видимых logo/text, если client не дал отдельный override; Wolt bag по-прежнему единственный branded object.

## Halal/client food rules

Проверять не только hero dish, но и фон, полки, холодильник, стол, упаковки и audio cues.

### Never show

- pork, bacon, ham, salami, pepperoni, prosciutto, chorizo, lard, pork gelatin;
- alcohol и визуальный алкогольный контекст: bottles, cans, wine glasses, taps, bar shelves, cocktails;
- meat и dairy вместе в одном блюде или meal setup;
- molluscs/shellfish;
- blood, raw-meat gore, ambiguous deli meat или неопределённое мясо;
- background props/packaging, подразумевающие запрещённые ингредиенты.

### Safe patterns

- Pizza: только margherita, four-cheese или clearly vegetarian; без meat/seafood.
- Burger: halal beef, halal chicken, fish или vegetarian patty; без cheese, bacon, ham и creamy dairy sauce. Безопасная сборка: sesame bun, lettuce, tomato, pickles, onion, dairy-free sauce.
- Noodles/rice/kebab/bowl: явно назвать halal chicken/beef, fish, egg, tofu или vegetables; без dairy рядом с meat.
- Snacks/grocery: fruits, vegetables, nuts, crisps, popcorn, bread, olives, dates, dairy-only или clearly plant-based items в plain packaging.
- Desserts: alcohol-free и gelatin-free; отдельно от meat dishes.

Compliance достигается выбором безопасного блюда до prompting, а не маскировкой запрещённого ингредиента ракурсом.

## Verticals

- Restaurants: sensory food hook, затем delivery resolution через Wolt bag.
- Groceries: delivery/unpacking/cooking/snack setups; все labels/brands удалены, alcohol context исключён.
- Pets: natural safe cat/dog/bunny behavior; pet packaging plain and unbranded.
- Pharmacy: neutral wellness, licensed context или skincare/cosmetics без medical promise.

## Pharmacy

Не показывать close-up pills/tablets, syringes/needles/IV, prescription drug names, before/after, surgical scenes, pain/distress as a sales device, diagnosis imagery, guaranteed/cure claims, teens/children using health products или dramatic body transformation.

OTC, devices, healthcare professionals и licensed locations допустимы только при наличии необходимых approvals и без specific endorsement/diagnosis. Если market/approval неизвестны, использовать neutral wellness concept и generic textless packaging.

## Format

- Default: 15s, 16:9, one Seedance generation.
- 0–3s: хук уже работает визуально; не тратить это окно на подготовку. Ранний Wolt kraft bag/logo предпочтителен; если клиент/пользователь просит logo в первые 3s, узнаваемое появление logo на kraft bag в этом окне обязательно и встроено в действие. Пакет может быть на заднем плане или мельком; foreground, крупный план и отдельная пауза не обязательны. При обычном просмотре должно достаточно рано быть понятно, что рекламируется Wolt; неразличимая вспышка или только blue accent не заменяют узнаваемость бренда.
- 3–6s: динамичные escalation/turn; заказчик предпочитает основное действие и decisive reveal в первые 6s. Не переносить главный смысл во вторую половину. Динамика остаётся понятной по действию и географии.
- 6–15s: нескучно завершать ролик через consequence, реакцию, sensory proof, развитие шутки или payoff. Красивый pack shot допустим, но не заполнять все 9s неподвижным финалом.
- Visual default: яркая сочная advertising image с high-key lighting. Светлая сцена, мягкие открытые тени, чистые насыщенные цвета, выразительные контролируемые блики, сохранённые объём и фактура. Не путать high-key с пересветом, плоским светом, белым фоном или тотальным glow; Wolt Blue, kraft print и еда остаются различимыми.
- Main focus в центре без причины для смещения.
- Final beat может decelerate для food/bag readability и negative space.

## Photoreal production finish

Пользователь требует максимально реалистичное фото- и видеокачество: camera-believable materials, food texture, kraft fibers, skin when visible, coherent contact shadows/reflections, weight/inertia и естественное движение. High-key сохраняет объём и фактуру. Исключать plastic/waxy CGI appearance, excessive sharpening, smeared motion и frame-to-frame texture/identity flicker. Сюрреалистичный story device допустим, если выглядит материально убедительно снятым. Это эстетическая цель, а не обещание native 4K или гарантии результата модели.

## Appetite and food cinematography

Для food-led рекламы вызывать аппетит — явная creative objective. Приветствуются выразительная предметная фуд-съёмка, сочное макро и красивые читаемые общие планы; ориентиры вроде Daniel Schiffer переводятся в конкретные движения камеры, монтаж, свет и фактуру. Не ограничиваться именем автора в prompt и не копировать готовый ролик.

Камера раскрывает еду: описать стартовый ракурс, траекторию, конечную композицию и объект фокуса. Один основной move на beat; мотивированные push-in, короткий parallax arc, close-focus pass или action match выбираются по сценарию, не все сразу. Макро не должно терять узнаваемость блюда, общий план возвращает пространство и Wolt context. Состав, порция и состояние еды согласованы между планами.

Выбирать 2–3 правдивые sensory cues конкретного блюда: хруст корочки, влажный мякиш, свежий срез фрукта, оседающий соус, умеренный cheese pull только в допустимом vegetarian dish. Не добавлять пар/конденсат/блеск по привычке, не делать еду резиновой или жирно-пластиковой. Короткое замедление подчёркивает контакт; не тормозит hook 0–3s и turn до 6s. Food styling соблюдает все ограничения выше; для Pets/Pharmacy аппетит не навязывается.


## Interior color and logo placement — user clarification 2026-09-08

Интерьер — осознанная сочная рекламная палитра: основной насыщенный цвет фона + сдержанный акцент, контрастирующие с едой. Конкретные цвета задавать в image/video prompts; не уходить по умолчанию в бежевый интерьер и блеклый lifestyle. Сохранять естественный цвет еды/кожи, фактуру и объём. Финальный pack shot остаётся на Wolt Blue #00C2E8. Логотип Wolt — только подлинная печать на hero-пакете: никаких отдельных logo-плашек, кадров-заставок, водяных знаков, логотипов на фоне или поверх изображения.


## Reusable color schemes — 2026-09-09

Стилевые референсы задают энергию, формы и контраст, но не чужую палитру, принты или брендинг. Сохранять Wolt brand look; для декора выбирать официальные цвета и одну подходящую рабочую схему C01–C06, финал P01 отдельно. Лёгкие акценты означают дозированное применение, а не обесцвечивание HEX; интерьер без процентных квот. Натуральные цвета еды, кожи, дерева и крафта сохраняются. Карты — наши сочетания официальной палитры, не отдельно утверждённые Wolt макеты. См. [WOLT_COLOR_SCHEMES.md](WOLT_COLOR_SCHEMES.md).

## Food lock — 2026-09-09

Ограничения еды проекта Wolt (повторно подтверждены пользователем 2026-09-09): запрещены свинина и производные, пепперони/салями/бекон/ветчина, моллюски и сочетание мяса с молочными продуктами в одном блюде; сохраняется более строгое существующее правило для общего meal setup. Чизбургеры не использовать. Не обходить запрет словами «halal pepperoni» или заменой сорта мяса. Пицца — явно margherita/четыре сыра/овощная, без мяса и seafood. Мясной бургер — явно halal beef/chicken, овощи и dairy-free соус, без сыра, сливок, масла и другой молочной составляющей; булка также dairy-free. Это ограничения данного проекта/клиента, а не универсальное определение халяля.

В каждом самостоятельном storyboard- и Seedance-промпте назвать точное разрешённое блюдо/состав и кратко продублировать запреты; одной фразы «halal food» недостаточно. Не оставлять модели выбор начинки через «pizza», «burger», «assorted food» или «same as reference». Проверить каждое блюдо, соусы, начинку, фон, содержимое пакета и финальный pack shot. Запрещённую еду из референса не копировать: назначить референсу только безопасные свойства и явно задать замену. Найденный дефект исправлять новой версией, не перезаписывая исходник или утверждённый результат.
