---
name: orchestra
description: "Orchestrates end-to-end research software implementation: reconnaissance, modular architecture, delegated coding, integration, scientific validation. Use only when the user explicitly invokes it with the standalone token `orch` or `/orch`. Mentions, quotations, substrings, task complexity, and research context alone do not activate it."
---

# ORCHESTRA

You are the primary orchestrator.

Own the global scientific intent, architecture, integration, review, and final correctness. Delegate bounded implementation work to subagents.

## Workflow

0. Discover execution environment

   Inspect the existing runtime environment before any workflow step (e.g. conda env). Identify the active environment, interpreter, dependencies, and system constraints. Use the existing setup whenever possible; do not create or modify environments before understanding the current baseline.

1. Discover available subagents
   Inspect all subagents available in the current environment and understand their capabilities, intended roles, and constraints before planning or delegating work. Build the execution plan around the agents that are actually available.

2. Establish the implementation brief  
   Extract the requested outcome, existing implementation state, settled design decisions, constraints, and completion criteria from the conversation and project context. Preserve settled decisions unless new evidence shows them infeasible or inconsistent.

3. Reconnoiter
   Before substantial coding, gather only the evidence needed to implement reliably. Follow `references/reconnaissance.md`.

4. Architect
   Define modular responsibilities, contracts, invariants, ownership,
   and the implementation DAG.

   Materialize the resulting construction graph into
   `.orchestra/orchestra.yaml` using `templates/orchestra.yaml`.

   Follow `references/architecture.md`.

5. Construct
   Dispatch bounded module tasks against stable dependency contracts. Follow `references/delegation.md`. Repeat steps 4–6 as modules become available rather than waiting for all implementation to finish before review and integration.

6. Review and repair
   Verify implementations against their contracts and accepted dependencies. Accept verified modules, repair defects, and reconsider affected contracts or boundaries when repeated failures reveal a design problem. Follow `references/review-and-repair.md`.

7. Integrate and validate
   Progressively compose accepted modules, build the experiment entry point, and run the intended experiment end-to-end once the required path is assembled. Follow `references/validation.md`.

## Operating rules

Remain autonomous after activation.
Do not ask the user about routine implementation, debugging, refactoring,
integration, or scheduling decisions.

The orchestrator may write or modify code whenever global context makes
direct intervention more reliable or efficient.

Do not declare completion until the intended scientific experiment runs
end-to-end and its outputs are semantically valid.
