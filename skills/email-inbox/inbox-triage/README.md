# Inbox Triage

> Sorts a week of inbox into five buckets, drafts the replies, and writes you a dated report, without moving a single message until your rules file says it can.

## What it produces

- A triage report, triage-YYYY-MM-DD.md, saved to OneDrive at /Documents/Cowork/triage/, with counts and per-category tables for needs-reply-today, needs-reply-this-week, waiting-on-others, FYI and noise.
- Reply drafts in your Drafts folder for the messages that need answers, each labelled DRAFT on the first line. Nothing is ever sent.
- Moves and archives only for the senders and subject patterns you list yourself in references/triage-rules.md. Until you edit that file, the skill reports and drafts but touches nothing.
- actions-YYYY-MM-DD.md as a file fallback if you ask for follow-up tasks and Planner or To Do writes cannot be verified.

## Install

**Quickest: upload the zip.** [Download `inbox-triage.zip`](https://github.com/kesslernity/awesome-copilot-cowork-skills/raw/main/dist/zips/inbox-triage.zip). In Cowork, open **Customize**, select the **Skills** tab, select the arrow next to **Add**, then **Upload skill**, and choose the file. Cowork validates it and saves the skill to your OneDrive for you, so you never create a folder.

**Or copy this folder** into OneDrive at `/Documents/Cowork/skills/inbox-triage/`. The lowercase `skills` folder name is case-sensitive, and you copy the skill folder itself, not the category folder above it.

Either way, start a **NEW** Cowork conversation afterwards: skills are discovered only when a conversation starts. Then use one of the trigger phrases below.

Custom skills are not supported in Cowork on a phone or tablet, so this needs a laptop or desktop.

## Example triggers

- "Triage my inbox from the last week."
- "What needs a reply today? Draft the replies for me."
- "I am back from two weeks of leave, catch me up on my inbox and sort it into a report."
- "Clean up my inbox using my triage rules."

## Why this exists

Inbox cleanup is one of the most repeated asks from people testing Cowork-style agents: see the Cowork preview thread at https://www.reddit.com/comments/1shymgj/. The blocker is trust: nobody wants an agent archiving the wrong email. This skill splits the job in two: it categorises and drafts freely, and it moves mail only on rules you wrote down first.

## Status

Tested in Cowork: 2026-06-16, passed. Format-validated against the Agent Skills spec.

## Changelog

| Version | Date | Notes |
|---|---|---|
| 1.0 | 2026-06-10 | Initial version |
