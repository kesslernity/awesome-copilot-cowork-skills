# Insight Pack — Structure & Rules

The structure for the DRAFT insight pack. It accelerates an analyst's first read; it is never the source of truth.

## Document structure

1. **Header / DRAFT line** — "DRAFT insight pack for <dataset> — generated <date>. Exploration only; figures are unverified and observations are leads, not conclusions. The analyst must verify in the data platform."
2. **Profile** — row count, columns + apparent types, missing/blank per key column, duplicates, value ranges/categories. Label counts "as read — verify in source".
3. **Observations (leads)** — each cites the column(s)/values and is phrased as a lead.
4. **Caveats** — completeness, sample size, correlation-not-causation, ambiguities.
5. **Suggested next steps & charts** — follow-up analyses and chart ideas for the analyst to build.

## How to phrase an observation

- Good (lead): "Average [value] in [segment A] appears ~30% higher than [segment B] (col: region, value) — worth confirming and investigating why."
- Bad (conclusion/cause): "Segment A outperforms because of better service." ❌ (asserts cause)
- Bad (authoritative): "Total revenue is $4.2M." ❌ — instead: "Sum of [amount] as read is ~$4.2M — verify in source."

## Never include

- A cause for an observed pattern (correlation is not causation).
- A business decision or recommendation as the answer (offer next questions/options instead).
- A data-quality verdict or an official metric value.
- Quoted individual records that look like personal/sensitive data — flag for privacy review instead.

Every figure in the pack is a draft to verify. The number that ships comes from a reproducible query, not this pack.
