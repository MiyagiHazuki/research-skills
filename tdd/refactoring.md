# Research Refactor Candidates

After TDD cycle, look for:

## Software Engineering

- **Duplication** → Extract function/class
- **Long methods** → Break into named subroutines (keep tests on public interface)
- **Shallow modules** → Combine or deepen
- **Feature envy** → Move logic to where data lives
- **Primitive obsession** → Introduce value objects (e.g., `Grid`, `Mesh`, `StepSize`)

## Numerical Quality

- **Mixed precision hotspots** → Check where float32/float64 interact, ensure controlled casting
- **Cancellation-prone expressions** → `sqrt(x+1) - sqrt(x)` → `1/(sqrt(x+1)+sqrt(x))`
- **Summation order** → `sum()` → `math.fsum` for large arrays, or Kahan summation
- **Softmax/log-sum-exp** → Use numerically stable `log_softmax` over raw `softmax` then `log`
- **Condition number awareness** → Check matrices before `solve()`; add `rcond` or SVD fallback

## Performance & Vectorization

- **Loop over batch dimension** → Vectorize: replace Python `for` with NumPy/PyTorch broadcast
- **Repeated allocation** → Pre-allocate buffers, reuse in loop
- **Recomputed intermediates** → Cache: compute once, not per iteration
- **GPU/CPU transfer inside loop** → Move `.cuda()` / `.cpu()` outside
- **Eager gradient computation** → Use `torch.no_grad()` for eval-only code

## Experiment Architecture

- **Ablation separability** → Can you swap one component (loss, optimizer, architecture) without touching others?
- **Config sprawl** → Centralize hyperparameters into a dataclass; one source of truth
- **Metric computation mixed with training** → Extract metric logging into separate callbacks
- **Hard-coded paths** → Extract to config or pathlib-based project root
- **Notebook cell order dependency** → Extract functions so cells are idempotent when re-run

## Checklist

```
[ ] Numerical expressions checked for cancellation / instability
[ ] Loops vectorized where data size allows
[ ] Intermediate quantities cached to avoid recomputation
[ ] Components independently swappable for ablation
[ ] Config centralized (no scattered magic numbers)
[ ] All tests pass after each refactor step
```
