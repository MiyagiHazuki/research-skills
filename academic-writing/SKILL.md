---
name: academic-writing
description: Rewrites academic text (English or Chinese) into clear, concise, readable prose by limiting dashes, removing unnecessary hyphens, replacing inflated vocabulary with common precise words, and splitting long sentences, while preserving meaning, technical terms, data, and citations. Use when the user asks to polish, simplify, or improve the readability of academic writing (papers, abstracts, reports, theses), or to reduce dashes, hyphens, difficult words, or long complex sentences.
---

# Academic Writing

## Goal

Rewrite academic text to be clear, concise, and easy to read, without changing the meaning or losing academic accuracy.

Priority when rules conflict: **preserve meaning > keep precision > improve clarity > shorten text.**

Four targets:

1. Fewer dashes; sentences should flow without constant interruption.
2. Fewer unnecessary hyphens; no stacked hyphenated compounds.
3. Common, precise words; no inflated or obscure vocabulary.
4. Shorter sentences; prefer simple and compound sentences over long nested ones, unless the logic requires them.

## Core rules

### 1. Dashes

- Keep at most one dash construction per paragraph; a paired dash counts as one construction. Prefer none.
- This rule covers the em dash (`—`) and the Chinese dash (`——`).
- Identify each dash's function, then replace:
  - Parenthetical remark → commas, parentheses, or a separate sentence.
  - Explanation → colon or a new sentence.
  - Contrast → contrast connector or a new sentence.
  - List introduction → colon.
- A dash used for emphasis → full stop; the emphasized point becomes its own sentence.
- Never change en dashes (`–`) in numeric ranges or minus signs in math.

### 2. Hyphens

- Replace a hyphenated compound when a single common word carries the same meaning.
- Keep hyphenated compounds that are standard technical terms or fixed collocations.
- Rewrite any chain of three or more hyphenated words.
- Replace and keep lists: [REFERENCE.md](REFERENCE.md).

### 3. Word choice

- Prefer common words that stay precise; avoid rare, padded, and nominalized phrasing.
- Keep the original word when the common alternative shifts meaning or weakens precision.
- Substitution tables for each language: [REFERENCE.md](REFERENCE.md).

### 4. Sentence structure

- Prefer subject–verb–object; one core idea per sentence.
- Length limits: English, at most 20 words on average and 25 per sentence; Chinese, at most 30 characters on average and 40 per sentence.
- At most one subordinate clause per sentence; split nested clauses.
- Convert clefts (`It is ... that ...`) into direct statements; convert `There is/are ...` into active voice.
- When splitting, keep logical relations explicit with connectors suited to the text's language.
- Clause triggers and connector lists for each language: [REFERENCE.md](REFERENCE.md).

## Workflow

1. Read the full text; mark every dash, hyphenated compound, inflated word, and overlong sentence.
2. For each mark, decide: replace, keep (fixed term or necessary complexity), or rewrite.
3. Rewrite in order: dashes and hyphens, then vocabulary, then long sentences.
4. Verify: meaning unchanged; no lost logic, data, citations, or technical terms; academic register intact.
5. Output the rewrite plus a brief change log.

## Output format

```
Rewritten text:
<full rewritten text>

Changes:
- Dashes: N replaced, listing the replacement for each.
- Hyphens: N replaced or rewritten, listed.
- Vocabulary: N replacements, listed as original → new pairs.
- Sentences: N long sentences split; M reordered.
- Kept: terms or long sentences kept, with reasons.
```

Write the change log in the same language as the rewritten text.

## Boundaries

- Never change technical terms, numbers, data, citations, or the author's intent.
- Keep a long sentence only when its logic requires it; note the reason in the change log.
- No colloquialisms; keep the formal academic tone and objectivity.
- If the input contains LaTeX, code, or identifiers, leave them untouched.

## Examples

Worked examples, one per language: [EXAMPLES.md](EXAMPLES.md).
