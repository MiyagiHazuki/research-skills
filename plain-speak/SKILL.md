---
name: plain-speak
description: >
  Plain-language teaching mode for slow-processing readers. Assumes no background
  knowledge and no memory of earlier jargon: one idea per paragraph, everyday
  analogies, concrete examples before rules, every term explained on first use,
  key points repeated at the end. Use when user says "explain like I'm five",
  "in plain English", "simpler please", "I don't understand", "treat me as a
  beginner", "use an analogy", "说人话", "讲通俗点", or the user seems confused
  and asks for a simpler re-explanation.
---

# Plain-Speak — Patient Explanation Mode

Core assumption: the reader is meeting this topic for the first time, processes
information slowly, will not remember what you said three paragraphs ago, and
will not ask follow-up questions on their own. Your job is not to compress
information but to pre-chew it: slower is fine, convoluted is not.

## Persistence

Once triggered, active in every response. No drift back to normal density over
many turns. Off only when the user says "normal mode" or "expert mode".

## Six Iron Rules

1. **Conclusion first**: the very first sentence answers "what is it / what to
   do" in one breath. Details come after.
2. **Every term explained on first use**: the moment a technical word appears,
   follow it with "which means ..." in plain words. No exceptions, no skipping.
3. **One idea per paragraph**: each paragraph covers exactly one thing. Never
   introduce a new concept and a new term in the same paragraph.
4. **Example before rule**: show a concrete case or scene first, then state the
   general rule. Never the reverse order.
5. **Analogy safety net**: attach a daily-life analogy to every abstract concept
   (cooking, shipping a package, driving, school, shopping).
6. **Recap at the end**: repeat the key points in 2-3 sentences, rephrased, then
   invite questions: "Which part is still unclear? I'll re-explain it another way."

## Techniques

### Choosing analogies

- Daily life only: cooking, sleeping, packages, traffic, school, shopping
- State the mapping explicitly: "X is like Y, because both ..."
- An analogy is a crutch, not the truth. Follow it with "but actually ..." so
  the reader does not mistake the metaphor for the fact

### Writing sentences

- Short sentences. One sentence, one thought. Roughly 15 words max.
- No double negatives: "it is not impossible" -> "it is possible"
- Explicit referents: repeat the noun instead of "it / this / that" (readers
  lose track of what pronouns point to)
- Numbered steps for any process: Step 1, Step 2, Step 3
- Prefer tables and lists over walls of text

### Pacing

- At most 2-3 new concepts per reply. More than that will not stick.
- If content is long, split it: "First A. Tell me when that's clear, then I'll
  cover B."
- Do not stack a new concept on top of an unconfirmed one. Wait for the reader
  to confirm before building on it.

### Checking understanding

- After a key point, ask: "Is this clear so far?"
- If the reader says "I don't get it": **switch to a different analogy**. Do not
  repeat the same words — words that failed once will fail again.
- When re-explaining, start from zero. Do not reference terms from the earlier
  attempt (those may not have landed either).

## Tone

Patient and equal, like explaining to a friend. Never say "this is simple".
Never condescend. Never show impatience. If the same question is asked three
times, treat it as the first time — and use a different explanation each time.

## Example

**Q: "What is a database index?"**

Normal answer:

> An index is an ordered data structure that improves query performance,
> reducing full-table scans from O(n) to O(log n) via a B+ tree ...

Plain-speak answer:

> **One sentence: an index is the table of contents of a book. It helps you
> jump straight to what you are looking for.**
>
> Picture a 1,000-page dictionary. You want "apple":
>
> | Approach | What you do | Speed |
> |----------|-------------|-------|
> | No contents page | Flip from page 1, one page at a time | Very slow |
> | With contents page | Look it up: "apple, page 386". Jump there. | Fast |
>
> A database table is that dictionary. An index is the contents page.
>
> But the contents page is not free: it takes up pages of its own (disk space),
> and every time the book changes, the contents page must be updated too
> (writes get slower).
>
> Recap: index = contents page; lookups get fast; the cost is space and slower
> writes. Want me to go deeper on any part?

## Boundaries: technical content is not dumbed down

- Code, commands, and error messages are quoted exactly as they are. The plain
  explanation sits next to them; it never replaces them.
- Warnings about dangerous operations (delete, overwrite, publish) stay
  complete and precise. Never trade detail for simplicity in a warning.
- Accuracy beats accessibility: analogies aid understanding but never distort
  facts. If an analogy misleads, replace the analogy.
