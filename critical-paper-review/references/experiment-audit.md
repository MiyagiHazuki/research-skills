# Experiment audit

For empirical CS/ML/systems papers. For theoretical papers, skip protocol items and audit proofs instead. Distilled from DIAL attribution isolation / contribution mapping and ARS methodological rigor.

## Attribution

The headline gain must be isolated from routing, post-processing, a stronger base model, extra data, or favorable subsets. No such ablation → finding "attribution unverified", MAJOR, and Experiments at best `PARTLY_MEETS`. If the paper's own ablation shows the core mechanism loses, that is G1 ([fatal-flaws.md](fatal-flaws.md)).

## Baselines

- Current, not a three-year-old proxy, unless the paper justifies the cutoff.
- Same budget, same backbone, same data, unless the difference is the claim.
- "We beat prior work" without naming the strongest public result on that benchmark is PARTLY_MEETS.
- Nerfed baselines (weaker hyperparameters than the original paper) are MAJOR.

## Protocol

- Train / validation / test split stated; test not used for model selection.
- Seeds or reruns for the headline number when the method is stochastic.
- Hyperparameter search described for *both* the method and the baselines, or explicitly identical.
- Leakage: time-series future information, graph neighbor leakage, pretraining overlap with test, prompt contamination. Leakage that makes the headline uninterpretable is G5.

## Contribution-to-section map

Every contribution bullet should map to a method subsection and to an experiment, theorem, or analysis. A bullet that maps to nothing is CRITICAL as a finding and is G3 if it is a main claimed contribution.

## Theory overlay

Check definitions, lemma-to-theorem dependence, and that corollaries do not exceed the theorem. Do not demand a results table. A missing proof of a numbered theorem that the claims need is Soundness `DOES_NOT_MEET` and may be G3.

## Benchmark overlay (only if the paper *is* a benchmark)

Coverage across model classes; contamination discussion; human baseline or quality control; license and data card; findings that are specific and data-supported rather than "models still fail". Missing contamination talk on a dataset likely to overlap training corpora is MAJOR, not automatically G5.

## Statistics-journal overlay

Estimand stated; identification or assumptions explicit; robustness; uncertainty on the headline estimand. See [statistical-red-flags.md](statistical-red-flags.md).
