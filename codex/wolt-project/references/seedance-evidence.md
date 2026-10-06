# Seedance 2.5 — evidence and prompting scope

Verified 2026-09-08 against the [official model page](https://seed.bytedance.com/en/seedance2_5) and ByteDance Seed’s [official Seedance 2.5 announcement and prompt examples, 2026-07-31](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5).

The announcement describes up to 30 seconds per generation, multimodal references, extensions and timestamp-based editing. Its examples assign distinct subjects/scenes/motion to references and describe evolving action and camera behavior. It also acknowledges remaining problems with complex physical motion and multiple interacting subjects.

Our application: retain 15s as the Wolt client format; bind references to narrow jobs; write explicit timed action/camera beats; simplify difficult contacts before adding more constraints. These choices are consistent with the published examples, not a guarantee of exact execution. Check the selected product interface before relying on its attachment syntax, available modes, limits or resolution.

The 3+3+9 advertising structure, EN-first language, 250–450-word editing range, 4–6-shot preference, compact negative constraints and minimal storyboard selection are project conventions. The source does not establish these as universal Seedance requirements or prove Chinese outperforms English. Photoreal/high-key is the client art direction. No real generation comparison or latency benchmark was performed for this update.

## Image handoff: primary sources checked 2026-09-08

Google's [Gemini image-generation documentation](https://ai.google.dev/gemini-api/docs/image-generation) identifies Nano Banana Pro as Gemini 3 Pro Image and illustrates commercial photography prompts with a specific product, background, light purpose, angle, focus and ratio. Keep the user's selected Pro workflow; API model names and app controls are not interchangeable promises.

OpenAI's [image prompting guide](https://openai.com/academy/image-generation/) recommends clear subject/purpose/style, specific framing/light/constraints, explicit reference roles and targeted edits. A simple image need not have a long prompt.

Applied here: a short, self-contained single-frame or grid instruction; named attachment jobs; visible food state, texture, focus and light; explicit change/preserve boundaries. Camera motion and timed action belong in Seedance, not in a still's description. Longer prompts are justified by real continuity needs, not a word quota. Food appetite and filmmaker-inspired camera choices are our art direction, not vendor requirements. No generator has been tested in this audit.
