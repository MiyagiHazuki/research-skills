# Examples

Schematic. Not a real paper. Do not copy these sentences into a live dissect.

## Good fill (engineering method, 4 modules)

Core map reads without the nickname, one language per file:

- dissect.zh.md：在只能看到当前问题和一个可检索文档库、且没有逐步标准答案的前提下，把问题变成带出处的短答案。
- dissect.en.md: Under access to the question and a retrievable corpus only, and with no gold chain of steps, turn a question into a short answer with citations.

S1 retrieve → S2 compress → S3 generate → S4 verify. Section 7 uses those ids. The headline result's Y is the cited short answer, same Y as section 3. Hidden inputs list the frozen retriever checkpoint. Any equation in a slot is KaTeX, e.g. the mixing rule $d' = (1-\alpha)\,d + \alpha\,\tfrac{\lVert d\rVert}{\lVert s\rVert}\,s$. Output lands in two parallel files: `dissect.zh.md` and `dissect.en.md`, same content, one language each.

## Bad fills (reject these patterns)

- One bilingual file: `中：`/`EN:` pairs stacked inside every slot, instead of separate `dissect.zh.md` and `dissect.en.md`.
- The zh and en files drift: zh lists 4 steps, en lists 3; or a page id appears in one file only.

- Plain-text pseudo formula: `d'=(1-a)d+a(||d||/||s||)s` instead of KaTeX `$d' = (1-\alpha)\,d + \alpha\,\tfrac{\lVert d\rVert}{\lVert s\rVert}\,s$`.

- Recap of the introduction's history paragraph in section 4.
- Section 6 titled `S1 Introduction` / `S2 Related Work`.
- Y = `our FancyNet-v3 optimizer` when the sell is a generator.
- Inventing a reranker the paper never described, instead of `原文不足`.
- Section 3 says the output is a dataset; the headline result claims +12 F1. That is a section 8 mismatch: rewrite section 3, do not leave both.
- Drawing a related-work citation graph in section 7.
- Scoring 6/10 or writing an accept/reject paragraph.
