---
name: tdd
description: Test-driven development with red-green-refactor loop for research code. Use when user wants to reproduce a paper, verify numerical correctness, implement algorithms from formulas, catch regressions in experiments, run ablation studies, test convergence, or set up reproducible experiment pipelines. Triggers: "TDD", "red-green-refactor", "test-first", "复现", "数值回归", "收敛验证", "消融实验", "可复现性", "写测试".
---

# Test-Driven Development for Research

## Philosophy

**Core principle**: Tests verify _scientific correctness_ through the public behavior of algorithms, models, and data pipelines. Implementation can change; the mathematical contract must not.

**Good research tests** describe what the algorithm/model _should produce_ given known inputs. They validate against:

- **Analytical solutions**: known closed-form results
- **Benchmark datasets**: standard reference outputs
- **Numerical invariants**: conservation laws, monotonicity, finite-ness
- **Convergence properties**: error decreases with more steps/data/resolution
- **Reproducibility**: same seed + same input → same output

A good test reads like a claim you'd make in a paper: "gradient descent reduces loss monotonically on convex problem" or "model output matches analytical solution within 1e-6 relative error."

**Bad research tests** are coupled to implementation. They test internal tensor shapes, optimizer internal state, or exact floating-point equality. The warning sign: your test breaks when you vectorize a loop or change optimizer, but the mathematical output is still correct.

See [tests.md](tests.md) for examples and [mocking.md](mocking.md) for research mock guidelines.

## Anti-Pattern: Horizontal Slices

**DO NOT write all tests first, then all implementation.** This is "horizontal slicing" — treating RED as "write all tests" and GREEN as "write all code."

This produces **crap tests**:

- Tests written in bulk test _imagined_ behavior, not _actual_ algorithm behavior
- You end up testing the _shape_ of things (tensor dimensions, internal data structures) rather than mathematical correctness
- Tests become insensitive to real bugs — they pass when convergence breaks, fail when refactoring is harmless
- You outrun your headlights, committing to test structure before understanding the numerics

**Correct approach**: Vertical slices via tracer bullets. One test → one implementation → repeat. Each test responds to what you learned from the previous cycle.

```
WRONG (horizontal):
  RED:   test1, test2, test3, test4, test5
  GREEN: impl1, impl2, impl3, impl4, impl5

RIGHT (vertical):
  RED→GREEN: test1→impl1
  RED→GREEN: test2→impl2
  RED→GREEN: test3→impl3
  ...
```

## Workflow

### 1. Planning

Before writing any code:

- [ ] Identify the research hypothesis or algorithm being implemented
- [ ] Locate the paper/proof/derivation that defines expected behavior
- [ ] Identify known benchmark results or analytical solutions to test against
- [ ] List the measurable correctness properties (convergence rate, error bounds, invariants)
- [ ] Check for domain glossary or notation conventions in the project
- [ ] Identify opportunities for [deep modules](deep-modules.md) (small interface, deep numerics)
- [ ] Design interfaces for [testability](interface-design.md)
- [ ] Confirm scope with user: which behaviors to test first

Ask: "What is the simplest case with a known answer? Which mathematical property matters most?"

**You can't test everything.** Confirm the most critical correctness property. Focus on the _one thing_ that would invalidate the result if wrong.

### 2. Tracer Bullet

Write ONE test that confirms ONE correctness property:

```
RED:   Write test for first property → test fails
GREEN: Write minimal code to pass → test passes
```

Research tracer bullets:

- 1 sample forward pass produces finite output
- 1 optimization step reduces loss
- 1D analytical solution matches within tolerance
- Fixed seed → deterministic output

This proves the pipeline works end-to-end with a verifiable oracle.

### 3. Incremental Loop

For each remaining behavior:

```
RED:   Write next test → fails
GREEN: Minimal code to pass → passes
```

Rules:

- One correctness property per test
- Only enough code to pass current test
- Don't anticipate future experiments
- Assert mathematical properties, not internal state

### 4. Refactor

After all tests pass, look for [refactor candidates](refactoring.md):

- [ ] Vectorize loops for numerical performance
- [ ] Cache intermediate quantities
- [ ] Extract reusable numerical utilities
- [ ] Structure for ablation (swap one component, keep others fixed)
- [ ] Run tests after each refactor step

**Never refactor while RED.** Get to GREEN first.

## Numerical Verification

Use [numerical-regression.md](numerical-regression.md) for:

- Relative/absolute tolerance (`rtol`/`atol`)
- Finite-ness checks (`np.isfinite`, `torch.isfinite`)
- Convergence order verification
- Golden file / snapshot regression
- Cross-platform floating-point tolerance

## Reproducibility

Use [reproducibility.md](reproducibility.md) for:

- Seed injection and random source isolation
- Deterministic test patterns
- Config/hyperparameter versioning
- Environment snapshots for regression

## Checklist Per Cycle

```
[ ] Test verifies a mathematical property, not implementation details
[ ] Test uses public algorithm interface only
[ ] Test would survive refactoring (vectorization, optimizer change, loop rewrite)
[ ] Assertions use appropriate numerical tolerance
[ ] Code is minimal for this test
[ ] No speculative features added
```
