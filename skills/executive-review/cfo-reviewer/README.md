# CFO Reviewer

> Pressure-test your business case against a CFO archetype before the real CFO does it for you, in the meeting.

## What it produces

A structured review document, `<artifact-name>-cfo-review.docx`, saved to `/Documents/Cowork/reviews/` in your OneDrive, containing:

- **VERDICT**: proceed, proceed with conditions, or not ready
- **TOP FINDINGS**: each one quotes or cites the exact part of your document it is about, no generic feedback
- **RISKS**: from the finance lens (cash timing, budget displacement, contract exposure, benefit realisation)
- **WHAT WOULD CHANGE MY MIND**: the specific evidence that would move the verdict up
- **5 INTERROGATION QUESTIONS**: the questions the real CFO is likely to ask in the room

The persona lives in `references/persona.md`: mandate, ten probes, red flags, what convinces a CFO and what gets dismissed, plus documented blind spots so a validator can challenge the feedback where the archetype distorts it.

## Install

**Quickest: upload the zip.** [Download `cfo-reviewer.zip`](https://github.com/kesslernity/awesome-copilot-cowork-skills/raw/main/dist/zips/cfo-reviewer.zip). In Cowork, open **Customize**, select the **Skills** tab, select the arrow next to **Add**, then **Upload skill**, and choose the file. Cowork validates it and saves the skill to your OneDrive for you, so you never create a folder.

**Or copy this folder** into OneDrive at `/Documents/Cowork/skills/cfo-reviewer/`. The lowercase `skills` folder name is case-sensitive, and you copy the skill folder itself, not the category folder above it.

Either way, start a **NEW** Cowork conversation afterwards: skills are discovered only when a conversation starts. Then use one of the trigger phrases below.

Custom skills are not supported in Cowork on a phone or tablet, so this needs a laptop or desktop.

## Example triggers

- "Run a CFO review on q3-platform-business-case.docx"
- "What would a CFO say about this proposal before I take it to finance?"
- "Pressure-test this deck from a finance lens, I present to the investment board next week"
- "I'm pitching our CFO on Thursday. Find the holes in this business case first."

## Why this exists

This skill is one of seven reviewers in the executive-review suite. It answers a recurring ask from people preparing business cases: pressure-test the document against the executive who will actually interrogate it, before the meeting, not during it. Finance review is the gate where most proposals stall, so the CFO reviewer is the one to run first. It works standalone; you do not need the rest of the suite installed.

## Status

Tested in Cowork: 2026-06-16, passed. Format-validated against the Agent Skills spec.

## Changelog

| Version | Date | Notes |
|---------|------------|-----------------|
| 1.0 | 2026-06-10 | Initial version |
