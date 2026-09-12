---
name: zoom-out
description: >
  Give a one-layer-up orientation map of an unfamiliar code area: what this
  layer does, nearby modules, and direct callers/callees. Use when the user
  is lost in code and wants orientation of a function, module, file, or class
  — 这段/这个代码/函数/模块/文件/类干什么的, 有什么用, 整体看一下这段代码,
  "zoom out", "how this code fits", "bigger picture of this code",
  "unfamiliar with this code", or /zoom-out. Do not use for beginner-only
  explanations (plain-speak, 说人话, 讲通俗点), paper teardown,
  debugging/diagnose, or architecture refactoring. Do not use for bare
  是什么 / 解释一下 / 讲解一下 / 怎么回事 / 怎么实现 without a code,
  function, module, file, or class referent.
---

# Zoom-out

Go up **one** layer of abstraction. Map where this code sits. Do not refactor.

## Persistence

This reply only. Next turn is normal. A follow-up like 「那这个文件呢」 is a
**new** zoom-out if it still matches, not leftover mode.

## No target

If the user says `/zoom-out` or "zoom out" with no function/module/file/class:
**ask which one**. Do not map the whole repository.

## Every reply

Look up the target and its **direct** callers and callees (one hop). Do not
guess. Do not invent a glossary. Use names as they appear in code.

Output four blocks, then one short 人话 paragraph. Headings follow the user.
Chinese default below; English: What this layer does / Nearby modules /
Direct callers and callees / One layer up.

1. **这一层干什么** — one sentence.
2. **相关模块** — this layer plus one-hop neighbors.
3. **谁调谁** — `caller → target → callees` only. No second hop.
4. **再上一层** — what the caller is doing with this.

**人话** (after the four blocks): one short paragraph restating the same map.
Identifiers stay; describe duties. No analogies, no one-idea-per-paragraph,
no "which part is unclear?". This trailer is not plain-speak and does not persist.

## Boundaries

- **plain-speak**: user only wants 说人话 / a beginner explanation, not a code
  map → do not load this.
- **improve-codebase-architecture**: no deepening, no split/merge, no refactor.
- **diagnose**: not for bugs, NaNs, or "why is this wrong".
- **paper-dissect**: not for papers.

## Example

User: 「整体看一下这段 `trainer.py`」

**这一层干什么**
把一次训练 step 串起来：前向、指标、checkpoint。

**相关模块**
`trainer.py`（本层）、`forward.py`、`metric.py`、`checkpoint.py`。

**谁调谁**
`experiment.py` → `trainer.py` → `forward.py`, `metric.py`, `checkpoint.py`。

**再上一层**
`experiment.py` 在跑一整场实验；本层只负责其中一个 step。

**人话**
`trainer.py` 不负责整场实验，只负责把一轮训练的三件事接上：`forward.py`
算出输出，`metric.py` 记分，`checkpoint.py` 存盘。真正启动实验的是上一层
`experiment.py`。
