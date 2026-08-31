# Genres

Load only the section you need. Apply [CRAFT.md](CRAFT.md) inside the structure below.

## Methods paper (conference or journal)

Spine: problem → idea → evidence → what it changes.

- **Title.** Name the idea or the result. Not "A Novel Framework for X."
- **Abstract.** Complete argument (CRAFT). One number if you have one that a reviewer would miss.
- **Introduction.** World → obstacle → cost of the gap → this paper's move → contributions as *results*, each with an evidence pointer. Three contributions is enough.
- **Related work.** Contrast with the closest one or two methods and say the difference. Do not dump a bracketed list.
- **Method.** Teach on the running example, then state the general form. Symbols stay consistent with the user's notes.
- **Experiments.** Each subsection opens with the claim it tests. Report against the strongest baseline first. Setup must be copyable: data, splits, compute if it matters.
- **Limitations.** Real ones: setting, scale, assumption. Not "we did not try every dataset."
- **Conclusion.** Restate the takeaway in one sentence. One specific next measurement, not "paves the way."

ICLR/NeurIPS: terse, results-forward. Journal: more setup, same claim-evidence discipline.

## Nature-style review or insight

Spine: teach the mechanism, then show why practice moved.

- Open with the world. Obstacle before taxonomy.
- A running example carries the whole piece.
- Architectures or schools of thought appear as answers to that obstacle, not as a catalog.
- Industry or scientific consequence is named (a product class, a lab task, a community that switched).
- Close with labeled bets about where the field goes, each one testable in spirit.

Do not fake a review if the user only has one method and three tables. That is a methods paper.

## Abstract (standalone pass)

If the user only wants the abstract: write it as a complete argument, then stop. Match the venue word limit when they give one. Otherwise keep it under ~200 English words or ~400 Chinese characters unless they ask otherwise.

## Introduction (standalone pass)

If the user only wants the introduction:

1. Why the reader already cares (concrete).
2. The obstacle and what it costs.
3. The move this paper makes (one paragraph).
4. Contributions as results, not restatements of the abstract.
5. Optional roadmap: one sentence, only if the paper is long.

Do not spend the introduction surveying the field. That belongs in related work.

## Rebuttal

Default shape: **a short narrative, then a point-by-point appendix.**

**Narrative (first).** Name the shared concern across reviewers. Say what you changed in the manuscript and why that is enough. Do not reopen the whole paper.

**Appendix.** One block per reviewer item (`R1.1`, `R2.3`):

- Recap the concern in one sentence.
- Agree or disagree, without heat.
- Point to evidence (new table, existing figure, citation the user supplied).
- State the manuscript change, or state that you did not change it and why.

Never invent an experiment to satisfy a reviewer. If the experiment does not exist, say so and offer a limitation or a plan only if the user provided that plan.

## Appendix: grant text (not the main job)

A proposal sells **vision plus feasibility**. Do not flatten ambition. Do not invent preliminary data.

By the end of page 1 (NIH-style aims) or pages 2–3 (NSF-style / 国自然立项), the reader must hold: hook, gap and its cost, one-sentence idea, parallel aims as *outcomes*, payoff. Aims must not collapse as a chain. Each bold claim needs a footing the user actually supplied.

For 国自然-style text: 立项依据 (gap + cost), 研究内容 (questions, not a method list), 技术路线, 创新点 (specific), 研究基础 (only real prior work).
