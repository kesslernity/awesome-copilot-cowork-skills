# COO Reviewer

> Pressure-test a plan against the operations lens before the real COO does it in the meeting.

## What it produces

A DRAFT Word review of your proposal, business case, deck or plan, written in character as a Chief Operating Officer archetype, saved to `/Documents/Cowork/reviews/<artifact-name>-coo-review.docx`. The review contains:

- **VERDICT**: proceed / proceed with conditions / not ready
- **TOP FINDINGS**: each one quotes or cites the specific section, page or slide it is about
- **RISKS**: delivery and operational risks from the COO lens
- **WHAT WOULD CHANGE MY MIND**: the evidence that would move the verdict
- **5 INTERROGATION QUESTIONS**: the questions the real executive would ask in the meeting

## Install

**Quickest: upload the zip.** [Download `coo-reviewer.zip`](https://github.com/kesslernity/awesome-copilot-cowork-skills/raw/main/dist/zips/coo-reviewer.zip). In Cowork, open **Customize**, select the **Skills** tab, select the arrow next to **Add**, then **Upload skill**, and choose the file. Cowork validates it and saves the skill to your OneDrive for you, so you never create a folder.

**Or copy this folder** into OneDrive at `/Documents/Cowork/skills/coo-reviewer/`. The lowercase `skills` folder name is case-sensitive, and you copy the skill folder itself, not the category folder above it.

Either way, start a **NEW** Cowork conversation afterwards: skills are discovered only when a conversation starts. Then use one of the trigger phrases below.

Custom skills are not supported in Cowork on a phone or tablet, so this needs a laptop or desktop.

## Example triggers

- "Review my Q3 expansion proposal as a COO before Thursday's steering committee."
- "Run a COO review on rollout-plan.docx."
- "Pressure-test this business case from an operations angle: capacity, timeline, dependencies."
- "What would a COO ask about this deck? Give me the hard questions before the meeting."

## Why this exists

This skill is one of the reviewers in the executive-review suite, which exists because people keep asking for a way to pressure-test documents before real executive reviews: the questions that kill a proposal in the meeting are predictable, and it is cheaper to face them from an archetype first. The COO is the reviewer who checks whether the plan survives contact with a real calendar, a real org chart and a finite amount of people's time. Run it standalone, or run the other reviewers in the category for more lenses. Drop an `org-profile.md` into `/Documents/Cowork/` (template in this skill's references folder) and the review uses your company context instead of staying generic.

## Status

Tested in Cowork: 2026-06-16, passed. Format-validated against the Agent Skills spec.

## Changelog

| Version | Date | Notes |
|---|---|---|
| 1.0 | 2026-06-10 | Initial version |
