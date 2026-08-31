# Review dimensions

Seven dimensions. Labels: `EXCEEDS | MEETS | PARTLY_MEETS | DOES_NOT_MEET | NOT_ASSESSED`. Each label needs at least one verbatim quote from the manuscript, or an explicit search miss. These labels are categories, not points. Only `scripts/map_score.py` may turn them into a number ([score-mapping.md](score-mapping.md)).

Distilled from ARS review-criteria framework / quality rubrics and DIAL handbook 1.1 (what reviewers punish). Paraphrase, not a dump.

## Judgement form (every dimension)

| Field | Required |
| :--- | :--- |
| Judgement | one of the five labels |
| Quote or miss | section/page + verbatim span, or "search: &lt;query&gt; → no verified hit" |
| Why this label | one or two sentences tied to the criterion below |
| Decision-bearing? | yes/no; if yes, which gate or table cell it feeds |

`NOT_ASSESSED` is for missing access (search down, proofs not in the PDF), not for indecision. Do not pick `MEETS` as a midpoint.

## The seven

**Originality.** What defensible contribution does the paper make relative to the 3–5 closest *verified* works, on the difference axes the paper itself claims? Replication and boundary tests can `MEETS`. "We are the first" without a search is not `EXCEEDS`. Search failed → `NOT_ASSESSED`, never a hallucinated literature.

**Soundness.** Can the design, execution, analysis, and (for theory) proofs support the inferences? Apply the paper's own paradigm: do not demand ablations of a pure existence proof, and do not accept a learning paper whose estimator is unidentified.

**Evidence.** Does each material claim have evidence of the right type, quality, and coverage? A claim with no experimental or proof trace is `DOES_NOT_MEET` for that claim. Model memory is not evidence ([claim-evidence.md](claim-evidence.md)).

**Experiments.** For empirical papers: baselines, protocol, attribution, leakage, seeds. For theoretical papers, read this as proofs and analysis completeness, not "missing a results table". For mixed papers, score the empirical half here and the proofs under Soundness.

**Significance.** Do the claimed implications follow from the evidence and matter for the stated audience? Modest, well-supported contributions can `MEETS`. Do not require cross-field impact. Do not reward hype.

**Literature.** Does the paper critically integrate the work needed to establish its question, alternatives, and contribution? Coverage is relative to the claims, not a citation count. Missing work should be named when known from search. This dimension does not enter *D*/*P*/*E*; it can still be MAJOR and can trigger G4.

**Clarity.** Is the reasoning precise enough to interpret and verify? Separate meaning problems from non-native phrasing. Copyediting is MINOR. Clarity `DOES_NOT_MEET` subtracts at most 1 from the conference score and cannot raise it.

## Paper-type overlays (add, do not replace)

**Empirical ML / systems.** Hypothesis or claim testable; splits and leakage; internal validity; conclusion conservatism.

**Theoretical / statistical theory.** Definitions stable; proof chain closed; alternatives handled; testable implications if the paper claims empirical relevance.

**Benchmark / eval.** Gap is measurable and non-trivial; coverage across models; contamination discussed; findings surprising and data-supported. Extra checks in [experiment-audit.md](experiment-audit.md).

**Statistics journal empirical.** Identification, estimand, uncertainty, effect size, robustness. Extra checks in [statistical-red-flags.md](statistical-red-flags.md).

## `MEETS` vs neighbours (avoid inflation)

- `EXCEEDS`: the criterion is satisfied *and* the paper does something the venue rarely sees done well (isolated mechanism, unusually complete uncertainty, or a contribution that survives the closest-work table). Rare.
- `MEETS`: a competent top-venue paper on this axis. Most accepts live here.
- `PARTLY_MEETS`: the axis is attempted but a named piece is missing or overclaimed.
- `DOES_NOT_MEET`: the axis fails in a way that would survive a rebuttal unless the paper changes.

## Findings severity (orthogonal to labels)

- **CRITICAL**: would force reject or a fatal gate if unrepaired (broken argument, unsupported headline claim, equivalent prior work).
- **MAJOR**: first-round reviewer flag; repairable in a revision cycle.
- **MINOR**: polish. Do not let a pile of MINOR items impersonate a reject.

Severity honesty cuts both ways: do not upgrade taste to CRITICAL, and do not bury a logic break as MINOR.
