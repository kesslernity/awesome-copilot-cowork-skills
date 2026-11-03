# Meeting Prep One-Pager

> Walk into any meeting with a one-page brief instead of digging through email, Teams and files first.

## What it produces

A single Word document, hard-capped at one page, saved to OneDrive at `/Documents/Cowork/output/meeting-prep-YYYY-MM-DD-<short-meeting-name>.docx`. Six sections: meeting purpose, attendees and what each likely wants, open threads and unresolved questions, relevant files with one-line summaries, suggested talking points, and risks or tensions to be aware of. The skill gathers the calendar invite, recent email threads with the attendees, Teams messages and recently shared files, then distils them into the brief. It reads everything and writes only the one .docx, labelled DRAFT.

## Install

**Quickest: upload the zip.** [Download `meeting-prep-onepager.zip`](https://github.com/kesslernity/awesome-copilot-cowork-skills/raw/main/dist/zips/meeting-prep-onepager.zip). In Cowork, open **Customize**, select the **Skills** tab, select the arrow next to **Add**, then **Upload skill**, and choose the file. Cowork validates it and saves the skill to your OneDrive for you, so you never create a folder.

**Or copy this folder** into OneDrive at `/Documents/Cowork/skills/meeting-prep-onepager/`. The lowercase `skills` folder name is case-sensitive, and you copy the skill folder itself, not the category folder above it.

Either way, start a **NEW** Cowork conversation afterwards: skills are discovered only when a conversation starts. Then use one of the trigger phrases below.

Custom skills are not supported in Cowork on a phone or tablet, so this needs a laptop or desktop.

## Example triggers

- "Prep me for my next meeting."
- "Build a one-pager for the Q3 vendor renewal review on Thursday."
- "What do I need to know before my 2pm with the platform team?"
- "Brief me before the steering committee. Focus on the budget question."

## Why this exists

Demand signal: a thread on r/microsoft_365_copilot asking for exactly this kind of automated pre-meeting brief: https://reddit.com/r/microsoft_365_copilot/comments/1sr3azp/. Cowork already has the individual pieces (Calendar Management, Email, Enterprise Search, Meetings, Word) but no built-in workflow that composes them into a meeting brief. This skill is that workflow, with a strict one-page cap so the brief gets read rather than filed.

## Status

Tested in Cowork: 2026-06-11, Frontier tenant, passed (brief produced at the named path, signal-traceability rules held). Format-validated against the Agent Skills spec.

## Changelog

| Version | Date | Notes |
|---------|------------|-----------------|
| 1.0 | 2026-06-10 | Initial version |
