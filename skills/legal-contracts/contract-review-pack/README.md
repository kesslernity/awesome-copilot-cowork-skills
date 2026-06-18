# Contract Review Pack

> Abstracts a contract into a key-terms table, compares it against your own playbook of standard positions, and produces a DRAFT review pack — preparation for a lawyer, never legal advice.

## What it produces

- `DRAFT-contract-review-<Contract>-<date>-v1.docx`: a review pack with a key-terms abstraction (each value cited to a clause), a deviations-and-issues list against your playbook, open questions, and a reviewer checklist. DRAFT-labelled in the filename and on the first line.
- `contract-key-terms-<date>.md` (optional): the raw key-terms abstraction.

Both save next to the source contract in OneDrive, with the exact paths reported in the conversation.

## Install in 60 seconds

1. Copy this folder into OneDrive at `/Documents/Cowork/skills/` (keep the folder name `contract-review-pack`; the lowercase `skills` folder name is case-sensitive). Drop your own standard-positions file into the folder as `*playbook*.md` or `*playbook*.docx` — start from `references/playbook-template.md`.
2. Start a NEW Cowork conversation (skills are only discovered when a conversation starts).
3. Use one of the trigger phrases below.

## Example triggers

- "Review nda-acme.docx against our playbook"
- "Abstract the key terms of this MSA and flag deviations from our standard positions"
- "Pressure-test the Fabrikam services agreement and give me an issues list"
- "Build a contract review pack from the licence agreement in the Legal folder"

## Why this exists

In-house legal and contract teams re-do the same first pass by hand: read the contract, pull the key terms into a table, check each one against the team's standard positions, and write up the deviations for a lawyer to action. This skill does that first pass from your own playbook, cites every term to a clause, refuses to call anything acceptable or enforceable, and never invents a term the contract does not contain. The lawyer still decides everything.

For a legal-lens review of a *proposal, business case or deck* (rather than a contract), use the [`general-counsel-reviewer`](../../executive-review/general-counsel-reviewer/) skill instead.

## Status

Tested in Cowork: not yet — format-validated against the Agent Skills spec; run a live tenant test before relying on it.

## Changelog

| Version | Date | Notes |
| --- | --- | --- |
| 1.0 | 2026-06-18 | Initial version |
