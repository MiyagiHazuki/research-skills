# Review and Repair

The orchestrator is the final technical and scientific authority.

A subagent reporting success does not make a module accepted. Acceptance requires orchestrator verification that the implementation satisfies its contract, integrates correctly, and preserves scientific validity.

## Review

Review the actual implementation, not only the agent's summary.

For significant modules, verify:

- local correctness;
- adherence to the module contract;
- interface compatibility;
- dependency assumptions;
- unintended scope changes;
- scientific invariants;
- consistency with the intended algorithm;
- relevant tests and diagnostics.

Research software may execute successfully while being scientifically wrong. Treat semantic correctness as a first-class review concern.

## Acceptance

A module node becomes `accepted` only after its dependencies are accepted and the orchestrator verifies its contract and integration with those dependencies. It can then safely serve as an implemented dependency for higher-level integration. Coding against a stable contract may begin earlier.

Acceptance records verified contract compliance, not merely successful code execution.

If uncertainty remains material, keep the node under review or reopen it for repair.

Record acceptance and reopening using the state rules in Ledger below.

## Direct Repair

The orchestrator may edit any code directly.

Prefer direct repair when the defect is:

- small;
- obvious;
- integration-related;
- dependent on global context;
- faster and safer to fix centrally.

Do not delegate trivial repairs merely for procedural purity.

Direct repair should preserve the existing module contract unless the defect reveals that the contract itself is incorrect.

## Resume a Subagent

When a defect is local to a module and the original coding agent's context remains useful, resume that session when possible.

Provide:

- the observed failure;
- relevant reproduction evidence;
- the orchestrator's diagnosis;
- a repair direction when useful;
- the expected validation after repair.

If the original session cannot be resumed, create a new repair task containing:

- the module contract;
- current implementation state;
- failure evidence;
- relevant diagnosis.

## Repeated Failure

Do not mechanically retry a repeatedly failing implementation.

Repeated failure may indicate a problem with:

- the module contract;
- abstraction boundary;
- dependency assumptions;
- chosen implementation strategy;
- surrounding architecture.

Escalate the issue to the orchestrator level and reconsider the affected design.

When necessary, redesign the affected subgraph, then reopen and revalidate affected dependent nodes.

## Blocked Outcomes

Continue repair while there is a concrete, testable next step within the available resources and agreed scope. Do not repeat attempts without new evidence or a materially different approach.

If missing data, credentials, compute, an unresolved scientific decision, or exhausted repair options prevent safe progress, mark affected nodes `blocked` and record the blocker. Continue independent work where useful, but do not claim overall completion while required work remains blocked.

When no independent work can proceed, preserve the current state and report what was completed, the blocking evidence, and the specific input or decision needed to resume. Ask the user only for a non-routine decision or resource the orchestrator cannot obtain independently; do not silently change the scientific objective or weaken acceptance criteria.

## Independent Verification

Use a separate verifier subagent only when independent review provides meaningful value.

Typical cases include:

- core scientific algorithms;
- numerically delicate implementation;
- complex transformations;
- high-risk experimental logic;
- code prone to silent failure.

Do not create verifier agents routinely when the orchestrator can confidently adjudicate correctness.

Independent verification supplements orchestrator review; it does not replace ownership of acceptance decisions.

## Ledger

Keep `.orchestra/orchestra.yaml` current when work starts, is submitted for review, is accepted, is blocked or reopened, changes ownership, or undergoes material redesign.

Use these node states:

- `ready`: the contract and required dependency contracts are stable, and implementation or repair can start;
- `implementing`: implementation or repair is in progress;
- `review`: the implementation is available for orchestrator review; acceptance may still await dependency acceptance or verification evidence;
- `accepted`: the acceptance conditions above have been verified;
- `blocked`: no safe next implementation or review step is available; `blocker` records what must be resolved.

The normal path is `ready` → `implementing` → `review` → `accepted`. Reopening is an action, not another state: withdraw acceptance and return the node to `ready` for repair, `review` for revalidation only, or `blocked` if progress is prevented. When a blocker is resolved, clear `blocker` and return to `ready` or `review` according to the remaining work.

When a contract, implementation, or dependency change invalidates prior evidence, reopen the affected nodes and transitive dependents whose acceptance relied on that evidence. Pause affected in-flight work before changing its contract or write scope; unaffected branches retain their status.

If the change affects an integrated execution path, reset `integration.status` to `active` (or `pending` if no assembled path remains). Reset affected validation to `pending` and record which earlier evidence is superseded in `validation.log`; historical passes are not current acceptance evidence. Restore completion states only after the affected checks are rerun.
