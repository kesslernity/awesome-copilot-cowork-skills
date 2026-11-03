# Custom Daily Brief

> A morning brief that covers what your role actually needs, saved as a dated Word document, not a one-size-fits-all summary.

## What it produces

- `/Documents/Cowork/briefs/daily-brief-YYYY-MM-DD.docx`: emails needing answers, today's calendar with conflicts flagged, Teams mentions, deadlines for the next 7 days, and (optionally) yesterday's meeting actions, in the section order your preset defines.
- An optional email Draft of the brief addressed to yourself (left in Drafts, never sent).

The built-in Daily Briefing skill gives everyone the same summary in chat. This skill composes it with the Email, Calendar Management, Scheduling, Enterprise Search, Meetings and Word built-ins and adds the parts the built-in lacks: role presets (PM, EA, IT admin, sales), a custom section list you edit in `references/brief-config.md`, a saved file with a predictable name, and a consistent format every day. Once installed, you can also ask Cowork to run it on a schedule each weekday morning (Cowork allows up to five scheduled prompts per user, so budget this against your other schedules).

## Install

**Quickest: upload the zip.** [Download `custom-daily-brief.zip`](https://github.com/kesslernity/awesome-copilot-cowork-skills/raw/main/dist/zips/custom-daily-brief.zip). In Cowork, open **Customize**, select the **Skills** tab, select the arrow next to **Add**, then **Upload skill**, and choose the file. Cowork validates it and saves the skill to your OneDrive for you, so you never create a folder.

**Or copy this folder** into OneDrive at `/Documents/Cowork/skills/custom-daily-brief/`. The lowercase `skills` folder name is case-sensitive, and you copy the skill folder itself, not the category folder above it.

Either way, start a **NEW** Cowork conversation afterwards: skills are discovered only when a conversation starts. Then use one of the trigger phrases below.

Custom skills are not supported in Cowork on a phone or tablet, so this needs a laptop or desktop.

## Example triggers

- "Run my daily brief."
- "Give me my morning brief as an IT admin."
- "Build my start-of-day summary and email me a draft of it."
- "Change my daily brief to include yesterday's meeting actions."

## Why this exists

A configurable daily brief was the most-repeated custom workflow in our scan of what Cowork preview users are actually building: at least 7 independent users described building their own variant, all working around the same gap, namely that the built-in Daily Briefing cannot be tuned per role or saved to a file. See the threads at https://redd.it/1t8or2n, https://redd.it/1slxidi and https://redd.it/1tkio2o. This skill is one maintained version of that pattern instead of seven private ones.

## Status

Tested in Cowork: 2026-06-16, passed. Format-validated against the Agent Skills spec.

## Changelog

| Version | Date | Notes |
|---------|------------|-----------------|
| 1.0 | 2026-06-10 | Initial version |
