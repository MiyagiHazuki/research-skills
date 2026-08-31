# Statistical red flags

Use on quantitative CS/ML papers and, more strictly, on statistics-journal papers. Distilled from ARS statistical reporting standards; APA formatting is **not** required at NeurIPS/ICML. Do not punish a conference paper for missing Cohen's *d* when it reports the task metric with uncertainty.

## Always check (empirical papers)

- Headline metric: definition, split, and direction of improvement.
- Uncertainty: interval, standard deviation across seeds, or an equivalent. Absence on the *headline* number is MAJOR; if the paper is a statistics journal and the estimand has no uncertainty, consider G5.
- Multiple testing: many datasets × many metrics × many ablations, only the wins discussed → MAJOR; if that fishing *is* the claim, G5.
- Leakage and double-dipping (test-set tuning, feature selection on full data).
- Sample size and attrition, if humans or observational units are the sample.

## Statistics-journal extras

- Estimand and identifying assumptions.
- Effect size, not only a star on a *p*-value.
- Exact *p* or a likelihood-based interval; do not require APA punctuation.
- Pre-specification vs HARKing (hypotheses that appear only after the significant table).
- Uncorrected comparisons; hidden non-results.
- For means of integer-bounded items, a GRIM-class sanity check is allowed when the numbers are reported with enough precision to test; a mismatch is G5 only if the impossible number is load-bearing.

## p-hacking / HARKing signals (findings, then judge G5)

Optional stopping implied but not stated; dozens of metrics, one "significant"; covariates added until the star appears; the intro's hypothesis matches only the winning specification. One signal is MAJOR. A pattern that makes the headline untrustworthy is G5.

## What is not G5

A missing CI on a secondary ablation; a conference paper that reports mean ± std over three seeds; a theoretical paper with no experiment; non-significant results that *are* reported. Those can still be MINOR or MAJOR.
