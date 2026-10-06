# Idea Library & Duplicate Control

## Local states

- `ideas/inbox/` — captured requests not yet selected.
- `ideas/active/` — concepts in development, client review, generation or delivery.
- `ideas/archive/` — closed concepts. Archive includes successful delivery as well as rejection, merge, pause or compliance block.
- `ideas/INDEX.md` — rebuildable local overview; individual records are authoritative.

All of these are production data and remain ignored by Git.

## Before creating an idea

1. Search every state with `scripts/find-similar-ideas.py "<raw idea or fingerprint>"`.
2. Compare the story engine: hook device, core transformation/action, payoff and Wolt role.
3. Classify the relationship:
   - `duplicate`: same engine and payoff; merge the raw request into the existing record;
   - `variant`: same engine but a meaningful new audience, vertical, payoff or execution hypothesis;
   - `adjacent`: shared motif/style only; a separate idea is allowed.
4. Create a new file only when it adds a meaningful hypothesis. Similar titles alone do not prove a duplicate, and different titles do not prove originality.

## Evidence-based learning

Track client acceptance, creative clarity, generation reliability, delivery and campaign performance separately. “Client approved”, “video generated” and “campaign performed” are different claims.

Record performance only with a metric, value, source and measurement window. Without those, use `no-data` or `unknown`; never convert preference or anecdote into a result.

## Closing an idea

1. Fill the project `09-retrospective.md` when a developed concept closes.
2. Copy the evidence-backed conclusions into the idea record.
3. Add variant/duplicate relationships and the reusable/avoid lesson.
4. Move it with `scripts/transition-idea.py <file> archive --reason "<reason>"`.
5. Rebuild `ideas/INDEX.md` with `scripts/rebuild-idea-index.py --write`.

An archived successful mechanism may be reused as a deliberate variant, but not silently renamed and presented as a new idea.
