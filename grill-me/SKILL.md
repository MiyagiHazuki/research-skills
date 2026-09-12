---
name: grill-me
description: >
  Interview the user relentlessly about a plan or design until reaching
  shared understanding, resolving each branch of the decision tree.
  Use when user wants to stress-test a plan, get grilled on their design,
  or mentions "grill me".
---

Interview me relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one.

## Language

Do not hardcode a grilling language. The skill body (this file) stays in English for the model. All user-facing text must follow the language decided below.

Before any user-facing narration or questions, run this workflow:

1. **Detect** from the initiating user message that started this grilling (including slash-command arguments). Ignore system/skill-injected instruction text. Score only natural-language intent sentences. Do not count file paths, code, identifiers, or quoted original text.

2. **Decide** — only Chinese and English are supported grilling outputs:
   - If intent sentences contain Chinese characters → Chinese. Script follows the prompt (Simplified vs Traditional). Mixed script → majority; tie → session Locale's zh script (`zh-CN` → Simplified, `zh-TW`/`zh-HK` → Traditional, else Simplified).
   - Else if intent is clearly English → English.
   - Else detection failure → session Locale: `zh-CN` → Simplified Chinese, `zh-TW`/`zh-HK` → Traditional Chinese, `en*` → English, any other locale → English.

   This skill does not promise grilling in Japanese, Korean, or other languages. Non-Chinese/English prompts are detection failures and follow Locale above. Do not add special cases for them.

3. **Lock** the decided language for the rest of the session.

4. **Switch** only by behavior, never by verbal command. If two consecutive user messages have a free-text body whose dominant language is the other supported language (Chinese ↔ English), switch and re-lock. Option clicks, code, paths, and messages with no free-text body do not count as a round. Do not parse commands like "ask in English" / 「用英文问」 as a switch.

5. **Localize** every user-facing field into the current grilling language: `question`, `header`, option `label` and `description`, narration, and the recommended marker (Chinese: 「推荐」; English: `(Recommended)`). Keep code, paths, identifiers, and terms with no established translation in their original form.

## Process

1. **Explore first** — If any question can be answered by exploring the codebase, do that first to narrow down what actually needs asking.

2. **Batch all questions into a single `question` tool call** — Collect EVERY unresolved question about the plan/design upfront. For each question:
   - Put your recommended answer as the first option, labelled with the recommended marker in the current grilling language (「推荐」 or `(Recommended)`).
   - Provide alternative answers as additional options.
   - Keep `header` under 30 chars.
   - Use `multiple: true` where multiple answers may apply.

   Do NOT ask questions one at a time. Batch everything into one call.

3. **Iterate** — Once the user responds, incorporate their answers and proceed to the next branch of the decision tree. Repeat steps 1-2 as needed, always batching all pending questions into a single `question` call per round.
