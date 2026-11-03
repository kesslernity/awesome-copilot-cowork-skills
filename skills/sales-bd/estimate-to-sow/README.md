# Estimate to SOW

> Turns a priced estimate spreadsheet into a DRAFT statement of work built from your own template, with the maths checked before a single sentence is drafted.

## What it produces

- `DRAFT-SOW-<Client>-<date>-v1.docx`: your SOW template populated with scope, deliverables, schedule and fees taken only from the estimate, DRAFT-labelled in the filename and on the first line.
- `estimate-validation-<date>.md`: every arithmetic check (line maths, phase subtotals, grand total) with cell references for any discrepancy found.

Both files are saved next to the source estimate in OneDrive, with the exact paths reported in the conversation.

## Install

**Quickest: upload the zip.** [Download `estimate-to-sow.zip`](https://github.com/kesslernity/awesome-copilot-cowork-skills/raw/main/dist/zips/estimate-to-sow.zip). In Cowork, open **Customize**, select the **Skills** tab, select the arrow next to **Add**, then **Upload skill**, and choose the file. Cowork validates it and saves the skill to your OneDrive for you, so you never create a folder.

**Or copy this folder** into OneDrive at `/Documents/Cowork/skills/estimate-to-sow/`. The lowercase `skills` folder name is case-sensitive, and you copy the skill folder itself, not the category folder above it.

Either way, start a **NEW** Cowork conversation afterwards: skills are discovered only when a conversation starts. Then use one of the trigger phrases below.

Custom skills are not supported in Cowork on a phone or tablet, so this needs a laptop or desktop.

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
