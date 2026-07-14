# Caveman Thinking — Before/After Examples

Each example shows the same reasoning task done conventionally (verbose) vs compressed (caveman-thinking).

---

## Example 1: Debugging a Null Reference Error

**Context**: User reports `TypeError: Cannot read properties of null` at `src/api/users.ts:42`.

### Verbose (Before)

```
Let me think about this error. The user is seeing a TypeError
at src/api/users.ts line 42. This typically means we're trying
to access a property on something that is null or undefined.

I should look at the code around line 42 to understand what's
happening. The error message says "Cannot read properties of
null", so we're dealing with a null value, not undefined.

Now, what could cause this? There are several possibilities:
1. A database query returning null instead of a user object
2. An async operation that hasn't resolved yet
3. A conditional path where we don't handle the null case

Let me trace the data flow. The function at line 42 is probably
trying to access something like user.email or user.role. If
the user variable is null at that point, we need to add a null
check before accessing properties.

I should check: where is the user variable assigned? Is there
a guard clause earlier that might not cover all cases?
```

### Compressed (After)

```
TypeError L42: null.property access

trace user var assignment
  DB query → null? (no result)
  async race? (not awaited)
  missing guard? (conditional gap)

check L42 context → likely user.email or user.role
find user assignment point → verify null paths covered
fix: add null guard OR fix upstream to never return null
```

**Token reduction**: ~70%

---

## Example 2: Architecture Decision

**Context**: Choosing between REST API vs GraphQL for a new microservice.

### Verbose (Before)

```
Okay, I need to decide between REST and GraphQL for this
new microservice. Let me think about the tradeoffs.

REST is simpler to implement and has better caching support
out of the box. It's also more familiar to the team, which
means less onboarding time. However, REST can lead to
over-fetching and under-fetching if the client needs specific
combinations of fields.

GraphQL, on the other hand, gives the client precise control
over what data it receives. This is great for mobile clients
with bandwidth constraints. But it adds complexity on the
server side — we'd need to implement resolvers, handle N+1
queries, and set up proper authorization at the field level.

Given that our current use case is a simple CRUD service
with a single client type, and the team has strong REST
experience, I think REST is the better choice here. We can
always migrate later if the client data requirements become
more complex.
```

### Compressed (After)

```
REST vs GraphQL — new ms

REST: simple, cache, team knows it, over/under-fetch risk
GraphQL: precise, mobile-friendly, server complexity↑

this use case: simple CRUD, 1 client, team=REST expert
→ REST fits. migrate later if data reqs grow.

decision: REST ✓
```

**Token reduction**: ~75%

---

## Example 3: Mathematical Reasoning

**Context**: Working through why a gradient descent step diverges.

### Verbose (Before)

```
Let me analyze why the gradient descent is diverging.
The loss function is L(w) = (1/2) * ||Xw - y||^2 + λ * ||w||^2.

The gradient is ∇L = X^T(Xw - y) + 2λw.

With our current learning rate α = 0.1 and λ = 0.01, let me
check if the step size is too large. The Lipschitz constant
of the gradient is approximately ||X^T X|| + 2λ. If α > 2/L,
then gradient descent will diverge.

Let me compute L. X is a 1000×50 matrix, so X^T X is 50×50.
The spectral norm ||X^T X|| is approximately the largest
singular value squared. If the data isn't normalized, this
could be very large, making L large and requiring a smaller
learning rate.

I should check: is the data normalized? If not, the effective
learning rate might be too high, causing the divergence.
```

### Compressed (After)

```
GD diverging — why?

L(w) = ½||Xw-y||² + λ||w||²
∇L = Xᵀ(Xw-y) + 2λw

α=0.1, λ=0.01
Lipschitz L ≈ ||XᵀX|| + 2λ
divergence if α > 2/L

X: 1000×50 → XᵀX: 50×50
data not normalized? → ||XᵀX|| huge → L huge → α too big
fix: normalize X OR reduce α

root cause: unnormalized features → effective α too large
```

**Token reduction**: ~65%

---

## Example 4: Code Exploration / Multi-File Search

**Context**: Finding where authentication logic is implemented to add a new role.

### Verbose (Before)

```
I need to find where the authentication and role-checking
logic lives in this codebase. Let me think about where to
look. The project structure seems to have an src/ directory
with subdirectories for middleware, routes, and services.

The authentication logic is probably in the middleware
directory, since auth checks typically happen as middleware
before route handlers. But there might also be a separate
auth service that handles token generation and validation.

Let me search for patterns like "authenticate", "authorize",
"role", "jwt", and "token" across the codebase. I should
also check the route files to see how middleware is applied.

Once I find the auth middleware, I'll need to understand:
1. How roles are defined (enum, string, database?)
2. How role checks are performed (middleware chain?)
3. Where to add the new "editor" role
```

### Compressed (After)

```
find auth + role logic → add "editor" role

likely locations:
  src/middleware/auth* → auth checks
  src/services/auth* → token gen/validation
  src/routes/ → middleware application

search: "authenticate", "authorize", "role", "jwt", "token"

once found → check:
  role def: enum? string? DB table?
  role check: middleware? decorator? inline?
  add point: role list + permission mapping
```

**Token reduction**: ~60%

---

## Example 5: Test Failure Diagnosis

**Context**: Test `should return 404 for deleted user` fails with 500 instead.

### Verbose (Before)

```
The test expects a 404 status code when requesting a deleted
user, but it's getting a 500 instead. This is interesting —
a 500 means an unhandled server error, not a missing resource.

Let me think about what could cause this. The flow should be:
1. Request comes in for user ID 123
2. Database query finds the user is soft-deleted
3. The controller checks the deleted flag
4. Returns 404 if deleted

But instead, step 3 or 4 is throwing an exception. The most
likely cause is that the controller is trying to access a
property on the user object that doesn't exist for deleted
users. For example, if it tries to format user.email but
the deleted user record has email set to null.

I should check the controller code for property access
on the user object without null checks. Also check if the
error handler middleware is catching this correctly —
if it's returning 500, the error might not be properly
classified as a 404.
```

### Compressed (After)

```
test: GET /users/123 → expect 404, got 500

expected flow: request → DB(soft-deleted) → check flag → 404
actual: step 3/4 throws exception

likely: property access on null field
  deleted user → user.email=null → format crashes
  OR: deleted flag check itself throws (null ref)

check: controller property access, null guards
check: error handler — 500 vs 404 classification
fix: null-guard property access OR early return for deleted
```

**Token reduction**: ~65%
