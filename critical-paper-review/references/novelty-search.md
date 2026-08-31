# Novelty search

Originality is judged against verified closest work, not against model memory. Distilled from DIAL retrieval-grounded novelty (pre-submission-reviewer Step 1 and deep-research citation protocol).

## Procedure

1. Copy the claimed contributions as bullets (intro / abstract). If the paper does not state them, write "unstated" and search from the title and method name anyway.
2. For each bullet, run at least two queries: (a) the paper's own keywords plus the task, (b) the closest method the paper itself cites plus the claimed difference axis. Record query strings and access date.
3. Keep a hit only if you can verify it (open abstract or page you actually fetched). Grey zone (broken link, metadata-only, "I recall a paper") is **unused**.
4. Build a table of 3–5 closest works. Columns: work (verified citation), year, venue, what it does, difference axis claimed by *this* paper, whether that axis is real given the hit.
5. Label Originality from the table, not from adjectives in the intro.

## Labels (Originality)

- `EXCEEDS`: a defensible delta on a named axis, and the closest works do not already occupy it.
- `MEETS`: a clear, bounded contribution (including a careful replication or a new setting of a known method).
- `PARTLY_MEETS`: a delta exists but is smaller than claimed, or the closest work is missing from the related-work section.
- `DOES_NOT_MEET`: no remaining delta on the paper's own axes.
- `NOT_ASSESSED`: search tools failed or returned nothing verifiable. **Do not invent papers.** Do not fire G4. Mark the mapped score provisional.

## G4

Hit G4 only when a verified closest work already delivers the claimed contribution on the same axes. Cite that work in the finding. Incremental work is not G4. Missing a citation that does not collapse the delta is Literature MAJOR, not G4.

## What not to do

- Do not pad the table with famous papers that are not close.
- Do not use training-cutoff "knowledge" as a source for 2025–2026 work.
- Do not conclude "first" because the authors said so.
- Record misses: query → zero verified hits is itself evidence.
