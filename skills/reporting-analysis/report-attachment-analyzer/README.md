# Report Attachment Analyzer

> Turns the report that lands in your inbox every week into a maintained trend spreadsheet and a one-page summary of what changed.

## What it produces

All saved to OneDrive under `/Documents/Cowork/output/report-attachment-analyzer/<report-name>/`:

- `trends.xlsx`: one append-only row per reporting period, with the metrics you chose
- `summary-YYYY-MM-DD.docx` and `summary-latest.docx`: deltas versus the previous period plus flagged anomalies, labelled DRAFT
- `processed-log.md`: every handled email logged by message ID, so no figure is ever double-counted
- `attachments/`: a dated copy of each source file, kept for audit

## Install in 60 seconds

1. Copy this folder into OneDrive at `/Documents/Cowork/skills/` (keep the folder name `report-attachment-analyzer`, and note the lowercase `skills` folder is case-sensitive).
2. Start a NEW Cowork conversation. Skills are only discovered when a conversation starts.
3. Use one of the trigger phrases below.

On the first run the skill asks for your report details (sender, subject, metrics) and writes them into `references/report-config.md` for you, or you can edit that file yourself before step 2.

## Example triggers

- "Update the trends for the weekly sales report"
- "Check my inbox for the latest ops KPI report and tell me what changed"
- "Has the monthly cloud cost report arrived? Pull the numbers into the trend sheet"
- "Set up tracking for the finance report I get every Monday"

## Why this exists

The OP of a thread on r/microsoft_365_copilot about Cowork's plugin support (https://www.reddit.com/r/microsoft_365_copilot/comments/1t4x740/) described building exactly this workflow: "scan my inbox for those emails, scan those attachments and give me the analytics". This skill composes Cowork's Email, Excel, PDF and Word built-ins into that workflow, and adds a processed-message log so re-runs never count the same report twice.

## Status

Tested in Cowork: 2026-06-16, passed. Format-validated against the Agent Skills spec.

## Changelog

| Version | Date | Notes |
|---------|------|-------|
| 1.0 | 2026-06-10 | Initial version |
