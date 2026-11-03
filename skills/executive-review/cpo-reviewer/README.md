# CPO Reviewer

> Pressure-test your product plan against a CPO archetype before the real one asks where the users are.

## What it produces

A structured review document, `<artifact-name>-cpo-review.docx`, saved to `/Documents/Cowork/reviews/` in your OneDrive, containing:

- **VERDICT**: ready, ready with conditions, or not ready
- **TOP FINDINGS**: each one quotes or cites the exact part of your document it is about, no generic feedback
- **RISKS**: from the product lens (adoption failure, roadmap opportunity cost, scope creep, missing kill criteria)
- **WHAT WOULD CHANGE MY MIND**: the specific evidence that would move the verdict up
- **5 INTERROGATION QUESTIONS**: the questions the real CPO is likely to ask in the room

The persona lives in `references/persona.md`: mandate, ten probes, red flags, what convinces a CPO and what gets dismissed, plus documented blind spots so a validator can challenge the feedback where the archetype distorts it.

## Install

**Quickest: upload the zip.** [Download `cpo-reviewer.zip`](https://github.com/kesslernity/awesome-copilot-cowork-skills/raw/main/dist/zips/cpo-reviewer.zip). In Cowork, open **Customize**, select the **Skills** tab, select the arrow next to **Add**, then **Upload skill**, and choose the file. Cowork validates it and saves the skill to your OneDrive for you, so you never create a folder.

**Or copy this folder** into OneDrive at `/Documents/Cowork/skills/cpo-reviewer/`. The lowercase `skills` folder name is case-sensitive, and you copy the skill folder itself, not the category folder above it.

Either way, start a **NEW** Cowork conversation afterwards: skills are discovered only when a conversation starts. Then use one of the trigger phrases below.

Custom skills are not supported in Cowork on a phone or tablet, so this needs a laptop or desktop.

## Example triggers

- "Run a CPO review on q3-roadmap-proposal.docx"
- "What would a Chief Product Officer say about this business case?"
- "Pressure-test this deck from a product lens, I present to the product council on Monday"
- "I'm pitching our CPO next week. Find the adoption holes in this plan first."

## Why this exists

This skill is a bench persona for the executive-review suite. The core board covers the executives who gate most approvals; bench personas extend it with the other seats at the table, and the CPO seat asks the questions the rest of the board does not: who has this problem, what do they do about it today, what does adoption cost them, and which roadmap bets this displaces. It works standalone; you do not need the rest of the suite installed.


## Status

Tested in Cowork: 2026-06-16, passed. Format-validated against the Agent Skills spec.

## Changelog

| Version | Date | Notes |
|---------|------------|-----------------|
| 1.0 | 2026-06-10 | Initial version |
