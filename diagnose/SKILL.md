---
name: diagnose
description: >
  Disciplined diagnosis loop for research code bugs — dimension/index errors,
  numerical instability, iteration/convergence failures, algorithm implementation
  errors, and intent-code gaps. Reproduce → hypothesise → instrument → fix
  → regression-test. Use when user says "diagnose this" / "debug this",
  reports a bug, algorithm not converging, NaN/Inf values, results don't match
  paper/textbook, array dimension mismatch, or code behavior doesn't match intent.
---

# Diagnose (Research)

Research bugs are silent. Code runs, no crash — but results are wrong, algorithm
doesn't converge, numbers don't match the reference. **The bug is a gap between
what you think the code does and what it actually computes.**

Full taxonomy + instrumentation cookbook: [REFERENCE.md](REFERENCE.md).

## Bug Taxonomy (Quick Reference)

| # | Category | Telltale | First Check |
|---|---|---|---|
| 1 | **Dimension / Index** | Wrong array shape, off-by-one, broadcast surprise | `print(.shape)` / `size()` at boundaries |
| 2 | **Numerical Instability** | NaN/Inf, catastrophic cancellation, precision loss | Min/max after first few operations |
| 3 | **Data Pipeline** | Statistics differ between splits, unreproducible runs | Disable shuffle, inspect raw values |
| 4 | **Algorithm Error** | Formula→code translation wrong, missing edge case | Compare against reference implementation |
| 5 | **Convergence / Iteration** | Infinite loop, stuck, wrong stopping criterion | Print iteration count + objective value |
| 6 | **Reproducibility** | Same code+data ≠ same results | Fix all RNG seeds, pin environment |
| 7 | **Metric / Evaluation** | Good intermediate numbers, wrong conclusion | Verify formula by hand on one sample |
| 8 | **Intent-Code Gap** | Code "should do X" but silently does Y | In-place vs copy? Condition scope right? Operator precedence? |

## Phase 1 — Build a Feedback Loop

Try in order. **Don't proceed to Phase 2 without a working loop.**

1. **Minimal test case.** Smallest possible input (1-2 elements). Verify output by hand.
2. **Numerical sanity.** Assert no NaN/Inf. Print min/max/mean at key computation points.
3. **Component isolation.** Test each function independently with known input/output pairs.
4. **Reference baseline.** Run textbook/paper formula in pure math (numpy, Wolfram, hand calc). Compare.
5. **Ablation.** Remove/replace one component. Bug persists → elsewhere. Vanishes → located.
6. **Ground truth test.** Feed input with hand-computed expected output. Diff exactly.
7. **Deterministic run.** Fix all seeds. Pin OS-level state. Must be bitwise reproducible.

See [REFERENCE.md](REFERENCE.md#phase-1-detail) for code patterns.

## Phase 2 — Reproduce

Run loop. Confirm failure matches user's description. Wrong bug = wrong fix.

## Phase 3 — Hypothesise

Generate **3–5 ranked, falsifiable hypotheses.** Use bug taxonomy (above) as checklist.
Format: `If <category #N> is cause, then <intervention> → <prediction>.`

Show ranked list to user before testing. They often know which category.

## Phase 4 — Instrument

One variable at a time. General toolkit (see [REFERENCE.md](REFERENCE.md#instrumentation-cookbook)):

- **Value ranges at boundaries:** min, max, mean, std after key operations
- **Sensitivity check:** change input slightly → output changes correctly?
- **Term-by-term inspection:** print intermediate values, not just final result
- **Distribution shape:** are values clustering at unexpected points (e.g., all zeros)?
- **State tracking:** which variables actually changed vs. should have changed?

Tag every probe `[DEBUG-xxx]`. grep-cleanable.

## Phase 5 — Fix + Regression Test

Write regression test **before fix** — if correct seam exists:
- Test on minimal input with known output
- Assert value ranges AND exact values where possible, not just "no crash"

No correct seam → document gap. That's a finding about architecture.

## Phase 6 — Cleanup + Post-Mortem

- [ ] Original repro fixed
- [ ] Regression test passes (or seam gap documented)
- [ ] All `[DEBUG-xxx]` removed
- [ ] Correct hypothesis stated in commit message
- [ ] Ask: what architectural change prevents this class of bug?
