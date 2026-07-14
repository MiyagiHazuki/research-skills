# Good and Bad Research Tests

## Good Tests

**Behavior-verifying**: Test what the algorithm/method _should produce_.

### Numerical correctness against known solution

```python
# GOOD: Tests mathematical correctness
def test_poisson_solver_matches_analytical():
    """1D Poisson -u'' = f with u(0)=u(1)=0, f=1 → u(x)=x(1-x)/2."""
    solver = PoissonSolver1D(n=64)
    u = solver.solve(f=lambda x: 1.0, bc=(0.0, 0.0))
    x = solver.grid
    u_exact = 0.5 * x * (1 - x)
    assert np.allclose(u, u_exact, rtol=1e-6, atol=1e-8)
```

### Convergence verification

```python
# GOOD: Error decreases with resolution
def test_convergence_rate():
    """Error should scale as O(h^2) for second-order method."""
    errors = []
    for n in [16, 32, 64, 128]:
        solver = PoissonSolver1D(n=n)
        u = solver.solve(f=lambda x: 1.0, bc=(0.0, 0.0))
        error = np.max(np.abs(u - exact(solver.grid)))
        errors.append(error)
    rates = np.log2(np.array(errors[:-1]) / np.array(errors[1:]))
    assert np.all(rates > 1.8)  # approximately second order
```

### Loss decreases (smoke test)

```python
# GOOD: One optimization step reduces loss
def test_training_step_reduces_loss():
    model = LinearModel(d_in=10, d_out=1)
    x = torch.randn(32, 10)
    y = torch.randn(32, 1)
    loss_before = F.mse_loss(model(x), y).item()
    optim = SGD(model.parameters(), lr=0.01)
    optim.zero_grad()
    loss = F.mse_loss(model(x), y)
    loss.backward()
    optim.step()
    loss_after = F.mse_loss(model(x), y).item()
    assert loss_after < loss_before
```

### Reproducibility

```python
# GOOD: Same seed → same output
def test_deterministic_output():
    torch.manual_seed(42)
    out1 = initialize_weights(LinearModel(d_in=10, d_out=1))
    torch.manual_seed(42)
    out2 = initialize_weights(LinearModel(d_in=10, d_out=1))
    assert torch.allclose(out1, out2)
```

Characteristics:

- Tests a scientific claim or mathematical property
- Uses public algorithm/model interface
- Survives implementation refactors (loop → vectorized, optimizer swap)
- Uses appropriate numerical tolerance, not exact equality
- One correctness property per test

## Bad Tests

**Implementation-coupled**: Break when internals change but correctness stays.

```python
# BAD: Tests internal tensor shape, not correctness
def test_forward_output_shape():
    model = Transformer(d_model=512, n_heads=8, n_layers=6)
    x = torch.randn(16, 64, 512)
    out = model(x)
    assert out.shape == (16, 64, 512)  # shape not the correctness contract

# GOOD: Tests that attention preserves the right properties
def test_attention_normalization():
    model = Transformer(d_model=512, n_heads=8, n_layers=6)
    x = torch.randn(16, 64, 512)
    out = model(x)
    assert torch.all(torch.isfinite(out))  # correctness property
```

```python
# BAD: Asserts exact loss value (fragile across hardware, optimizers)
def test_loss_exact():
    model = MLP()
    loss = F.mse_loss(model(x), y)
    assert loss.item() == 2.347  # floats are never exact

# GOOD: Asserts loss is finite and decreases
def test_loss_is_finite():
    model = MLP()
    loss = F.mse_loss(model(x), y)
    assert torch.isfinite(loss)
```

```python
# BAD: Tests optimizer internal state
def test_optimizer_internals():
    optim = Adam(model.parameters())
    optim.step()
    assert optim.state[list(model.parameters())[0]]["exp_avg"].sum() > 0
    # breaks if you switch from Adam to SGD

# GOOD: Test that optimization achieves the goal
def test_optimization_converges():
    model = LinearModel()
    loss_history = train(model, x, y, steps=100)
    assert loss_history[-1] < loss_history[0] * 0.5
```

```python
# BAD: Tests implementation detail of data loading
def test_dataloader_internal():
    loader = DataLoader(dataset, batch_size=32, shuffle=True)
    batch = next(iter(loader))
    assert len(batch) == 32  # batch size not a correctness guarantee

# GOOD: Test that data pipeline produces valid values
def test_data_range():
    loader = DataLoader(dataset, batch_size=256)
    x, y = next(iter(loader))
    assert torch.all(torch.isfinite(x))
    assert torch.all(torch.isfinite(y))
    assert y.min() >= 0 and y.max() <= num_classes - 1
```

Red flags:

- Asserting on tensor shapes instead of values
- Exact float equality assertions
- Testing optimizer internal state
- Testing data loader batch counts
- Test breaks when you vectorize, swap optimizer, or restructure
- Test name describes HOW not WHAT
