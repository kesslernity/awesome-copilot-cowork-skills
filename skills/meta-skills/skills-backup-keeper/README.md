# Skills Backup Keeper

> Your skills folder can be wiped without warning. This skill makes sure that costs you five minutes, not five weeks.

## What it produces

- A dated, never-overwritten copy of your whole skills folder at `/Documents/Cowork/skills-backup/YYYY-MM-DD/`, with a `backup-manifest.md` listing exactly what was copied.
- An append-only `session-journal.md` (goal, files touched, decisions, next steps) stored in `skills-backup/`, outside the skills folder, so a wipe cannot take it too. A new conversation reads it and resumes where the last one stopped.
- A guided, approval-gated restore that copies a chosen backup back into `/Documents/Cowork/skills/` and verifies the result against the manifest.

## Install in 60 seconds

1. Copy this folder into OneDrive at `/Documents/Cowork/skills/` (so you have `/Documents/Cowork/skills/skills-backup-keeper/SKILL.md`). The lowercase `skills` folder name is case-sensitive.
2. Start a NEW Cowork conversation. Skills are only discovered when a conversation starts.
3. Use one of the trigger phrases below.

## Example triggers

- "Back up my skills folder before I edit anything"
- "Update the session journal: we finished the budget review skill, next step is testing"
- "New conversation. Where did we leave off?"
- "My skills folder is empty again. Restore from the latest backup."

## Why this exists

The number-one pain reported by Cowork Frontier preview users is losing everything at once. Between 23 and 27 May 2026, a tenant-wide incident wiped skills folders, conversation history and tasks, generating more than 50 same-question reports on Microsoft Q&A (https://learn.microsoft.com/en-ca/answers/questions/5900350/m365-copilot-cowork-missing-history-scheduled-task), and the problem recurred on 9 June 2026. This skill is the repo's answer to those incidents: it cannot stop Microsoft wiping the folder, but it makes the wipe recoverable in minutes and keeps a journal so even an interrupted session can be resumed in a fresh conversation.

## Restore after a wipe, step by step

1. Start a NEW Cowork conversation. If `skills-backup-keeper` itself was wiped, first re-copy this folder from this repo into `/Documents/Cowork/skills/` (step 1 of the install above), then start the new conversation.
2. Say: "Restore my skills from the latest backup."
3. Cowork lists the dated folders under `/Documents/Cowork/skills-backup/`, proposes the most recent, and shows you what its manifest says it contains.
4. If anything already in `/Documents/Cowork/skills/` would be replaced, Cowork lists each collision and asks for your approval before touching it. Nothing is overwritten without your yes.
5. Cowork copies the backup into `/Documents/Cowork/skills/`, then compares folder and file counts against `backup-manifest.md` and reports any mismatch.
6. Start one more NEW conversation. Restored skills are only discovered at conversation start.
7. Ask "Where did we leave off?" to have the session journal read back, with the open next steps quoted verbatim.

## Status

Tested in Cowork: 2026-06-16, passed. Format-validated against the Agent Skills spec.

## Changelog

| Version | Date | Notes |
|---|---|---|
| 1.0 | 2026-06-10 | Initial version |
