# Estimate to SOW

> Turns a priced estimate spreadsheet into a DRAFT statement of work built from your own template, with the maths checked before a single sentence is drafted.

## What it produces

- `DRAFT-SOW-<Client>-<date>-v1.docx`: your SOW template populated with scope, deliverables, schedule and fees taken only from the estimate, DRAFT-labelled in the filename and on the first line.
- `estimate-validation-<date>.md`: every arithmetic check (line maths, phase subtotals, grand total) with cell references for any discrepancy found.

Both files are saved next to the source estimate in OneDrive, with the exact paths reported in the conversation.

## Install in 60 seconds

1. Copy this folder into OneDrive at `/Documents/Cowork/skills/` (keep the folder name `estimate-to-sow`, the lowercase `skills` folder name is case-sensitive), then drop your own SOW template into the folder as a .docx.
2. Start a NEW Cowork conversation (skills are only discovered when a conversation starts).
3. Use one of the trigger phrases below.

## Example triggers

- "Turn estimate-acme-q3.xlsx into a statement of work"
- "Build an SOW from the Fabrikam migration estimate"
- "Convert this quote spreadsheet into our SOW template"
- "Draft a statement of work from the pricing workbook in the Presales folder"

## Why this exists

MSP and consulting pre-sales teams keep rebuilding the same document by hand: a priced estimate lives in Excel, the statement of work lives in Word, and someone retypes line items, hours, rates and totals between the two, occasionally carrying a broken subtotal straight into a signed contract. This skill does the transfer from your own template, refuses to draft until the estimate adds up, and never invents scope that is not in the spreadsheet.

## Status

Tested in Cowork: 2026-06-16, passed. Format-validated against the Agent Skills spec.

## Changelog

| Version | Date | Notes |
| --- | --- | --- |
| 1.0 | 2026-06-10 | Initial version |
