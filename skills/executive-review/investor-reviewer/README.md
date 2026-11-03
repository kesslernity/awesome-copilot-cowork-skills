# Investor Reviewer

> Pressure-test your business case against the person whose capital is at stake, before you ask for the money in the room.

## What it produces

A structured review document, `<artifact-name>-investor-review.docx`, saved to `/Documents/Cowork/reviews/` in your OneDrive, containing:

- **VERDICT**: ready, ready with conditions, or not ready (conditions phrased as terms: gates, tranches, evidence required)
- **TOP FINDINGS**: each one quotes or cites the exact part of your document it is about, no generic feedback; where your document is silent, the finding records the open question rather than inventing an answer
- **RISKS**: from the capital lens (capital at risk before first evidence, opportunity cost, missing staging, downside and unwind costs)
- **WHAT WOULD CHANGE MY MIND**: the specific evidence or restructuring of the ask that would move the verdict up
- **5 INTERROGATION QUESTIONS**: the questions a real investor is likely to ask in the room

The persona lives in `references/persona.md`: mandate, ten probes, red flags, what convinces an investor and what gets dismissed, plus documented blind spots so a validator can challenge the feedback where the archetype distorts it.

## Install

**Quickest: upload the zip.** [Download `investor-reviewer.zip`](https://github.com/kesslernity/awesome-copilot-cowork-skills/raw/main/dist/zips/investor-reviewer.zip). In Cowork, open **Customize**, select the **Skills** tab, select the arrow next to **Add**, then **Upload skill**, and choose the file. Cowork validates it and saves the skill to your OneDrive for you, so you never create a folder.

**Or copy this folder** into OneDrive at `/Documents/Cowork/skills/investor-reviewer/`. The lowercase `skills` folder name is case-sensitive, and you copy the skill folder itself, not the category folder above it.

Either way, start a **NEW** Cowork conversation afterwards: skills are discovered only when a conversation starts. Then use one of the trigger phrases below.

Custom skills are not supported in Cowork on a phone or tablet, so this needs a laptop or desktop.

## Example triggers

- "Run an investor review on platform-funding-case.docx"
- "What would an investor say about this business case before I ask for the budget?"
- "Pressure-test this deck from a capital lens, I pitch the investment committee next week"
- "We're asking the board sponsor for the full amount upfront. Find the holes first."

## Why this exists

This skill is a bench persona for the executive-review suite. The core reviewers review from inside the org chart: can we run this, secure it, staff it, fund it from this year's budget. The investor reviews from outside it: should this capital be committed at all, in what stages, and what does failure cost. Proposals that survive every operational reviewer still die on that question, so the bench extends the suite beyond the C-suite to the people whose money is actually on the table. It works standalone; you do not need the rest of the suite installed.


## Status

Tested in Cowork: 2026-06-16, passed. Format-validated against the Agent Skills spec.

## Changelog

| Version | Date | Notes |
|---------|------------|-----------------|
| 1.0 | 2026-06-10 | Initial version |
