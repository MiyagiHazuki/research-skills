# Review letter (English)

Fill every section. Do not leave instructional comments in the delivered letter. Quotes must be verbatim from the manuscript. The score block must match `scripts/map_score.py` stdout.

---

## Confidential comments to the area editor / action editor

**Paper:** {title}
**Venue overlay:** {conference_default | neurips2025 | journal_default | tmlr | named venue}
**Reviewer role:** independent peer reviewer (not an author of this paper)

**Recommendation class:** {accept-side 6–10 | borderline 5 | reject-side 1–4}

**One-paragraph assessment.** {What the paper claims, whether the evidence supports it, the single most important reason for the recommendation. No prestige comments. No fabricated related work.}

**Decision-bearing issues (for the AE).**
1. {issue} — {CRITICAL|MAJOR} — {why it moves the score}
2. ...

**Non-decision-bearing notes.** {Optional. Do not hide a gate here.}

**Confidence.** {low | medium | high} plus one sentence on expertise limits. Do not claim calibration.

**Calibration:** `NOT_CALIBRATED`. Score is table output of the dimension vector below, not a venue accept-rate forecast.

---

## Review for the authors

### Summary

{5–8 sentences. Problem, method, headline evidence, claimed contributions. Neutral. Authors should recognise their paper.}

### Strengths

- {Strength with quote: "..." (§x). Only strengths you actually found.}
- ...

### Weaknesses

Each item: severity, dimension or gate, quote, why it matters, whether a revision could fix it.

1. **[{CRITICAL|MAJOR|MINOR}] [{dimension or G#}]** {title}
   - Quote: "..." (§x / Table y)
   - Why it matters: {criterion}
   - Repairability: {one revision cycle / would need a different paper / not applicable}

2. ...

### Questions for the authors

3–5 questions. Each states the criterion under which the score would move.

1. {Question}
   - Score-changing if: {what answer would raise or lower which dimension}
2. ...

### Novelty (closest work)

| Work | Year | Venue | Relation | Delta real? |
| :--- | :--- | :--- | :--- | :--- |
| {verified citation} | | | | {yes / partial / no / unused grey zone} |

Queries and access date: {see novelty-trace.md}. Originality label: {label}. If search failed: Originality `NOT_ASSESSED`; this score is provisional.

### Dimension table

| Dimension | Label | Quote / miss | Decision-bearing |
| :--- | :--- | :--- | :--- |
| Originality | | | |
| Soundness | | | |
| Evidence | | | |
| Experiments | | | |
| Significance | | | |
| Literature | | | |
| Clarity | | | |

Gates hit: {none | G1 ...}. Counts: D={ } P={ } E={ }. Clarity penalty: {yes|no}.

### Score (copied from the script)

```
{paste scripts/map_score.py JSON stdout here}
```

**Conference:** {n}/10, {verbal} (NeurIPS 2024 meanings unless another overlay is named).
**Journal:** {Accept | Minor revision | Major revision | Reject | TMLR wording}.

Integrity: recomputed from the same vector; stated score equals table output. If these two lines ever disagree, delete the numeric score and fix the run.

### Minor comments

- {page/line nits. Not a second reject.}

---

## End matter

Reviewer did not rewrite the manuscript. Reviewer did not use model memory as a source for related work or numbers.
