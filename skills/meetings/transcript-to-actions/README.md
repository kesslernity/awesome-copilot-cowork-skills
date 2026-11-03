# Transcript to Actions

> Turn any meeting transcript into owned, dated action items, tracked tasks, and per-owner follow-up email drafts, with a file you can trust even when Planner writes fail.

## What it produces

- `actions.md` in OneDrive at `/Documents/Cowork/meeting-actions/<date>-<meeting>/`: decisions, an action-items table (owner, verb-led action, due date, source quote), open questions, and a write log.
- Tasks in Microsoft To Do or a named Planner plan, created only where Cowork can confirm the write by reading the task back. Unconfirmed writes fall back to the file and are reported as such.
- One Outlook Draft per action owner listing their items, subject prefixed `DRAFT:`, never sent.
- A run report stating the exact save path of every artifact and which task writes succeeded.

## Install

**Quickest: upload the zip.** [Download `transcript-to-actions.zip`](https://github.com/kesslernity/awesome-copilot-cowork-skills/raw/main/dist/zips/transcript-to-actions.zip). In Cowork, open **Customize**, select the **Skills** tab, select the arrow next to **Add**, then **Upload skill**, and choose the file. Cowork validates it and saves the skill to your OneDrive for you, so you never create a folder.

**Or copy this folder** into OneDrive at `/Documents/Cowork/skills/transcript-to-actions/`. The lowercase `skills` folder name is case-sensitive, and you copy the skill folder itself, not the category folder above it.

Either way, start a **NEW** Cowork conversation afterwards: skills are discovered only when a conversation starts. Then use one of the trigger phrases below.

Custom skills are not supported in Cowork on a phone or tablet, so this needs a laptop or desktop.

## Example triggers

- "Turn this transcript into action items and follow-up emails."
- "Here's the recap from Monday's steering meeting. Pull out the actions and put them in Planner."
- "Get the action items from yesterday's project sync, create To Do tasks, and draft the follow-ups."
- "Extract the decisions, actions, and open questions from the transcript at Documents/Recordings/q3-review.docx."

## Why this exists

Transcript-to-tasks is one of the most commonly rebuilt Cowork workflows, and field reports agree on the same friction: Cowork writes to Planner and To Do can fail silently, so a task you were told was created may simply not exist. This skill is built around that reality. It makes the OneDrive actions file the source of truth, verifies every task write by reading it back, and reports honestly which items reached To Do or Planner and which live only in the file.

## Status

Tested in Cowork: 2026-06-16, passed. Format-validated against the Agent Skills spec.

## Changelog

| Version | Date | Notes |
|---|---|---|
| 1.0 | 2026-06-10 | Initial version |
