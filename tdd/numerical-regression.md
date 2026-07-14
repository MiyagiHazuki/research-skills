# Numerical Regression Testing

Research code correctness hinges on _acceptable numerical error_, not exact equality. Use these patterns to write robust assertions.

## Core Concepts

### Relative vs Absolute Tolerance

```python
# np.allclose(a, b, rtol=1e-5, atol=1e-8)
# satisfied when: |a - b| <= atol + rtol * |b|

# For values near zero, absolute tolerance dominates
assert np.allclose(result, 0.0, atol=1e-12)

# For large values, relative tolerance dominates
assert np.allclose(result, 1e6, rtol=1e-7)
```

### Guidelines

| Scenario | rtol | atol | Why |
|---|---|---|---|
| Unit tests, clean inputs | 1e-7 | 1e-12 | Tight tolerance when no noise |
| Single-precision (float32) | 1e-4 | 1e-6 | FP32 has ~7 decimal digits |
| Iterative solver output | 1e-5 | 1e-8 | Accumulated roundoff |
| Gradient-based optimization | 1e-3 | 1e-6 | Stochastic + approx gradients |
| Cross-platform (CPU vs GPU) | 1e-4 | 1e-6 | Different reduction orders |
| Monte Carlo (stochastic) | — | — | Use statistical tests instead |

## Common Assertions

### Finite-ness

```python
# After any numerical operation, check for NaN/Inf
assert np.all(np.isfinite(result)), "result contains NaN or Inf"
assert torch.all(torch.isfinite(tensor)), "tensor contains NaN or Inf"
```

### Monotonicity

```python
# Loss should decrease over training
losses = [step["loss"] for step in history]
assert all(losses[i] >= losses[i+1] for i in range(len(losses)-1)), \
    "loss not monotonically decreasing"
```

### Conservation / Invariant

```python
# Mass conservation in PDE solver
initial_mass = np.sum(u0)
final_mass = np.sum(u_final)
assert np.abs(final_mass - initial_mass) / np.abs(initial_mass) < 1e-10, \
    "mass not conserved"
```

### Convergence Order

```python
def test_convergence_order():
    """Error ~ O(h^p). Doubling resolution → error drops by factor 2^p."""
    errors = []
    for n in [16, 32, 64, 128]:
        sol = solve(n=n)
        errors.append(compute_error(sol))

    # Rate p ≈ log2(error_n / error_2n)
    rates = [np.log2(errors[i] / errors[i+1]) for i in range(len(errors)-1)]
    expected_order = 2.0
    assert all(r > expected_order * 0.9 for r in rates), \
        f"expected order {expected_order}, got {rates}"
```

### Bounds

```python
# Probability outputs must be in [0, 1]
assert torch.all((probs >= 0) & (probs <= 1))

# Distance must be non-negative
assert torch.all(distances >= 0)
```

## Golden File / Snapshot Regression

When exact inputs → exact outputs must be preserved across changes:

```python
# Save golden reference (run once, commit to repo)
def generate_golden():
    result = expensive_computation()
    np.savez("tests/golden/result.npz", output=result)

# Test against golden
def test_matches_golden():
    golden = np.load("tests/golden/result.npz")["output"]
    result = expensive_computation()
    assert np.allclose(result, golden, rtol=1e-7, atol=1e-12)
```

**Golden file rules**:
- Commit `.npz` to git (small arrays only — <1MB)
- Use `.gitattributes` to store as LFS for larger files
- Regenerate when algorithm intentionally changed
- Document which commit produced the golden

## Cross-Platform Tolerance

CPU vs GPU results will differ due to:
- Different reduction order (non-associative floating-point)
- Different math library implementations
- FMA (fused multiply-add) availability

```python
# GPU results may differ from CPU — relax tolerance
assert torch.allclose(gpu_result, cpu_result, rtol=1e-4, atol=1e-6), \
    "GPU and CPU results differ beyond cross-platform tolerance"
```

## Checklist

```
[ ] Tolerance chosen for precision regime (fp32/fp64), not default
[ ] NaN/Inf checked after every numerical operation
[ ] Monotonicity asserted for loss curves
[ ] Conservation laws verified for PDE/integral methods
[ ] Convergence order matches theoretical expectation
[ ] Bounds checked for probability/normalized outputs
[ ] Golden files small enough to commit
[ ] Cross-platform tolerance documented where needed
```
