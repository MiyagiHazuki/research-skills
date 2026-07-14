# When to Mock (Research)

Mock at **system boundaries** only:

- **Data loaders / datasets** — mock to provide fixed, known inputs
- **Pre-trained model weights** — mock to isolate your component from upstream
- **Random number generators** — mock to control stochasticity
- **Distributed communication** (DDP, MPI) — mock for single-device testing
- **I/O-heavy operations** (file reads, network) — rarely needed in unit tests

Don't mock:

- Your own model components
- Internal algorithm steps
- Anything you control the implementation of

## Research Mock Patterns

### 1. Mock data loaders with fixed tensors

```python
# GOOD: Provide known data, bypass file I/O
def test_model_trains_on_known_data():
    # Mock dataset returns fixed tensors
    x = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
    y = torch.tensor([0, 1])
    model = SimpleClassifier()
    batch_loss = train_one_batch(model, x, y)
    assert torch.isfinite(batch_loss)
```

### 2. Inject random sources (don't import them)

```python
# GOOD: Random source passed in, controllable by test
def monte_carlo_estimate(f, n_samples, rng=np.random.default_rng):
    samples = rng.uniform(-1, 1, n_samples)
    return f(samples).mean()

# Test with fixed seed
def test_mc_convergence():
    rng = np.random.default_rng(42)
    result = monte_carlo_estimate(np.sin, n_samples=10000, rng=rng)
    assert np.abs(result) < 0.1  # sin is odd on [-1,1]

# BAD: Hard-coded random source
def monte_carlo_estimate(f, n_samples):
    samples = np.random.uniform(-1, 1, n_samples)  # can't control
    return f(samples).mean()
```

### 3. Mock pre-trained components

```python
# GOOD: Replace heavy model with lightweight stub
def test_loss_computation():
    backbone = DummyEncoder(output_dim=128)  # returns fixed features
    head = MyHead(input_dim=128, output_dim=10)
    features = backbone(torch.randn(4, 3, 224, 224))
    logits = head(features)
    assert logits.shape == (4, 10)
    assert torch.all(torch.isfinite(logits))

# The DummyEncoder is a simple class you control:
class DummyEncoder(nn.Module):
    def __init__(self, output_dim):
        super().__init__()
        self.output_dim = output_dim
    def forward(self, x):
        return torch.zeros(x.shape[0], self.output_dim)
```

### 4. Mock distributed for single-device testing

```python
# GOOD: Test algorithm logic without distributed overhead
def test_all_reduce_implementation():
    # Replace all_reduce with identity for testing
    mock_reduce = lambda x, op: x
    result = my_sync_batch_norm(
        x, world_size=1, all_reduce=mock_reduce
    )
    # Verify the normalization formula, not the communication
    assert torch.allclose(result.mean(), torch.tensor(0.0), atol=1e-6)
    assert torch.allclose(result.std(), torch.tensor(1.0), atol=1e-6)
```

### 5. Smoke test: 1 sample, 1 step

Before mocking anything complex, ask: "Can I test this with 1 sample and 1 step?"

```python
# GOOD: Minimal end-to-end smoke test
def test_pipeline_smoke():
    model = MyModel()
    x = torch.randn(1, 3, 32, 32)  # smallest possible input
    y = model(x)
    assert torch.all(torch.isfinite(y))  # forward doesn't crash/NaN
    loss = y.sum()
    loss.backward()
    for p in model.parameters():
        assert p.grad is not None
        assert torch.all(torch.isfinite(p.grad))  # gradients are finite
```

## SDK-style for research APIs

Prefer narrow, single-purpose functions over generic dispatchers:

```python
# GOOD: Each function independently mockable
class ExperimentAPI:
    def load_checkpoint(self, path): ...
    def save_metrics(self, run_id, metrics): ...
    def log_artifact(self, run_id, name, data): ...

# BAD: Generic runner with conditional logic
class ExperimentAPI:
    def run(self, command, **kwargs):  # hard to mock specific operations
        if command == "load": ...
        elif command == "save": ...
```
