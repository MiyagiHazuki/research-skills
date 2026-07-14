---
name: init-with-grilling
description: Initializes research projects by eliciting a precise question, hypotheses, evidence plan, methods, provenance, computational environment, and reproducibility constraints, then writes a research charter. Use for new experiments, paper reproductions, analysis projects, or "/init-with-grilling".
---

# Init with Grilling

Turn an underspecified research idea into an auditable research charter. Aim: make claims testable, assumptions visible, evidence traceable, and future work reproducible. Do not optimize for production delivery or premature architecture.

**Prerequisite**: load `grill-me` only when interactive questioning helps. Its mechanics are optional; do not inherit its production-oriented assumptions. For a well-specified request, infer explicit facts and ask only for blocking unknowns.

## Language

Use the user's language unless repository convention says otherwise. Preserve exact names of datasets, methods, variables, instruments, genes, packages, and statistical terms.

## Workflow

### 1. Reconnoiter before questioning

Inspect existing README, protocols, notebooks, data dictionaries, configs, tests, environments, and prior results.

- separate observed facts from assumptions;
- avoid asking for information already present;
- never invent a dataset, baseline, parameter, result, citation, or causal interpretation;
- if no repository exists, mark the charter as planning and distinguish planned from observed content.

### 2. Ask research questions

Ask one batched round when interaction is needed. Ask a second, smaller round only for blocking ambiguity. Use options only for real methodological trade-offs; never mark a choice recommended merely because it is fashionable.

Cover unresolved dimensions:

| Dimension | Extract |
|---|---|
| Research question & scope | Falsifiable question, phenomenon, unit of analysis, target population/system, non-goals |
| Claims & hypotheses | Primary claim, competing explanations, directional hypotheses, null/negative outcomes, claim strength |
| Operationalization | Variables, estimands, metrics, controls, inclusion/exclusion rules, meaningful effect size |
| Evidence & provenance | Data/source versions, acquisition date, license/ethics, preprocessing, labels, citation, bias/leakage |
| Method & comparison | Baselines, ablations, controls, splits, seeds, statistical model, uncertainty, sensitivity analyses |
| Reproducibility | Environment, dependencies, hardware, commands, artifacts, deterministic limits, external services |
| Research boundaries | Assumptions, limitations, forbidden shortcuts, privacy/safety constraints, stop conditions |

### 3. Build the research charter

Write `AGENTS.md` at project root using [REFERENCE.md](REFERENCE.md).

Rules:

- label statements `observed`, `planned`, `assumed`, or `unknown` where confusion is possible;
- no placeholders in completed sections; unresolved blockers go in `Open decisions` with next evidence needed;
- distinguish exploratory from confirmatory analysis;
- treat negative, null, and failed results as valid outcomes;
- point every major claim to data, code, derivation, or citation;
- prefer the smallest experiment that can answer the question;
- preserve source, version/date, transformation, and decision provenance;
- never claim reproducibility while uncontrolled dependencies, data, randomness, or services remain.

### 4. Confirm and hand off

Report: research question, primary hypothesis, decisive experiment, largest uncertainty, and files written. Never present hypotheses as findings. Update the charter when question, protocol, data, or interpretation changes.

## Research integrity guardrails

- no fabricated observations, citations, metrics, sample sizes, or certainty;
- no silent changes to preprocessing, exclusions, metrics, or stopping rules after seeing results;
- exploratory findings remain separate from preregistered/confirmatory claims;
- report uncertainty, missingness, selection bias, multiple comparisons, and failed runs when relevant;
- use synthetic or anonymized data for private/sensitive material;
- record version, access date, and configuration for benchmarks and external services;
- scientific validity, traceability, and honest uncertainty outrank shipping speed.
