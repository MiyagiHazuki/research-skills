# Claim vs evidence

Review lens, not a writing aid. Distilled from ARS claim-strength ladder / protected hedges and DIAL evidence hierarchy plus hedge ladder. Mechanism shape of the ladder is borrowed (via ARS) from Yila-AI/sci-ssci-skills.

## Source hierarchy (reviewer)

| Level | What it is | Can support in the review |
| :--- | :--- | :--- |
| L1 | The manuscript, supplement, user-supplied code/data | quotes, numbers, claims about *this* paper |
| L2 | Verified abstract of a retrieved paper | that work's direction and headline, not its tables |
| L3 | Verified metadata (title, authors, year, venue) | "X et al. (year) exist and addressed Y" |
| L0 | Uncontroversial field common knowledge | background only; no numbers, names, or comparisons |
| L4 | Model memory | **nothing** |

If you hesitate whether something is L0, it is not. Search or mark `NOT_ASSESSED`.

## Strength ladder (read the paper against it)

```
is consistent with / may suggest
  < is associated with / correlates with
    < predicts
      < contributes to
        < affects / leads to
          < causes / demonstrates / proves
```

Flag when the **manuscript** sits higher than its evidence. "Prove" belongs to mathematics. "State-of-the-art" needs the benchmark, the split, and the comparison set. "We are the first" needs [novelty-search.md](novelty-search.md). Dropping a hedge ("may improve" → "improves") is a silent up-move: MAJOR if it is a headline claim.

## Hedge ladder (for judging, not for rewriting)

- Strong: show, demonstrate, establish, confirm — needs multiple independent results or a closed proof.
- Medium: suggest, indicate, consistent with — typical empirical paper.
- Weak: may, might, appears to — mechanism-only or single-dataset.
- None: "to our knowledge", "open question".

Stacked hedges are not a virtue. Underclaiming a theorem is as wrong as overclaiming a correlation.

## Checks

1. List the 3–7 material claims (abstract + contribution bullets + last paragraph of intro).
2. For each, point to the theorem, table, or figure that bears it.
3. A contribution with no experimental or proof trace is CRITICAL as a finding and pulls Evidence toward `DOES_NOT_MEET`.
4. Do not strengthen or weaken claims in the review letter beyond what the quotes support.
5. Do not attach a background citation's result to this paper's finding.
