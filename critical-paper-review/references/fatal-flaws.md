# Fatal flaws (manuscript gates)

Gates feed [score-mapping.md](score-mapping.md). A gate is **hit** only with a verbatim quote (or a verified equivalent paper for G4). Not every weakness is a gate. Distilled from ARS Devil's Advocate CRITICAL criteria and DIAL idea-evaluator F1, F3, F6, F10 plus the data-refuted-mechanism rule, restricted to *completed manuscripts*.

## Hard gates → conference score = 3, journal Reject

**G1 Foundation collapse.** The core problem, mechanism, or premise does not stand. Includes DIAL's data-refuted mechanism: the paper's own tables already show the isolated core mechanism matched or beaten by a baseline, ablation, or simple control. Do not call that "a few more experiments away". Do not invent a threshold that would let it pass. Untested mechanisms are not G1.

**G2 Data–conclusion mismatch.** The headline claim does not follow from the reported evidence (wrong direction, wrong quantity, conclusion scoped beyond the sample or the theorem). Quote both the claim and the result.

**G4 Novelty collapse.** Search found prior work that already does the claimed contribution on the paper's own difference axes, with no remaining defensible delta. A weaker baseline or a missing citation is not G4. G4 cannot fire if Originality is `NOT_ASSESSED`.

**G6 Fabricated or unverifiable key result.** A load-bearing number, citation, or theorem cannot be tied to the manuscript, supplement, or a verified source. Grey-zone retrieval is unused, not G6. Tool failure is not G6.

## Soft gates → conference score = 4 (if no hard gate)

**G3 Logic-chain break.** A listed contribution maps to no section or experiment; the intro's problem is not the problem the method solves; or removing one unreplicated step collapses the argument. DIAL: contribution-to-section mismatch is CRITICAL as a finding; here it is G3 when it is the main chain, not a leftover bullet.

**G5 Serious statistical-reporting failure.** Not a formatting niggle. Examples: no uncertainty on the headline metric in a statistics journal; uncorrected 20-test fishing that *is* the claim; train/test leakage that makes the number uninterpretable. See [statistical-red-flags.md](statistical-red-flags.md). Missing one CI in an otherwise careful ML paper is MAJOR, not G5.

## Manuscript-applicable DIAL flaws (usually MAJOR, not automatic gates)

Use these as findings. Promote to a gate only when they meet the definitions above.

| Source | Manuscript reading |
| :--- | :--- |
| F1 no novelty vs closest work | feeds Originality; G4 only if equivalent |
| F3 baseline is not the real baseline | Experiments `PARTLY_MEETS` or `DOES_NOT_MEET`; not G1 unless the "win" vanishes against the real baseline *in the paper's own numbers* |
| F6 unverifiable claim | Evidence `DOES_NOT_MEET`; G6 if the key result cannot be located at all |
| F10 no failure case | Significance / overclaim; rarely a gate |

Do **not** apply F2 (venue coaching as the review), F5 (student capability), F7 (IRB the reviewer cannot see), F8 (scope as career advice), F9 (solution-looking-for-problem) unless the manuscript itself shows them.

## What is not fatal

Writing quality, missing related work that does not collapse novelty, a weaker-than-ideal ablation that still isolates something, incremental contributions, negative results, non-native English. Those can be MAJOR or MINOR. They are not G1–G6.
