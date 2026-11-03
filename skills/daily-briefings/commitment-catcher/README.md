# Commitment Catcher

> Nothing you promised, and nothing promised to you, slips through the last 24 hours unnoticed.

## What it produces

- **commitments.md**, a running ledger at /Documents/Cowork/commitments/ in your OneDrive, tracking every commitment in both directions (things you said you would do, and things others said they would do for you) with open, done and overdue statuses, overdue items always at the top
- **Microsoft To Do tasks** in a "Commitments" list for new promises you made, verified after creation because To Do writes can fail silently
- **actions.md**, a dated checkbox fallback file written only when a To Do write cannot be verified, so nothing is lost either way

Sources scanned each run: sent and received email, Teams chats and channel messages, and meeting transcripts from the last 24 hours (or back to the previous run if longer).

## Install

**Quickest: upload the zip.** [Download `commitment-catcher.zip`](https://github.com/kesslernity/awesome-copilot-cowork-skills/raw/main/dist/zips/commitment-catcher.zip). In Cowork, open **Customize**, select the **Skills** tab, select the arrow next to **Add**, then **Upload skill**, and choose the file. Cowork validates it and saves the skill to your OneDrive for you, so you never create a folder.

**Or copy this folder** into OneDrive at `/Documents/Cowork/skills/commitment-catcher/`. The lowercase `skills` folder name is case-sensitive, and you copy the skill folder itself, not the category folder above it.

Either way, start a **NEW** Cowork conversation afterwards: skills are discovered only when a conversation starts. Then use one of the trigger phrases below.

Custom skills are not supported in Cowork on a phone or tablet, so this needs a laptop or desktop.

## Example triggers

- "What did I promise people in the last 24 hours?"
- "Run my commitment sweep."
- "Is anyone late on something they owe me?"
- "Update the commitments ledger and flag anything overdue."

## Why this exists

A user in r/microsoft_365_copilot described building an ADHD-support system that scans the previous 24 hours for commitments they made and then forgot, because promises made in passing (in a chat reply, at the end of a call) vanish unless something writes them down within a day: https://www.reddit.com/r/microsoft_365_copilot/comments/1t8or2n/ This skill turns that pattern into a maintained ledger with state across runs, both directions of obligation, and a file fallback for the To Do writes that fail silently.

## Status

Tested in Cowork: 2026-06-16, passed. Format-validated against the Agent Skills spec.

## Changelog

| Version | Date | Notes |
|---|---|---|
| 1.0 | 2026-06-10 | Initial version |
