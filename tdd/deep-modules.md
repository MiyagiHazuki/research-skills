# Deep Modules

From "A Philosophy of Software Design":

**Deep module** = small interface + lots of implementation

```
┌─────────────────────┐
│   Small Interface   │  ← Few methods, simple params
├─────────────────────┤
│                     │
│                     │
│  Deep Implementation│  ← Complex logic hidden
│                     │
│                     │
└─────────────────────┘
```

**Shallow module** = large interface + little implementation (avoid)

```
┌─────────────────────────────────┐
│       Large Interface           │  ← Many methods, complex params
├─────────────────────────────────┤
│  Thin Implementation            │  ← Just passes through
└─────────────────────────────────┘
```

## Research Deep Modules

### Solver

```
┌──────────────────────────┐
│  solver.step(state)       │  ← One method, one state arg
├──────────────────────────┤
│  - Time integration       │
│  - Boundary conditions    │
│  - Flux computation       │
│  - Stability checks       │
│  - Adaptive timestep      │
└──────────────────────────┘
```

Test: `solver.step(state0)` produces correct state1. Implementation can use any integration scheme.

### Model Forward

```
┌──────────────────────────┐
│  model(x) → dict          │  ← One call, tensor in, dict out
├──────────────────────────┤
│  - Architecture layers    │
│  - Normalization          │
│  - Dropout (training)     │
│  - Attention mechanism    │
│  - Residual connections   │
└──────────────────────────┘
```

Test: `model(x)` returns finite outputs. Internals (attention, residual) hidden from test.

### Data Loader

```
┌──────────────────────────┐
│  loader[i] → (x, y)       │  ← Indexing interface
├──────────────────────────┤
│  - File I/O               │
│  - Preprocessing/augment│
│  - Shuffling              │
│  - Batching               │
│  - Normalization          │
└──────────────────────────┘
```

Test: `loader[i]` returns valid, finite (x, y) pair. File handling, transforms hidden.

### Optimization Loop

```
┌──────────────────────────┐
│  trainer.step(batch)      │  ← One method
├──────────────────────────┤
│  - Forward pass           │
│  - Loss computation       │
│  - Backpropagation        │
│  - Gradient clipping      │
│  - Parameter update       │
│  - LR schedule            │
└──────────────────────────┘
```

Test: `trainer.step(batch)` reduces loss. How it reduces is hidden.

## Design Questions

When designing research modules, ask:

- Can I reduce the interface to one primary method (`step`, `forward`, `__getitem__`)?
- Can I replace 5 config parameters with 1 config dataclass?
- Can I hide the iteration/loop behind the interface?
- Can I hide the discretization/implementation choice behind the interface?
