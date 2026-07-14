# AGENTS.md Reference

Canonical template for `init-with-grilling`. This is a research charter, not a product specification. Keep unresolved items explicit rather than filling them with guesses.

## AGENTS.md Template

```markdown
# Research Charter: <short title>

> Status: exploratory | preregistered | confirmatory | archival
> Last updated: <YYYY-MM-DD>
> Maintainer: <person or group>

## 1. Research Question & Scope

- **Question**: <falsifiable question>
- **Phenomenon/system**: <what is studied>
- **Unit of analysis**: <sample, subject, run, image, document, etc.>
- **Target population or regime**: <where the claim is intended to hold>
- **Deliverable**: <paper, dataset, model, analysis, or reproduction>
- **Non-goals**: <claims this project will not support>

## 2. Claims, Hypotheses & Alternatives

| ID | Type | Statement | Observable implication | Status |
| :--- | :--- | :--- | :--- | :--- |
| H1 | Primary hypothesis | <directional or mechanistic hypothesis> | <what result supports it> | planned |
| H0 | Null | <null/no-effect expectation> | <what result fails to distinguish alternatives> | planned |
| A1 | Alternative | <competing explanation> | <how it differs empirically> | planned |

**Claim boundary**: <strongest conclusion justified by planned evidence>
**Negative result interpretation**: <what a null result would and would not imply>

## 3. Operationalization & Analysis Contract

- **Exposure/intervention**: <definition and assignment>
- **Outcome**: <definition, measurement, direction>
- **Estimand**: <quantity being estimated>
- **Primary metric**: <metric and rationale>
- **Meaningful effect threshold**: <domain-justified threshold>
- **Controls/covariates**: <what is controlled and why>
- **Inclusion/exclusion**: <rules fixed before confirmatory analysis>
- **Uncertainty**: <CI/credible interval/bootstrap/posterior/etc.>
- **Multiplicity**: <correction or explicit rationale>
- **Sensitivity analyses**: <reasonable alternate specifications>

## 4. Data, Materials & Provenance

| Artifact | Source/version/date | License/ethics | Transformation | Integrity check |
| :--- | :--- | :--- | :--- | :--- |
| <dataset/material> | <source> | <status> | <pipeline step> | <hash/count/check> |

- **Data dictionary**: <path or not yet available>
- **Known limitations**: <missingness, selection, measurement error, leakage, batch effects>
- **Privacy/safety controls**: <controls or N/A>

## 5. Method, Baselines & Experiment Matrix

| Experiment | Purpose | Comparison/control | Variables | Replicates/seeds | Decision rule |
| :--- | :--- | :--- | :--- | :--- | :--- |
| E1 | <decisive test> | <baseline/control> | <changed variables> | <count/seeds> | <predefined interpretation> |

- **Baseline**: <minimal credible baseline and source>
- **Ablations**: <components or assumptions removed>
- **Split/design**: <split, randomization, blocking, or sampling>
- **Stopping rule**: <when to stop, repeat, or expand>
- **Failure criteria**: <what invalidates a run or triggers diagnosis>

## 6. Computational Reproducibility

- **Environment**: <lockfile/container/OS/interpreter/compiler>
- **Hardware**: <CPU/GPU/RAM and relevant precision>
- **Entry points**: <commands for prepare, run, evaluate, reproduce>
- **Randomness**: <seeds and deterministic limits>
- **External dependencies**: <APIs, models, services, access date/version>
- **Artifacts**: <logs, figures, tables, checkpoints, hashes>
- **Expected variance**: <nondeterminism and acceptable tolerance>

## 7. Evidence Ledger

| Claim/result | Evidence location | Evidence type | Confidence/uncertainty | Caveat |
| :--- | :--- | :--- | :--- | :--- |
| <claim> | <file, figure, table, log, citation> | observed/planned/derived/cited | <assessment> | <limitation> |

## 8. Open Decisions & Research Log

| Decision/question | Current state | Evidence needed | Owner | Due/trigger |
| :--- | :--- | :--- | :--- | :--- |
| <item> | unknown | <next observation or analysis> | <person> | <condition> |

Record protocol changes, surprising results, failed attempts, and interpretation updates. Do not rewrite history silently.

## 9. Research Guardrails

- No fabricated data, citations, results, or certainty.
- Separate exploratory analysis from confirmatory claims.
- Preserve raw inputs; make transformations executable and inspectable.
- Record versions, access dates, seeds, exclusions, and failed runs.
- Do not alter primary metric or stopping rule after inspecting results without logging the change.
- Protect private, sensitive, or hazardous materials.
- No commit, publication, deletion, or irreversible data operation without explicit authorization.
```

## Question design guide

- vague question → ask target population, measurable outcome, and falsifiable contrast;
- vague success → ask what effect is scientifically meaningful, not merely detectable;
- method-first request → ask what claim the method tests and what baseline could falsify it;
- dataset-first request → ask what population it represents and what leakage exists;
- metric shopping → define primary metric before secondary metrics;
- one impressive run → require replicates, uncertainty, and failure/stop rule;
- reproduction request → identify paper version, code/data commit, deviations, and tolerance;
- terminology drift → maintain operational definitions, not just names;
- overloaded infrastructure → choose the smallest setup able to answer the question.

The charter should make the next experiment obvious. If not, question the uncertainty instead of adding architecture.
