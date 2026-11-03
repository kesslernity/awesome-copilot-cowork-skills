# General Counsel Reviewer

> Pressure-test your proposal against a General Counsel archetype before the real one asks where the liability cap went.

## What it produces

A structured review document, `<artifact-name>-general-counsel-review.docx`, saved to `/Documents/Cowork/reviews/` in your OneDrive, containing:

- **VERDICT**: ready, ready with conditions, or not ready
- **TOP FINDINGS**: each one quotes or cites the exact part of your document it is about; where your document is silent, the finding records an open question rather than inventing terms
- **RISKS**: from the legal lens (contractual exposure, liability and indemnities, IP ownership, regulatory standing, signing authority, termination)
- **WHAT WOULD CHANGE MY MIND**: the documents and written confirmations that would move the verdict up
- **5 INTERROGATION QUESTIONS**: the questions the real General Counsel is likely to ask in the room

The persona lives in `references/persona.md`: mandate, ten probes, red flags, what convinces a General Counsel and what gets dismissed, plus documented blind spots so a validator can challenge the feedback where the archetype distorts it.

## Install

**Quickest: upload the zip.** [Download `general-counsel-reviewer.zip`](https://github.com/kesslernity/awesome-copilot-cowork-skills/raw/main/dist/zips/general-counsel-reviewer.zip). In Cowork, open **Customize**, select the **Skills** tab, select the arrow next to **Add**, then **Upload skill**, and choose the file. Cowork validates it and saves the skill to your OneDrive for you, so you never create a folder.

**Or copy this folder** into OneDrive at `/Documents/Cowork/skills/general-counsel-reviewer/`. The lowercase `skills` folder name is case-sensitive, and you copy the skill folder itself, not the category folder above it.

Either way, start a **NEW** Cowork conversation afterwards: skills are discovered only when a conversation starts. Then use one of the trigger phrases below.

Custom skills are not supported in Cowork on a phone or tablet, so this needs a laptop or desktop.

## Example triggers

- "Run a general counsel review on vendor-partnership-proposal.docx"
- "What would legal say about this deal before I send it to the counterparty?"
- "Pressure-test this business case from a legal lens, contract review is on Friday"
- "I present this plan to our GC next week. Find the legal holes first."

## Why this exists

This skill is a bench persona for the executive-review suite. The core reviewers cover the C-suite roles most proposals meet first; bench personas extend them to the reviewers a specific document actually faces. Plans that involve a counterparty, a regulator or anything that gets signed eventually cross the General Counsel's desk, and the questions asked there (who owns the IP, where the liability cap sits, who had authority to promise that) are cheaper to answer before the meeting than during it. It works standalone; you do not need the rest of the suite installed.


## Status

Tested in Cowork: 2026-06-16, passed. Format-validated against the Agent Skills spec.

## Changelog

| Version | Date | Notes |
|---------|------------|-----------------|
| 1.0 | 2026-06-10 | Initial version |
