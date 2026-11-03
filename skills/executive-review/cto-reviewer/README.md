# CTO Reviewer

> Pressure-test a proposal against the questions a Chief Technology Officer will actually ask, before you are in the room with one.

## What it produces

A DRAFT Word review document, `<artifact-name>-cto-review.docx`, saved to `/Documents/Cowork/reviews/`, containing:

- **VERDICT**: proceed, proceed with conditions, or not ready, with justification
- **TOP FINDINGS**: three to seven findings, each citing the exact phrase, section, slide or page it is about
- **RISKS**: architecture, technical debt, build versus buy, security of design, capacity and vendor lock-in
- **WHAT WOULD CHANGE MY MIND**: the specific evidence that would raise the verdict
- **5 INTERROGATION QUESTIONS**: the questions the real executive would ask in the meeting

The artifact you submit is read, never modified. If `/Documents/Cowork/org-profile.md` exists, the review uses it as company context; otherwise it runs generic and tells you where the template lives.

## Install

**Quickest: upload the zip.** [Download `cto-reviewer.zip`](https://github.com/kesslernity/awesome-copilot-cowork-skills/raw/main/dist/zips/cto-reviewer.zip). In Cowork, open **Customize**, select the **Skills** tab, select the arrow next to **Add**, then **Upload skill**, and choose the file. Cowork validates it and saves the skill to your OneDrive for you, so you never create a folder.

**Or copy this folder** into OneDrive at `/Documents/Cowork/skills/cto-reviewer/`. The lowercase `skills` folder name is case-sensitive, and you copy the skill folder itself, not the category folder above it.

Either way, start a **NEW** Cowork conversation afterwards: skills are discovered only when a conversation starts. Then use one of the trigger phrases below.

Custom skills are not supported in Cowork on a phone or tablet, so this needs a laptop or desktop.

## Example triggers

- "Give the Q3 platform migration business case a CTO review before Thursday's steering committee."
- "Pressure-test proposal-vendor-consolidation.docx as a CTO."
- "What would a CTO ask about this plan? Here is the text: ..."
- "Run a technical review of the data-platform deck from the technology seat."

## Why this exists

This is one seat of the executive-review suite: executive archetypes that interrogate a document the way a real leadership team would, so the author fixes the gaps before the actual meeting. It answers a recurring ask from people shipping business cases and decks: a way to pressure-test a document against hard executive questions before the real review. The CTO seat covers the questions that most often sink technology proposals: scale assumptions, hidden debt, vendor exit terms and capacity displacement. It works standalone.

## Status

Tested in Cowork: 2026-06-16, passed. Format-validated against the Agent Skills spec.

## Changelog

| Version | Date | Notes |
| --- | --- | --- |
| 1.0 | 2026-06-10 | Initial version |
