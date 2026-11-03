# RFP Comparison Pack

> Reads several bid responses against your requirements and produces a DRAFT comparison pack — a requirement-by-supplier matrix, gaps, and clarification questions. Prepares the panel; never scores or picks a winner.

## What it produces

- `DRAFT-rfp-comparison-<Category>-<date>-v1.docx`: a comparison pack — matrix (each cell cited to a response), gaps per supplier, clarification questions, and neutral observations. DRAFT-labelled in the filename and first line.
- `DRAFT-rfp-comparison-<Category>-<date>-v1.xlsx` (optional): the matrix as a workbook.

Both save next to the responses in OneDrive, with the exact paths reported in the conversation.

## Install

**Quickest: upload the zip.** [Download `rfp-comparison-pack.zip`](https://github.com/kesslernity/awesome-copilot-cowork-skills/raw/main/dist/zips/rfp-comparison-pack.zip). In Cowork, open **Customize**, select the **Skills** tab, select the arrow next to **Add**, then **Upload skill**, and choose the file. Cowork validates it and saves the skill to your OneDrive for you, so you never create a folder.

**Or copy this folder** into OneDrive at `/Documents/Cowork/skills/rfp-comparison-pack/`. The lowercase `skills` folder name is case-sensitive, and you copy the skill folder itself, not the category folder above it.

Either way, start a **NEW** Cowork conversation afterwards: skills are discovered only when a conversation starts. Then use one of the trigger phrases below.

Custom skills are not supported in Cowork on a phone or tablet, so this needs a laptop or desktop.

## Example triggers

- "Compare these three tender responses against our requirements"
- "Build a comparison matrix from the bids in the Sourcing folder"
- "Collate the supplier proposals for the cleaning tender against the RFP"
- "Matrix these RFQ responses and list the gaps"

## Why this exists

Evaluation panels lose hours hand-collating bids into a grid before they can even start scoring — and a rushed grid is where requirements get missed and fairness slips. This skill does the collation from your requirements, cites every cell back to a response, and stops cleanly at comparison: it never scores, ranks, or recommends, so the panel's evaluation stays theirs and stays auditable.

## Status

Tested in Cowork: not yet — format-validated against the Agent Skills spec; run a live tenant test before relying on it.

## Changelog

| Version | Date | Notes |
| --- | --- | --- |
| 1.0 | 2026-06-18 | Initial version |
