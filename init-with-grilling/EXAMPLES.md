# Usage Example — Research Edition

Compact walkthrough: turning an underspecified ML reproduction into an auditable research plan.

## Session: Reproducing a Robustness Claim

### Repository reconnaissance

Repository contains a paper PDF, incomplete training script, and no locked environment. Agent does not invent a stack or claim reproducibility. It asks one batched round for missing scientific decisions:

```json
{
  "questions": [
    {
      "header": "Research Question",
      "question": "Which claim should the reproduction test, and on what target regime?",
      "options": [
        {"label": "Test robustness under shift", "description": "Reproduce main comparison, then evaluate predefined shifted-data condition."},
        {"label": "Headline metric only", "description": "Lower scope; cannot support a robustness claim."}
      ]
    },
    {
      "header": "Hypothesis",
      "question": "What result supports the claim, and what competing explanation must be tested?",
      "options": [
        {"label": "Predefined effect + uncertainty", "description": "Report effect, interval, seeds, and baseline; one run is insufficient evidence."},
        {"label": "Exploratory comparison", "description": "Useful for discovery; not confirmatory without a fixed protocol."}
      ]
    },
    {
      "header": "Operationalization",
      "question": "Which primary metric, split, baseline, and meaningful effect threshold define success?",
      "options": [
        {"label": "Paper metric + fixed split", "description": "Match paper first; log deviations and add a practical threshold."},
        {"label": "Best discovered metric", "description": "Exploratory only; cannot replace primary metric silently."}
      ]
    },
    {
      "header": "Provenance",
      "question": "Which paper/code/data versions are authoritative, and what deviations are allowed?",
      "options": [
        {"label": "Pin versions + log deviations", "description": "Record commit, release, access date, preprocessing, and unavailable dependency."},
        {"label": "Use current versions", "description": "Fast but weakens auditability."}
      ]
    },
    {
      "header": "Integrity",
      "question": "What must every run record, and which actions require authorization?",
      "options": [
        {"label": "Seeds, environment, failures", "description": "Keep commands, configs, metrics, uncertainty, and failed runs."},
        {"label": "Optimize one successful run", "description": "Insufficient evidence for a scientific claim."}
      ]
    }
  ]
}
```

### User response

> Test robustness under shift. Match paper metric and split, use five seeds, compare paper baseline plus stronger baseline. Pin dataset release and log unavailable augmentation. Null result remains valid. Do not download restricted data or publish artifacts without approval.

### Generated `AGENTS.md` excerpt

```markdown
# Research Charter: Robustness Under Distribution Shift

> Status: exploratory
> Last updated: 2026-07-14

## 1. Research Question & Scope

- **Question**: Does the reported method retain its advantage under the paper's predefined shift?
- **Unit of analysis**: independent training run evaluated on fixed test splits.
- **Deliverable**: reproduction report with deviations and uncertainty.
- **Non-goals**: production deployment, new SOTA claims, or causal claims beyond the experiment.

## 2. Claims, Hypotheses & Alternatives

| ID | Type | Statement | Observable implication | Status |
| :--- | :--- | :--- | :--- | :--- |
| H1 | Primary | Advantage persists under shift | Mean metric exceeds baseline across five seeds | planned |
| H0 | Null | Advantage is practically negligible | Interval includes zero or practical threshold | planned |
| A1 | Alternative | Advantage depends on augmentation/tuning | Ablation reduces effect | planned |

## 5. Method, Baselines & Experiment Matrix

| Experiment | Purpose | Comparison/control | Seeds | Decision rule |
| :--- | :--- | :--- | :--- | :--- |
| E1 | headline reproduction | paper baseline | 5 | report metric + interval |
| E2 | robustness test | method vs. baselines under shift | 5 | compare effect to threshold |
| E3 | mechanism check | ablate augmentation/tuning | 5 | assess alternative |
```

The agent reports the decisive experiment and largest uncertainty. It does not call H1 a result until E2 exists.
