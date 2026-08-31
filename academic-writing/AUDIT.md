# Audit (after the draft)

Do not edit while auditing. List hits, then rewrite. Preserve every number, equation, citation key, and the author's claim unless the claim is stronger than the evidence (then downgrade or flag).

## 1. Em dashes

Remove every em dash (`—`) and every Chinese dash (`——`). Recast with a period, colon, comma, or parentheses. Do not replace them with spaced hyphens. Keep en dashes in ranges (`2--6%`, `2012--2015`) and minus signs in math.

## 2. General AI tells

Fix these unless a supplied voice sample uses them on purpose:

- Formulaic openers: "In recent years", "With the rapid development of", "Despite recent advances"
- Inflated significance: "paves the way", "sheds light on", "of paramount importance", "opens new avenues", "revolutionize"
- AI vocabulary: delve, underscore, intricate, tapestry, testament, pivotal, showcase, foster, seamless, leverage (as filler), realm, landscape (when abstract)
- Copula avoidance: "serves as" → "is"
- Rule-of-three padding; elegant variation (cycling synonyms for one referent)
- Filler: "it is worth noting that", "in order to", "Notably,", "Importantly,"
- Superficial `-ing` tails: ", highlighting..."

## 3. Academic tells

- Over-claiming verbs: empirical work *shows* or *finds*; it does not *prove* a measured result. Keep "prove" for theorems.
- Empty intensifiers: "extensive experiments", "a wide range of", "comprehensive" with no list.
- Novelty padding: "novel" more than once per section; "to the best of our knowledge"; "for the first time" without a scoped claim.
- Consecutive sentences starting Moreover / Furthermore / Additionally / 此外 / 同时.
- Contribution lists that restate the abstract instead of naming a result.
- Citation dumps: `[3, 7, 9, 12, 15]` with no contrast. Cite the closest work and say the difference.
- Vague hedging: somewhat, relatively, fairly, 在一定程度上. Quantify or cut.
- Unquantified "significantly" without a test or a number.

## 4. Defensive posture

Do not write as if a reviewer, contrarian, or compliance officer is already in the room. Cut hedges that protect claims nobody has challenged. Keep evidence-tied hedges (section 5).

Delete or recast:

- Split that does no work: "On the one hand... on the other..." / 一方面……另一方面…… when one clause already states the claim.
- Caveat on a relation that already stands: "This does not mean A necessarily causes B, although they are often related." / 「这并不意味着 A 就必然导致 B，尽管在许多情况下两者相关」
- Disclaimer on an unchallenged premise: "It should be noted that this is a general trend; exceptions exist." / 「需要指出的是，这里讨论的是一般趋势，个别例外仍然存在」
- Fake contrast for thickness: "This is not merely X, but Y" / 「这不仅仅是 X，更是 Y」 when Y is not more precise than X.

Rebuttal exception: answer reviewer points that were raised. Still cut unasked pre-answers, fake contrasts, and caveats on common-sense relations.

## 5. Preserve

- Evidence-tied hedging: "suggests", "is consistent with", "we hypothesize", "may indicate". A hedge whose only job is to pre-answer an unasked objection is not this.
- Passive voice when the actor does not matter.
- First-person plural "we".
- Definitions, method names, metrics, symbols, LaTeX, identifiers.
- Labeled judgment ("we think", "we expect") in reviews and grant vision.

Wrong fix: turning "the results suggest X" into "the results prove X."

## 6. Claim ↔ evidence

For every empirical sentence:

- Unbacked → add the pointer the user supplied, or delete the sentence, or mark a gap (do not invent).
- Verb stronger than evidence → downgrade.
- Vague magnitude → a number or a range, attributed to method, metric, and the strongest baseline.

Lead comparisons with the strongest competitor, not the trivial baseline.

## 7. Lean wording (do not swap if meaning shifts)

English: utilize → use; in order to → to; due to the fact that → because; a number of → several; has the ability to → can; in the event that → if; facilitate → help (unless it is a technical term). Keep "demonstrate" for proofs.

Chinese: 进行了……的分析 → 分析了……; 存在着 → 有; 具有重要的意义 → say what changed, or cut; 起到了……的作用 → write the verb; 诸多 → 许多; stacked 的 → split and repeat the head noun.

Do not replace a precise technical word with a common one.

## 8. Voice

If a prior-paper sample was given, match: sentence rhythm, how sections open, notation. Do not import the sample's claims or its preemptive caveats. If no sample, stay with CRAFT.md: neutral, precise, concrete.

## Report

```
Audit:
- Patterns removed: ...
- Claims softened or given pointers: ...
- Kept (term, long teaching sentence, hedge): ... with reasons
- Numbers/citations altered: none
```
