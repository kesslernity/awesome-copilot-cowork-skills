# Awesome Copilot Cowork Skills

> **15 workflow skills plus a 16-persona executive review suite for Microsoft 365 Copilot Cowork.** Drop a folder into OneDrive: no admin, no Copilot Studio, no app package. The same SKILL.md runs verbatim in Claude Code.

> **Preview status, June 2026.** Cowork is a [Frontier preview](https://adoption.microsoft.com/en-us/copilot/frontier-program/), not generally available. You need a paid M365 Copilot licence plus Frontier programme enrolment, with Anthropic enabled as a subprocessor for your tenant. EU tenants are off by default. The documentation is prerelease, so limits and behaviour may change. GA date and pricing are unknown. This is a community library, not affiliated with or endorsed by Microsoft.

[![GitHub stars](https://img.shields.io/github/stars/kesslernity/awesome-copilot-cowork-skills?style=flat-square)](https://github.com/kesslernity/awesome-copilot-cowork-skills/stargazers)
[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
[![Format: Agent Skills open standard](https://img.shields.io/badge/format-Agent%20Skills%20open%20standard-blue.svg)](https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-plugin-development)

---

## Who This Is For

You are inside the Frontier preview with a paid M365 Copilot licence, and you want Cowork to produce files rather than chat answers. The skills here are built for project managers, IT and MSP admins, executive assistants, and sales and finance people.

Quick check: Microsoft's [Use Cowork](https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/use-cowork) guide shows the Cowork home page. If you cannot open Cowork the way that guide describes, you are not in the preview yet; start with [awesome-copilot-chat-agents](https://github.com/kesslernity/awesome-copilot-chat-agents) instead.

Everyone else, there is a better repo for you:

- **No Copilot licence?** [awesome-copilot-chat-agents](https://github.com/kesslernity/awesome-copilot-chat-agents): 52 agents that run on the free Copilot Chat tier included with any commercial M365 licence.
- **Want a governed, org-wide agent instead of a personal skill?** [awesome-copilot-studio-agents](https://github.com/kesslernity/awesome-copilot-studio-agents): 78 agents built for M365 Copilot premium in Copilot Studio.
- **Just need prompts?** [awesome-microsoft-copilot-prompts](https://github.com/kesslernity/awesome-microsoft-copilot-prompts): single-message prompts for M365 Copilot.

---

## What a Cowork Skill Is (60 seconds)

A custom skill is a folder you drop into OneDrive at `/Documents/Cowork/skills/<skill-name>/`, containing one file named `SKILL.md`: YAML frontmatter with exactly two fields (`name`, `description`), then Markdown instructions. Cowork discovers it automatically at the start of each new conversation. No registration, no admin, no package.

The format rules every skill in this repo follows:

- `name` is kebab-case and identical to the folder name. The Agent Skills open standard requires this. Some published examples do not follow this; every skill here does, which is why these files also run verbatim in Claude Code and VS Code.
- `description` is the trigger. Cowork is model-invoked: it activates a skill by matching conversation context against descriptions. Ours are written in third person with concrete trigger conditions ("Use when the user ..."), one to three sentences, under 500 characters.
- Limits: 50 custom skills per user, 1 MB per `SKILL.md` (we target under 300 lines, body under roughly 5,000 tokens), maximum 20 companion files per skill, 10 MB total per skill. Companion files are referenced by relative path from the skill root, forward slashes, one level deep.
- No scripts. Whether Cowork executes bundled scripts is undocumented, so every skill here is instructions plus Markdown reference files only.
- Per Microsoft's documentation, Cowork reads and writes OneDrive and SharePoint files only, never local device files.

### How a custom skill compares

| | Custom skill (this repo) | Built-in skill | Plugin skill | Copilot Studio agent |
|---|---|---|---|---|
| What it is | A folder with a `SKILL.md` in your OneDrive | One of the 13 capabilities Cowork ships with | The same `SKILL.md` format packaged into an M365 app package | A separate agent you @mention, built in Copilot Studio |
| Who deploys it | You, with a folder drop | Microsoft | IT admin or the Microsoft 365 App Store | A maker, via a publish and approval flow |
| Scope | Your account only | Every Cowork user | Tenant-wide | Whoever it is shared with |
| Registration | None, auto-discovered at the start of each new conversation | Not applicable | Manifest validation, then admin deployment | Copilot Studio publish flow |
| Can it reuse a built-in's name? | No, built-ins take naming priority | Not applicable | No | Not applicable |

### The 13 built-in skills

Word, Excel, PowerPoint, PDF, Email, Scheduling, Calendar Management, Meetings, Daily Briefing, Enterprise Search, Communications, Deep Research, Adaptive Cards ([Microsoft's list](https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/use-cowork#cowork-skills)).

Every skill in this repo **composes** these built-ins into a workflow. None duplicates one, and none reuses a built-in's name.

### The boundary

If it fits in one chat message, it is a prompt, and it belongs in [awesome-microsoft-copilot-prompts](https://github.com/kesslernity/awesome-microsoft-copilot-prompts). Everything here plans and executes a multi-step workflow and produces artifacts: documents, spreadsheets, files with named save locations, often with maintained state between runs.

---

## Install in 60 Seconds

Sixty seconds per skill, once you have the repo downloaded:

0. Get the files. On the repo page, click **Code**, then **Download ZIP**. Extract it anywhere outside OneDrive; you will copy individual skill folders from the extracted copy. (Developers can `git clone` instead, also outside OneDrive.)
1. In OneDrive, open `/Documents/Cowork/`. If it does not exist yet, create it yourself; Microsoft's [own instructions](https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/use-cowork#create-custom-skills) say to create the folder if it is missing. Inside it, create a lowercase `skills` folder.
2. Copy a skill folder from the extracted repo (the whole folder, including its `references/` subfolder where present) into `/Documents/Cowork/skills/`. Keep the folder name exactly as shipped: it must match the `name` field inside.
3. Start a **new** Cowork conversation and use one of the example triggers from the skill's README. New to Cowork itself? Microsoft's [Use Cowork](https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/use-cowork) guide shows where the Cowork home page lives and how conversations work.

Do this from a desktop: either drag the extracted skill folder into OneDrive in the browser, or copy it into your synced OneDrive folder in Explorer or Finder. The OneDrive mobile app cannot upload folders, so come back on a desktop if you are reading this on your phone.

Three community-reported gotchas:

- The `skills` folder name is lowercase and case-sensitive. `Skills` will not be found.
- Discovery happens at the **start** of a conversation. A conversation that is already open will not see a skill you just added; start a new one.
- Copy folders into OneDrive rather than working with git there. A `.git` directory inside an actively syncing OneDrive folder can cause sync conflicts and partial-state corruption; keep your clone or extracted copy elsewhere and copy folders across. (The tenant-side wipe incidents of May and June 2026 are a separate problem, documented with a source in [`skills-backup-keeper`](skills/meta-skills/skills-backup-keeper/), which exists for exactly that reason.)

Still stuck, or wondering about licences, the EU, safety, or scheduling? The [FAQ](FAQ.md) answers the questions readers actually ask.

**Give this to IT:** for org-wide deployment, Microsoft documents an admin path that packages the same skill folders into a Microsoft 365 app package, deployed as a plugin through the admin centre or the Microsoft 365 App Store. See [Build plugins for Copilot Cowork](https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-plugin-development). Personal OneDrive skills currently need no admin involvement; admin controls for them may be added later.

---

## Featured: The Executive Reviewers

Before you walk a document into a steering committee, run it past the executive who will actually interrogate it. Sixteen reviewer personas, each a standalone skill: the C-suite seven (CFO, COO, CTO, CMO, CRO, CBO and CISO) plus a bench of nine (CHRO, General Counsel, product, data, procurement, investor, customer advocate, frontline skeptic and works council representative).

Every reviewer reads your document through its own mandate and produces the same artifact: a DRAFT review with a verdict, cited findings, risks, and the five interrogation questions you will face in the real meeting. Run one persona standalone (a CFO pass on a business case, a CISO pass on a vendor proposal), or run several in sequence and reconcile the conflicts yourself; the disagreement between two reviews is usually where the real work is.

---

## Skill Directory

Every skill folder contains the `SKILL.md` plus a README with install steps, triggers and a changelog.

**Status, June 2026:** every skill is format-validated against the Agent Skills spec. Tenant testing is under way: `meeting-prep-onepager` and `no-delete-guardrail` passed a live Frontier tenant test on 2026-06-11 (see their READMEs); the rest carry "tenant test pending" until they pass, and per-skill READMEs gain tested-with-date lines as they do.

### Executive Review
`skills/executive-review/`

**The 16 reviewer personas.** Every reviewer produces the same artifact through its own lens: a DRAFT review .docx with a verdict, cited findings, risks and five interrogation questions. Each runs standalone.

The C-suite seven: [`cfo-reviewer`](skills/executive-review/cfo-reviewer/) · [`coo-reviewer`](skills/executive-review/coo-reviewer/) · [`cto-reviewer`](skills/executive-review/cto-reviewer/) · [`cmo-reviewer`](skills/executive-review/cmo-reviewer/) · [`cro-reviewer`](skills/executive-review/cro-reviewer/) · [`cbo-reviewer`](skills/executive-review/cbo-reviewer/) · [`ciso-reviewer`](skills/executive-review/ciso-reviewer/)

The bench: [`chro-reviewer`](skills/executive-review/chro-reviewer/) · [`general-counsel-reviewer`](skills/executive-review/general-counsel-reviewer/) · [`cpo-reviewer`](skills/executive-review/cpo-reviewer/) · [`cdo-reviewer`](skills/executive-review/cdo-reviewer/) · [`procurement-reviewer`](skills/executive-review/procurement-reviewer/) · [`investor-reviewer`](skills/executive-review/investor-reviewer/) · [`customer-advocate-reviewer`](skills/executive-review/customer-advocate-reviewer/) · [`frontline-skeptic-reviewer`](skills/executive-review/frontline-skeptic-reviewer/) · [`works-council-reviewer`](skills/executive-review/works-council-reviewer/)

### Meetings
`skills/meetings/`

| # | Skill | What it produces | Example trigger |
|---|-------|------------------|-----------------|
| 1 | [`meeting-prep-onepager`](skills/meetings/meeting-prep-onepager/) | One-page Word prep brief for any upcoming meeting | "Prep me for my next meeting" |
| 2 | [`transcript-to-actions`](skills/meetings/transcript-to-actions/) | Action-items file, confirmed To Do or Planner tasks, DRAFT owner emails | "Turn this transcript into action items and follow-up emails" |

### Project Management
`skills/project-management/`

| # | Skill | What it produces | Example trigger |
|---|-------|------------------|-----------------|
| 3 | [`project-status-tracker`](skills/project-management/project-status-tracker/) | Four living project files plus a weekly status-YYYY-WW.docx draft | "Produce this week's status report for helios-migration" |

### Daily Briefings
`skills/daily-briefings/`

| # | Skill | What it produces | Example trigger |
|---|-------|------------------|-----------------|
| 4 | [`custom-daily-brief`](skills/daily-briefings/custom-daily-brief/) | Role-tuned morning brief DOCX: emails, calendar, Teams mentions, deadlines | "Run my daily brief" |
| 5 | [`commitment-catcher`](skills/daily-briefings/commitment-catcher/) | Commitments ledger (made and owed, overdue flagged) plus To Do entries | "What did I promise people in the last 24 hours?" |

### Email & Inbox
`skills/email-inbox/`

| # | Skill | What it produces | Example trigger |
|---|-------|------------------|-----------------|
| 6 | [`inbox-triage`](skills/email-inbox/inbox-triage/) | Dated triage report, five-bucket inbox sort, labelled reply drafts | "Triage my inbox and draft what needs a reply" |

### Writing & Communication
`skills/writing-communication/`

| # | Skill | What it produces | Example trigger |
|---|-------|------------------|-----------------|
| 7 | [`write-like-me`](skills/writing-communication/write-like-me/) | Voice profile file plus email and docx drafts in your voice | "Draft this email in my voice" |
| 8 | [`branded-deck-builder`](skills/writing-communication/branded-deck-builder/) | Brand-compliant .pptx deck on your template, plus outline and compliance report | "Build a 12-slide deck on our company template" |

### Reporting & Analysis
`skills/reporting-analysis/`

| # | Skill | What it produces | Example trigger |
|---|-------|------------------|-----------------|
| 9 | [`report-attachment-analyzer`](skills/reporting-analysis/report-attachment-analyzer/) | Trend spreadsheet plus DRAFT delta summary from recurring emailed reports | "Update the trends for the weekly sales report" |
| 10 | [`news-monitor-digest`](skills/reporting-analysis/news-monitor-digest/) | Dated 5-8 item news digest as Word doc or email draft | "Sweep my news sources and build today's digest" |

> **Data boundary note for admins:** `news-monitor-digest` reaches outside the tenant by design. It fetches external web content through the Deep Research built-in on every run, and its safety rules treat all fetched web content as untrusted data. No other skill in this library reads anything outside the tenant.

### IT Operations
`skills/it-operations/`

| # | Skill | What it produces | Example trigger |
|---|-------|------------------|-----------------|
| 11 | [`sharepoint-review-sweeper`](skills/it-operations/sharepoint-review-sweeper/) | Overdue-review spreadsheet plus per-owner reminder email Drafts, never sent | "Which documents in our library are past their review date?" |

### Dashboards & Microapps
`skills/dashboards-microapps/`

| # | Skill | What it produces | Example trigger |
|---|-------|------------------|-----------------|
| 12 | [`project-dashboard-builder`](skills/dashboards-microapps/project-dashboard-builder/) | Single-file offline HTML dashboard from project tracker files | "Build a dashboard for the website-relaunch project" |

### Sales & BD
`skills/sales-bd/`

| # | Skill | What it produces | Example trigger |
|---|-------|------------------|-----------------|
| 13 | [`estimate-to-sow`](skills/sales-bd/estimate-to-sow/) | DRAFT statement-of-work .docx from your estimate spreadsheet, maths validated first | "Turn estimate-acme-q3.xlsx into a statement of work" |

### Meta-Skills
`skills/meta-skills/`

| # | Skill | What it produces | Example trigger |
|---|-------|------------------|-----------------|
| 14 | [`no-delete-guardrail`](skills/meta-skills/no-delete-guardrail/) | Approval gates, versioned files, append-only change journal every conversation | "Clean up my project folder, but ask before removing anything" |
| 15 | [`skills-backup-keeper`](skills/meta-skills/skills-backup-keeper/) | Dated skills-folder backups with manifest, plus append-only session journal | "Back up my skills folder before I edit anything" |

---

## Also Runs in Claude Code and VS Code

Microsoft's plugin-development page, [Build plugins for Copilot Cowork (Frontier)](https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-plugin-development), states that skills use the Agent Skills open standard, the same format supported by Claude Code, Visual Studio Code Copilot, Gemini CLI, Cursor, JetBrains Junie, and 30+ other AI tools.

Identical format, identical files. To reuse any skill in this repo:

- **Claude Code:** copy the skill folder into `~/.claude/skills/` (available in every project) or into a project's `.claude/skills/`.
- **VS Code (GitHub Copilot):** copy the skill folder into `.github/skills/` in your repository.
- **Org-wide Cowork plugin path:** Microsoft publishes a [conversion script](https://aka.ms/copilot-cowork-plugin-conversion-script) (`Convert-ClaudePluginToMOS3.ps1`) that packages skill folders into a Microsoft 365 app package.

The Cowork-specific parts of each skill (OneDrive save paths, Planner and To Do fallbacks, Drafts-only email) degrade gracefully in other runtimes: the workflow and output structure still apply.

---

## Quality and Safety Bar

This repo was written as one batch in early June 2026, built from the demand and failure threads on r/microsoft_365_copilot; that is why every changelog starts at 1.0 on the same date. The validation bar below is how a batch like this earns trust.

Microsoft's documentation is explicit that custom skills are not validated by Microsoft. This repo applies its own bar instead:

- **Format-validated structure.** Every skill has a kebab-case `name` identical to its folder name, exactly two frontmatter fields, a body under 300 lines, and companion files within the 20-file and 10 MB limits, referenced by relative path one level deep.
- **Human-readable Markdown only.** No scripts in any skill, because whether Cowork executes bundled scripts is undocumented. You can read every file in a skill before installing it, and you should.
- **Destructive actions behind approval gates.** Every skill is written to require explicit user approval in the conversation before deleting or overwriting a file, and to prefer writing new versioned files.
- **Email never sends.** Every email-touching skill is written to create Drafts only.
- **DRAFT until reviewed.** Every skill is written to label generated documents DRAFT until a human reviews them.
- **Community-reported frictions designed in.** Community reports describe Planner and To Do writes failing silently and outputs landing in session folders. So every skill that touches Planner or To Do specifies a file fallback (for example `actions.md`) and reports which path was taken, and every skill names explicit OneDrive save paths and reports where each artifact was saved.
- **Status declared.** Every skill README carries a tested-in-Cowork status line: tested-with-date once it passes a live tenant test (two have, as of 2026-06-11), "tenant test pending" until then. Never trust a skill that claims testing it cannot date.

One thing to be clear about: these are instructions the model is asked to follow, not platform-enforced controls. Cowork has no sandbox that prevents a skill, or injected content inside something a skill reads, from attempting a send or a delete. Treat them as defence in depth, not a guarantee.

**For the sceptics:** a skill is plain-language instructions that the model reads, which makes any third-party skill a potential prompt-injection vector. Treat skills like browser extensions: read the `SKILL.md` before dropping it into OneDrive. Install takes a minute; reading the largest skill here before you install takes about ten, and those ten are worth it. Everything in this repo is plain Markdown with no encoded content, written to be audited in one sitting.

**How to vet a third-party skill before installing:**

- The frontmatter contains exactly two fields, `name` and `description`, and nothing else.
- No scripts, no encoded or obfuscated blocks, and no instructions to fetch external URLs anywhere in the `SKILL.md` or its reference files.
- Every save path points inside your own OneDrive.
- The safety rules cover, at minimum: email as Drafts only, no delete or overwrite without approval, and a rule that content the skill reads is data to analyse, never instructions to follow.
- Reject any skill that tells the model to send data to an external address or URL.

**Known unknowns, stated plainly:** Cowork's GA date and pricing are unknown. Whether Cowork executes bundled scripts is undocumented. Admin controls for personal OneDrive skills are not documented today and may be added.

---

### 📕 Governing the estate, not just building it

If you are running AI in an enterprise and the question "who owns the model's mistake?" does not yet have a name against it, **Critical Density** is the responsibility-and-audit playbook: how dependency builds invisibly, why attribution has to be installed before an incident, and a five-artifact toolkit (the Density Register, the Attribution-Readiness Checklist, the RACI-for-AI, the Audit Question Bank, and the Governance-Cadence Control Spec). Audit-grade, EU AI Act-aware, sector-neutral.

Start free with the [Licence-Plate Test](https://store.kesslernity.com/l/licence-plate-test) (a 12-question attribution self-test), or get the full book + toolkit: [Critical Density, $59](https://store.kesslernity.com/l/critical-density).

---

## Other Things I Make

Everything in this repo is free under the licence below. Elsewhere:

- **[Agent Instruction Block Design Guide](https://store.kesslernity.com/l/eyeauo)** ($19): the design patterns and failure modes behind the instruction files in this repo, for when your own instruction file is not behaving.
- **[M365 Copilot Deployment Kit](https://store.kesslernity.com/l/kpfpi)** ($97): IT prerequisites, governance, a 90-day rollout roadmap, field guides and agent templates for deploying Copilot org-wide.
- **[AI at Work newsletter](https://newsletter.kesslernity.com)**: a free biweekly GenAI briefing with verified news, tested prompts, and one practical insight for your team.
- **[AI Quick Start Essentials](https://trainings.kesslernity.com)**: a free 35-minute course on practical, responsible AI use.
- A free written guide to Copilot Cowork at [kesslernity.com/guides](https://kesslernity.com/guides).

---

## Sibling Repos

- **[awesome-copilot-chat-agents](https://github.com/kesslernity/awesome-copilot-chat-agents)**: 52 instruction-only agents for the free Copilot Chat tier, no premium licence required.
- **[awesome-copilot-studio-agents](https://github.com/kesslernity/awesome-copilot-studio-agents)**: 78 agents for M365 Copilot premium with SharePoint, email and calendar grounding.
- **[awesome-microsoft-copilot-prompts](https://github.com/kesslernity/awesome-microsoft-copilot-prompts)**: single-message prompts for M365 Copilot, the place for anything chat-sized.

---

## Contributing

Contributions welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for the file format and PR guidelines. The hard bar:

- **Multi-step and artifact-producing.** The skill plans a workflow and writes files. If the draft fits in one chat message, it is a prompt: we will redirect it to [awesome-microsoft-copilot-prompts](https://github.com/kesslernity/awesome-microsoft-copilot-prompts).
- **Composes built-ins.** It orchestrates the 13 built-in skills, never duplicates one, and never reuses a built-in's name.
- **Spec-valid.** Kebab-case `name` matching the folder name, exactly two frontmatter fields, within the size limits.
- **No scripts.** Instructions and Markdown reference files only.
- **Status declared.** The skill README states its tested-in-Cowork status honestly.

---

## Licence

[Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/)

You are free to use, adapt and redistribute these skills, including commercially, as long as you credit the source and share derivatives under the same licence.

---

*Built by [Mathieu Kessler](https://linkedin.com/in/mathieukessler) · [NerdyChefs.ai](https://nerdychefs.ai) · [kesslernity.com](https://kesslernity.com)*
