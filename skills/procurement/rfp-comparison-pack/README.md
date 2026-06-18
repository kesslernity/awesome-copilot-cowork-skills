# RFP Comparison Pack

> Reads several bid responses against your requirements and produces a DRAFT comparison pack — a requirement-by-supplier matrix, gaps, and clarification questions. Prepares the panel; never scores or picks a winner.

## What it produces

- `DRAFT-rfp-comparison-<Category>-<date>-v1.docx`: a comparison pack — matrix (each cell cited to a response), gaps per supplier, clarification questions, and neutral observations. DRAFT-labelled in the filename and first line.
- `DRAFT-rfp-comparison-<Category>-<date>-v1.xlsx` (optional): the matrix as a workbook.

Both save next to the responses in OneDrive, with the exact paths reported in the conversation.

## Install in 60 seconds

1. Copy this folder into OneDrive at `/Documents/Cowork/skills/` (keep the folder name `rfp-comparison-pack`; the lowercase `skills` folder name is case-sensitive).
2. Start a NEW Cowork conversation (skills are only discovered when a conversation starts).
3. Put the requirements and the supplier responses in OneDrive/SharePoint and use a trigger below.

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
