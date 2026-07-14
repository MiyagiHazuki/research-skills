# Reproducibility Testing

Research results must be reproducible. TDD provides the guardrails.

## Seed Management

### Inject seeds, don't hardcode

```python
# GOOD: seed passed as parameter
def initialize_model(model_cls, seed: int):
    torch.manual_seed(seed)
    return model_cls()

# Test: same seed → same weights
def test_deterministic_init():
    m1 = initialize_model(MLP, seed=42)
    m2 = initialize_model(MLP, seed=42)
    for p1, p2 in zip(m1.parameters(), m2.parameters()):
        assert torch.equal(p1, p2)

# BAD: hardcoded global seed
def initialize_model(model_cls):
    torch.manual_seed(42)  # always same seed, untestable
    return model_cls()
```

### Isolate random sources

```python
# GOOD: Each stochastic component gets its own generator
def monte_carlo(func, n_samples, rng):
    samples = rng.uniform(0, 1, n_samples)
    return func(samples).mean()

# GOOD: PyTorch — seed per call
def train_step(model, batch, seed_for_dropout=None):
    if seed_for_dropout is not None:
        torch.manual_seed(seed_for_dropout)
    return model(batch)

# BAD: All randomness shares global state
def monte_carlo(func, n_samples):
    samples = np.random.uniform(0, 1, n_samples)  # global state
    return func(samples).mean()
```

## Deterministic Tests

### Verify determinism

```python
def test_forward_deterministic():
    """Same model + same input + same seed → same output."""
    model = MyModel()
    model.eval()
    x = torch.randn(4, 3, 32, 32)

    torch.manual_seed(123)
    out1 = model(x)

    torch.manual_seed(123)
    out2 = model(x)

    assert torch.allclose(out1, out2)
```

### Enable deterministic algorithms (PyTorch)

```python
# For deterministic CUDA ops (slower but reproducible)
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False

# Use in test setup
@pytest.fixture(autouse=True)
def deterministic_mode():
    was_deterministic = torch.backends.cudnn.deterministic
    was_benchmark = torch.backends.cudnn.benchmark
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
    yield
    torch.backends.cudnn.deterministic = was_deterministic
    torch.backends.cudnn.benchmark = was_benchmark
```

## Config & Environment Versioning

### Snapshot hyperparameters

```python
from dataclasses import dataclass, asdict
import json

@dataclass
class ExperimentConfig:
    model: ModelConfig
    training: TrainingConfig
    data: DataConfig

    def hash(self) -> str:
        """Deterministic hash of config for version tracking."""
        raw = json.dumps(asdict(self), sort_keys=True)
        return hashlib.sha256(raw.encode()).hexdigest()[:8]

# Test: same config → same hash
def test_config_deterministic():
    c1 = ExperimentConfig(model=..., training=..., data=...)
    c2 = ExperimentConfig(model=..., training=..., data=...)
    assert c1.hash() == c2.hash()
```

### Environment snapshot for regression tests

```python
def test_environment_snapshot():
    """Record key versions; test warns (not fails) on mismatch."""
    import sys, torch, numpy

    snap = {
        "python": sys.version.split()[0],
        "torch": torch.__version__,
        "numpy": numpy.__version__,
    }
    # Compare against committed snapshot
    # assert snap == expected_snap  # only if strict reproducibility needed
    # More commonly: warn on mismatch, fail only on known incompatibilities
```

## Common Pitfalls

| Pitfall | Fix |
|---|---|
| `np.random.seed()` in function body | Inject RNG as parameter |
| `torch.manual_seed(0)` hardcoded | Pass seed from config |
| Forgetting to set model to `eval()` | `model.eval()` in test fixture |
| DataLoader `shuffle=True` without seed | `torch.Generator().manual_seed(seed)` |
| GPU non-determinism | `torch.backends.cudnn.deterministic = True` |
| `random` module mixed with `np.random` | Use one RNG source, inject it |
| `time.time()` as seed | Use fixed seed in tests, only vary in experiments |

## Checklist

```
[ ] All randomness goes through injectable generators (not global state)
[ ] Fixed-seed deterministic test proves reproducibility
[ ] Config hashable for version tracking
[ ] cudnn deterministic mode enabled in test suite
[ ] model.eval() called before deterministic forward check
[ ] DataLoader uses seeded generator
[ ] Golden files (numerical-regression.md) paired with environment snapshot
```
