# Score mapping (deterministic)

Language generation may produce categorical labels with quotes. It may **not** choose the number. Run `scripts/map_score.py` and copy its output. If the letter disagrees with the script, the run is invalid.

Status: **unvalidated** (charter D1). Calibration: `NOT_CALIBRATED`. Do not claim the table matches a venue's accept rate.

## Inputs

Seven dimension labels, each `EXCEEDS | MEETS | PARTLY_MEETS | DOES_NOT_MEET | NOT_ASSESSED`, each with a quote or an explicit search miss:

| ID | Dimension | In the 1–10 table? |
| :--- | :--- | :--- |
| Originality | defensible contribution vs closest verified work | yes |
| Soundness | design, proofs, execution support the inferences | yes |
| Evidence | each material claim has the right kind of evidence | yes |
| Experiments | empirical protocol / proofs isolate the claim | yes |
| Significance | implications follow and matter for the stated audience | yes |
| Literature | critically integrates the literature the claims need | no (findings only; can trigger G4) |
| Clarity | meaning is reviewable; not prestige English | −1 cap only |

Fatal gates, each hit/miss with a quote. Definitions: [fatal-flaws.md](fatal-flaws.md).

- **G1** foundation collapse (including a data-refuted core mechanism)
- **G2** data–conclusion mismatch
- **G3** logic-chain break (contribution maps to no section, or argument does not close)
- **G4** novelty collapse (search found equivalent prior work)
- **G5** serious statistical-reporting failure (not a missing comma in a *p*-value)
- **G6** fabricated or unverifiable key result or citation

`NOT_ASSESSED` on a scientific dimension is excluded from counts *D*, *P*, *E*. If fewer than three of {Originality, Soundness, Evidence, Experiments, Significance} are assessed, the script refuses a score. Originality `NOT_ASSESSED` (search failed) forbids G4 and marks the score **provisional**.

## Procedure (must match the script)

1. If G1 or G2 or G4 or G6 is hit: conference score = 3. Skip the count table.
2. Else if G3 or G5 is hit: conference score = 4. Skip the count table.
3. Else, on the assessed scientific five, let *D* = count of `DOES_NOT_MEET`, *P* = `PARTLY_MEETS`, *E* = `EXCEEDS`:

| *D* | *P* | Conference | Verbal (NeurIPS 2024) |
| :--- | :--- | :--- | :--- |
| ≥ 2 | any | 3 | Reject |
| 1 | ≥ 2 | 4 | Borderline reject |
| 1 | 0–1 | 5 | Borderline accept |
| 0 | ≥ 3 | 5 | Borderline accept |
| 0 | 2 | 6 | Weak accept |
| 0 | 1 | 6 | Weak accept |
| 0 | 0 | 7 | Accept |
| 0 | 0 and *E* ≥ 2 | 8 | Strong accept |
| 0 | 0 and *E* ≥ 4 | 9 | Very strong accept |

4. If Clarity is `DOES_NOT_MEET`, subtract 1, floor 1. Clarity cannot raise the score.
5. Journal recommendation from the **post-clarity** conference score:

| Conference | Journal default |
| :--- | :--- |
| 8–9 | Accept |
| 7 | Minor revision |
| 6 | Minor revision |
| 5 | Major revision |
| 4 | Major revision, or Reject if G3 or G5 |
| 1–3 | Reject |

TMLR and NeurIPS 2025 overlays: [venue-overlays.md](venue-overlays.md).

## Integrity

Recompute from the same JSON twice. The two scores must be identical (charter E2). Do not round toward accept. Do not average imaginary reviewer personas.
