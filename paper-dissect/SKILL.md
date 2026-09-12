---
name: paper-dissect
description: >
  Dissects a research paper PDF into one core sell, input-output mapping,
  module-level dataflow, and an abstract-vs-body check. Does not recap,
  score, or invent modules the paper never stated. Use when the user wants
  论文拆解, 拆解这篇论文, 核心卖点, 核心映射, 吃进去吐出来, paper teardown,
  unpack what this paper sells, or to check whether the body delivers the
  abstract. Do not use for peer review, scoring, or drafting the paper.
---

# Paper Dissect

Not a summary. Not a review. Four questions only:

1. What **one** thing is this paper selling?
2. What does it eat, and what does it spit?
3. How does the inside actually run?
4. Did the body close the abstract's claim?

If a module is not in the paper, write `原文不足` (source insufficient). Never invent parts the authors did not state.

## Hard rules

- Run **0→8 in order**. Do not skip. Do not reorder.
- One core sell (the contribution title and abstract keep repeating). Extra contributions go in remarks only.
- Drop background, history, related-work survey, acknowledgements, and future work — unless the paper **is** a survey or a dataset/benchmark (then that material **is** the sell).
- Do not score, accept/reject, polish, or rewrite the paper.
- Headings are frozen. Fill [TEMPLATE.md](TEMPLATE.md) exactly; `dissect.en.md` uses the English heading mapping inside it. Do not add, rename, or delete headings.
- Talk to the user in their language. Always emit **two files**: `dissect.zh.md` (Chinese) and `dissect.en.md` (English) — same heading structure, same content, one language per file. Never mix `中：`/`EN:` pairs inside a slot; the two files must not drift apart.
- **All math in KaTeX.** Any formula, norm, fraction, or multi-symbol expression goes in KaTeX — inline `$...$`, display `$$...$$`, in both files. Never plain-text pseudo formulas (`d'=(1-a)d+...`). A lone Greek letter in running prose (`α`) is allowed.
- **Load `academic-writing` before writing the dissect files.** Invoke the `academic-writing` skill first and write every slot with its craft: tight, concrete sentences, no filler, no overclaim. Each file is a full template — keep every slot telegraphic, never restate one fact across sections.
- **Workspace only.** Create dirs and write files under the current workspace root. Never write outside it (not home, not the skill dir, not `/tmp`, not MCP cache as a deliverable).

## Intake

Need a PDF path, arXiv id, or already-extracted text. If missing, ask and stop.

Default: read the **full** paper. If the user named chapters, read only those.

**Read via MCP**, not memory: `nano-pdf-mcp_read_pdf` in page ranges; `look_at` is a skim only. arXiv id → arXiv MCP download/read if available. Record printed page or PDF index for every quote. Failed pages go under incomplete pages. Abstract-or-methods-only → confidence = `低`.

## Workflow

Follow [WORKFLOW.md](WORKFLOW.md) while filling the template.

0. Read. 1. Init (gap sentence / object of sale / mechanism / headline result). No name for the object of sale → ask, stop. 2. Type. 3. Core map: under premise P, turn X into Y. 4. Why it matters (from the gap sentence only). 5. Essence, no nicknames. 6. Module steps S1…Sn. 7. Mermaid or `未触发`. 8. Check headline result vs section 3; mismatch → rewrite section 3 before emit.

## Boundaries

- Peer review / 1–10 / accept-reject → `critical-paper-review`.
- Draft or polish the manuscript → `academic-writing`.
- Appendix: skip unless the core logic is unreadable without it.

## Output

Create `paper-dissect/<slug>/` in the workspace if missing. Write the Chinese fill to `paper-dissect/<slug>/dissect.zh.md` and the English fill to `paper-dissect/<slug>/dissect.en.md`. `<slug>` = arXiv id, or a short ASCII slug from the title.

Do not write anywhere else. Paste the version matching the user's language in the reply, and name the other file's path.

Headings from [TEMPLATE.md](TEMPLATE.md). Schematic fill: [EXAMPLES.md](EXAMPLES.md).
