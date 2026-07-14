# Archive — Examples

> Template documentation. Use these when executing archive phases.

---

## Repository Analysis Report

Generated at the end of Phase 1 (Reconnaissance). Copy and fill in.

```markdown
## Repository Analysis

### Detected project type
[Brief description: e.g., "PyTorch research codebase for image segmentation"]

### Important directories

| Path | Likely purpose | Evidence |
|---|---|---|
| `src/models/` | Model definitions | Contains `unet.py`, `resnet.py` |
| `experiments/` | Experiment scripts | Shell scripts with training commands |
| `paper/` | LaTeX source | Contains `main.tex`, `figures/` |

### Important files

| File | Likely purpose | Evidence |
|---|---|---|
| `train.py` | Training entry point | Imports model, dataloader, calls `train()` |
| `requirements.txt` | Python dependencies | Lists torch, numpy, matplotlib |
| `Makefile` | Build/paper compile | Targets for `paper`, `figures`, `clean` |

### Existing structure assessment
Disciplined / Transitional / Chaotic / Greenfield

### Risks or uncertainties
- [risk 1]
- [risk 2]
```

---

## INTENT.md Template

Generated in Phase 2 for each important directory.

```markdown
# Directory Intent: `<path>`

## Purpose

[One paragraph explaining what this directory contains and why it exists]

## Main Contents

| File or Subdirectory | Role |
|---|---|
| `model.py` | Core model architecture definition |
| `train.py` | Training loop |

## Author Intent

[What the original author(s) intended — inferred from code, comments, README]

## Relationship to the Paper or Experiments

[How this directory's contents relate to specific paper sections or experiment runs]

## Maintenance Notes

[Any gotchas, dependencies, or conventions to know when modifying]
```

---

## Migration Plan Template

Generated in Phase 4. Present to user for confirmation before executing.

```markdown
## Proposed Repository Structure

\`\`\`text
project/
├── paper/latex/
├── src/
│   ├── models/
│   ├── data/
│   ├── training/
│   └── evaluation/
├── configs/
├── scripts/
├── datasets/
├── results/
│   ├── logs/
│   ├── checkpoints/
│   └── figures/
├── docs/
└── tests/
\`\`\`

## Proposed Moves

| Current Path | Proposed Path | Reason | Risk |
|---|---|---|---|
| `model/unet.py` | `src/models/unet.py` | Model definition → src/models/ | Low — no imports broken |
| `exp/run.sh` | `scripts/run.sh` | Experiment script → scripts/ | Medium — may reference relative paths |

## Files to Keep In Place

| Path | Reason |
|---|---|
| `README.md` | Project root documentation |
| `.gitignore` | Already correctly placed |

## Open Questions

1. [question 1]
2. [question 2]

## Recommended Plan

[Step-by-step execution order with risk staging]
```
