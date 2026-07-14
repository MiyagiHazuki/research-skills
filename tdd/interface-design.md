# Interface Design for Research Code Testability

Good interfaces make testing natural. Research code has different interface patterns than production services.

## 1. Accept dependencies, don't create them

```python
# Testable — config / components passed in
class Solver:
    def __init__(self, discretization, linear_solver):
        self.discretization = discretization
        self.linear_solver = linear_solver

# Hard to test — hard-coded dependencies
class Solver:
    def __init__(self):
        self.discretization = FiniteDifference(n=512, scheme="upwind")
        self.linear_solver = ConjugateGradient(tol=1e-8)
```

## 2. Return results, don't mutate in place

```python
# Testable — pure function, returns result
def compute_gradient(f, x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2 * h)

# Hard to test — mutates external state, no return
def compute_gradient(f, x, result_array, h=1e-6):
    result_array[:] = (f(x + h) - f(x - h)) / (2 * h)
```

## 3. Model forward as the public interface

```python
# Testable — forward() returns dict with all relevant outputs
class MyModel(nn.Module):
    def forward(self, x):
        h = self.encoder(x)
        logits = self.head(h)
        return {"logits": logits, "features": h, "loss": loss}

# Hard to test — side effects, scattered state
class MyModel(nn.Module):
    def forward(self, x):
        h = self.encoder(x)
        self.last_features = h       # hidden side-effect
        self.head.train_on(h, y)     # trains during forward!
        return self.head.predict(h)
```

## 4. Configuration as injected object, not global

```python
# Testable — config passed explicitly
def run_experiment(config: ExperimentConfig):
    model = build_model(config.model)
    data = load_data(config.data)
    return train(model, data, config.training)

# Hard to test — reads globals, env vars, argparse
def run_experiment():
    model = build_model()           # reads from global CONFIG
    data = load_data(DATA_PATH)     # reads env var
    return train(model, data)       # uses argparse namespace
```

## 5. Small surface area per module

- Solver: `solve()` or `step()` — one entry point
- Model: `forward()` — one method, returns dict
- Data pipeline: `__getitem__` + `__len__` — PyTorch convention
- Loss function: one callable `loss(pred, target) → scalar`

## 6. Arrays in, arrays out

```python
# Testable — ndarray/tensor boundaries are clean
def solve_linear_system(A: np.ndarray, b: np.ndarray) -> np.ndarray:
    ...

# Hard to test — file paths, side channels
def solve_linear_system(matrix_path: str, rhs_path: str, out_path: str):
    ...
```

## Research Interface Checklist

```
[ ] Dependencies injected via constructor or arguments, not imported internally
[ ] Functions return values (no in-place mutation of inputs)
[ ] Model forward returns all needed outputs in a dict
[ ] Config passed as object, not read from globals/env
[ ] ndarray/tensor as I/O boundaries (not file paths in leaf functions)
[ ] Small surface: one primary method per module
```
