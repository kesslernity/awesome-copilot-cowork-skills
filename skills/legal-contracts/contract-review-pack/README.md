# Contract Review Pack

> Abstracts a contract into a key-terms table, compares it against your own playbook of standard positions, and produces a DRAFT review pack — preparation for a lawyer, never legal advice.

## What it produces

- `DRAFT-contract-review-<Contract>-<date>-v1.docx`: a review pack with a key-terms abstraction (each value cited to a clause), a deviations-and-issues list against your playbook, open questions, and a reviewer checklist. DRAFT-labelled in the filename and on the first line.
- `contract-key-terms-<date>.md` (optional): the raw key-terms abstraction.

Both save next to the source contract in OneDrive, with the exact paths reported in the conversation.

## Install

**Quickest: upload the zip.** [Download `contract-review-pack.zip`](https://github.com/kesslernity/awesome-copilot-cowork-skills/raw/main/dist/zips/contract-review-pack.zip). In Cowork, open **Customize**, select the **Skills** tab, select the arrow next to **Add**, then **Upload skill**, and choose the file. Cowork validates it and saves the skill to your OneDrive for you, so you never create a folder.

**Or copy this folder** into OneDrive at `/Documents/Cowork/skills/contract-review-pack/`. The lowercase `skills` folder name is case-sensitive, and you copy the skill folder itself, not the category folder above it.

Either way, start a **NEW** Cowork conversation afterwards: skills are discovered only when a conversation starts. Then use one of the trigger phrases below.

Custom skills are not supported in Cowork on a phone or tablet, so this needs a laptop or desktop.

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
