# Delegation

Delegate bounded implementation work after the architecture and module contracts are established.

The orchestrator decomposes the architecture DAG into implementation tasks and assigns them to coding subagents while retaining responsibility for global reasoning, architecture consistency, and scientific validity.

Coding subagents are strong local implementers. They should not be required to reconstruct the entire research project, redefine objectives, or redesign established architecture.

## Task Boundary

A delegated task should correspond to one contract-defined module or a clearly bounded contract change.

Provide only the context required to implement the task correctly.

A useful task packet may include:

- exact responsibility;
- relevant module and files;
- public interface;
- inputs and outputs;
- dependency contracts and current acceptance status;
- expected behavior;
- scientific invariants;
- permitted write scope;
- validation expectations.

Do not over-prescribe implementation details when the contract is sufficient.

Coding subagents should implement within the established architecture. They may report architectural inconsistencies, but should not independently redesign module boundaries, dependency relations, or scientific objectives unless explicitly requested.

## Dependency Order

Delegate implementation according to the architecture DAG.

A coding task may start when its required dependencies have stable contracts, even if their implementations are not yet accepted. Identify any validation that must wait for those implementations; contract-level checks do not establish integration correctness.

Integrate a module with its actual dependencies, and accept it, only after those dependencies are `accepted` by the orchestrator. A completed implementation or a subagent's successful self-check is not acceptance. Apply this gate to the dependencies of the execution path being integrated, not to every node in the DAG.

Prefer implementing foundational modules before higher-level composition. If a dependency contract changes during coding, pause affected work and reconcile the task with the revised contract before resuming.

When multiple modules share a dependency, preserve the shared dependency as a single owned implementation node rather than duplicating work across agents.

## Direct Modification

Coding subagents must edit the working project directly.

Do not ask them to return code for the orchestrator to manually copy into files.

They should inspect the files necessary to understand their local context, implement the change, run appropriate validation, and report what they changed.

## Write Ownership

Assign ownership according to architecture boundaries rather than file boundaries.

A subagent owns the implementation of assigned modules, not arbitrary files.

Avoid concurrent modification of the same file.

Parallel coding is appropriate when:

- dependency constraints allow it; and
- write scopes do not overlap.

Files requiring cross-module integration or global coordination should normally remain under orchestrator control.

## Testing and Diagnosis

For implementation tasks, attach suitable testing and debugging capabilities.

Prefer the user's installed:

- `tdd`
- `diagnose`

when applicable.

If they are unavailable, inspect the installed skill environment and use the closest appropriate alternatives.

Subagents should validate their own work before returning it, but their validation does not replace orchestrator review.

## Agent Sessions

When the environment supports persistent or resumable subagent sessions, retain the relevant session reference in `.orchestra/orchestra.yaml`.

Prefer resuming the original implementation session for local follow-up work when its existing context remains useful.

## Return Expectations

A coding subagent should return a concise implementation report containing the information required for orchestrator review:

- files changed;
- contract implemented;
- behavior implemented;
- tests or diagnostics performed;
- unresolved assumptions or failures.

Do not require verbose narration of internal reasoning.
