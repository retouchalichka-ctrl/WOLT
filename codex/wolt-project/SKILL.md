---
name: wolt-project
description: "Create distinctive Wolt ad ideas, client stories, storyboard prompts and production-ready Seedance 2.5 prompts. Works from any chat, with optional managed project memory, approvals and delivery. The sole Wolt domain skill."
---

# Wolt Project

For a developed spot, follow the literal four-section layout in [output-contract](references/output-contract.md): title/story EN/RU, timed scenes, conditional storyboard prompt, Seedance prompt. Start at section 1 and stop after the final prompt; titles belong inside section 1.

## Final reply gate

For a full production handoff, return ordinary chat Markdown, never a document/canvas/`:::writing` wrapper. A titled prose section is not a copyable prompt. Section 3 (when a new board is needed) and section 4 each contain their own literal opening ` ```text ` line and closing ` ``` ` line; keep attachment lines outside. Read [output-contract](references/output-contract.md) before composing.

Validate the **exact final reply**, not just project files. When Python is available, write it to a temporary Markdown file and run `python3 <this-skill>/scripts/validate_handoff.py <reply.md>`. Repair reported issues before sending that same Markdown unchanged; do not print the check report in the production package. The check covers four sections, independent fences, references, scene/video timing, and budgets: 180 words outside prompts, 220 storyboard, 450 video. These are maximums for the default 15s handoff; shorter is welcome. Only an explicit user-requested format/length override changes these limits. For a narrow request, follow its scope instead of applying the full-package checker. Without Python, inspect these same properties silently; never claim a script ran.

Make strong, visually readable Wolt ads quickly. Deliver one decisive creative solution with production detail that earns its place. Never invoke or read `wolt-dop` or `seedance-2-5-dop`.

Challenge a concrete weakness and offer one executable improvement when warranted; do not manufacture objections. Respect informed creative preferences. Viral potential is a hypothesis, never a promised outcome.

## Mode and minimum reads

- **Managed:** current directory or an ancestor has `.wolt-project.json` or the matching workspace structure. Use local state. Workspace `AGENTS.md` is already active.
- **Standalone:** otherwise use this skill and the conversation. Do not search other disks, projects or personal chats for memory. Do not create files unless asked. No cross-session originality claim.
- **Bootstrap:** only when explicitly asked to initialize a workspace, run `scripts/init_workspace.py <target>`. `--merge` requires a request to add missing files to a non-empty target; originals are never overwritten.

Read each needed resource once per task; reuse already loaded, unchanged context. Batch independent reads. Do not load every reference or walk the whole workspace.

| Request | Read |
|---|---|
| Brainstorm | [creative-rules](references/creative-rules.md); managed idea index and relevant brief requirements; one duplicate search |
| Selected idea / full revision | Creative rules, [production-prompt](references/production-prompt.md), [output-contract](references/output-contract.md); only affected idea/project, refs and applicable brief |
| Brief intake | Supplied brief and [workflow](references/workflow.md); format skill only if needed |
| Approval / feedback | Affected versions and [client-gate](references/client-gate.md) |
| Storyboard prompt / image handoff | Output contract; [storyboard-render](references/storyboard-render.md) only for rendering or external-board intake |
| Chinese translation only | Current final EN prompt and attachment map; production-prompt language contract; no new ideation |
| Generation / upscale / delivery | Approved inputs and [delivery](references/delivery.md) |
| Save / archive / outcome | Affected record and [idea-library](references/idea-library.md) |
| Mechanism audit / maintenance | Relevant mechanism, memory and scripts; do not develop production concepts as a side effect |

In managed mode read `memory/DECISIONS.md` for conflicts or mechanism changes; broader memory only for missing facts. Latest explicit client/user instruction overrides recorded memory, then local brand canon, then bundled references. Do not treat the newest directory name as proof of an active brief. Internal team packages may contain `assets/internal-briefs/`; use only the relevant brief.

Bundled brand assets live at `assets/workspace-template/assets/brand/`. Available files are not automatically attached references. Never invent attachment tags.

For color-map/styling work, read [color-schemes](references/color-schemes.md). Select an appropriate reusable scheme when useful; reference pictures convey character, never permission to copy foreign palettes/prints/branding. Palette cards are in `assets/color-maps/`; describe actual color roles inside prompts, without adding output sections.

## Fast creative execution

**Brainstorm:** return exactly the requested number of distinct short concepts: title plus 1–2 sentences showing opening action, turn/payoff and Wolt role. Compare story engines, not renamed props. One duplicate scan across managed inbox/active/archive is enough; reuse it when selecting from that list if unchanged. The search is lexical assistance, not proof of originality. Create no idea/project files until selection or explicit save.

**Selected idea:** A single supplied concept/synopsis (including a pasted/attached numbered idea) counts as the selected idea to develop now unless the user says context-only, remember, wait, or asks for a narrower task. “Continue / what next?” with a missing package also means deliver it now. In ONE final response give Client Story EN/RU, a compact numbered scene list, one chosen minimal visual-reference format with full image prompt when useful, and the full Seedance EN master prompt. Each prompt gets its own copyable block and ordered reference header within that same response. Never end with context acknowledgement, an outline, a menu, file links alone or an offer to do the package later. Preparation needs no generation approval. Ask only for an essential blocker; an unrendered board alone is not one. Keep one 15s multi-shot generation: integrate cuts, relevant negatives and final pack shot into the master prompt; do not substitute separate shot renders or a separate end-frame prompt without an explicit request. If the full package is already delivered, answer an ordinary next-step question directly.

Return the full current production package by default; no extra “go to production” confirmation. In managed mode create/merge one idea record, link one project, and fill only `00–05` at `INTERNAL_READY`. Keep `06–09` untouched until their stages. Standalone returns the same creative package without filesystem ceremony.

Use the output-contract as the sole final-answer layout. Detailed production reasoning is input to the two prompts, not additional user-facing sections. Each prompt has its own actual attachment list immediately above its text fence. Write one compact paragraph per scene/panel, and state shared rules once per prompt. A supplied failed output accompanying a format complaint is maintenance evidence, not a selected concept to develop. Revisions return the replacement four-section package; narrow requests return only their requested part. Preserve earlier client-facing versions and invalidate affected approval when content changes.

Use one creative pass and one focused check before delivery. Reopen only a specific unresolved weakness; do not run repeated internal tournaments, scoring loops or synonym rewrites. Ask only when the answer changes the concept, mandatory format, rights, claim or essential reference; otherwise state a brief assumption and continue.

## Detail and latency budget

- Prefer 4–6 shots for 15 seconds; a motivated continuous take is valid. Shot count is a default, not a quota.
- `01-scenario.md` is a compact decision/shot record, never a second video prompt. Other files hold their own stage data, not repeated prose.
- Default handoff limits: storyboard ≤220 English words; Seedance EN ≤450; outside the prompts ≤180. RU faithfully translates the 1–2 short client-story sentences. Retain necessary action/contacts/brand rules by removing repetition; no minimum word count.
- Each standalone prompt states its own essential global rules once. Beats describe visible changes and cinematography. Avoid generic lens/light/quality adjectives that do not change the result.
- Managed: run `scripts/validate-project.py <project>` once after writing; rerun only to verify repairs. It checks structure, not creative quality, visual compliance or semantic parity. Perform one focused content check; do not repeat structural QA manually. Standalone uses that content check without looking for a validator.
- Routine creative work needs no web trend hunt unless requested or a current factual claim needs verification. Do not change Codex model/settings to meet a speed target. Report measured speed only after an actual timed run.

## Production defaults and boundaries

- 15 seconds, 16:9, one complete Seedance 2.5 multi-shot generation unless explicitly overridden. “Viral” alone does not change the client's aspect ratio.
- `0–3s` readable hook; decisive story readable by `6s`; `6–15s` consequences, sensory proof and payoff. This is not a nine-second static pack shot. The client prefers dynamic action concentrated in the first 6s. Early Wolt recognition is preferred; a client/user request for logo in 0–3s makes recognizable bag-logo exposure in that window mandatory. Background or a brief moving glimpse is valid if Wolt is identifiable at normal playback; no forced close-up or logo hold. Keep the remaining 9s rewarding with consequence, reaction, sensory proof or payoff.
- Visual default: maximally photoreal, camera-believable premium stills/video; natural materials, weight, contact and motion, no plastic CGI or waxy food. Surreal story rules remain valid when their material execution looks filmed. Bright, juicy high-key advertising imagery, open soft shadows, clean saturated color, controlled highlights and preserved food/kraft texture. High-key does not mean overexposed, flat, glowing or necessarily white-background.
- For brand-color props/interior details, read [brand-colors](references/brand-colors.md): 11 verified HEX colors and official usage scope. Interior branding uses only light scenario-appropriate accents, with no percentage quota or predominantly blue-room requirement; 80% is a graphic-layout rule excluding photography/3D.
- Interior art direction: name a saturated background palette that contrasts with the hero food, plus a restrained accent; avoid default beige-on-beige styling while preserving natural food/skin colors.
- Food-led ads must create appetite: truthful sensory action, selective juicy macro and attractive readable wider compositions, with motivated camera movement. Translate filmmaker references into concrete shot/motion/light choices; follow creative-rules without adding a mandatory montage or slowing the first 6s.
- The Wolt bag always contains scene-appropriate products. Show remaining contents whenever the interior is visible; never an empty cavity, including after removal. Closed bags retain believable loaded volume and weight.
- Final frame: loaded Wolt bag on Wolt Blue `#00C2E8`, surrounded by scenario-appropriate delivered food/groceries/goods, never a lone bag. Preserve readable logo and post-copy space; apply this to the final storyboard state and Seedance beat unless explicitly overridden.
- Only the hero kraft bag carries branding/print. No standalone/background/overlay Wolt logo or logo-only title card in any storyboard or video frame. All other packaging and courier gear are generic, textless, unbranded. No generated copy or infographics by default.
- Food restrictions are mandatory in every standalone image/video prompt: no pork/derivatives, pepperoni, salami, bacon, ham, molluscs/shellfish, alcohol or meat+dairy combinations; no cheeseburgers. Name permitted ingredients for every dish, including background and final pack shot; pizza is meat-free, meat burgers have dairy-free buns/sauce and no cheese. Reference food never overrides these rules. Apply the complete food and Pharmacy rules in creative-rules to the whole frame. These are project/client constraints, not a universal definition of halal. Courier shots always crop below the chin.
- Instrumental music and synchronized SFX/Foley; no speech/VO/vocals/lyrics by default. Visual meaning survives muted playback.
- Select the smallest sufficient reference from the scenario: single frame, 2×1, 2×2, 3×2 or 3×3 (columns × rows). Choose by distinct visual states/continuity needs, not shot count; briefly explain the choice. Use the output-contract selection guide. Default delivery is a copy-ready image prompt and exact attachments for ChatGPT or Gemini/Nano Banana Pro. Rendering here requires an explicit image request and `imagegen`; never launch an external generation by implication.
- Video generation requires evidenced `APPROVED_FOR_GENERATION: YES` for exact current versions. Preparation and translation do not require generation approval.
- After master selection, 4K is a separate upscale using the deliverable's aspect ratio (default landscape UHD 3840×2160), not native Seedance 4K.
- Preserve originals and approved versions; never alter `assets/brand/` for a concept. Never commit/push `briefs/`, `ideas/`, `projects/`, `assets/incoming/` or `memory/private/`. Publishing the mechanism requires an explicit request.
