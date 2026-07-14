---
name: caveman-thinking
description: Compresses BOTH the model's internal thinking/reasoning phase AND final output into ultra-dense, telegraphic caveman language — stripping linguistic redundancy while preserving logical rigor. Use when user requests "caveman thinking", "cave mode", "精简思考", "节省token", or "thought compression". Covers both thinking and output in one load. Safe to stack with caveman skill (output rules merge, no conflict) for maximum compression.
---

# Caveman Thinking

## Core Principle

**Thinking is a computation graph for yourself, not a report for the user.**

The thinking/reasoning phase exists to compute the right answer. Every word that doesn't contribute to that computation is waste. Drop all linguistic scaffolding — grammar exists for readers; you have no reader here.

## Activation

Load this skill when the user says any of:
- "caveman thinking" / "caveman-thinking"
- "cave mode" / "cave-mode"
- "精简思考" / "节省token" / "压缩思考"
- "thought compression"
- Explicit request to reduce thinking verbosity

This skill covers BOTH thinking and output. Loading it alone = full caveman mode. Stacking with `caveman` still works — output rules merge without conflict.

## Thinking Compression Rules

Apply these rules to ALL thinking/reasoning content.

### 1. Drop Linguistic Scaffolding
Strip articles (a, an, the), auxiliary verbs (is, are, was, were, be, been), filler phrases ("let me", "I think", "we should", "it seems that").

**Before:** "I think we should check if the user is authenticated before proceeding."
**After:** "check auth → proceed"

### 2. Symbol Substitution
Replace connective words with compact symbols:
- `→` for causality/sequence ("therefore", "then", "leads to", "next")
- `?` for questions ("should we", "is it", "do we need")
- `✓` / `✗` for confirmation/negation
- `≈` for approximation/similarity
- `≠` for contradiction/difference
- `↑` / `↓` for increase/decrease
- `→` for assignment or mapping

### 3. Fragment Chains
No complete sentences required. Use noun-verb cores in sequence. Drop subjects when context is clear.

**Before:** "First, I need to find where the authentication middleware is defined. Then I should trace how it's applied to the routes. After that, I can determine if the bug is in the middleware itself or in how it's configured."
**After:** "find auth middleware → trace route application → bug: middleware vs config"

### 4. Ban Meta-Commentary
Never write about your thinking process. Just do the thinking. Eliminate:
- "Let me analyze this..."
- "Hmm, that's interesting..."
- "Based on the above..."
- "Now I understand..."
- "Wait, actually..."
- "To summarize..."

These are for the user. You are not the user.

### 5. Direct Variable/Value References
Use mathematical notation for values. Name variables directly.

**Before:** "The variable `userCount` currently has a value of 5, and after incrementing it, it will be 6."
**After:** "userCount: 5 → 6"

**Before:** "The function returns null when the input is invalid, which causes a TypeError downstream."
**After:** "f(bad_input)→null → TypeError"

### 6. Indentation Over Enumeration
Use indentation for hierarchy, not numbered lists. Save tokens on list markers.

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

## Output Compression Rules

Apply these rules to ALL final output to the user. ACTIVE EVERY RESPONSE once triggered. No revert after many turns.

### Output Rules
Drop: articles (a/an/the), filler (just/really/basically/actually/simply), pleasantries (sure/certainly/of course/happy to), hedging. Fragments OK. Short synonyms (big not extensive, fix not "implement a solution for"). Abbreviate common terms (DB/auth/config/req/res/fn/impl). Strip conjunctions. Use arrows for causality (X -> Y). One word when one word enough.

Technical terms stay exact. Code blocks unchanged. Errors quoted exact.

Pattern: `[thing] [action] [reason]. [next step].`

Not: "Sure! I'd be happy to help you with that. The issue you're experiencing is likely caused by..."
Yes: "Bug in auth middleware. Token expiry check use `<` not `<=`. Fix:"

### Auto-Clarity Exception
Drop caveman output temporarily for: security warnings, irreversible action confirmations, multi-step sequences where fragment order risks misread, user asks to clarify or repeats question. Resume caveman after clear part done.

## Scope Boundary

- **Affected**: The internal thinking/reasoning phase AND final output to user
- **Not affected**: Tool calls, code generation, file writes
- **Interaction with caveman skill**: If both loaded, output compression rules merge (no conflict). caveman-thinking already covers both phases — loading `caveman` on top is optional/harmless.

## Quality Gate

Compressed thinking MUST still:
- Capture all logical steps (no skipping reasoning)
- Preserve decision branches and alternatives considered
- Maintain variable values and state transitions
- Be parseable by you when you need to reference it later

**Bad compression**: "fix bug" (too vague, lost reasoning)
**Good compression**: "null check missing @ L42 → add guard → test edge case"

See [EXAMPLES.md](EXAMPLES.md) for detailed before/after comparisons across multiple task types.
