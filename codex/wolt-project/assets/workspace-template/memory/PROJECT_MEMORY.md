# Project Memory

## Purpose

Persistent state for Wolt advertising work managed by the installed `$wolt-project` skill.

## Local preferences

- Exactly four sections: title/story inside section 1; end after the Seedance fence. Outside prompts only headings, title/story, scene timing and reference lines. One compact paragraph per beat inside prompts, shared rules once.
- Dense production handoff: English title + Russian translation; 1–2 sentence client story EN/RU; one timed sentence per scene; conditional detailed storyboard prompt; detailed Seedance EN prompt. Each prompt has its own ordered attachments. No extra QA/continuity/camera chapters. Storyboard panels are clean scene images without captions, numbers, timecodes or overlays; authentic bag branding remains.
- Communication language: Russian unless the user requests otherwise.
- Seedance package: complete English prompt; Russian Client Story is a brief description only, no technical translation. Chinese only on request.
- Final frame: loaded Wolt bag on Wolt Blue #00C2E8, surrounded by scenario-appropriate delivered items, with readable logo and post-copy space. Never a lone bag; match the final storyboard panel and Seedance beat.
- Images/storyboards normally use a copy-ready prompt in ChatGPT or Gemini/Nano Banana Pro; rendering here requires an explicit request.
- Record client acceptance, creative clarity, generation reliability, delivery and campaign performance separately.

Add workspace-specific preferences only when they are stable and evidenced by the user or client.

Visual reference выбирается по сценарию: один кадр или 2×1 / 2×2 / 3×2 / 3×3 (столбцы × строки). Минимально достаточный формат по состояниям/контактам/географии; не автоматическая сетка и не число shots. Одной фразой объяснить выбор. Single frame может задавать вид/композицию или конкретное состояние, не обязательно первый кадр; сетка не должна появляться в видео.

Actual reply check: default full handoff is ordinary chat Markdown, never Canvas/:::writing. Each prompt is an independent literal text fence. Validate exact output via the bundled scripts/validate_handoff.py when Python is available; otherwise inspect directly. Project-file validation is separate. Default maxima: outside 180 words, image 220, video 450; no minimum.

Интерьер — осознанная сочная рекламная палитра: основной насыщенный цвет фона + сдержанный акцент, контрастирующие с едой. Конкретные цвета задавать в image/video prompts; не уходить по умолчанию в бежевый интерьер и блеклый lifestyle. Сохранять естественный цвет еды/кожи, фактуру и объём. Финальный pack shot остаётся на Wolt Blue #00C2E8. Логотип Wolt — только подлинная печать на hero-пакете: никаких отдельных logo-плашек, кадров-заставок, водяных знаков, логотипов на фоне или поверх изображения.

В интерьере допустимы лёгкие фирменные акценты Wolt; никаких процентных требований, обязательного преобладания голубого или полностью брендового интерьера. Для деталей/реквизита брать точные названия и HEX из WOLT_COLORS.md / skill brand-colors.md. Акценты применять дозированно по контрасту с едой; не считать generic cobalt/teal/coral официальными цветами. Правило 80% голубого не распространять на фотографию/3D. Цветные детали не разрешают дополнительные логотипы; logo остаётся только на пакете.


## Wolt brand look — 2026-09-09

Стилевые референсы задают энергию, формы и контраст, но не чужую палитру, принты или брендинг. Сохранять Wolt brand look; для декора выбирать официальные цвета и одну подходящую рабочую схему C01–C06, финал P01 отдельно. Лёгкие акценты означают дозированное применение, а не обесцвечивание HEX; интерьер без процентных квот. Натуральные цвета еды, кожи, дерева и крафта сохраняются. Карты — наши сочетания официальной палитры, не отдельно утверждённые Wolt макеты.

## Food lock — 2026-09-09

Ограничения еды проекта Wolt (повторно подтверждены пользователем 2026-09-09): запрещены свинина и производные, пепперони/салями/бекон/ветчина, моллюски и сочетание мяса с молочными продуктами в одном блюде; сохраняется более строгое существующее правило для общего meal setup. Чизбургеры не использовать. Не обходить запрет словами «halal pepperoni» или заменой сорта мяса. Пицца — явно margherita/четыре сыра/овощная, без мяса и seafood. Мясной бургер — явно halal beef/chicken, овощи и dairy-free соус, без сыра, сливок, масла и другой молочной составляющей; булка также dairy-free. Это ограничения данного проекта/клиента, а не универсальное определение халяля.

В каждом самостоятельном storyboard- и Seedance-промпте назвать точное разрешённое блюдо/состав и кратко продублировать запреты; одной фразы «halal food» недостаточно. Не оставлять модели выбор начинки через «pizza», «burger», «assorted food» или «same as reference». Проверить каждое блюдо, соусы, начинку, фон, содержимое пакета и финальный pack shot. Запрещённую еду из референса не копировать: назначить референсу только безопасные свойства и явно задать замену. Найденный дефект исправлять новой версией, не перезаписывая исходник или утверждённый результат.
