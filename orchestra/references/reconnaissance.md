# Reconnaissance

Use reconnaissance only for uncertainty that could materially affect architecture, correctness, implementation choices, or experimental validity.

Reconnaissance serves the user's established task; preserve settled decisions unless new evidence shows them infeasible or inconsistent.

## Evidence needed

Identify the concrete uncertainty before dispatching a scout.

Use research-oriented capabilities for scientific knowledge — prior methods, assumptions, established results, benchmark conventions, known failure modes. Use implementation-oriented capabilities for how a method or system works in practice — reference implementations, APIs, libraries, repository structure, numerical details, reusable components, validation patterns.

Assign these roles only to subagents confirmed available during capability discovery; one investigation may require both.

## Dispatch

Dispatch the minimum scouts needed to resolve material uncertainties; parallelize independent investigations, avoid redundant searches.

Give each scout the scientific and project context plus the specific uncertainty to resolve.

Each scout returns:
- the finding;
- supporting evidence or source;
- its implication for the current task;
- any important unresolved uncertainty.

Prefer primary, official, or author-maintained sources; treat implementations as evidence, not authority.

## Synthesize

Reconcile reconnaissance findings with the current method, experimental setting, and project environment before acting on them. Stop once further investigation is unlikely to change a material implementation decision.

Resolve remaining uncertainty explicitly. If it does not threaten correctness or scientific validity, record the assumption in the relevant contract or task packet and proceed. If it prevents a defensible implementation or validation decision, block the affected work and follow Blocked Outcomes in `review-and-repair.md`; do not silently guess or change the scientific objective. Before a module ledger exists, report the unresolved prerequisite directly.
