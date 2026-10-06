# Wolt Seedance Production Prompt

Read this only when developing or revising a selected Wolt spot, storyboard or Seedance prompt.

## Choose one mode

- `text-to-video`: no visual identity needs preservation;
- `image-to-video`: one still controls an object, identity, composition or start state;
- `reference-to-video`: assets control narrowly assigned visual or motion properties;
- `edit`: keep most of a supplied video and state explicit `LOCK`, `CHANGE`, `INTEGRATE` and time range;
- `extend`: define the exact handoff state, locked continuity and one new dramatic function;
- `white-model` or `green-screen`: use only when the user actually supplies or requests that workflow.

Default Wolt spot uses one 15-second generation. This is the client format, not a claimed model duration limit. A single prompt may contain multiple shots; “one generation” does not mean “one continuous take”. Keep transitions, relevant negative constraints and the final pack shot within the complete master prompt. Do not substitute separate shot generations or a separate end-frame prompt unless requested; simplify difficult choreography within the default first.

Official capability grounding and the boundary between vendor facts and our directing heuristics: [seedance-evidence.md](seedance-evidence.md). Read it for capability questions or integration updates, not for every concept.

## Prompt architecture

Write one standalone production instruction in this order:

1. deliverable, duration, ratio and mode;
2. core idea and first visible action;
3. narrow reference assignments and exclusions;
4. contiguous timestamped beats covering `0–15s`;
5. playable action, blocking and object contacts;
6. shot sizes, angles, camera paths and focus behavior;
7. photoreal advertising finish with believable material, weight, contact and motion; motivated bright high-key lighting: soft open shadows, clean saturated colors, controlled highlights, preserved food/product texture and volume;
8. complementary cuts, transitions and integrated VFX;
9. instrumental music plus synchronized SFX/Foley;
10. continuity protections and exact final frame: loaded Wolt bag on Wolt Blue #00C2E8, surrounded by named delivered items appropriate to this story, readable logo and post-copy space; never a lone bag;
11. only 3–7 failure protections relevant to the scene.

Whenever a Wolt bag appears, state that it contains scene-appropriate products throughout. Specify remaining contents after removal and visible products/plain containers in interior views; no empty cavity or bare bottom. For a closed bag, describe loaded volume/weight without forcing it open or overflowing. Reference emptiness must not override this rule.

Name the interior background/accent colors selected to contrast with the food; when using brand colors, take the exact name/HEX and usage scope from brand-colors.md. The prompt must exclude standalone logos/logo title cards and state Wolt bag-only branding, generic textless packaging, no generated copy/infographics, applicable food/Pharmacy constraints and intentional negative space for post copy.

Use compact production syntax: one paragraph per timed beat, shared continuity rules once, relevant exclusions in one sentence. Do not repeat a global lock in every scene or put each adjective/prohibition on a separate line. State global requirements once, then keep timestamped beats specific to visible action, shot, camera and transition. Prefer four to six shots for a 15-second spot; more shots require a clear action or continuity reason. The default master prompt is at most 450 English words, with no minimum; the brief Russian client story remains outside it. Remove repetition rather than omitting required choreography. Chinese is optional on request, usually `700–1200` Han characters, with fidelity taking priority over length. Do not expand the prompt to mirror the internal scenario file.

## Timing and edit

- `0–3s`: working first-frame hook and immediate action. Early bag/logo is preferred; if requested, recognizable logo on the kraft bag in this window is mandatory. A background placement or brief moving glimpse is valid if Wolt registers at normal playback; no obligatory close-up or hold, no floating overlay.
- `3–6s`: escalation or decisive reveal completed.
- `6–15s`: consequence, food/product proof, resolution and readable final pack shot. Add a fresh visible payoff after the early reveal; do not fill nine seconds with a static hold. A typical last 1.5–3s can stabilize for recognition, unless a loop or client spec needs another ending.
- Every cut adds information. Preserve screen direction, action phase, eye trace and object count.
- Use motivated action matches, texture matches or cause-and-effect transitions instead of a decorative transition pack.

For food-led spots, direct appetite explicitly: identify the edible hero, one truthful sensory action and the texture revealed. Use selective macro plus a readable hero-wide when useful, with consistent ingredients/portion across cuts. Describe camera start → path → landing and focus target; keep one dominant move per beat. A short speed ramp or slow-motion contact can emphasize the food, but preserve the 0–3s hook and turn by 6s. Translate filmmaker/style references into these visible decisions rather than relying on a name. Select only techniques that serve this scene; do not turn this into a mandatory shot checklist.

## Reference contract

- Storyboard + images: storyboard `@Image1`, real images `@Image2+` in attachment order. A reduced board controls its depicted states, framing and continuity, not every intermediate cut. A one-panel-per-shot board specifies intended shot order; the timed prompt remains authoritative and execution is not guaranteed.
- Storyboard only: storyboard `@Image1`.
- Images only: first real image `@Image1`.
- Video and audio use independent `@Video1+` and `@Audio1+` sequences.
- Every reference gets `USE FOR`, `DO NOT COPY/CHANGE`, priority and applicable time range.
- Bag reference controls only geometry, kraft material, handles, food-icon print and logo placement.
- Courier references control only clothing silhouette, Wolt Blue and gear geometry. Suppress courier logos/text and keep every courier frame below the chin.

Never say “copy the reference” and never create a tag for a file that will not be attached. Internal @Image1/@Video1 notation is a reference map; bind it to the actual attachment tokens/slots exposed by the selected Seedance interface before execution. Do not assume identical limits or tag syntax across providers.

## Storyboard

Use an existing storyboard for depicted states, framing, composition and continuity. A one-panel-per-shot board may specify intended shot order; the timed prompt remains authoritative. Do not replace it without an explicit request. A single frame controls only its assigned look/composition/state and is not automatically the opening frame or a motion reference.

Select one frame or a 2×1, 2×2, 3×2 or 3×3 grid (columns × rows) using the output-contract guide. Match the number of visual anchors to the actual scenario uncertainty, not shot count. For grids, instruct Seedance to use the depicted states as references for full-frame video, never reproduce the grid/gutters or animate the sheet. The image contains no captions, numbers, timecodes, labels or decorative typography. Rendering still requires a separate explicit user request.

## Language contract

Default: one complete English fenced video prompt, with the brief Russian Client Story serving as its description; no duplicate RU technical translation. No Chinese unless requested. When requested in the full package, add a complete native Simplified Chinese block after EN. For “only Chinese”, return the current attachment list and complete Chinese prompt only.

Build all languages from the same shot plan. Preserve numeric time ranges, counts, screen direction, references, food rules and final frame; natural Chinese phrasing must not change execution. Follow output-contract for revisions and narrow requests.

## QA

Silently repair contradictions, unsafe food, weak Wolt role, timing gaps/overlaps, random cuts, impossible choreography, logo drift, phantom references and excess constraints. For a failed first generation, change one major variable at a time: contradiction, reference assignment, complexity, then timing/cut.

Food scenes: apply the explicit food lock in creative-rules.md independently inside both prompt blocks. Specify permitted dishes/ingredients and exclude pork/derivatives, pepperoni, cheeseburgers, molluscs/shellfish, alcohol and meat+dairy across the entire frame and final pack shot. Never let reference imagery or generic dish names supply unverified toppings. Keep these constraints inside the existing prompt budget; add no fifth output section.
