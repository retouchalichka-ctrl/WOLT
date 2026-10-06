# Managed Wolt Workspace

This workspace was initialized by the portable `$wolt-project` skill. It stores persistent production state while the installed skill supplies the Wolt creative, compliance, storyboard and Seedance rules.

## Start

- Ask for a short brainstorm; candidates are not saved until selected.
- Send a brief; originals remain unchanged under `briefs/<date-name>/source/`.
- Select an idea; it moves to `ideas/active/` and receives a named folder under `projects/`.
- Run `scripts/validate-project.py projects/<project-folder>` after a package is written.

## Privacy

The included `.gitignore` excludes real briefs, ideas, projects, incoming assets and private memory. Do not weaken that boundary without reviewing the exact files that would become trackable.

## Skill

This workspace intentionally does not contain a second copy of the skill instructions. Install and invoke `$wolt-project`; the workspace holds state and deterministic helpers.

## Output default

Selected ideas immediately receive Client Story EN/RU, conditional storyboard prompt, and one complete Seedance 2.5 English prompt with exact attachments. Russian is only a brief description, not a technical translation. Chinese is available on request. Images/storyboards normally use prepared prompts in ChatGPT or Gemini/Nano Banana Pro. Local rendering requires an explicit request.
