# Venue overlays

Freeze the venue at intake. Default conference scale is NeurIPS 2024 1–10 because the skill's example score is "6/10, weak accept". Do not invent a scale. Cite the venue page if you use a non-default overlay. What each venue's review form asks for: [official-reviewer-guides.md](official-reviewer-guides.md).

## Conference default (NeurIPS 2024 overall)

Meanings only, accessed 2026-08-31: [NeurIPS 2024 Reviewer Guidelines](https://neurips.cc/Conferences/2024/ReviewerGuidelines).

| Score | Verbal (copied into the letter) |
| :--- | :--- |
| 10 | Award quality |
| 9 | Very strong accept |
| 8 | Strong accept |
| 7 | Accept |
| 6 | Weak accept |
| 5 | Borderline accept |
| 4 | Borderline reject |
| 3 | Reject |
| 2 | Strong reject |
| 1 | Very strong reject |

The mapping table never emits 10 (reserved for a human who wants to override, logged). The script emits 1–9. JSON field: `"venue": "conference_default"`.

## NeurIPS 2025 (only if the user names it)

[NeurIPS 2025 Reviewer Guidelines](https://neurips.cc/Conferences/2025/ReviewerGuidelines), accessed 2026-08-31. Overall is 1–6. Set `"venue": "neurips2025"`. The script still computes the 1–10 table first, then reports `neurips2025_score`. Do not mix the two numbers in the letter without labelling both.

## Journal default

Accept / Minor revision / Major revision / Reject. Aligns with the user's requested vocabulary and with JMLR's nearby set (accept, conditional accept, reject with encouragement to resubmit, reject; [JMLR reviewer guide](https://www.jmlr.org/reviewer-guide.html), accessed 2026-08-31). Map "conditional accept" to Minor revision in the letter unless the user asks for JMLR wording.

## TMLR

[Editorial policies](https://jmlr.org/tmlr/editorial-policies.html), accessed 2026-08-31. Decisions: Accept as is / Accept with minor revision / Reject. **No Major revision.** Set `"venue": "tmlr"`. Criteria to mention: claims supported by accurate, convincing, clear evidence; some audience interest. Modest contributions can be accepted. The script maps Major → Reject unless the only defect is Clarity `DOES_NOT_MEET` with no scientific `DOES_NOT_MEET` and no gates, in which case Accept with minor revision.

## ICLR / ICML / ACL / VLDB / SIGMOD

If the user names one, keep the 1–10 default unless they supply that year's official scale. State in the letter which overlay was used. Do not fake a venue-specific number you did not look up.

## What the overlay must not do

- Change *D*, *P*, *E*, or gate hits.
- Invent "Major revision" for TMLR.
- Claim the mapped score is calibrated to that venue's acceptance rate.
