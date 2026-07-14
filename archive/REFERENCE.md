# Archive — Reference

> Full workflow details. See SKILL.md for quick start and core principles.

---

## Phase 1 — Reconnaissance

Inspect the current working directory. Recursively list files and directories.

Identify:
- source code directories
- paper/LaTeX directories
- experiment scripts
- configuration files
- datasets or dataset descriptors
- results, logs, checkpoints, figures
- tests
- documentation
- temporary/cache/debug artifacts

Detect existing conventions: package manager, language ecosystem, test framework,
build system, paper compilation workflow, experiment entry points, result-generation pipeline.

Summarize findings before proposing changes using the template in [EXAMPLES.md](EXAMPLES.md#repository-analysis-report).

---

## Phase 2 — Intent Documentation

For every important directory, generate or update an `INTENT.md`.

An important directory contains: source code, paper content, configs, datasets,
scripts, results, documentation, tests, or reusable utilities.

Skip `INTENT.md` inside obvious cache / vendor / build directories unless needed.

Use the template in [EXAMPLES.md](EXAMPLES.md#intent.md-template).

If intent is uncertain, state uncertainty explicitly — do not invent certainty.

---

## Phase 3 — Cleanup

Classify cleanup candidates into three confidence levels.

### Auto-cleanable (delete without asking)

- `__pycache__/`
- `.pytest_cache/`
- `.mypy_cache/`
- `.ruff_cache/`
- `.ipynb_checkpoints/`
- `.DS_Store`
- editor swap files (`*.swp`, `*~`)
- empty temporary directories
- bytecode files (`*.pyc`)
- cache folders already listed in `.gitignore`
- build artifacts in known output dirs (e.g. `dist/`, `build/`)

Before deleting, record paths in a cleanup summary. These are clearly safe and
the assistant should act without user confirmation.

### Ask-before-delete (ask user)

- experiment logs
- generated figures not committed to paper
- result tables
- notebooks (`*.ipynb`)
- checkpoints (`.pt`, `.ckpt`, `.h5`)
- intermediate datasets
- debug scripts
- old test files
- duplicated-looking outputs
- files whose purpose is unclear

### Never delete (unless user explicitly instructs)

- source code (`*.py`, `*.js`, `*.ts`, etc.)
- paper files (`*.tex`, `*.bib`)
- datasets or dataset metadata
- final results backing paper claims
- model weights used for reported results
- config files
- README / docs
- tests encoding expected behavior

---

## Phase 4 — Restructure Proposal

### Standard Target Structure

```text
project/
├── README.md
├── LICENSE
├── paper/
│   └── latex/
├── src/
│   ├── models/
│   ├── data/
│   ├── training/
│   ├── evaluation/
│   └── utils/
├── configs/
├── scripts/
├── datasets/
├── results/
│   ├── logs/
│   ├── checkpoints/
│   └── figures/
├── docs/
└── tests/
```

### Mapping Rules

| Content Type                                 | Target               |
|----------------------------------------------|----------------------|
| LaTeX, bib, paper-only figures               | `paper/latex/`       |
| Core experiment / source code                | `src/`               |
| Model definitions                            | `src/models/`        |
| Dataset loading / preprocessing              | `src/data/`          |
| Training logic                               | `src/training/`      |
| Evaluation metrics / benchmarks              | `src/evaluation/`    |
| Shared helpers                               | `src/utils/`         |
| YAML / TOML / JSON experiment configs        | `configs/`           |
| CLI scripts, shell scripts, one-off runners  | `scripts/`           |
| Raw/processed datasets, dataset cards        | `datasets/`          |
| Logs, metrics, output tables                 | `results/logs/`      |
| Checkpoints, weights, serialized models      | `results/checkpoints/`|
| Generated plots, visualizations, figures     | `results/figures/`   |
| Project documentation, supplementary notes   | `docs/`              |
| Unit / integration tests                     | `tests/`             |

### Migration Plan

Use the template in [EXAMPLES.md](EXAMPLES.md#migration-plan-template).

Stage migration by risk:
1. Create target directories.
2. Move obvious documentation / paper files first.
3. Move source code with import updates.
4. Move configs / scripts / results.
5. Run smoke checks (imports, build, paper compile).
6. Update README and `INTENT.md`.

Only execute after the user confirms the plan.

---

## Phase 5 — Execution & Verification

After confirmation, execute changes. After each batch:
- Verify directory tree matches proposal.
- Verify important files still exist.
- Check imports / scripts / LaTeX paths for obvious breaks.
- Confirm no unconfirmed files were deleted.

Under Git: show `git status`. Do not commit unless explicitly asked.

---

## Safety Constraints

1. No destructive action on research artifacts without asking.
2. No deleting results, checkpoints, or logs that may support paper claims.
3. No moving files that may affect reproducibility without warning.
4. No assumptions about experiment importance from file names alone.
5. No overwriting existing documentation without preserving useful content.
6. No removing notebooks unless clearly cache/checkpoint files.
7. No committing unless explicitly requested.

When uncertain: **keep file + document uncertainty** over delete or move aggressively.

---

## User Interaction Style

Do not ask for routine, high-confidence actions. Batch related questions
together instead of interrupting repeatedly.

**CRITICAL: All user-facing questions MUST use Chinese language and the `question` tool** —
never plain text, never English. Structure every prompt into the `question` tool
with Chinese header, description, and options.

When asking:
- state the uncertainty (Chinese);
- list the affected files (Chinese labels);
- give a recommended action as the first option + "(推荐)";
- offer a safe default.

Example — using `question` tool:

```
question(
  header="8个旧实验日志文件",
  question="发现了8个看起来是旧实验日志的文件，可能仍对可复现有用。不建议直接删除。如何处理？",
  options=[
    {label: "移到 results/logs/archive/ (推荐)", description: "保留备查，不影响当前结构"},
    {label: "删除", description: "永久删除这8个日志文件"},
    {label: "保持原位", description: "不做任何移动"}
  ]
)
```
