# Inbox Triage

> Sorts a week of inbox into five buckets, drafts the replies, and writes you a dated report, without moving a single message until your rules file says it can.

## What it produces

- A triage report, triage-YYYY-MM-DD.md, saved to OneDrive at /Documents/Cowork/triage/, with counts and per-category tables for needs-reply-today, needs-reply-this-week, waiting-on-others, FYI and noise.
- Reply drafts in your Drafts folder for the messages that need answers, each labelled DRAFT on the first line. Nothing is ever sent.
- Moves and archives only for the senders and subject patterns you list yourself in references/triage-rules.md. Until you edit that file, the skill reports and drafts but touches nothing.
- actions-YYYY-MM-DD.md as a file fallback if you ask for follow-up tasks and Planner or To Do writes cannot be verified.

## Install in 60 seconds

1. Copy this folder into OneDrive at /Documents/Cowork/skills/ so the file sits at /Documents/Cowork/skills/inbox-triage/SKILL.md.
2. Start a NEW Cowork conversation. Skills are discovered at conversation start, not mid-chat.
3. Use one of the trigger phrases below. To allow moving or archiving, edit references/triage-rules.md first and set Rules enabled to yes.

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
