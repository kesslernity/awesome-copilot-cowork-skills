# FAQ

Answers to the questions readers ask most. Where a topic has a fuller treatment in the [README](README.md), the answer links there instead of repeating it.

---

## Do I need a licence to use these?

For Cowork, yes: a paid M365 Copilot licence. Cowork has been generally available worldwide since 16 June 2026, but it is **off by default** — an admin has to enable it and grant you access. Quick check: if you cannot open Cowork the way Microsoft's [Use Cowork](https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/use-cowork) guide describes, it is not switched on for your account yet; ask your admin. Beyond the licence, Cowork runs add usage-based charges in Copilot Credits — see the README's [Pricing & cost (GA)](README.md#pricing--cost-ga).

No Copilot licence at all? Start with [awesome-copilot-chat-agents](https://github.com/kesslernity/awesome-copilot-chat-agents): 57 agents that run on the free Copilot Chat tier included with any commercial M365 licence. The other routes are in the README's [Who This Is For](README.md#who-this-is-for) section.

The skill files themselves are free under CC BY-SA 4.0, and they also run in Claude Code and VS Code (see below), so a Cowork licence is only required for the Cowork runtime.

## I am in the EU. Why can I not see Cowork?

Cowork is **off by default everywhere**, EU included — an admin has to enable it and grant you access. It also runs on third-party models (Anthropic's Claude) under Microsoft's standard data-protection commitments, and follows the same [data residency model as the rest of Copilot](https://learn.microsoft.com/en-us/microsoft-365/enterprise/m365-dr-service-copilot). If Cowork is not appearing for you, it has not been switched on for your tenant or your account yet — that is an admin action, not a sign you are excluded.

## Are these skills safe to install? How do I audit one before trusting it?

A skill is plain-language instructions the model reads, which makes any third-party skill a potential prompt-injection vector. Treat skills like browser extensions: read the `SKILL.md` before dropping it into OneDrive. Everything in this repo is plain Markdown with no encoded content and no scripts, written to be audited in one sitting.

To vet any skill, from this repo or anywhere else, use the checklist in the README's [Quality and Safety Bar](README.md#quality-and-safety-bar): exactly two frontmatter fields, no scripts or encoded blocks, no instructions to fetch external URLs, save paths inside your own OneDrive, safety rules covering Drafts-only email and approval-gated deletes, and an explicit rule that content the skill reads is data to analyse, never instructions to follow. Reject any skill that tells the model to send data to an external address.

One thing to be clear about: these safety rules are instructions the model is asked to follow, not platform-enforced controls. Treat them as defence in depth, not a guarantee.

## Have these been tested in a real Cowork tenant?

Yes. This repo was written as one batch in early June 2026, built from the demand and failure threads on r/microsoft_365_copilot, and every skill is format-validated against the Agent Skills spec. All of them have since passed a live tenant test — `meeting-prep-onepager` and `no-delete-guardrail` first, on 2026-06-11, and the rest on 2026-06-16. Each skill's README carries its own tested-with-date line, because a status you cannot date is not one to trust.

## Why are there no scripts in any skill?

Whether Cowork executes bundled scripts is undocumented. Until Microsoft documents it, every skill here is instructions plus Markdown reference files only. This also keeps every skill fully human-readable: you can audit the entire thing before installing it, which is the point of the safety bar above.

## My skill is not being discovered. What do I check?

Three community-reported gotchas, in the order they usually bite:

1. **The `skills` folder name is lowercase and case-sensitive.** `Skills` will not be found. The full path is `/Documents/Cowork/skills/<skill-name>/`.
2. **Discovery happens at the start of a conversation.** A conversation that is already open will not see a skill you just added. Start a new one.
3. **OneDrive sync delay.** Cowork reads OneDrive and SharePoint files only, never local device files. If you copied the folder into your synced OneDrive folder in Explorer or Finder, wait for the sync to finish (check the OneDrive icon) before starting that new conversation; until the files reach OneDrive itself, Cowork cannot see them.

Also confirm the folder name exactly matches the `name` field inside `SKILL.md`, and that the frontmatter contains exactly `name` and `description` and nothing else. The full install steps are in the README's [Install in 60 Seconds](README.md#install-in-60-seconds).

## Can Cowork really lose my skills folder?

It has happened. Between 23 and 27 May 2026 a tenant-wide incident wiped skills folders, conversation history and tasks, generating more than 50 same-question reports on [Microsoft Q&A](https://learn.microsoft.com/en-ca/answers/questions/5900350/m365-copilot-cowork-missing-history-scheduled-task), and the problem recurred on 9 June 2026.

[`skills-backup-keeper`](skills/meta-skills/skills-backup-keeper/) exists for exactly this. What it does: keeps dated, never-overwritten copies of your whole skills folder at `/Documents/Cowork/skills-backup/YYYY-MM-DD/` with a manifest, plus an append-only session journal stored outside the skills folder so a wipe cannot take it too, and an approval-gated restore. What it does not do: it cannot stop Microsoft wiping the folder, it cannot recover work done since your last backup, and it cannot help if you never ran a backup before the wipe.

Belt and braces: keep your clone or extracted copy of this repo somewhere outside OneDrive and copy skill folders across, as the install steps describe. That way the shipped skills are always re-installable in minutes even if both the skills folder and the backup were lost.

## Do these work in Claude Code and VS Code?

Yes, verbatim. Skills use the Agent Skills open standard, the same format supported by Claude Code, VS Code Copilot and 30+ other AI tools, per Microsoft's [plugin-development page](https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-plugin-development). Per runtime:

- **Claude Code:** copy the skill folder into `~/.claude/skills/` (available in every project) or into a project's `.claude/skills/`.
- **VS Code (GitHub Copilot):** copy the skill folder into `.github/skills/` in your repository.

The Cowork-specific parts (OneDrive save paths, Planner and To Do fallbacks, Drafts-only email) degrade gracefully in other runtimes; the workflow and output structure still apply. More in the README's [Also Runs in Claude Code and VS Code](README.md#also-runs-in-claude-code-and-vs-code).

## Can my IT department deploy these org-wide?

Yes. Microsoft documents an admin path that packages the same skill folders into a Microsoft 365 app package, deployed as a plugin through the admin centre or the Microsoft 365 App Store: see [Build plugins for Copilot Cowork](https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-plugin-development). Microsoft also publishes a [conversion script](https://aka.ms/copilot-cowork-plugin-conversion-script) (`Convert-ClaudePluginToMOS3.ps1`) that does the packaging. Personal OneDrive skills currently need no admin involvement; admin controls for them are not documented today and may be added later.

## Can I build my own reviewer persona?

Yes. Each reviewer is a small standalone skill with the same structure. Copy an existing one (for example `cfo-reviewer`), rewrite the persona sections (mandate, what I probe first, red flags, what convinces me, vocabulary and tone, known blind spots), and rename the folder and the frontmatter `name` to `<role>-reviewer`. Two rules carry over: archetypes only, never a real named individual; and fill in the blind spots honestly, because an honest KNOWN BLIND SPOTS section is what keeps the persona's verdict trustworthy.

## What is org-profile.md, and is my data safe in it?

`/Documents/Cowork/org-profile.md` is an optional context file for the review personas: business model, customers, stage, priorities, constraints, recent decisions. With it, persona findings land on your business instead of a generic one; without it, personas treat every organisation fact as unknown and turn context-dependent findings into open questions. To create it, copy the `references/org-profile-template.md` that ships inside any reviewer skill (for example [`cfo-reviewer`](skills/executive-review/cfo-reviewer/references/org-profile-template.md)), fill it in, and save it at that path.

It stays in your OneDrive. Cowork reads and writes OneDrive and SharePoint files only, and no skill in this library instructs the model to send content to an external address or URL. Only one skill reaches the open web at all: `news-monitor-digest`, by design, and it does not read your org profile outward. The usual caveat applies: skill rules are instructions, not platform-enforced controls.

## Can I schedule skills?

Yes, via Cowork's scheduled prompts: ask Cowork to run a skill's trigger phrase on a schedule, for example `custom-daily-brief` each weekday morning. Cowork allows up to five scheduled prompts per user, so budget skill runs against your other schedules. One restriction: skills whose steps require your explicit approval in the conversation, such as `commitment-catcher`'s ledger save, are not suitable for unattended scheduled runs; the per-skill READMEs say so where it applies.

---

Question not answered here? Open a [GitHub issue](https://github.com/kesslernity/awesome-copilot-cowork-skills/issues) and ask; answers that help more than one person get added to this page.
