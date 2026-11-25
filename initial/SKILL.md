---
name: initial
description: Creates or updates a repository's AGENTS.md from verified commands, architecture boundaries, code conventions, and existing instruction files. Use when the user asks to initialize, generate, refresh, or consolidate AGENTS.md or repository agent instructions.
---

# initial

Create or update `AGENTS.md` for future coding agents entering this repository.

**Core filter:** Before adding any line, ask: *"Without this, where would an agent likely fail or waste time?"* If there is no concrete answer, omit it.

## 1. Gather Evidence

1. **Confirm target:** Default to `<repo-root>/AGENTS.md` unless the user specifies a subdirectory. If the current working directory is not a project and no path is given, ask for the path first. Note any specific areas the user wants audited.
2. **Read existing instructions:** Check the target `AGENTS.md` (if present), plus `CLAUDE.md`, `.cursor/rules/`, `.cursorrules`, `.github/copilot-instructions.md`, and `opencode.json` (`instructions` field). Note any scoped or nested `AGENTS.md` files.
3. **Inspect ground-truth configs:** Check manifests (`package.json`, `pyproject.toml`, `Cargo.toml`, `Makefile`, etc.), lockfiles, workspace configs, task runners, and CI workflows. Trace commands to their actual execution point—verify working directories, argument forwarding, and prerequisites.
4. **Sample code minimally:** Only when configs leave ambiguity, read a few representative files (entry points, one implementation + its test) to confirm real conventions. Never elevate a one-off pattern into a global rule.

## 2. What to Include

- **Commands (High Priority):** Exact build, lint, format, typecheck, and test commands. **Prioritize how to run a single test file or test case** using a real path from the repo (if the runner only supports package/suite granularity, state the smallest verifiable scope). Include working directories or prerequisites only when they affect execution.
- **Architecture & Gotchas:** Non-obvious constraints that change how work is done—module dependency boundaries, codegen/schema rebuild steps, or tests requiring local services. Use actionable triggers: *"When changing X, run Y in Z."*
- **Conventions:** Record project-specific decisions (naming, error handling, import patterns) that tools do not enforce. For anything handled by formatters, linters, or typecheckers, provide the check command instead of listing style rules.
- **Progressive Disclosure:** If detailed docs exist (e.g., `docs/architecture.md`, `docs/api.md`), do not copy them. Add a brief pointer stating **when** an agent should read them.
- **Consolidating Existing Rules:** Deduplicate overlapping rules while preserving scope. Keep subdirectory rules local and link to them from the root file if helpful.
  - *Command conflicts:* Resolve against actual scripts and CI.
  - *Policy conflicts:* If two active team rules contradict each other, preserve both and flag the discrepancy to the user.

## 3. Strict Constraints (What to Exclude)

- **Length budget:** Keep the file concise (target under 150 lines; small repos need far fewer). If approaching the limit, cut redundancy and link to dedicated docs.
- **No generic advice:** Never include standard software engineering platitudes (e.g., *"write clean code"*, *"add unit tests"*, *"handle errors properly"*).
- **No full directory trees:** Agents can inspect files themselves. Mention only key entry points or non-obvious layouts.
- **No unverified claims:** Never invent or guess commands, flags, or file paths.

## 4. Write, Verify, and Report

1. **Respect existing files:** When updating an existing `AGENTS.md`, preserve its language and accurate sections; modify only what is outdated or missing. For new files, match the user's requested language or the repo's documentation language. Skip empty sections.
2. **Verify safely:** Double-check all commands, paths, test names, and links. Run lightweight, read-only/no-side-effect checks if the environment allows. **Never** run migrations, deployments, or spin up external services just to document them.
3. **Final diff & report:** Edit only the target `AGENTS.md` (leave it untouched if already accurate). Report:
   - File path and key changes made.
   - Which key commands were **actually executed** vs. **verified from config/CI**.
   - Any blocking ambiguities or rule conflicts that could not be resolved from the repo (batch into a single concise list).