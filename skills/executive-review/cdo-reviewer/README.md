# CDO Reviewer

> Pressure-test your business case against a Chief Data Officer archetype before the real one asks where your numbers actually come from.

## What it produces

A structured review document, `<artifact-name>-cdo-review.docx`, saved to `/Documents/Cowork/reviews/` in your OneDrive, containing:

- **VERDICT**: ready, ready with conditions, or not ready
- **TOP FINDINGS**: each one quotes or cites the exact part of your document it is about, no generic feedback; where your document is silent on a probe, the finding becomes an open question, never an invented fact
- **RISKS**: from the data lens (measurement integrity, data quality, lawful basis and privacy, vendor data flows, AI and model governance)
- **WHAT WOULD CHANGE MY MIND**: the specific evidence and definitions that would move the verdict up
- **5 INTERROGATION QUESTIONS**: the questions the real CDO is likely to ask in the room

The persona lives in `references/persona.md`: mandate, ten probes, red flags, what convinces a CDO and what gets dismissed, plus documented blind spots so a validator can challenge the feedback where the archetype distorts it.

## Install in 60 seconds

1. Copy this folder (`cdo-reviewer`) into your OneDrive at `/Documents/Cowork/skills/` (the lowercase `skills` folder name is case-sensitive).
2. Start a NEW Cowork conversation. Skills are discovered at conversation start, not mid-conversation.
3. Use one of the trigger phrases below, naming the file you want reviewed.

## Example triggers

- "Run a CDO review on customer-360-business-case.docx"
- "What would a Chief Data Officer say about this analytics proposal?"
- "Pressure-test the data and AI governance claims in this deck before the steering committee sees it"
- "Every number in this plan needs a source. Interrogate it like a CDO would."

## Why this exists

The executive-review suite ships a core of C-suite reviewers. Bench personas like this one extend the suite beyond that core line-up to the executives who interrogate a specific dimension of a proposal. The CDO seat covers the questions the core bench leaves thinnest: whether the headline metrics have definitions and source systems, whether the data is fit and lawfully usable, and whether the AI components are governed rather than just mentioned. It works standalone; you do not need the rest of the suite installed.


## Status

Tested in Cowork: pending (June 2026). Format-validated against the Agent Skills spec.

## Changelog

| Version | Date | Notes |
|---------|------------|-----------------|
| 1.0 | 2026-06-10 | Initial version |
