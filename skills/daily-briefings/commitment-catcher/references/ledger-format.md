# File formats: commitments.md and actions.md

Exact structures for the two files this skill maintains. Follow them precisely so every run can parse the previous run's output.

## commitments.md structure

```markdown
# Commitments ledger

Maintained by the commitment-catcher Cowork skill. Entries are never deleted; statuses change instead.
Ledger folder: /Documents/Cowork/commitments/
Last run: 2026-06-10 08:15 (UTC+2), window 2026-06-09 08:15 to 2026-06-10 08:15

## Overdue

| ID | Direction | Who | Commitment | Due | Source | Status | Last update |
|---|---|---|---|---|---|---|---|
| C-009 | MADE | Dana Verma, Contoso | Send the Q3 forecast workbook | 2026-06-08 | Email to Dana, 5 Jun 2026, "Q3 planning" | overdue | 2026-06-10 |

## Open

| ID | Direction | Who | Commitment | Due | Source | Status | Last update |
|---|---|---|---|---|---|---|---|
| C-014 | MADE | Priya Nair | Review the onboarding deck and return comments | 2026-06-12 (inferred) | Teams chat with Priya, 9 Jun 2026 | open | 2026-06-10 |
| C-015 | OWED | Tom Eklund, Fabrikam | Send the signed SOW | none stated | "Vendor sync" meeting transcript, 9 Jun 2026 | open | 2026-06-10 |

## Done (last 14 days)

| ID | Direction | Who | Commitment | Due | Source | Status | Last update |
|---|---|---|---|---|---|---|---|
| C-011 | MADE | Priya Nair | Book the workshop room | 2026-06-09 | Teams chat, 8 Jun 2026 | done (booking confirmation sent 9 Jun) | 2026-06-09 |

## Archive

| ID | Direction | Who | Commitment | Due | Source | Status | Last update |
|---|---|---|---|---|---|---|---|
```

## Rules

- **ID**: C-NNN, zero-padded to three digits, strictly increasing, never reused, sequence continues across runs.
- **Direction**: exactly MADE or OWED.
- **Who**: the counterparty, never the user. Display name, plus organisation when external.
- **Commitment**: one sentence, the deliverable. Conditional commitments include the condition in this cell.
- **Due**: YYYY-MM-DD, with "(inferred)" appended when resolved from a relative phrase, or "none stated".
- **Source**: enough to find the original (channel, person, date, subject or meeting title).
- **Status**: open, overdue or done. Cancelled items become "done (cancelled by user, DATE)". Done items carry brief closing evidence in parentheses.
- **Section order is fixed**: Overdue, Open, Done (last 14 days), Archive. A row lives in exactly one section, matching its status.
- Done rows older than 14 days move to Archive on the next run. Nothing is ever removed from the file.
- Update the "Last run" header line on every run with the timestamp and the window scanned.

## actions.md structure (To Do fallback)

Append a new dated section per run; never rewrite earlier sections.

```markdown
# To Do fallback: commitments that could not be written to Microsoft To Do

## 2026-06-10 run

- [ ] C-014 (MADE, due 2026-06-12) Review the onboarding deck and return comments for Priya Nair
- [ ] C-016 (MADE, due none stated) Send conference notes to the #q3-launch channel
```

Each line carries the ledger ID, direction, due date and deliverable so the user can act from this file alone.
