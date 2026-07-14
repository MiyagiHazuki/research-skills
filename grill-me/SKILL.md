---
name: grill-me
description: >
  Interview the user relentlessly about a plan or design until reaching
  shared understanding, resolving each branch of the decision tree.
  Use when user wants to stress-test a plan, get grilled on their design,
  or mentions "grill me".
---

Interview me relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one.

## Language

**ALWAYS use Simplified Chinese (简体中文) for ALL interactions.** This includes:
- Every `question` field (the full question text)
- Every `header` (still keep under 30 chars)
- Every option `label` and `description`
- All narration and follow-up text

Only use English when quoting code, identifiers, file paths, or technical terms that have no standard Chinese translation.

## Process

1. **Explore first** — If any question can be answered by exploring the codebase, do that first to narrow down what actually needs asking.

2. **Batch all questions into a single `question` tool call** — Collect EVERY unresolved question about the plan/design upfront. For each question:
   - Put your recommended answer as the first option, labelled with `"(Recommended)"`.
   - Provide alternative answers as additional options.
   - Keep `header` under 30 chars.
   - Use `multiple: true` where multiple answers may apply.

   Do NOT ask questions one at a time. Batch everything into one call.

3. **Iterate** — Once the user responds, incorporate their answers and proceed to the next branch of the decision tree. Repeat steps 1-2 as needed, always batching all pending questions into a single `question` call per round.
