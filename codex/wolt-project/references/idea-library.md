# Idea Library

Read this reference whenever capturing, selecting, merging, archiving or learning from an idea in managed workspace mode. In standalone mode there is no persistent cross-session duplicate claim; compare only with the current conversation and say so only when it materially affects the request.

## States

- `ideas/inbox/`: captured, not selected.
- `ideas/active/`: under development, review, generation or delivery.
- `ideas/archive/`: closed with an explicit reason. Successful delivery also belongs here after closeout.
- `ideas/INDEX.md`: derived overview; rebuild it after changes. Idea records remain authoritative.

## Duplicate check

Before creating an idea, run `scripts/find-similar-ideas.py` with the raw wording or proposed fingerprint and review candidates from every state. Reuse the completed brainstorm scan when selecting from its unchanged list; `new-idea.sh "name" --skip-search` avoids running it twice. Search matches words, not semantic equivalence; compare visible fingerprints yourself, including cross-language similarity. No matches is not proof of originality.

Compare: vertical, audience/job, hook device, core action/transformation, payoff and Wolt role.

- Same story engine and payoff: treat as `duplicate`; append the new raw wording to the existing record's Related requests.
- Same engine with a meaningful new hypothesis: create a linked `variant` and state what variable changes.
- Shared object, theme or style only: classify as `adjacent`; a separate record may be justified.

Do not infer originality from a different title. Do not suppress a genuinely different idea merely because it shares a motif.

## Learning

Never reduce outcome to one success/failure label. Track separately:

1. client acceptance and approval iterations;
2. creative clarity with specific feedback;
3. generation reliability and attempts to master;
4. technical delivery;
5. campaign performance with metric, value, source and measurement window.

Without evidence, record `unknown` or `no-data`. Approval is not performance; delivery is not performance.

## Closeout

For a developed idea, fill `09-retrospective.md`, update the idea's outcome review and relationships, move it to archive with `scripts/transition-idea.py ... archive --reason ...`, then run `scripts/rebuild-idea-index.py --write`.
