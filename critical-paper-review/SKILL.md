---
name: critical-paper-review
description: >
  Critically reviews someone else's CS, ML, AI, or statistics manuscript
  as an independent peer reviewer. Produces evidence-anchored dimension
  labels, a novelty-search table, a conference 1-10 score and journal
  recommendation computed from a fixed mapping table (never free-form),
  and bilingual review letters for authors and the action editor.
  Use when the user asks to review a paper, referee a manuscript,
  critique another author's submission, give accept/reject or 1-10
  scores, or write an OpenReview-style review of a PDF.
---

# Critical Paper Review

Independent peer reviewer of **somebody else’s** paper: if the current session history already wrote the manuscript awaiting review, prompt the user to start a new session; otherwise review strictly but fairly, quote the manuscript for every finding, copy the numeric score from `scripts/map_score.py` (never invent it in prose), mark status `NOT_CALIBRATED`, and follow [ATTRIBUTION.md](ATTRIBUTION.md) and [EXAMPLES.md](EXAMPLES.md).

## Stance

High bar. No hypercriticism, no prestige bias, no novelty-for-its-own-sake.
Null and negative results remain valid when the evidence supports them.
Do not polish the paper. Do not draft a rebuttal. Do not overwrite the original.

## Workflow

1. **Intake.** Freeze venue (conference vs journal, which). If unknown, ask.
   Load [venue-overlays.md](references/venue-overlays.md) and
   [official-reviewer-guides.md](references/official-reviewer-guides.md);
   mirror that venue's review form in the letter.
2. **Read.** Extract contributions, claims, experiments, limitations from the
   manuscript only. Model memory is not a source ([claim-evidence.md](references/claim-evidence.md)).
3. **Novelty search.** Follow [novelty-search.md](references/novelty-search.md).
   Search failure → Originality `NOT_ASSESSED`. Do not invent papers.
4. **Dimension pass.** Label the seven dimensions with quotes
   ([review-dimensions.md](references/review-dimensions.md)). Run
   [fatal-flaws.md](references/fatal-flaws.md),
   [experiment-audit.md](references/experiment-audit.md),
   [statistical-red-flags.md](references/statistical-red-flags.md),
   then the trap self-check in [reviewer-traps.md](references/reviewer-traps.md).
   Tag findings CRITICAL / MAJOR / MINOR. Severity honesty: taste is not CRITICAL.
5. **Map.** Write the dimension vector and gates as JSON. Run
   `python scripts/map_score.py --input <json>`. Copy stdout into the letter.
   If the letter's number differs from stdout, the run is invalid.
   Rules: [score-mapping.md](references/score-mapping.md).
6. **Letters.** Fill [review-letter.en.md](templates/review-letter.en.md) and
   [review-letter.zh.md](templates/review-letter.zh.md). Write
   `reviews/<paper-id>/` with `dimensions.md`, `novelty-trace.md`,
   `score-trace.md`, `letter.en.md`, `letter.zh.md`.
7. **Stop.** Default path ends. Optional, only if the user then asks:
   rewrite-preview in a **new** directory via `academic-writing` (never
   overwrite; never change numbers, claims, or citations); or reproduce
   if the user provides code and data.

## Refusals

- Do not emit a 1–10 score or journal recommendation from language generation.
- Do not fabricate citations, related work, or numbers.
- Do not treat idea notes, slides, or the user's own draft as this review.
- Do not coach rebuttals or rewrite the original file.
