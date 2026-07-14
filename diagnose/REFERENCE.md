# Diagnose — Reference

> Full bug taxonomy, instrumentation cookbook, and anti-pattern catalog for
> general scientific computing. **All code is pseudocode** — translate to your
> language of choice (Python, R, MATLAB, Julia, C, Fortran, etc.).
> See SKILL.md for quick start and 6-phase workflow.

**Pseudocode conventions:**

| Notation | Meaning |
|---|---|
| `SHAPE(x)` | dimensions of x, e.g. `(100, 10)` |
| `MEAN(x, axis=rows)` | mean along specified axis (`axis=all` for global) |
| `SUM(x, axis=...)`, `STD(x)` | sum, standard deviation |
| `MAX(x)`, `MIN(x)` | extreme values |
| `RANDN(r, c)` | random normal array of shape `(r, c)` — seed your RNG first |
| `ISNAN(x)`, `ISINF(x)` | element-wise NaN/Inf check |
| `ANY(x)` | true if any element is true |
| `ALLCLOSE(a, b, tol=1e-6)` | approximate equality (relative + absolute tolerance) |
| `CLAMP(x, lo, hi)` | clip values to range |
| `LOG(x)`, `EXP(x)`, `SQRT(x)` | standard math functions |
| `ABS(x)` | absolute value |
| `ZEROS(shape)`, `ONES(shape)` | constant arrays |
| `ASSERT(condition)` | halt if false |
| `PRINT(...)` | output to console |
| `COPY(x)` | independent copy, not reference |

---

## Bug Taxonomy — Full Catalog

### 1. Dimension / Index Errors

**Why it's silent:** Wrong array dimensions don't always crash. Broadcasting, implicit
reshaping, or indexing errors produce output that "looks right" but has wrong shape
or silently drops/duplicates data.

```pseudocode
# WRONG AXIS IN AGGREGATION
data = RANDN(100, 10)                 # (samples, features)
means = MEAN(data, axis=columns)      # per-feature means. Correct.
means = MEAN(data, axis=all)          # single scalar. Probably wrong.
means = MEAN(data, axis=rows)         # per-sample means. Different intent.

# OFF-BY-ONE IN SLICING / LOOP BOUNDS
t = LINSPACE(0, 1, 100)
x = t[2:]                             # dropped the first element
# Paper says "for t from 0 to 1 with step 0.01" — need all points?
# Does algorithm start at t=0 or t=dt? Off-by-one changes semantics.

# BROADCAST SURPRISE
a = ONES(3, 1)                        # shape (3, 1)
b = ONES(4)                           # shape (4)
c = a + b                             # shape (3, 4) — intended or accidental?

# FORGOT TO PRESERVE DIMENSION
x = RANDN(8, 16, 16)
x_norm = x / MAX(x)                   # MAX over all axes → scalar → broadcast back
x_norm = x / MAX(x, axis=(cols,depth), keepdims=true)  # per-sample. Correct.

# WRONG RESHAPE ORDER
x = ARANGE(12).reshape(3, 4)          # layout depends on language
# Column-major (MATLAB/Julia/R) vs row-major (C/Python)
# Same call → different array in different languages!
```

**Diagnosis:** Insert `PRINT(SHAPE(x))` after every array transformation. For each
variable, know what each axis represents. Verify against paper/textbook.

---

### 2. Numerical Instability

**Why it's silent:** NaN propagates silently through computation. Inf looks like
"large value" until it gets divided. Catastrophic cancellation produces
wrong-but-plausible numbers. Affects ALL languages equally.

```pseudocode
# CATASTROPHIC CANCELLATION
# Computing variance naively: E[x²] - E[x]²
x = [1000000.1, 1000000.2, 1000000.3]
var_bad = MEAN(x^2) - MEAN(x)^2        # loses precision
var_good = STD(x)^2                    # uses stable algorithm internally

# LOG OF ZERO / NEGATIVE
p = [1e-300, 1e-300]                   # underflows to 0
log_p = LOG(p)                         # → -inf, propagates
log_p = LOG(CLAMP(p, 1e-300, inf))     # clamp before log

# DIVISION BY NEAR-ZERO
x = [1.0, 1e-200]
result = 1.0 / x                       # → [1.0, inf]
result = 1.0 / (x + 1e-300)            # stabilized

# EXP OVERFLOW
logits = [1000, 1000, 1000]            # EXP(1000) overflows!
shifted = logits - MAX(logits)         # subtract max before exp
probs = EXP(shifted) / SUM(EXP(shifted))

# FLOAT COMPARISON — NEVER USE ==
a = 0.1 + 0.2
ASSERT(a == 0.3)                       # FAILS in every language
ASSERT(ABS(a - 0.3) < 1e-10)           # correct

# SUMMATION ORDER MATTERS
x = ONES(10_000_000) * 1e-8
total = SUM(x)                         # may lose digits
# Use higher-precision accumulator if available
```

**Diagnosis:** After every major step: `ANY(ISNAN(x))`, `ANY(ISINF(x))`, `MIN(x)`, `MAX(x)`.
For precision issues: recompute in higher precision and compare.

---

### 3. Data Pipeline Errors

**Why it's silent:** Data looks right. Pipeline runs. But statistics are subtly wrong —
leakage between splits, wrong normalization, labels misaligned after shuffle.

```pseudocode
# TRAIN/TEST LEAKAGE VIA NORMALIZATION
data = LOAD_DATA()                      # all data
mean = MEAN(data, axis=all)             # ✗ computed over BOTH train and test
data = (data - mean) / STD(data, axis=all)
train, test = data[1:800], data[801:]   # test info leaked!

# Correct:
train_raw, test_raw = data[1:800], data[801:]
mean = MEAN(train_raw, axis=all)        # stats from train only
train = (train_raw - mean) / STD(train_raw)
test  = (test_raw  - mean) / STD(train_raw)  # apply SAME transform

# LABEL MISALIGNMENT AFTER SHUFFLE
data   = RANDN(1000, 10)
labels = ARANGE(1000)
idx    = SHUFFLE_INDICES(1000)          # random permutation
data_shuffled   = data[idx]
labels_shuffled = labels[idx]           # must shuffle BOTH identically
# Common silent bug: shuffling data but forgetting labels.

# MISSING VALUE PROPAGATION
x = [1.0, 2.0, NaN, 4.0]
avg = MEAN(x)                           # → NaN
avg = MEAN(x, skip_nan=true)            # → 2.333 — correct, but intentional?
```

**Diagnosis:** Disable all randomization. Run pipeline twice on same input. Output
must be identical. Val metrics consistently better than train → leakage.

---

### 4. Algorithm Implementation Errors

**Why it's silent:** Code compiles and runs. Output looks plausible. But implementation
doesn't match mathematical specification — wrong sign, missing term, wrong operation.

```pseudocode
# WRONG MATHEMATICAL OPERATION
# Textbook: ||x - y||² (squared Euclidean distance)
dist_bad = NORM(x - y)                  # forgot to square
dist_good = SUM((x - y) ^ 2)

# WRONG AGGREGATION: SUM VS MEAN
# Paper: "minimize expected loss" → MEAN, not SUM
loss = SUM(criterion(pred, target))     # scale depends on batch size
loss = MEAN(criterion(pred, target))    # scale-independent. Correct.

# MISSING NORMALIZATION CONSTANT
# Gaussian PDF: (1 / √(2πσ²)) · exp(-(x-μ)²/(2σ²))
pdf = EXP(-(x-mu)^2 / (2*sigma^2))                    # ✗ forgot constant
pdf = EXP(...) / SQRT(2 * PI * sigma^2)               # correct

# WRONG INDEXING: 1-BASED VS 0-BASED
# Paper: "for k = 1, ..., K"
for k = 0 to K-1:                       # k starts at 0 → wrong value
for k = 1 to K:                         # correct (verify your language!)

# EDGE CASE NOT HANDLED
function SAFE_DIVIDE(a, b):
    if b == 0: return 0                 # handle zero explicitly
    return a / b
```

**Diagnosis:** Implement the algorithm in a separate reference script, line-by-line
matching equations. Compare every intermediate value. First divergence = bug location.

---

### 5. Convergence / Iteration Failures

**Why it's silent:** Loop runs without crashing. But doesn't converge, converges to
wrong point, or exits too early/late. No built-in correctness check.

```pseudocode
# INFINITE LOOP (subtle)
x = 1.0
while ABS(x - target) > 1e-6:
    x = UPDATE(x)
    # UPDATE() never brings x within tolerance → infinite loop

# ALWAYS guard with max iterations:
for iter = 1 to MAX_ITER:
    if CONVERGED(): break
else:
    PRINT("WARNING: did not converge in ", MAX_ITER, " iterations")

# WRONG STOPPING CRITERION
# |x_new - x_old| < tol → stops when step size is small
# But oscillating algorithm takes large steps near solution → never stops
# Better: check BOTH |objective(x)| < tol AND |x_new - x_old| < tol

# WRONG STEP SIZE
x = x - 10.0 * gradient                # too large → diverges
x = x - 0.000001 * gradient            # too small → never converges

# STUCK AT WRONG FIXED POINT
x = 0.0                                # symmetric init → gradient zero → stuck
x = RANDN() * 0.01                     # break symmetry
```

**Diagnosis:** Print iteration count, objective value, and change magnitude every
few iterations. Plot convergence curve. Flat / noisy / oscillating → bug in update rule.

---

### 6. Reproducibility Failures

**Why it's silent:** Looks deterministic. Same code, same data. Results subtly differ
across runs. Tiny numerical differences compound in iterative algorithms.

```pseudocode
# NO SEED SET → different results every run
SET_RANDOM_SEED(42)                     # do this ONCE at script start

# PARALLELISM → different execution order → different float accumulation
# Multiple threads/processes: results differ by ~1e-15 per run
# This is NOT a bug, but document it. For exact repro: run single-threaded.

# HARDCODED PATHS → unreproducible on another machine
data = LOAD_FILE("/home/alice/project/data.csv")   # ✗
data = LOAD_FILE(PROJECT_ROOT + "/data.csv")        # ✓

# ENVIRONMENT DIFFERENCES
# Library versions, BLAS implementation, CPU → float results differ
# Document versions in your paper's reproducibility statement.

# INHERENTLY NON-DETERMINISTIC ALGORITHMS
# k-means, t-SNE, Monte Carlo → different results per run unless seeded
model = KMEANS(n_clusters=3, random_seed=42)  # pin the seed
```

**Diagnosis:** Fix all seeds. Run twice. `ALLCLOSE(run1, run2)`. Different → non-determinism.
Identical but wrong → bug elsewhere.

---

### 7. Metric / Evaluation Errors

**Why it's silent:** Numbers move in expected direction. But you're measuring wrong
thing or measuring it wrong. Conclusion is wrong even though trend looks correct.

```pseudocode
# WRONG FORMULA
y_true = [3.0, -0.5, 2.0, 7.0]
y_pred = [2.5,  0.0, 2.0, 8.0]
ss_res = SUM((y_true - y_pred) ^ 2)
ss_tot = SUM((y_true - MEAN(y_true)) ^ 2)
r2 = 1 - ss_res / ss_tot               # correct R²

# COMPARING INCOMPARABLES
# A tuned on test set vs B with defaults → A wins from leakage, not quality

# NOT REPORTING VARIANCE
# "Accuracy = 85.2%" → anecdotal
# "Accuracy = 85.2% ± 2.1% over 5 runs" → proper

# WRONG BASELINE
# "Our method: 80%" — random=50%, trivial heuristic=78% → 2% gap may be noise
```

**Diagnosis:** Compute metric by hand on one data point. Test on synthetic data with
known answer. Compare against standard library implementation.

---

### 8. Intent-Code Gap

**Why it's silent:** Hardest category. You *believe* code does X, it actually does Y.
No crash. Must question your own assumptions.

```pseudocode
# IN-PLACE VS COPY
a = [1, 2, 3]
b = a                                   # b IS a (reference), NOT a copy
b[1] = 99
PRINT(a)                                # [99, 2, 3] — surprise!
b = COPY(a)                             # independent copy

# VARIABLE SHADOWING
function COMPUTE(data):
    result = PREPROCESS(data)
    # ... 50 lines ...
    result = POSTPROCESS(result)        # overwrites — intentional?
    # Later code using `result` gets POSTPROCESSED value.
    # If you expected PREPROCESSED → bug.

# OPERATOR PRECEDENCE
cond = x > 0 AND x < 2                  # ambiguous! Use parentheses:
cond = (x > 0) AND (x < 2)

# MUTABLE DEFAULT STATE
function PROCESS(data, cache={}):       # ✗ cache persists across calls
    ...
function PROCESS(data, cache=null):     # ✓
    if cache is null: cache = {}

# UNIT / SCALE MISMATCH
# seconds vs ms, radians vs degrees, Hz vs normalized freq
# → plausible numbers at wrong scale, no crash.

# FUNCTION MUTATES CALLER'S DATA
function NORMALIZE(arr):
    arr = arr / SUM(arr)                # modifies original!
    return arr
# Caller's array now changed unexpectedly.
# Fix: work on COPY inside function.
```

**Diagnosis:** Read code line by line, articulating what EACH line *actually does* per
the language spec. Not what you intend — what the interpreter actually executes.

---

## Phase 1 Detail — Feedback Loop Methods

### Method 1: Minimal Test Case

Smallest possible input where you can hand-compute expected output.

```pseudocode
function TEST_MINIMAL():
    x = [[1.0, 2.0],
         [3.0, 4.0]]                    # 2×2 — can compute by hand

    # Hand-computed expected output:
    # Algorithm: normalize each row to unit norm
    # Row 1: [1,2] → norm = √5 → [1/√5, 2/√5] ≈ [0.4472, 0.8944]
    # Row 2: [3,4] → norm = 5  → [0.6, 0.8]
    expected = [[0.4472136, 0.8944272],
                [0.6,       0.8      ]]

    result = MY_ALGORITHM(x)
    ASSERT(ALLCLOSE(result, expected, tol=1e-6))
    PRINT("Minimal test: PASSED")
```

- Fails on minimal input → bug in core logic
- Passes minimal, fails on real data → bug in data pipeline or scaling
- NaN on minimal input → numerical bug (Category 2)

### Method 4: Reference Baseline

Implement formula one-to-one with paper. No optimizations, no vectorization.

```pseudocode
function REFERENCE(x):
    # Paper Eq. (3): y_i = Σ_j w_ij · x_j / (ε + Σ_k |x_k|)
    n, d = SHAPE(x)
    y = ZEROS(n, d)
    for i = 1 to n:
        denom = 1e-8
        for k = 1 to d:
            denom = denom + ABS(x[i][k])     # Σ_k |x_k|
        for j = 1 to d:
            w = COMPUTE_WEIGHT(i, j)
            y[i][j] = w * x[i][j] / denom    # Eq. (3) exactly
    return y

# Compare
test_input = RANDN(10, 5)
optimized = MY_OPTIMIZED(test_input)
reference = REFERENCE(test_input)
diff = MAX(ABS(optimized - reference))
PRINT("Max difference: ", diff)             # must be near zero
```

### Method 6: Ground Truth Test

```pseudocode
function TEST_GROUND_TRUTH():
    # Identity matrix → algorithm should extract diagonal
    x = [[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]]
    ASSERT(ALLCLOSE(MY_ALGORITHM(x), [1,1,1,1]))
    PRINT("Identity test: PASSED")

    # All zeros → output should be all zeros
    x = ZEROS(3, 3)
    ASSERT(ALLCLOSE(MY_ALGORITHM(x), ZEROS(3)))
    PRINT("Zero test: PASSED")

    # Degenerate case: single element
    x = [[5.0]]
    expected = [...]                       # hand-compute
    ASSERT(ALLCLOSE(MY_ALGORITHM(x), expected))
    PRINT("Single-element test: PASSED")
```

---

## Instrumentation Cookbook

### Value Ranges at Boundaries

Insert after every major computation step. Anomalies in min/max/NaN/zero-fraction
jump out immediately.

```pseudocode
function CHECK(name, x):
    PRINT("[DEBUG-", name, "] ",
          "shape=", SHAPE(x), " ",
          "min=", MIN(x), " max=", MAX(x), " ",
          "mean=", MEAN(x, axis=all), " std=", STD(x), " ",
          "has_nan=", ANY(ISNAN(x)), " has_inf=", ANY(ISINF(x)), " ",
          "zero_frac=", COUNT(x == 0) / COUNT(x))

# Usage: insert throughout computation
x = PREPROCESS(raw_data);   CHECK("after_preprocess", x)
y = CORE_ALGORITHM(x);      CHECK("after_algorithm", y)
z = POSTPROCESS(y);         CHECK("final", z)
```

### Sensitivity Check

Correct algorithms respond proportionally to small input changes.

```pseudocode
function SENSITIVITY(fn, x, eps=1e-5):
    y1, y2 = fn(x), fn(x + eps)
    rel = MAX(ABS(y2 - y1)) / (eps + MAX(ABS(y1)))
    if rel == 0:
        PRINT("WARNING: output does NOT respond to input — dead code?")
    else if rel > 100:
        PRINT("WARNING: output hypersensitive (", rel, "x)")
    else:
        PRINT("OK: sensitivity = ", rel)
```

### Term-by-Term Inspection

```pseudocode
# DON'T: result = term1 + term2 + term3 (opaque)
# DO: inspect each term
t1 = COMPUTE_TERM1(x); CHECK("term1", t1)
t2 = COMPUTE_TERM2(x); CHECK("term2", t2)
t3 = COMPUTE_TERM3(x); CHECK("term3", t3)
result = t1 + t2 + t3

# NaN term → bug there. Wrong sign → sign error.
# Wrong magnitude → scaling error. One term dwarfs others → others ignored.
```

### State Tracking (Iterative Algorithms)

```pseudocode
function TRACK(name, before, after):
    diff = MAX(ABS(after - before))
    frac = COUNT(before != after) / COUNT(before)
    PRINT("[DEBUG] ", name, ": max_change=", diff, " frac_changed=", frac)
    if diff == 0:     PRINT("  WARNING: no change — stuck?")
    if diff > 1000:   PRINT("  WARNING: massive change — diverging?")

# Usage:
for iter = 1 to MAX_ITER:
    old_state = COPY(state)
    state = UPDATE(state)
    TRACK("state", old_state, state)
```

---

## Non-Deterministic Bugs

1. **Seed lockdown.** Set every RNG. Document the seed.
2. **Eliminate parallelism.** Single-threaded only for debugging.
3. **Run twice, diff.** Save intermediates from two runs. Find first divergence point.
4. **Higher precision baseline.** Float32 non-det, float64 det → precision threshold.
5. **Bisect commits.** If results changed between versions.
6. **Document inherent non-determinism.** k-means, t-SNE, Monte Carlo → report mean ± std.

---

## Common Research Anti-Patterns

| Anti-Pattern | Why It Breaks | Fix |
|---|---|---|
| No shape/dimension assertion | Silent broadcast, wrong axis | `ASSERT(SHAPE(x) == (N,D))` after transforms |
| Aggregation without axis | Ambiguous scope | Always explicit about dimensions |
| Variable reuse in long functions | Shadowing, wrong reference | Unique names per version |
| Hardcoded file paths | Unreproducible | Config file, project-relative paths |
| No random seed | Different results every run | Seeds in first 5 lines |
| No convergence check | Infinite loop or premature stop | Max iter + tolerance + plot |
| Copy-pasting formula from paper | Notation ≠ semantics | Understand, then implement |
| `==` on floats | `0.1 + 0.2 != 0.3` | `ABS(a - b) < tolerance` |
| Assuming sorted input | Order-dependent algorithms | Sort explicitly or assert |
| No NaN check | NaN propagates silently | Check after every major step |
| Function mutates caller's data | Unexpected side effects | Work on COPY inside function |
| Silent integer division | `3/2 = 1` in some languages | `3.0 / 2.0` or cast to float |

---

## Language Translation Notes

When translating pseudocode to your language:

### Indexing

| Language | First element |
|---|---|
| Python, C, C++, Rust, Java | 0 |
| R, MATLAB, Julia, Fortran, Lua | 1 |
| Mathematical papers | 1 |

**Rule:** When paper says "for k = 1 to K", check whether your language needs `0..K-1`.
Getting this wrong produces subtly wrong results, not crashes.

### Memory layout

- **Row-major** (C, Python/NumPy): rows contiguous, `reshape` fills rows first
- **Column-major** (MATLAB, Julia, Fortran, R): columns contiguous, `reshape` fills columns first
- Same `reshape(1:12, [3,4])` → different array in different languages

### Division

- Python 3, R, MATLAB, Julia: `3 / 2 = 1.5` (float)
- Python 2, C (int), Java (int): `3 / 2 = 1` (integer truncation)
- **Prefer explicit float:** `3.0 / 2.0`

### Assignment (reference vs copy)

- **Reference** (Python, Java objects): `b = a` → same data, mutating `b` mutates `a`
- **Copy** (R, MATLAB arrays, C structs): `b = a` → independent copy
- **When in doubt:** `b = COPY(a)`
