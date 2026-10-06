# Client Review & Approval Gate

## Submission

Prepare the internal storyboard sheet plus a short 2–4 sentence scenario for client handoff. Send to a client only when the user explicitly authorizes sending. It must explain the 0–3 hook, main action by 6s, and 6–15 resolution/pack shot without production jargon.

## Versioning

Record each `v01`, `v02`, ... submission with date, storyboard file, scenario version, channel, decision, exact feedback, interpretation, and resolved version. Never overwrite an approved asset.

## Approval test

Generation is allowed only when `05-client-review.md` contains:

- `APPROVED_FOR_GENERATION: YES`;
- approval date and source/evidence;
- exact approved scenario version;
- exact approved storyboard version;
- exact approved video-prompt version.

Positive feedback with requested changes is `CHANGES_REQUESTED`, not approval. If approval evidence is missing, continue revision/preparation but stop before generation.

## Revision audit

After each change, recheck timing, bag/logo timing, shot-size/angle harmony, Wolt compliance, reference order, storyboard-to-prompt alignment, and EN consistency with the short RU story, and ZH parity only when requested. A code validator checks structure only, not these semantic properties.
