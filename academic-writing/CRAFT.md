# Craft

The standard: a smart outsider can follow the argument; a specialist still trusts it; a practitioner can see what to build next. Do not copy a review-genre shape onto a methods paper.

## Reader

Write for an intelligent non-specialist in *this* niche. For a Nature-style review, that is a scientist in another field. For NeurIPS/ICLR, that is a reviewer who knows ML but not your corner. Adjust jargon. Keep the teaching moves.

## Open with the world, not the literature

First paragraph: the reader already lives with the problem (search, a camera, a clinical alarm, a compiler). Not "In recent years, X has attracted increasing attention."

Then name the **obstacle** that made the old approach stall. Only then name your method. Definition follows need.

## Teach with one running example

Pick one concrete case and reuse it (an image going from pixels to parts; a house/car/person/pet classifier; one patient trajectory). The example should still be working in the method section and in a figure. A new example every paragraph is decoration.

## Define when needed, then reuse

Introduce a term at the moment the reader must have it. A metaphor is allowed if it earns the next sentence (weights as knobs; a loss as a landscape). Do not stack unused metaphors.

## History is an argument

A timeline is not a related-work dump. Use history only to show why a reasonable idea was dropped, what the fear was, and what evidence removed the fear. Cite the hinge paper because it changed practice, not because it exists.

## Stakes must be named

Not "many applications" or "various domains." Name the task, the metric, the deployment, or the scientific use. Prefer the strongest real comparison, not a trivial baseline.

## The abstract is a complete argument

Four jobs, usually four to six sentences: what the thing is; what it changed; how it works (one mechanism); which variant is for which data. No "novel framework." No citation unless the venue requires it.

## Judgment is allowed when labeled

"We think" / "we expect" is honest when it is a bet about the field. It is not a substitute for a result. Do not dress a wish as "the results demonstrate."

## Rhythm

- Teaching, a running example, or a short history may use a longer sentence that unfolds **one** idea.
- Claims, contrasts, and contributions are short.
- Do not stack three subordinate clauses. If a sentence needs a second idea, split.
- No numeric word cap. Clarity beats brevity; brevity beats padding.

## Figures teach

Intuition first, then the equation or the architecture. A figure caption should be readable without the main text. Point to the figure from the sentence that needs it.

## Close with a bet, not a slogan

The last section names what becomes possible (or what remains blocked) if the reader accepts the argument. One or two concrete bets beat a laundry list of "future work." For a methods paper, a real limitation is more persuasive than a visionary paragraph.

## Do not steal the review's shape

A methods paper still has method and experiments as the spine. Use these craft moves *inside* that spine. Do not turn a NeurIPS paper into a nine-page field essay.
