# Sisyphus Skills

Custom agent skills for [OpenCode](https://github.com/OhMyOpenCode/opencode). Each skill provides specialized instructions and workflows for specific tasks.

Load skills via `skill(name="skill-name")` or use task categories + `load_skills=[...]`.

---

## Skill Index

| # | Skill | Domain | Description | Triggers (EN) | Triggers (ZH) |
|---|---|---|---|---|---|
| 1 | `archive` | Codebase Curation | Transform messy research projects into clean, documented, reproducible open-source repositories. Five-phase workflow: reconnoiter → document → clean → restructure → verify. | "archive this repo", "prepare for release", "standardize project structure", "paper repo", `/archive` | "整理项目", "整理成论文仓库", "论文开源" |
| 2 | `caveman` | Communication | Ultra-compressed output mode. Cuts token usage ~75% by dropping filler, articles, and pleasantries while keeping full technical accuracy. | "caveman mode", "talk like caveman", "use caveman", "less tokens", "be brief", `/caveman` | — |
| 3 | `caveman-thinking` | Communication | Compresses BOTH internal thinking/reasoning AND final output into dense, telegraphic caveman language. Covers both phases in one load. Stacks safely with `caveman`. | "caveman thinking", "cave mode", "thought compression", `/caveman-thinking` | "精简思考", "节省token", "压缩思考" |
| 4 | `diagnose` | Debugging | Disciplined diagnosis loop for research code bugs: dimension/index errors, numerical instability, convergence failures, algorithm errors, intent-code gaps. Reproduce → hypothesise → instrument → fix → regression-test. | "diagnose this", "debug this", "algorithm not converging", "NaN/Inf values", "results don't match paper", "array dimension mismatch", `/diagnose` | — |
| 5 | `grill-me` | Planning | Interview the user relentlessly about a plan/design until reaching shared understanding. Walk down each branch of the decision tree, resolving dependencies one-by-one. Always batching questions into single `question` calls. | "grill me", "stress-test my plan" | — |
| 6 | `handoff` | Session Management | Compact current conversation into a minimal handoff block for a fresh agent. Strips temporary tool outputs, keeps core code & decisions, condenses history. | "hand off", "continue in new session", "hand off to another agent", `/handoff` | — |
| 7 | `improve-codebase-architecture` | Architecture | Find deepening opportunities in a codebase — turn shallow modules into deep ones. Surfaces architectural friction, proposes refactors for testability and AI-navigability. Informed by project domain docs (CONTEXT.md, AGENTS.md, ADRs). | "improve architecture", "find refactoring opportunities", "consolidate modules", "make codebase more testable", `/improve-codebase-architecture` | — |
| 8 | `init-with-grilling` | Research Setup | Initialize research projects by eliciting precise questions, hypotheses, evidence plan, methods, provenance, and reproducibility constraints. Produces a research charter (AGENTS.md) that separates observed/planned/assumed facts. | "init research project", "new experiment", "paper reproduction", `/init-with-grilling` | — |
| 9 | `tdd` | Testing | Test-driven development with red-green-refactor loop for research code. Tests verify scientific correctness (analytical solutions, invariants, convergence), not implementation internals. Vertical tracer bullets, not horizontal bulk tests. | "TDD", "red-green-refactor", "test-first", "verify numerical correctness", "catch regressions", "/tdd" | "复现", "数值回归", "收敛验证", "消融实验", "可复现性", "写测试" |
| 10 | `write-a-skill` | Meta | Create new agent skills with proper structure (SKILL.md + REFERENCE.md + scripts/). Progressive disclosure, bundled resources, review workflow. | "write a skill", "create a skill", "build a new skill", `/write-a-skill` | — |
| 11 | `zoom-out` | Code Understanding | Zoom out for broader context or higher-level perspective. Use when unfamiliar with a section of code or need to understand how it fits into the bigger picture. | "zoom out", "/zoom-out" | "有什么用", "干什么的", "怎么实现", "讲解一下", "怎么回事", "是什么", "解释一下", "整体看一下" |

---

## Quick Reference by Use Case

| You want to... | Load |
|---|---|
| Organize/archive a messy research repo | `archive` |
| Save tokens, compress all output | `caveman` + `caveman-thinking` |
| Debug NaN/Inf or non-converging algorithm | `diagnose` |
| Stress-test your design before building | `grill-me` |
| Continue work in a fresh session | `handoff` |
| Refactor for better architecture | `improve-codebase-architecture` |
| Start a new research project with rigor | `init-with-grilling` |
| Write tests for research code | `tdd` |
| Create a new reusable skill | `write-a-skill` |
| Understand unfamiliar code at a glance | `zoom-out` |

---

## Skill Structure

Each skill follows this directory layout:

```
skill-name/
├── SKILL.md           # Main instructions (required)
├── REFERENCE.md       # Detailed reference docs
├── EXAMPLES.md        # Usage examples
└── scripts/           # Utility scripts (optional)
```

---

## Installation

Skills are loaded from `~/.config/opencode/skills/`. Place new skill directories here to make them available to the agent.
