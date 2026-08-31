# Deepening brief: from decision to execution

This skill decides **why, what, and where**. The `/refactor` command decides **how**: mechanical transformation, LSP/AST-grep execution, continuous test verification. Neither should do the other's job.

- **This skill never implements.** If the user says "go ahead and do it" mid-grilling, produce the brief first, then give them the `/refactor` invocation.
- **`/refactor` never re-designs.** Everything in the brief's "Constraints" section is settled. Its intent gate should pass on the brief alone — the user shouldn't be re-asked what has already been decided.

The bridge between the two skills is the **deepening brief**: a short, structured markdown file that carries the grilling loop's output into `/refactor`'s pipeline. (Not to be confused with the separate `handoff` skill, which compacts conversations — a deepening brief is an execution specification for a single approved design.)

## When to write a brief

Write one when the grilling loop crystallizes a design the user intends to execute — now or later. Skip it when the user rejects the candidate (record the decision instead — see the side effects in SKILL.md).

- Location: `docs/briefs/<slug>.md` (create the folder lazily).
- Status field: `approved` when the user has signed off on the design; `draft` when saved for future exploration.
- An approved brief is the *only* artifact `/refactor` needs. A draft brief is a bookmark for a future session.

## Brief template

Every field maps to a phase of `/refactor`'s pipeline — fill them all, or the intent gate will bounce the request back to the user.

```markdown
# Deepening Brief: <name>

Status: approved | draft
Date: YYYY-MM-DD

## Goal
One paragraph, in the project's domain language (CONTEXT.md terms) and this
skill's architecture language (LANGUAGE.md terms). What becomes deeper, and
what friction disappears.

## Target
Explicit entry points for /refactor's intent gate — file paths and symbols:
- Primary: src/orders/intake.ts (OrderIntake)
- Also touched: src/orders/validate.ts, src/orders/notify.ts

## Scope
file | module | project — one line of rationale.

## Strategy
safe | aggressive — one line of rationale grounded in the test inventory
below. Aggressive only if the surviving tests genuinely pin behaviour.

## Designed interface  (settled — do not re-design)
Entry points, invariants, ordering constraints, error modes. The sketch from
the grilling loop or the INTERFACE-DESIGN.md comparison, trimmed to what an
implementer needs.

## Seam & adapters
- Seam placement: <where the interface lives, and why there>
- Dependency category (DEEPENING.md): in-process | local-substitutable |
  remote-but-owned | true-external
- Adapters: <production adapter>, <test adapter> — two adapters minimum,
  or justify the exception.

## Test plan
- Surviving tests (must pass throughout): <paths>
- Delete after deepening (old shallow-module unit tests): <paths>
- New tests at the interface: <list — the interface is the test surface>

## Constraints  (settled decisions — do not re-litigate)
- ADR-0007: <decision>
- <Any other constraint from the grilling loop>

## Verification
How success is checked beyond the test suites: <commands, manual checks,
observable outcomes through the interface>.
```

## The invocation line

End the session by giving the user the exact invocation:

```
/refactor "Execute deepening brief docs/briefs/<slug>.md" --scope=<scope> --strategy=<strategy>
```

A file path as the target is explicit, so `/refactor`'s intent gate classifies it as "Explicit — proceed" instead of re-interviewing the user. Its exploration phase then starts from the brief's Target, Seam, and Test plan instead of rediscovering them.

## What not to put in a brief

- **Implementation steps.** Sequencing the mechanical work is `/refactor`'s job (its codemap and plan phases). The brief states the destination, not the path.
- **Anything unsettled.** If a design question is still open, the grilling loop isn't done. A brief with "we could do X or Y" in Constraints will make `/refactor` guess.
- **Vocabulary drift.** Keep LANGUAGE.md terms exact; the brief is read by another agent that shares this skill's glossary only through what the brief carries.
