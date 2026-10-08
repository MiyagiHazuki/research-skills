# Validation

Validation determines whether the implemented system realizes the user's intended scientific experiment.

The orchestrator owns validation criteria and final completion decisions.

Validation subagents provide evidence and diagnosis; they do not replace orchestrator judgment.

## Validation Delegation

Consider delegating validation to sufficiently capable subagents when execution requires:

- complex experiment procedures;
- repeated runs or parameter verification;
- large-scale output inspection;
- scientific interpretation of results.

Assign validation tasks with:

- intended experimental objective;
- expected execution path;
- relevant acceptance criteria;
- required artifacts to inspect;
- known risks or invariants.

Prefer higher-capability subagents for scientific validation tasks because they require understanding of both implementation behavior and experimental intent.

## Progressive Integration

Do not postpone all integration until every isolated module is finished.

As accepted modules become available, compose them into increasingly complete execution paths.

Early integration should expose:

- interface mismatches;
- incorrect assumptions;
- configuration problems;
- incompatible data representations;
- scientific-semantic errors.

Resolve these before constructing further layers on top.

## Experiment Entry Point

Produce an appropriate user-facing entry point for the completed experiment.

It should assemble accepted components through the intended configuration and execution path.

The entry point may be:

- a CLI command;
- a script;
- a configuration-driven runner;
- another interface appropriate to the repository.

Global wiring and final assembly normally remain under orchestrator ownership.

Record the entry point relative to the project root in `integration.entry_point`. Set `integration.status` to `active` when composition begins and to `complete` when the required experiment path is assembled and its integration checks pass. Integration completion alone is not experiment completion.

## End-to-End Execution

Run the requested experiment through its actual execution path.

Do not substitute isolated validation for end-to-end execution.

Validation should confirm that the system produces the intended experimental artifacts, which may include:

- result files;
- metrics;
- model outputs;
- checkpoints;
- tables;
- logs;
- cached predictions;
- other scientifically meaningful artifacts.

## Scientific Validation

Check that successful execution corresponds to the intended experiment.

Evaluate issues such as:

- correct dataset and split;
- expected experimental configuration;
- correct method and model;
- valid evaluation procedure;
- absence of unintended leakage;
- plausible output structure;
- intended randomization and reproducibility.

Do not infer expected numerical outcomes unless they are independently established.

## Validation Outcomes

Set `validation.status` to `running` when validation starts and record execution commands, inspected artifacts, and check results in `validation.log`. Partial-path checks inform progressive integration; set `passed` only when the final completion criteria below are satisfied.

If execution or scientific-validity checks fail, set `validation.status` to `failed`, preserve the failure evidence, and return affected work to review and repair. Revise the architecture only when the evidence implicates a contract or boundary. Apply the Ledger rules in `review-and-repair.md` when reopening nodes or invalidating prior results, then rerun the affected checks and the intended end-to-end path.

If a missing resource or unresolved decision prevents validation, set `validation.status` to `blocked`, record the reason in `validation.log`, and follow Blocked Outcomes in `review-and-repair.md`. Once resolved, return validation to `pending` until execution resumes. Do not treat an unexecuted check as a pass or an implementation failure.

## Completion

Completion requires end-to-end execution and evidence that the implementation follows the intended method and evaluation protocol. Report the observed results faithfully, including negative or inconclusive findings.

Validation reports are evidence for completion decisions, not automatic acceptance.

Record the final validation state in `.orchestra/orchestra.yaml`.

Report the execution command and configuration, artifact locations, validation evidence, observed results, and any remaining limitations to the user. A blocked or failed outcome is not completion.
