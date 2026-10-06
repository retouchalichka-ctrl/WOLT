# Workflow & Workspace State

This file applies to managed workspace mode. In standalone mode, use the same creative and approval logic in the response but do not assume or create these paths. Initialize a workspace from the bundled template only after an explicit request.

## Brief

Create `briefs/YYYY-MM-DD-<slug>/` from `templates/brief/`. Originals go unchanged into `source/`. Separate explicit client facts, inference, conflicts, and open questions. Build both brief-derived and optional self-initiated directions.

## Ideas

For exploratory option lists, search the index once and return distinct short directions without creating a file per option. Before saving or developing a chosen idea, read `references/idea-library.md`; reuse a just-completed scan for an unchanged selection, otherwise search all idea states once. Each selected or explicitly saved non-duplicate direction starts at `ideas/inbox/YYYY-MM-DD-<slug>.md`; selected work moves to `ideas/active/`. Record source, fingerprint, hook, bag role, main action, viewer response, compliance risk and next action. Idea files are library records, not full production folders.

## Selected project

Create `projects/YYYY-MM-DD-<slug>/` from `templates/project/`. Link the source brief and idea. Populate files only when their lifecycle stage is active:

1. Concept development through `INTERNAL_READY`: `00-idea.md` through `05-client-review.md`.
2. After explicit client approval: `06-generation-log.md`.
3. After a master is selected: the applicable generation/delivery sections of `08-qa.md`, then `07-upscale-delivery.md`.
4. At closeout or after measurable results: `09-retrospective.md` and the final sections of `08-qa.md`.

The project scaffold may contain all files, but future-stage templates remain untouched. Do not fill them with `TBD`, `unknown`, empty logs or speculative values merely to make the folder look complete.

## Revisions

Create new versions for client-facing scenario, storyboard, and affected prompt. Preserve the client's exact wording and a separate interpretation/action. A revision request does not authorize generation.

## User handoff

For a selected concept or full revision, deliver the complete output-contract package in the same final response. Do not append stage, file links, gate status or next actions to the four-section production package; keep them in internal project records. For an explicit status-only request, report only the relevant state. Do not make the user reconstruct the deliverable from previous turns or files.

## Closeout and reuse

On closeout, update the retrospective and idea record with separate evidence for client acceptance, creative clarity, generation reliability, delivery and campaign performance. Archive with an explicit reason, rebuild the index, and preserve duplicate/variant relationships. Reusing an archived mechanism requires a declared variant hypothesis; renaming alone does not make it new.

## Challenge protocol

When a proposed direction is weak or wrong:

1. Name the exact risk: retention, clarity, product role, compliance, feasibility, continuity, or delivery.
2. Explain the likely visible consequence, not an abstract objection.
3. Give one stronger replacement that preserves the user's underlying intent.
4. If the issue is subjective, allow the user to keep the original after seeing the tradeoff. If it is factual/compliance-critical, do not silently validate it.
