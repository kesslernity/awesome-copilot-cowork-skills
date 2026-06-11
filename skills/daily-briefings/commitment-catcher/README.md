# Commitment Catcher

> Nothing you promised, and nothing promised to you, slips through the last 24 hours unnoticed.

## What it produces

- **commitments.md**, a running ledger at /Documents/Cowork/commitments/ in your OneDrive, tracking every commitment in both directions (things you said you would do, and things others said they would do for you) with open, done and overdue statuses, overdue items always at the top
- **Microsoft To Do tasks** in a "Commitments" list for new promises you made, verified after creation because To Do writes can fail silently
- **actions.md**, a dated checkbox fallback file written only when a To Do write cannot be verified, so nothing is lost either way

Sources scanned each run: sent and received email, Teams chats and channel messages, and meeting transcripts from the last 24 hours (or back to the previous run if longer).

## Install in 60 seconds

1. Copy this folder into your OneDrive at /Documents/Cowork/skills/ so the file sits at /Documents/Cowork/skills/commitment-catcher/SKILL.md (the lowercase skills folder name matters).
2. Start a NEW Cowork conversation. Skills are only discovered when a conversation starts.
3. Use one of the trigger phrases below.

## Example triggers

- "What did I promise people in the last 24 hours?"
- "Run my commitment sweep."
- "Is anyone late on something they owe me?"
- "Update the commitments ledger and flag anything overdue."

## Why this exists

A user in r/microsoft_365_copilot described building an ADHD-support system that scans the previous 24 hours for commitments they made and then forgot, because promises made in passing (in a chat reply, at the end of a call) vanish unless something writes them down within a day: https://www.reddit.com/r/microsoft_365_copilot/comments/1t8or2n/ This skill turns that pattern into a maintained ledger with state across runs, both directions of obligation, and a file fallback for the To Do writes that fail silently.

## Status

Tested in Cowork: pending (June 2026). Format-validated against the Agent Skills spec.

## Changelog

| Version | Date | Notes |
|---|---|---|
| 1.0 | 2026-06-10 | Initial version |
