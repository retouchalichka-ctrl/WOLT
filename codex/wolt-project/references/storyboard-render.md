# Explicit Storyboard Rendering

Use this only after a separate explicit user request to generate/render/create the storyboard image. Preparing or revising a storyboard prompt is not authorization to render it.

## Before rendering

1. In managed mode identify the project and read `03-storyboard.md`; standalone uses the current prompt and conversation attachments without requiring project files.
2. Confirm the exact current storyboard prompt version and `Attach for storyboard creation` list.
3. Use an existing storyboard only when the user explicitly asks to replace/regenerate it; otherwise preserve it.
4. If a required user-supplied asset is missing, ask the user to attach it again. Omit optional assets rather than inventing them.
5. Do not silently rewrite the scenario, shot order, visual direction, Wolt rules, or courier framing while moving from prompt to render.

## Render

- Apply the `imagegen` skill.
- Use the already prepared prompt and the listed local or conversation assets.
- Generate the selected single frame or exact grid from the current prompt, one image per explicit request unless variants are requested. Do not silently turn a single frame into a board or expand a grid. Inspect the selected state/job for a still; inspect reading order and distinct anchors for a grid.
- Keep the Wolt/halal, no-text, shot-size/angle harmony, continuity, and courier-below-chin rules from the prompt.

## After rendering

- Show the rendered storyboard to the user.
- Record prompt version, exact asset list, request date, and draft output in `03-storyboard.md` and `storyboard/drafts/` when a local artifact is available.
- Do not mark it client-approved or use it for Seedance until the user/client selects or approves it.
- If the render has a visible problem, identify the specific defect; do not spend another generation without a new explicit request unless the user originally requested multiple variants.

## External ChatGPT / Gemini workflow

For an image-prompt request, provide one copy-ready English prompt and exact named assets; do not invoke imagegen or operate either external service. Show @Image1/@Image2 upload-slot labels above the prompt with actual filenames and jobs. These labels do not assume native provider syntax; inside the image prompt identify refs by filename/order. Seedance receives its own tagged list later.

When the user returns a board, inspect the actual image against the current shot anchors, bag identity, object/hand geography and food rules. Record the supplied file and source prompt version when known. If unknown, mark source version unverified. Identify material mismatches and one precise correction; do not silently substitute a new story or mark the board client-approved. An existing mismatched board cannot claim control over revised actions.
