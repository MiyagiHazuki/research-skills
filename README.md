# Research Agent Skills

A human guide to this collection. The contract the agent actually follows is each folder's `SKILL.md`.

These are Agent Skills for **papers, experiments, and research code**: teardown, peer review, drafting, chartering, reproduction, diagnosis, repo cleanup, design grilling, and compressed conversation. They are not a general product-engineering toolkit, and they do not replace reading the literature, running the experiment, or owning the numbers.

**Not included:** machine-local environment notes. The public catalog is the 15 skills in this repository.

---

## How to get the most from them

1. **Name the job. Load one primary skill.** Say "teardown this paper", "review this", "charter this experiment", "what does `trainer.py` do". Stack only when a skill says it stacks (`caveman` + `caveman-thinking`).
2. **Put the artifact in the same message.** PDF / arXiv id, plan draft, repo, traceback, formula. Missing inputs make these skills stop and ask, not guess.
3. **Do not mix opposing skills.** Teardown is not review. Review is not ghostwriting. Plain-speak is not caveman. A code map is not a debugger.
4. **Align, then act.** `academic-writing` outlines before it drafts. `archive` confirms a move plan before it moves files. `improve-codebase-architecture` writes a deepening brief; it does not edit.

### Pick by intent

| You want | Use | Do not use |
|---|---|---|
| What this paper sells, eats, and spits | `paper-dissect` | `critical-paper-review` |
| Score / referee someone else's manuscript | `critical-paper-review` | `paper-dissect`, `academic-writing` |
| Draft from evidence you actually have | `academic-writing` | `critical-paper-review` |
| A testable research charter | `init-with-grilling` | `grill-me` |
| Stress-test a product / design / implementation plan | `grill-me` | `init-with-grilling` |
| Lost inside a function / file | `zoom-out` | `plain-speak`, `diagnose` |
| A beginner explanation of a concept | `plain-speak` | `zoom-out`, `caveman` |
| Runs, but numbers are wrong / NaN / no convergence | `diagnose` | `zoom-out` |
| Shallow modules, better seams | `improve-codebase-architecture` | `archive`, `diagnose` |
| Messy research repo → releasable paper repo | `archive` | `improve-codebase-architecture` |
| Shorter replies | `caveman` | `plain-speak` |
| Pass the session to a fresh agent | `handoff` | Stretching a dying context |

---

## Papers

### `paper-dissect`

**Does.** Four questions only: the one thing the paper sells, what it eats and spits, how the inside runs, whether the body closes the abstract. Writes parallel `dissect.zh.md` and `dissect.en.md`.

**Does not.** Recap, score, invent modules the authors never stated, peer-review, or draft. Missing pieces are `原文不足` (source insufficient).

**Trigger.** 论文拆解, 拆解这篇论文, 核心卖点, 吃进去吐出来, paper teardown, unpack what this paper sells, `/paper-dissect`. Give a PDF path or arXiv id.

**Best used.** Teardown first, then decide whether to review or write. Read the full paper; abstract-or-methods-only is low confidence. Review → `critical-paper-review`. Draft → `academic-writing`.

### `critical-paper-review`

**Does.** Independent peer review of **someone else's** CS / ML / AI / statistics manuscript: quoted dimension labels, a novelty-search table, a conference 1–10 score and journal recommendation from a fixed mapping table, plus bilingual letters.

**Does not.** Polish the paper, draft a rebuttal, review a manuscript this same session just wrote, or invent scores and citations in prose.

**Trigger.** Review this paper, referee, OpenReview-style, 1–10, accept / reject, `/critical-paper-review`.

**Best used.** Freeze venue first (conference vs journal, which). The number must come from `scripts/map_score.py`, not from free generation. If this session authored the paper, start a new session to review it.

### `academic-writing`

**Does.** Align your preferences with **evidence you actually have**, emit an argument outline, then draft venue-appropriate prose (methods, reviews, abstracts, introductions, rebuttals; grant text is an appendix). Default craft is CS/ML. Never invents results.

**Does not.** Draft before the four gates are known: evidence inventory, contribution sentence, venue/genre, voice. No invented numbers, citations, partners, or letters.

**Trigger.** 论文, 成稿, 提纲, Nature-style writing, contribution, introduction, abstract, rebuttal.

**Best used.** Hand over figures, numbers, negative results, and the target venue. Confirm the outline in a separate turn before drafting. This is an author, not a paraphraser.

---

## Research projects and code

### `init-with-grilling`

**Does.** Turn a vague research idea into an auditable charter (default: `AGENTS.md` at the project root): falsifiable question, hypotheses, operationalization, provenance, comparisons, reproducibility constraints.

**Does not.** Design production architecture. Invent datasets, baselines, results, or causal claims. A hypothesis is not a finding.

**Trigger.** New experiment, paper reproduction, analysis project, `/init-with-grilling`.

**Best used.** Run it inside the repo so it can reconnoiter before asking. Research questions live here; implementation / product plans belong in `grill-me`. Prefer the smallest experiment that can answer the question.

### `archive`

**Does.** Turn a messy research project into a documented, reproducible paper repository: reconnoiter → document intent → clean → restructure → verify.

**Does not.** Delete results, checkpoints, or other research artifacts without asking. Does not commit unless you ask. Does not treat a filename as proof that a file is junk.

**Trigger.** 整理项目, 整理成论文仓库, 论文开源, archive this repo, `/archive`.

**Best used.** Confirm the migration plan before files move. Use when preparing a release, not while the protocol is still moving.

### `tdd`

**Does.** Red-green-refactor for research code. Tests lock the mathematical contract (closed form, invariants, convergence, reproducibility), not tensor shapes.

**Does not.** Write every test, then every implementation (horizontal slice). Do not assert internals so a harmless vectorization fails the suite.

**Trigger.** TDD, red-green-refactor, 复现, 数值回归, 收敛验证, 消融实验, 写测试.

**Best used.** Ask "what is the simplest case with a known answer?" One property per cycle: one test → enough code to pass → next property. Never refactor while RED.

### `diagnose`

**Does.** Silent research bugs: shapes, numerical blow-ups, data pipelines, formula mistranslation, non-convergence, irreproducibility, wrong metrics, intent-code gaps. Loop: reproduce → hypothesise → instrument → fix → regression-test.

**Does not.** Teach beginners, deepen architecture, or tour the whole repository.

**Trigger.** diagnose this, debug this, not converging, NaN / Inf, does not match the paper / textbook, dimension mismatch.

**Best used.** Smallest hand-checkable input first. Rank 3–5 falsifiable hypotheses before patching. Write the regression test before the fix when a seam exists.

### `improve-codebase-architecture`

**Does.** Find deepening opportunities: more behaviour behind a smaller interface, for testability and AI-navigability. After you pick a candidate, it grills the design and writes a deepening brief for `/refactor`. It decides. **It does not implement.**

**Does not.** Start editing. Contradict an existing ADR without marking it. Treat "improve architecture" as "refactor now".

**Trigger.** Improve architecture, find refactoring opportunities, consolidate coupled modules, make the codebase AI-navigable.

**Best used.** Prefer a repo that already has `CONTEXT.md` / `AGENTS.md` / `INTENT.md`. Pick one candidate from the list. When you want code changes, run the `/refactor` invocation it prints.

---

## Conversation and handoff

### `grill-me`

**Does.** Walk every branch of a plan or design until you share an understanding. Explore first; each round batches unresolved questions (with a recommended option). User-facing grilling is Chinese or English only.

**Does not.** Implement, draft the paper, or write a research charter (`init-with-grilling` does that). Does not promise Japanese, Korean, or other grilling languages.

**Trigger.** grill me, `/grill-me`, paste a plan and ask to stress-test it.

**Best used.** Put the full plan in the opening message. Read the options; do not blindly accept every recommendation. Language switches only after two consecutive free-text messages in the other language, not via "ask in English".

### `plain-speak`

**Does.** Teach a slow-processing reader with no assumed background: conclusion first, every term explained on first use, one idea per paragraph, example before rule, analogy, recap. Stays on until you say normal / expert mode.

**Does not.** Map where code sits (`zoom-out`). Compress prose (`caveman`). Analogies must not distort facts; danger warnings stay precise.

**Trigger.** 说人话, 讲通俗点, explain like I'm five, I don't understand, treat me as a beginner.

**Best used.** When a concept did not land. If it still does not land, change the analogy; do not repeat the failed wording. Do not stack with `caveman`.

### `caveman`

**Does.** Compress **user-visible replies** only. Fluff dies; technical substance stays. Stackable with `caveman-thinking`.

**Does not.** Compress internal thinking by itself. Security warnings and irreversible confirmations temporarily drop the voice.

**Trigger.** caveman mode, talk like caveman, `/caveman`. Off this layer: `stop caveman`. Off both: `normal mode` / `stop less tokens`.

**Best used.** Long sessions where you already know the domain and want density. Teaching → `plain-speak`. Longest phrase wins: `use caveman thinking` does not turn this skill on.

### `caveman-thinking`

**Does.** Compress **internal thinking** only. Logical steps stay. What you read does not change unless `caveman` is also loaded.

**Does not.** Alter tool calls, code, or file writes. Collapsing a chain to "fix bug" is a failed compression.

**Trigger.** caveman thinking, cave mode, thought compression, `/caveman-thinking`. Off this layer: `stop caveman-thinking`.

**Best used.** When thinking-side tokens matter. Load both caveman skills if you want both sides short. Off-phrases use longest match so a short command does not hit the wrong layer.

### `zoom-out`

**Does.** One layer up for a function / module / file / class: what this layer does, neighbors, direct callers/callees, what the caller is doing with it. This reply only.

**Does not.** Map the whole repo, teach beginners, debug, refactor, or teardown a paper. Bare "what is this / explain" with no code referent is out of scope.

**Trigger.** 这段 / 这个函数 / 模块 / 文件干什么的, 整体看一下, zoom out, `/zoom-out`, plus a named target.

**Best used.** Point at a concrete file or symbol. "What about this other file?" is a new zoom-out, not leftover mode.

### `handoff`

**Does.** Compact the session into a block a fresh agent can continue: goal, decisions, essential paths, results, failed attempts, reproducibility, next steps and skills to load.

**Does not.** Finish the work in this session. Does not paste long tool dumps into the block.

**Trigger.** Continue in a new session, hand off to another agent, `/handoff`, ideally with the next focus.

**Best used.** Before context dies, or before switching model / person. Name the next session's focus and which skills it should load.

---

## Meta

### `write-a-skill`

**Does.** Author a new skill with progressive disclosure: a short `SKILL.md`, rare detail in `REFERENCE.md` / `EXAMPLES.md`, scripts only for deterministic steps.

**Does not.** Leave the description too vague for an agent to know when to load it. Do not turn `SKILL.md` into a book.

**Trigger.** Create / write / build a new skill.

**Best used.** One job per skill. Put triggers in the description. Gather requirements, draft, then review with the user.

---

## Three combined workflows

### 1. Read someone else's paper, then write yours

`paper-dissect` (sell and mapping) → if you need a verdict, new session with `critical-paper-review` → `academic-writing` from **your** evidence.

Teardown is mechanism. Review is publishability. Drafting is your results. Do not ask one skill to score and ghostwrite.

### 2. Start an experiment you can falsify and reproduce

`init-with-grilling` (charter) → `tdd` (implement against the math) → `diagnose` when the numbers lie. `archive` last, when the repo must ship with the paper.

Charter before tests. Smallest known answer before complexity. Do not open-source-clean a protocol that is still moving.

### 3. Lock a design, then continue later

Implementation or product plans → `grill-me`. Code shape → `improve-codebase-architecture` (brief only). After alignment, `/handoff` with the next focus and suggested skills.

Do not use `grill-me` as a substitute for research hypotheses and data protocol; that is `init-with-grilling`.

---

Hard rules, templates, and counterexamples live in each skill's `SKILL.md` and its `REFERENCE.md` / `EXAMPLES.md`. This README is only which skill to call, when, and how to call it so a turn is not wasted.
