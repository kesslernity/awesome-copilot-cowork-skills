# No-Delete Guardrail

> Makes every Cowork conversation list its changes before making them, write new versions instead of overwriting, journal everything, and refuse bulk deletes outright.

## What it produces

- /Documents/Cowork/output/change-journal.md on OneDrive: an append-only audit log with one row per create, modify, move, rename, archive or delete, including timestamp and approval status.
- Versioned files (report-v2.docx, then -v3, and so on) wherever any step would otherwise have overwritten an existing file.
- An enumerated change list in the conversation before anything is touched, and a per-item approval gate on every destructive action.
- A flat refusal, with alternatives, for any bulk destructive operation (whole folders, "everything older than", more than 10 items at once).

## Install in 60 seconds

1. Copy this folder into OneDrive at /Documents/Cowork/skills/ so the file sits at /Documents/Cowork/skills/no-delete-guardrail/SKILL.md.
2. Start a NEW Cowork conversation. Skills are discovered at conversation start, not mid-chat.
3. Use one of the trigger phrases below, or just start any task that touches files: the guardrail applies itself.

## Example triggers

- "Clean up my project folder, but check with me before you remove anything."
- "Reorganise the Q3 reports folder."
- "Archive last year's meeting notes."
- "Replace the old budget file with the new version."

## Why this exists

The single most direct download signal we found while researching this repo: in a Frontier preview thread on r/microsoft_365_copilot, an enterprise reported forcing a no-delete guardrail on all its Cowork users, and a commenter's reply was "Can you share this skill?" (https://www.reddit.com/r/microsoft_365_copilot/comments/1t58ty5/). This folder is that skill: short enough to load alongside everything else you install, strict enough that nothing gets destroyed without a human saying so, with a journal to prove it.

## Status

Tested in Cowork: 2026-06-11, Frontier tenant, passed (refused unapproved overwrite and bulk delete, journalled changes). Format-validated against the Agent Skills spec.

## Changelog

| Version | Date | Notes |
|---|---|---|
| 1.0 | 2026-06-10 | Initial version |
