---
name: caveman-thinking
description: >
  Compresses internal thinking/reasoning into ultra-dense telegraphic
  caveman language while preserving logical rigor. Does not compress
  user-visible output — output compression requires loading caveman
  separately (stackable; this file never copies output rules). Use when
  user says "caveman thinking", "caveman-thinking", "cave mode",
  "cave-mode", "thought compression", or invokes /caveman-thinking.
---

# Caveman Thinking

## Core Principle

**Thinking is a computation graph for yourself, not a report for the user.** Grammar exists for readers; you have no reader here.

## Division

This skill = **thinking only**. Output stays normal unless `caveman` is also loaded. If `caveman` is loaded, follow that skill for output. Never duplicate output rules here.

## Persistence

ACTIVE EVERY RESPONSE once triggered. Every subsequent thinking/reasoning block stays compressed until off.

## On / Off

Case-insensitive. **Longest phrase wins** — do not also fire a shorter phrase contained in a longer match (`use caveman thinking` is not `use caveman`; `stop caveman-thinking` is not `stop caveman`). Treat `caveman thinking` and `caveman-thinking` as the same phrase.

On: `caveman thinking` | `caveman-thinking` | `cave mode` | `cave-mode` | `thought compression` | `/caveman-thinking`

Off this layer: `stop caveman-thinking`

Off both layers: `stop less token` | `stop less tokens` | `normal mode`

If **only this layer** is on, any off phrase (`stop caveman`, `stop caveman-thinking`, `stop less token(s)`, `normal mode`) closes it (nearest layer). If **both layers** are on: `stop caveman-thinking` closes thinking only; `stop caveman` leaves this layer on.

## Thinking Compression Rules

Apply to ALL thinking/reasoning content.

### 1. Drop Linguistic Scaffolding
Strip articles (a, an, the), auxiliary verbs (is, are, was, were, be, been), filler ("let me", "I think", "we should", "it seems that").

**Before:** "I think we should check if the user is authenticated before proceeding."
**After:** "check auth → proceed"

### 2. Symbol Substitution
- `→` causality/sequence ("therefore", "then", "leads to", "next") or assignment/mapping
- `?` questions ("should we", "is it", "do we need")
- `✓` / `✗` confirmation/negation
- `≈` approximation/similarity
- `≠` contradiction/difference
- `↑` / `↓` increase/decrease

### 3. Fragment Chains
No complete sentences required. Noun-verb cores in sequence. Drop subjects when context is clear.

**Before:** "First, I need to find where the authentication middleware is defined. Then I should trace how it's applied to the routes. After that, I can determine if the bug is in the middleware itself or in how it's configured."
**After:** "find auth middleware → trace route application → bug: middleware vs config"

### 4. Ban Meta-Commentary
Never write about the thinking process. Just think. Eliminate: "Let me analyze this...", "Hmm, that's interesting...", "Based on the above...", "Now I understand...", "Wait, actually...", "To summarize..."

### 5. Direct Variable/Value References
**Before:** "The variable `userCount` currently has a value of 5, and after incrementing it, it will be 6."
**After:** "userCount: 5 → 6"

**Before:** "The function returns null when the input is invalid, which causes a TypeError downstream."
**After:** "f(bad_input)→null → TypeError"

### 6. Indentation Over Enumeration
**Before:**
```
1. Check auth token validity
2. If valid: proceed to handler
3. If invalid: return 401
```

**After:**
```
check auth token
  valid → handler
  invalid → 401
```

## Scope Boundary
- **Affected**: internal thinking/reasoning only
- **Not affected**: tool calls, code generation, file writes, user-visible output
- **Interaction**: if `caveman` is loaded, output follows that skill

## Quality Gate
Compressed thinking MUST still:

- Capture all logical steps (no skipping reasoning)
- Preserve decision branches and alternatives considered
- Maintain variable values and state transitions
- Be parseable by you when you need to reference it later

**Bad compression**: "fix bug" (too vague, lost reasoning)
**Good compression**: "null check missing @ L42 → add guard → test edge case"

Thinking-phase before/after: [EXAMPLES.md](EXAMPLES.md).
