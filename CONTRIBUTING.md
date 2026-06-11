# Contributing

Thanks for considering a contribution. This repository collects Agent Skills for Microsoft 365 Copilot Cowork: multi-step workflows that produce real artifacts (files, drafts, dashboards) by composing Cowork's built-in capabilities. The bar is deliberately high. One well-built skill that survives contact with a real tenant is worth more than ten that look plausible.

Read this whole file before opening a pull request. PRs that miss the quality bar will be redirected or closed with a pointer to the relevant rule.

## The quality bar

Every skill in this repository must pass all of the following. No exceptions.

1. **Multi-step and artifact-producing.** The skill must orchestrate a workflow with several dependent steps and leave behind at least one named artifact in a stated location (for example `actions.md` in OneDrive at `/Documents/Cowork/meeting-actions/<date>-<meeting>/`). If the value fits in a single message, it is a prompt, not a skill (see redirects below).
2. **Compose the 13 Cowork built-ins, never duplicate them.** Cowork ships built-in skills (Email, Meetings, Word, Excel, PowerPoint, PDF, Enterprise Search, Daily Briefing and so on). Your skill should chain and constrain them, not reimplement what one of them already does on its own. "Summarise this meeting" duplicates the Meetings built-in; "turn this transcript into an actions file, confirmed tasks, and per-owner email drafts" composes it.
3. **Frontmatter is exactly `name` and `description`.** The SKILL.md YAML frontmatter contains those two keys and nothing else. `name` is kebab-case and identical to the folder name (folder `inbox-triage` means `name: inbox-triage`). `description` states what the skill does and when Cowork should invoke it.
4. **No scripts.** Skills are instructions plus Markdown reference files only. No Python, no shell, no executable anything, until Microsoft documents script execution for Cowork skills. If your workflow needs code to work, it does not belong here yet.
5. **File fallbacks for Planner and To Do writes.** Cowork writes to Planner and To Do are known to fail silently. Any skill that writes tasks must verify each write by reading it back, fall back to a file entry when the write cannot be confirmed, and report the per-item outcome honestly. Never let a skill claim a task was created without read-back confirmation.
6. **Safety rules are mandatory.** Every SKILL.md carries a SAFETY RULES section that includes at minimum: no deletes or overwrites without explicit user approval (version files instead, `actions-v2.md` and so on); email goes to Drafts only, never sent or scheduled; every generated document carries a DRAFT label in its title and first line until a human reviews it.
7. **British spelling in prose.** Licence, organise, behaviour, summarise. Code identifiers and Microsoft product names keep their official spelling, and we standardise on "artifact" (the form Microsoft's documentation uses), not "artefact".
8. **No em dashes.** Anywhere, in any file. Use commas, colons or parentheses. This is checked on review.
9. **Declared tested-in-Cowork status.** The skill's README.md carries a Status line stating plainly whether the skill has been run in a real Cowork tenant or is format-validated only. Never imply tenant testing that did not happen.

Also banned in all prose: hype words (unlock, supercharge, game-changing, delve, seamless, revolutionise), exclamation marks, invented statistics, invented URLs, and vague claims where a concrete path, filename or number would do. Every capability the skill claims must be executable from the instructions alone.

## What gets redirected

This repository is one of four. Submit to the right one:

- **Single-message artifacts** (a prompt that produces its full value in one reply, with no multi-step orchestration or saved files) belong in [awesome-microsoft-copilot-prompts](https://github.com/kesslernity/awesome-microsoft-copilot-prompts).
- **Copilot Studio agent configurations** (topics, knowledge sources, Studio-specific setup) belong in [awesome-copilot-studio-agents](https://github.com/kesslernity/awesome-copilot-studio-agents).
- **Free-tier instruction blocks** (paste-in agents for Copilot Chat that need no premium licence) belong in [awesome-copilot-chat-agents](https://github.com/kesslernity/awesome-copilot-chat-agents).

If a maintainer redirects your PR, it is a routing decision, not a quality judgement.

## Folder layout for a new skill

Each skill lives in one folder under the matching category in `skills/` (for example `skills/meetings/transcript-to-actions/`). The folder name is kebab-case and identical to the frontmatter `name`.

```
skills/<category>/<skill-name>/
├── SKILL.md          # The skill itself: frontmatter + instructions Cowork follows
├── README.md         # For humans browsing GitHub
└── references/       # Markdown reference files the workflow cites (templates, rules)
```

### SKILL.md

Frontmatter: exactly `name` and `description`. Body: these H2 sections, in this order, all present:

1. `## PURPOSE`
2. `## WHEN TO RUN`
3. `## INPUTS YOU GATHER`
4. `## WORKFLOW` (numbered, multi-step)
5. `## OUTPUT ARTIFACTS` (exact filenames and save locations)
6. `## FALLBACKS AND EDGE CASES`
7. `## SAFETY RULES`
8. `## QUALITY SELF-CHECK` (checkbox list the skill runs before its final report)

### README.md

For humans, not for Cowork. In this order:

- H1 title (the human-readable skill title, for example Inbox Triage)
- One-line value statement as a blockquote
- `## What it produces`
- `## Install in 60 seconds`: three steps (copy this folder into OneDrive at `/Documents/Cowork/skills/`, start a NEW Cowork conversation, use one of the trigger phrases)
- `## Example triggers`: 3 to 4 realistic user phrasings
- `## Why this exists`: one short paragraph giving either a working URL where the skill answers an observed public ask, or a plainly stated suite rationale for persona and suite skills
- `## Status`: for new submissions this reads `Tested in Cowork: pending (June 2026). Format-validated against the Agent Skills spec.` If you have actually run it in a tenant, say so and state the date.
- `## Changelog`: a table starting with `1.0 | 2026-06-10 | Initial version` (use your actual submission date)

### references/

Any template, extraction rule set, or format spec the WORKFLOW cites lives here as Markdown, referenced by relative path (for example `references/actions-template.md`). Markdown only. If the workflow does not need reference files, the folder may be empty, but the WORKFLOW must then be fully self-contained.

## The smallest PR: contribute a persona

The `review-board` skill convenes reviewer personas from single Markdown files, and the board is meant to grow beyond the seven C-suite roles it ships with. Contributing one is the lowest-friction PR this repository accepts:

1. Copy `skills/executive-review/review-board/references/persona-template.md`.
2. Fill in all six sections. KNOWN BLIND SPOTS is mandatory and must be written against the persona; the red-team stage depends on it.
3. Save it as `skills/executive-review/review-board/references/persona-<role>.md` (kebab-case role).
4. Add one row to the persona list in the review-board README's "Extend the board" section if you are adding a commonly requested role.

Persona rules: role archetypes only, never a real named individual or anything derived from one person's profile; no organisation-specific facts (those belong in a user's private `org-profile.md`); the standard prose rules above apply. The original wishlist (CHRO, General Counsel, Chief Product Officer, Head of Procurement, investor, customer advocate, frontline skeptic, works council representative) has shipped: those roles, plus a Chief Data Officer, now exist as nine bench skills in `skills/executive-review/`. New contributions should cover roles not yet shipped, for example a Chief Sustainability Officer, a CIO, internal audit, a regulator lens, or an industry-specific buyer, and follow the same template. A contributed persona may ship either as a bench skill folder of its own or as a single persona file PR; maintainers will route it to whichever form fits.

## PR checklist

Copy this into your PR description and tick every box:

- [ ] Skill is multi-step and produces at least one named artifact in a stated location
- [ ] Composes the Cowork built-ins; duplicates none of them
- [ ] Folder name and frontmatter `name` match in kebab-case; README H1 is the human-readable title
- [ ] Frontmatter contains exactly `name` and `description`, nothing else
- [ ] SKILL.md has all 8 H2 sections in the required order
- [ ] No scripts: instructions and Markdown reference files only
- [ ] Every Planner or To Do write has read-back verification and a file fallback
- [ ] SAFETY RULES cover: no deletes without approval, email Drafts only, DRAFT labels on generated documents
- [ ] README has all 8 sections, including a truthful Status line and a Changelog row
- [ ] "Why this exists" gives a working URL where the skill answers an observed public ask, or a plainly stated suite rationale for persona and suite skills
- [ ] British spelling throughout; zero em dashes; no hype words; no exclamation marks
- [ ] No invented statistics, URLs, or experiences anywhere
- [ ] Every claimed capability is executable from the instructions alone

One skill per PR. If the skill changes an existing one, add a Changelog row and bump the version instead of editing history.
