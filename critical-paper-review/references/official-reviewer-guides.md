# Official reviewer guides (cited)

What the venues themselves ask reviewers to do. Use at **intake** (mirror the venue's review form in the letter) and when writing **Questions / requested changes**. Score scales live in [venue-overlays.md](venue-overlays.md); the number still comes only from `scripts/map_score.py`. These guides inform labels and letter shape — they never override the mapping.

All URLs accessed 2026-08-31. If the frozen venue is **not** in this file (ICML, ACL, VLDB, SIGMOD, ...): fetch the official reviewer guide at review time, record URL + access date in the review bundle, and do not treat anything here as that venue's policy.

## NeurIPS 2024 (conference default)

Source: [Reviewer Guidelines](https://neurips.cc/Conferences/2024/ReviewerGuidelines).

- Review form: paper summary; **strengths and weaknesses** framed as "reasons you might accept or reject"; separate ratings for quality, clarity, significance, originality; **questions** — about 3–5, actionable, and you are "strongly encouraged to state the clear criteria under which your evaluation score could increase or decrease"; **limitations** section; overall 1–10 (meanings: [venue-overlays.md](venue-overlays.md)).
- Judging each paper on its own merits; reviewers do **not** have to match the conference acceptance rate.
- Authors should be **rewarded, not punished**, for stating limitations up front.

Our letter already mirrors this: summary → strengths → weaknesses → 3–5 questions with score-changing criteria → recommendation.

## NeurIPS 2025 (1–6 overlay)

Source: [Reviewer Guidelines](https://neurips.cc/Conferences/2025/ReviewerGuidelines).

- Same skeleton; quality and significance are 1–4 sub-ratings; overall is 1–6.
- Answering "no" to a checklist item is "typically not grounds for rejection".
- Reviews and meta-reviews of accepted papers (and opted-in rejected papers) are made **public** — write the letter as if the authors and the community will read it.

## ICLR

Source: [Reviewer Guide](https://iclr.cc/Conferences/2025/ReviewerGuide).

Answer four key questions before recommending:

1. What is the specific question and/or problem tackled by the paper?
2. Is the approach well motivated, including being well-placed in the literature?
3. Does the paper support the claims — are results (theoretical or empirical) correct and scientifically rigorous?
4. What is the significance — does it contribute new, relevant, impactful knowledge? **State-of-the-art results are not required** for significance.

Review structure: summarize what the paper **claims** to contribute (be positive and constructive); list strong and weak points as comprehensively as possible; state the initial recommendation with one or two key reasons; give supporting arguments. In discussion, stay open to moving the recommendation in **either** direction.

## JMLR

Source: [Reviewer guide](https://www.jmlr.org/reviewer-guide.html).

Touch on as many of these as practical:

- **Goals**: research goals and learning task.
- **Description**: detailed enough to replicate; systems papers state contributions or principles; **theory papers should discuss practical utility**.
- **Evaluation**: claims clearly articulated and supported by experiments or theoretical analyses.
- **Significance**: significant, technically correct; sufficiently different from prior published work (**including the authors' own**); clear why the advance matters.
- **Related work**: strengths, limitations, and generality discussed relative to related work; predecessors credited.
- **Clarity**: readable by an ML-literate reader **without special knowledge of the paper's subject**; goals stated; replicable detail; new terminology justified; examples included.
- **Recommendation vocabulary**: accept / conditional accept / reject with encouragement to revise and resubmit / reject. Conditional accept requires "a precise list of changes that can easily be checked upon resubmission" — our Questions section must be checkable, not aspirational.

Letter mapping (from [venue-overlays.md](venue-overlays.md)): Accept→accept; Minor revision→conditional accept; Major revision→reject with encouragement to revise and resubmit; Reject→reject.

## TMLR

Sources: [Reviewer guide](https://jmlr.org/tmlr/reviewer-guide.html), [Acceptance criteria](https://jmlr.org/tmlr/acceptance-criteria.html), [Editorial policies](https://jmlr.org/tmlr/editorial-policies.html).

**Review format (mirror in the letter under this overlay):**

1. Summary of contributions, in the reviewer's words, with key strengths/weaknesses.
2. *Are the claims supported by accurate, convincing, clear evidence?* — **Yes/No + explanation.**
3. *Would at least some TMLR audience be interested?* — **Yes/No + explanation.**
4. Requested changes, **each marked** "critical to acceptance" vs "would strengthen".
5. Broader impact concerns, if any.

**Acceptance criteria that modify our defaults:**

- A claims–evidence gap can be closed by **more experiments or by reducing the claims**. Record both options in the repairability field.
- The second criterion is **interest, not novelty/significance**: do not reject for "not novel enough" or lack of SOTA. In our table, a careful replication can Originality-`MEETS` under this overlay.
- But: papers that **incorrectly claim novelty**, make bold unsupported statements, are unclearly written, or merely re-implement an already-reproduced idea **are rejectable**. The closest-work table still matters — for the *correctness* of the novelty claim, which can hit G4.
- Presentation problems count only where they **materially impede understanding** — same bar as our Clarity dimension.

**Process notes:**

- Double-blind guidance: do related-work searches **after a preliminary read** of the submission (our workflow step 2 → step 3 order matches).
- Reviewer-stage official vocabulary is accept / leaning accept / leaning reject / reject. If the user wants reviewer-stage wording: Accept as is → accept; Accept with minor revision → leaning accept; Reject → reject, or leaning reject when the claims–evidence gap could plausibly close in discussion by reducing claims. The script still emits the decision-stage set.
- LLM policy: TMLR allows LLM assistance but expects the reviewer's own judgment. When the venue has such a policy, **disclose tooling in the letter's end matter**; do not present an automated review as unaided.

## Venues not covered here

ICML, ACL/EMNLP, VLDB, SIGMOD, statistics journals: no in-session verified guide. At review time, fetch the official reviewer guide, follow it for letter shape, and record `URL + access date` in `reviews/<paper-id>/novelty-trace.md`. Do not generalize this file's defaults to them.
