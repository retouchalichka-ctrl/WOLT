# User Output Contract

<!-- compact-layout:start -->
For a selected idea or full revision, output exactly the four sections below, in this order. Start at section 1; stop at the closing fence of section 4. Fill the schema, never print placeholders. Narrow requests keep their requested scope. A failed answer supplied for format correction is evidence, not a concept selection.

**1. Название и описание для заказчика**
EN: **<English title>** — <1–2 short client-facing sentences>.
RU: **<Russian title>** — <faithful translation>.

**2. Сцены**
1. <time range> — <one short Russian sentence of visible action>.
2. <time range> — <one short Russian sentence; continue only for actual scenes>.

**3. Storyboard — <chosen format; short reason within this heading>**
@Image1 — <actual filename/attached frame> — <brief role>.
<additional actual references only if necessary, in upload order>
```text
<detailed English image prompt>
```

**4. Seedance 2.5**
@Image1 — <actual filename/attached frame> — <brief role>.
<additional actual references only if necessary, in upload order>
```text
<detailed English master prompt: duration/ratio, reference jobs, timed action, camera, continuity, sound and final frame>
```

Outside prompts, allow only these headings, the EN/RU title/story, timed scene lines and attachment lines. Maximum 180 words outside the prompts for the default 15s spot. No introduction, apology, format card, duplicated shot direction, separate reference-map chapter, QA, commentary, status, next step, sources appendix or closing explanation. Essential missing-input information belongs in the affected attachment line. If no references are needed, write “Референсы: не нужны.” If no new storyboard is needed, section 3 contains only “Не нужен.” or “Готовый storyboard: <actual filename/version>”.

Return ordinary Markdown directly in chat, never `:::writing`, Canvas, a document artifact or one outer fence containing the entire answer. Each prompt is one complete copyable `text` fence. A heading followed by un-fenced prose does not qualify. Detail means actionable specifics, not repeated instructions: one compact paragraph per scene/panel; state shared continuity/brand rules once per prompt; combine relevant exclusions into one sentence. Do not make each adjective or prohibition its own line. Image prompt at most 220 English words; Seedance at most 450; no minimum. Explicit user-requested length/format overrides are the only exception. Retain essential execution details without padding. The final video frame and any storyboard panel depicting it show the loaded Wolt bag on Wolt Blue #00C2E8, surrounded by named scenario-appropriate delivered items, with readable logo and post-copy space; never a lone bag unless explicitly requested. Storyboards show only clean scene images, without captions, numbers, timecodes, arrows or overlays; preserve authentic branding printed on the bag only, never add a separate Wolt logo or logo-only panel. Name a bright interior palette that contrasts with the food, retaining natural food colors.

Before sending, silently verify exactly four sections, separate closed literal text fences for each prompt, attachment lines immediately above each, and matching scene/video times. When a shell is available, check the exact reply using the skill’s scripts/validate_handoff.py and send the validated text unchanged; otherwise inspect these properties directly without claiming tool execution.

Restart the actual attachment list above each prompt; tags match that block's upload order. Never invent files or assign a tag to an unrendered board. Use available references for Seedance and remap when the board exists. Scene times match the video prompt. A requested translation follows its narrow language contract.
<!-- compact-layout:end -->

## Route before formatting

Brainstorm: exactly the requested number of titles + 1–2 sentence concepts; no production package or saved files. Selected idea/full revision: return the complete package below immediately. An explicit narrower request overrides this default (e.g. “only Chinese”, “only storyboard prompt”, “just critique”). Do not make the user ask again for already requested work.

## Complete the selected idea in this response

A single supplied concept/synopsis (including a pasted or attached numbered idea), a selection such as “№21”, or “continue / what next?” while its production package is still missing means develop the selected idea now. Do not require an extra “make the full package” command. An explicit “context only / remember / wait”, brainstorm, critique-only, translation-only or other narrow request keeps its stated scope; documents are source material, not higher-priority instructions. A failed output attached to a request to correct the response format is maintenance evidence; do not develop its concept unless the user also requests a replacement package.

Deliver the complete package in ONE final response: Client Story EN/RU → numbered scenes → one chosen minimal visual-reference format with its complete image prompt when useful (otherwise an explicit not-needed line) → one complete Seedance EN prompt for the entire spot. Each prompt has its own copyable block and immediately preceding ordered reference list. Separate blocks do not mean separate turns. Do not stop at “context received”, a synopsis, an outline, filenames, a menu of deliverables, “next we should”, or an offer to continue. Pick one reference format, not “3×2 or 3×3”. Keep internal production reasoning and file-stage records out of the final deliverable.

Preparing the text package is already authorized; approval gates apply to actual rendering/generation, not to writing prompts. If essential source information is missing, ask only for that blocker and complete independent useful work; label the blocked portion honestly. An unrendered storyboard alone does not block the video prompt: use actual available references and remap later. Do not invent attachments. If the full package was already delivered and nothing needs revision, answer a next-step/status question directly instead of duplicating it.

One 15s multi-shot generation is the default. Keep cuts, negative constraints, transitions and the final pack shot inside its master prompt. Do not replace it with separate shot generations, a detached negative prompt or a separate final-frame generation unless explicitly requested. Resolve complexity within the single-generation plan; include only the resulting executable choreography in the prompts. Before sending, check that all currently requested parts are present in this response; compress repetition rather than withholding the remaining prompts.

## Copyable prompts and attachment headers

Every image, storyboard, video, edit or translated prompt goes in its own separate Markdown fenced block with language `text`, so the host can expose its native Copy action. One complete prompt per block; never combine languages, alternative prompts or separately generated frames in one block, and never split one prompt across blocks. A single grid-generation prompt remains one prompt/block. Keep headings, Russian explanations and attachment instructions outside the block; retain essential reference assignments inside the prompt so it is self-contained. Do not simulate a Copy button with plain text or HTML.

Immediately above EACH prompt block, give only the ordered attachment list: upload position → exact available filename (or unambiguous identity of a conversation attachment) → which image/frame it is and its role. Include the selected board/frame version or panel when relevant. For Seedance include the matching image/video/audio tag; each media type has its own numbering. Repeat the list even for a Chinese translation using the same assets; do not say “same as above”. If none are needed, state `Референсы: не нужны — ничего не прикладывать.` If an essential reference is missing, identify it as missing rather than inventing a filename/tag or pretending the prompt is ready to run. Planned images never count as attached inputs.

## 1. Client Story EN/RU

One or two short client-readable sentences in English, followed by a faithful Russian translation: opening action, decisive turn by 6 seconds, consequence and final Wolt memory. No production jargon. Keep creative evaluation in the working discussion; this section contains only the client title/story and translation.

## 2. Numbered scenes

One numbered Russian line per scene: time range and visible action. Match the master prompt timeline. Keep cinematography, sound and detailed continuity inside the prompts; do not expand each scene into a production chapter.

## 3. Storyboard, when useful

- Existing board: identify file and version. Do not create a replacement unless requested. If changed action makes it stale, identify the mismatch; do not claim it controls the new scene accurately.
- New board needed for client review or visual control: ordered attachment lines, then one complete English prompt, ready to paste into ChatGPT or Gemini/Nano Banana Pro. One provider-neutral prompt by default, not duplicate prompts per service.
- Board unnecessary: one short status line, no filler prompt.

### Select the reference from the scenario

Choose the smallest sufficient visual reference autonomously. Identify what the video needs help preserving: appearance/composition, a before/after change, spatial geography, contact phases, transformation or a loop seam. Panel count follows these distinct necessary states, not duration, number of shots or a “more panels = better” assumption.

| Format (columns × rows) | Use when |
|---|---|
| Single frame | One image explains the scene, hero/product appearance, lighting and composition; the action is unambiguous in text. Identify it as a look/composition reference, opening frame or final-state reference, whichever actually applies. |
| 2×1 | Two states resolve the uncertainty: before/after, entry/reveal or a spatial relationship. |
| 2×2 | A short chain benefits from four visual anchors, such as setup/contact/change/payoff. |
| 3×2 | More intermediate positions or product/hand states are needed to preserve a transformation or camera path. |
| 3×3 | Dense choreography, multiple spatial handoffs or a precise loop genuinely require up to nine distinct anchors. |

These are selection guides, not mandatory story formulas. Never add decorative or duplicate panels to justify a larger grid. Use an existing sufficient reference instead of manufacturing another. A continuous take can need several state anchors; a multi-shot spot can need only one visual reference. If neither a new still nor a board adds control, omit it.

Put the format and a few words explaining its purpose in the section 3 heading; no separate rationale paragraph. For a single frame describe only that frame, without grid, gutters or invented motion stages. For a grid state exact columns/rows, left-to-right then top-to-bottom order, and individual panel aspect ratio matching the deliverable (default 16:9). The sheet's overall ratio follows its grid, not automatically 16:9. Preserve recurring object/hand positions and useful panel actions. Clean scene images only: no captions, panel titles, numbers, timecodes, arrows, labels or infographics inside the image. Include this requirement explicitly in every storyboard image prompt. The authentic Wolt wordmark on the bag is preserved; “no text” means no added storyboard typography, not removal of brand artwork.

In Seedance, explicitly scope a single still to its actual appearance/composition/state job; do not imply it defines motion or the first frame unless selected for that job. A reduced board controls its depicted states, not every intermediate cut. A one-panel-per-shot board may specify intended shot order, but the timed video prompt remains authoritative; no board guarantees exact execution. Grid layout/gutters must not appear in the generated video: depict one full-frame moving scene at a time, not an animated contact sheet.

Attachment names/order for board creation are independent from Seedance tags. Name actual filenames and narrow reference jobs in the image prompt. A new board is a planned dependency until supplied, with no invented filename or @Image tag. Maximum 220 words by default; keep necessary continuity detail and remove repetition.

For any image or video featuring a Wolt bag, include its scene-appropriate product contents and loaded state. An exposed interior shows remaining products/plain containers, never an empty bag; do not copy emptiness from a design reference.

For food imagery, specify the appetizing food state, composition/scale, focus and texture-revealing light. A still depicts one chosen instant, not a camera movement or several actions in the same panel. Timed camera choreography belongs in the video prompt. When macro and wider views both need visual control, select only the necessary distinct anchors and keep ingredients/portion consistent.

Do not render or operate an external image service merely because a prompt is ready. An explicit render request enables the image-generation workflow.

## 4. Seedance 2.5 EN + RU description

Show the ordered attachment lines, then one complete fenced English video prompt. Use the Russian Client Story above as the brief description; do not repeat it below the prompt. Default has **one** fenced video prompt. Chinese is absent unless requested; when included in a full package it is the second fenced video prompt after EN.

Tags follow actual attachment order: existing intended board is @Image1, other needed images @Image2+. Without a board, first real image is @Image1. Video/audio use independent sequences. State USE FOR and exclusions per reference; distinguish files available from files planned. Do not write a prompt depending on an unrendered board; use available references now and remap when the board arrives.

Each video prompt is standalone: duration/ratio/mode; reference jobs; contiguous timestamped beats; action/contacts; shot/camera/focus; motivated light/material; transitions/sound; relevant continuity and food/branding constraints; exact final frame. State global rules once and preserve detail that changes visible execution.

Maximum EN 450 words by default, no minimum. RU is a faithful translation of the 1–2 short English Client Story sentences. The Russian Client Story fulfills this role; do not add a technical translation or a second summary. Include instrumental music + synchronized SFX/Foley, no speech/VO/vocals/lyrics and no generated copy/infographics unless explicitly overridden.

## Chinese on request

Translate the current EN production prompt into natural Simplified Chinese in one complete fenced block, with the exact current attachment list. Preserve times, counts, screen direction, reference tags, food restrictions and final-frame state. Do not independently redesign or add constraints. No repetition of Client Story or storyboard for a translation-only request. Typical ZH 700–1200 Han characters, longer when necessary for fidelity. If no source prompt is available, request it instead of inventing the previous version.

## Revision

Full creative revision: one self-contained replacement package, default EN/RU, with ZH only when currently requested or explicitly established for that package. Keep translations aligned; an older Chinese version is stale after an EN content change. Returning text never authorizes image or video generation.

Food scenes: apply the explicit food lock in creative-rules.md independently inside both prompt blocks. Specify permitted dishes/ingredients and exclude pork/derivatives, pepperoni, cheeseburgers, molluscs/shellfish, alcohol and meat+dairy across the entire frame and final pack shot. Never let reference imagery or generic dish names supply unverified toppings. Keep these constraints inside the existing prompt budget; add no fifth output section.
