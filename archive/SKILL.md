---
name: archive
description: >
  Archive, document, and carefully restructure research projects into clean,
  publishable paper repositories by reconnoitering the codebase, classifying
  every file, documenting intent, cleaning up ephemera, and migrating to a
  standard academic layout. Use when user wants to archive, organize, clean,
  restructure, curate, or prepare an academic codebase for paper release,
  reproducibility, or open-source publication. Triggers: "整理项目",
  "archive this repo", "整理成论文仓库", "prepare for release",
  "standardize project structure", "论文开源", "paper repo", "/archive".
---

# Archive

Transform messy research projects into clean, documented, reproducible open-source
repositories. Five phases: reconnoiter → document → clean → restructure → verify.

Full details: [REFERENCE.md](REFERENCE.md). Templates: [EXAMPLES.md](EXAMPLES.md).

## Quick Start — 5-Phase Workflow

### 1. Reconnaissance
Scan directory tree. Identify source code, paper/LaTeX (if any), configs, datasets, results,
tests, docs, temp artifacts. Detect language ecosystem, build system, test framework.
Summarize findings before proposing changes.

### 2. Intent Documentation
Generate `INTENT.md` for each important directory. State purpose, contents, author intent,
relationship to paper/experiments. If uncertain, state uncertainty — don't invent.

### 3. Cleanup (Three Tiers)

| Tier | Action | Examples |
|---|---|---|
| Auto-delete | Remove without asking | `__pycache__/`, `.DS_Store`, `*.pyc`, build artifacts |
| Ask-before-delete | Confirm first | `.ipynb`, checkpoints, debug scripts, unclear files |
| Never-delete | Preserve always | `.py/.js/.ts`, `.tex/.bib`, datasets, configs, tests |

See [REFERENCE.md](REFERENCE.md#phase-3--cleanup) for full lists.

### 4. Restructure Proposal
Map current structure → standard layout (`paper/latex/`, `src/models/`, `configs/`,
`scripts/`, `datasets/`, `results/`, `docs/`, `tests/`). Create migration plan with
risk assessment. **Ask user to confirm before executing.**

See [REFERENCE.md](REFERENCE.md#phase-4--restructure-proposal) for target structure and mapping table.

### 5. Execution & Verification
Execute in risk-staged batches. After each batch: verify directory tree, check
imports/paths, confirm no deletions of unconfirmed files. `git status` — never commit
unless asked.

## Core Principles

### Pace & Reliability
- Scan broadly before modifying. Infer intent from multiple signals.
- Stage changes. Never one-shot large rewrites.
- Verify after every meaningful batch.
- Keep moves reversible. Preserve research artifact provenance.
- Adapt to existing layout — don't blindly impose target structure.

### Decision Policy
**Act independently** when: high confidence, low risk, reversible, or regenerable.

**Ask user** when: file may have research value, destructive operation, ambiguous
intent, multiple valid strategies, or moving files may break imports/scripts/LaTeX.

Don't ask for routine actions. Batch related questions.

**MUST: all user questions use Chinese + `question` tool.** Never ask in English
or via plain text. Always use the `question` tool with Chinese options/labels.

### Safety Constraints (Red Lines)
1. Never delete research artifacts without asking.
2. Never delete results/checkpoints/logs that support paper claims.
3. Never move files that break reproducibility without warning.
4. Never assume importance from filename alone.
5. Never overwrite documentation without preserving useful content.
6. Never commit unless explicitly requested.

**Default: keep file + document uncertainty** over aggressive delete/move.
