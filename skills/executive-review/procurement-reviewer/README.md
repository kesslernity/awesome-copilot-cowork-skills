# Procurement Reviewer

> Pressure-test your proposal against a Head of Procurement archetype before the real one reads the order form line by line.

## What it produces

A structured review document, `<artifact-name>-procurement-review.docx`, saved to `/Documents/Cowork/reviews/` in your OneDrive, containing:

- **VERDICT**: ready, ready with conditions, or not ready
- **TOP FINDINGS**: each one quotes or cites the exact part of your document it is about, no generic feedback; where the document is silent on a probe, an open question is recorded rather than an assumption
- **RISKS**: from the commercial lens (lock-in and switching cost, renewal and escalator exposure, single-source dependence, supplier continuity)
- **WHAT WOULD CHANGE MY MIND**: the specific terms and evidence that would move the verdict up
- **5 INTERROGATION QUESTIONS**: the questions the real Head of Procurement is likely to ask in the room

The persona lives in `references/persona.md`: mandate, ten probes, red flags, what convinces a procurement lead and what gets dismissed, plus documented blind spots so a validator can challenge the feedback where the archetype distorts it.

## Install

**Quickest: upload the zip.** [Download `procurement-reviewer.zip`](https://github.com/kesslernity/awesome-copilot-cowork-skills/raw/main/dist/zips/procurement-reviewer.zip). In Cowork, open **Customize**, select the **Skills** tab, select the arrow next to **Add**, then **Upload skill**, and choose the file. Cowork validates it and saves the skill to your OneDrive for you, so you never create a folder.

**Or copy this folder** into OneDrive at `/Documents/Cowork/skills/procurement-reviewer/`. The lowercase `skills` folder name is case-sensitive, and you copy the skill folder itself, not the category folder above it.

Either way, start a **NEW** Cowork conversation afterwards: skills are discovered only when a conversation starts. Then use one of the trigger phrases below.

Custom skills are not supported in Cowork on a phone or tablet, so this needs a laptop or desktop.

## Example triggers

- "Run a procurement review on crm-renewal-proposal.docx"
- "What would our Head of Procurement say about this vendor contract before we sign?"
- "Pressure-test this pricing deck from a commercial lens, the renewal lands next month"
- "I take this sourcing plan to the contracts committee on Tuesday. Find the holes first."

## Why this exists

This skill is a bench persona for the executive-review suite. The core suite covers the C-suite, but many proposals stall one level out from it: the vendor contract, the renewal, the statement of work that procurement will take apart clause by clause. Bench personas extend the suite beyond the C-suite to those gatekeepers, one role at a time. This one reviews the commercial substance of any document that commits the organisation to a counterparty. It works standalone; you do not need the rest of the suite installed.


## Status

Tested in Cowork: 2026-06-16, passed. Format-validated against the Agent Skills spec.

## Changelog

| Version | Date | Notes |
|---------|------------|-----------------|
| 1.0 | 2026-06-10 | Initial version |
