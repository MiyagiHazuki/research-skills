---
name: handoff
description: Compact the current conversation into a minimal handoff block for a fresh agent. Strips temporary tool outputs, keeps core code and decisions, condenses history. Use when user wants to continue work in a new session or hand off to another agent.
argument-hint: "What will the next session focus on?"
---

# Handoff (Research Compaction)

```
[Conversation history + tool outputs]
    │
    ▼  /handoff [focus]
[Filter & Prune] ── strip temporary tool outputs, keep core code snippets & system rules
    │
    ▼  (LLM summarise)
[Generate Compaction Block] ── condense history into structured block
    │
    ▼
[Free token space]
```

## Filter Rules

**Strip:** tool output longer than 5 lines unless it contains an error, file listing noise, re-reads of unchanged files, exploration dead ends, repeated content.

**Keep:** core code snippets, error messages, decisions made, system rules, seed values, config paths, user preferences, experiment results.

## Compaction Block Structure

```markdown
# Hypothesis / Goal
# Decisions Made & Why
# Key Code / Config (inline only what's essential; reference files by path)
# Results So Far
# Failed Attempts & Lessons
# Reproducibility (seeds, env versions, data paths, checkpoint paths)
# User Preferences (style, don't-do, conventions)
# Next Steps (ranked, with suggested skills)
```

## Rules

- Reference external artifacts by path — never duplicate their content.
- If user passed arguments, use them as the focus description.
- Suggest which skills to load in the next session.
