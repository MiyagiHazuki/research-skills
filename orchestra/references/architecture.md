# Architecture

Translate the scientific task into a modular implementation architecture before delegating substantial coding work.

The orchestrator owns this architecture.

## Project Structure

Adopt a clear repository structure with dedicated directories for reusable modules, data, configurations, and experiments.

For example:
- `./src/` for implementation;
- `./data/` for data resources;
- `./configs/` for configurations;
- `./experiments/` for experiment execution.

Each directory should have a clear ownership and purpose.

## Responsibility

Define responsibilities before implementation units.

A **responsibility** is a coherent area of decision ownership, with one identifiable purpose and one reason to change.

A good responsibility has a clear boundary, can be explained independently, needs only decision-relevant information, and can be validated without executing unrelated parts of the system.

Reject a responsibility that would:

- let another unit make or override the same decision;
- require unrelated orchestration state — e.g. an evaluator reading global CLI `args`, output paths, or checkpoint policy;
- mutate unrelated experiment state — e.g. `compute_metrics()` changing the optimizer, checkpoint state, or experiment configuration;
- absorb another responsibility — e.g. `evaluate()` also constructing datasets/loaders or managing result files;
- leave correctness to callers — e.g. a split routine relying on downstream code to enforce disjointness or reproducibility.

## Modules

Derive modules from established responsibilities, not from file layout, workflow stages, or coding convenience.

A **module** is an implementation boundary that owns one primary responsibility and exposes that responsibility through a bounded public interface.

Realize a module with the classes, functions, and data structures naturally required by that responsibility. Use a **class** when persistent state, invariants, and behavior belong to one coherent abstraction; otherwise prefer simpler module-level functions and data structures.

Prefer modules with high cohesion, low coupling, minimal duplicated functionality, explicit inputs and outputs, stable interfaces, clear ownership, and independent testability.

Reject a module boundary when correct use requires callers to know its internal representation, when multiple modules must coordinate private state to fulfill one responsibility, or when internal implementation changes force callers to change despite an unchanged contract.

## Operations

An **operation** is one bounded semantic action within a module.

Realize an operation as a **function** when it depends only on explicit inputs, and as a **method** when it naturally belongs to an object and depends on or modifies that object's state.

Prefer operations that perform one coherent action, expose explicit inputs and outputs, and make relevant side effects visible through their contract.

Reject an operation when it silently performs unrelated work (e.g. `compute_metrics()` also saves checkpoints), depends on unrelated global state, or shifts steps needed to fulfill its own contract onto callers. Explicit input preconditions are legitimate; hidden obligations to finish the operation are not.

## Contract Formation

Define a contract before substantial implementation or delegation so the module can be implemented and verified without reconstructing surrounding architecture.

A good contract is sufficient, minimal, traceable, stable, and independently verifiable.

Derive it from the established responsibility:

```text
owned decision
    ↓
required information + observable result
    ↓
public interface + dependencies
    ↓
invariants + acceptance
```

Every input, state variable, operation, output, and dependency must be justified by the owned decision. Keep implementation details internal unless callers must rely on them.

## Scientific Invariants

Some violations preserve program execution while invalidating the scientific conclusion. Capture these conditions explicitly in the module contract.

Good invariants make scientific validity conditions explicit, local to their owner, and independently checkable.

Examples include:

- train/test separation;
- absence of label leakage;
- normalization constraints;
- random seed propagation;
- correct data splits;
- required ordering or masking semantics;
- preservation of the intended algorithm;
- evaluation protocol consistency.

A scientific invariant is violated when the experiment can complete successfully while no longer evaluating the intended scientific procedure, e.g. test information influences preprocessing, data splits are inconsistent across runs, or the implementation silently changes the evaluated algorithm.

## Evolving Architecture

The architecture is a living dependency DAG, progressively constructed from foundational modules toward higher-level ones. Each node is a contract-defined module that can be independently implemented, validated, and accepted; each edge is a dependency that defines construction order — higher-level modules may depend on lower-level ones, while foundational modules stay independent of downstream use cases. Evolution proceeds along the dependency direction:

```text
foundational modules
        ↓
intermediate abstractions
        ↓
higher-level modules
        ↓
complete system
```

Establish the abstractions needed by the current task before composing higher-level capabilities: e.g. build MLP blocks, then Encoder and Decoder, then compose them with the objective and training logic into a complete VAE. The system emerges through composition of accepted modules, not monolithic implementation.

When multiple modules share a dependency, keep it as a single node with multiple dependents; never duplicate a responsibility merely to preserve a tree shape.

Judge abstraction boundaries:

- A higher-level module composes lower-level capabilities instead of absorbing their independent responsibilities.
- Consider splitting a module when its components own distinct decisions and benefit from separate contracts or validation.
- Extract modules for present responsibility boundaries and validation needs, not speculative reuse. A single consumer is not by itself evidence of a poor boundary.

When implementation evidence reveals an incorrect abstraction boundary, contract, or dependency relation, the orchestrator may split, merge, reorder, introduce, or redesign nodes; affected dependents are reopened and revalidated. Update `.orchestra/orchestra.yaml` whenever the dependency graph or module contracts materially change.
