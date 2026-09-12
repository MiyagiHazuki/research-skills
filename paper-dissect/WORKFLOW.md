# Workflow 0→8

Fill [TEMPLATE.md](TEMPLATE.md) as you go. Do not emit until section 8 has been checked against section 3.

Writing rules that gate the emit:

- **KaTeX everywhere.** Any formula, norm, fraction, or multi-symbol expression is written in KaTeX (`$...$` inline, `$$...$$` display), in both files. Plain-text pseudo formulas are forbidden.
- **academic-writing pass before saving.** After the section-8 check, load the `academic-writing` skill (via the skill tool) and tighten every slot with its craft: concrete nouns, no filler, no overclaim, no restating one fact across sections. Each file is a full template — keep slots telegraphic, do not pad.
- **Two files, zero drift.** `dissect.zh.md` and `dissect.en.md` must hold the same facts, same page ids, same S1…Sn ids. Translate; never summarize one version differently from the other.

Write only inside the workspace. After section 8, create `paper-dissect/<slug>/` under the workspace root (mkdir if needed) and save TWO files: `paper-dissect/<slug>/dissect.zh.md` (Chinese) and `paper-dissect/<slug>/dissect.en.md` (English). Never create files outside the work dir.

Template headings stay frozen. `dissect.zh.md` uses the Chinese headings; `dissect.en.md` uses the English headings given in parentheses below (full mapping in TEMPLATE.md). One language per file; the two files carry the same content.

## 0. Read (`读取`)

- Extract the PDF with MCP. Keep page numbers (printed page if visible, else PDF index).
- List pages that failed.
- Unspecified chapters → full paper. Named chapters → those only.
- If you only got the abstract or key method pages, set confidence (`置信`) to `低`.
- Do not fill later sections from title-memory or training data.

## 1. Init (`初始化`) — strip fluff, keep the sell

Throw away domain background, historical recap, related-work survey, acknowledgements, future work.

- **Introduction:** keep only the 1–2 sentences that name the research gap, with page or section id.
- **Related Work:** keep one sentence only if the authors explicitly draw a boundary with prior work.
- **Appendix:** skip unless the core logic is unreadable without it.

**Core sell** = the one contribution title and abstract keep repeating. Several contributions → keep that one; mention the rest in remarks (`备注`).

You must produce four things:

- **Gap sentence** (`缺口句`) ≤2 sentences, with page or section id
- **Object of sale** (`主卖对象`) = the paper's name for it + what it actually is (method, theorem, protocol, dataset, …)
- **Mechanism** (`机制`) = the key steps / parts / propositions from input to output
- **Headline result** (`主结果句`) ≤2 sentences, kept for section 8

Special cases:

- Survey → the related-work map **is** the sell. Do not delete it.
- Dataset / benchmark → collection protocol, annotation rules, and eval definition are the mechanism.

Cannot name the object of sale → stop and ask the user.

## 2. Type (`类型`)

Pick **one** primary type by what it **sells**, not by whether it has formulas or experiments:

`理论` (theory) / `工程` (engineering) / `实证` (empirical) / `其他` (other)

`其他` **requires** a subclass, exactly one of:

- 综述 (survey)
- 数据集/基准 (dataset/benchmark)
- 立场/展望 (position/outlook)
- 复现/再分析 (reproduction/reanalysis)
- 应用/案例 (application/case)
- 还是无法归类 (still unclassifiable)

Primary type is not `其他` → subclass (`子类`) write `无`.

Secondary flavour goes in remarks, e.g. `主类型工程，但带了实证验证` (primary type engineering, with empirical verification).

## 3. Core map (`核心映射`)

One sentence, aimed at the core sell:

**Under premise P, turn X into Y.**

- **X:** the actual raw input
- **Y:** the actual product
- **P:** assumptions, environment limits, information that is unavailable

Training tricks, optimizers, and scaffolding are not Y unless that **is** the sell.

No method nicknames. The sentence must still parse after the nickname is stripped.

## 4. Why the problem matters (`问题为什么重要`)

Use the gap sentence from section 1. Do not bring back the background you deleted.

- What gap do the authors claim?
- Who hurts, at which step?
- Is this a real constraint, or a packaging motive for publication?

## 5. Essence (`本质`)

One vernacular sentence: core logic + motive. **No method nicknames.**

## 6. Step breakdown (`步骤拆解`) — module dataflow, not chapter order

Decompose the **inside** of the core sell. Do **not** follow section 1, section 2, or chapter titles.

Default grain: modules (encoder, retriever, controller, loss, decoder, …). Not pseudocode lines, unless the user asked to drill one step.

Each step is exactly three lines:

- **Eats** (`吃什么`)
- **Does** (`做什么`) — plain language; still readable without jargon; any equation here is KaTeX
- **Emits, hands to** (`吐什么、交给谁`)

Number them `S1` … `Sn`. Same ids in section 7.

Do not put comparison experiments or tuning into steps. Exception: primary type is `实证` **and** the experiment **is** the sell → the experimental procedure may be steps.

Missing module in the text → that step's fields are `原文不足`.

## 7. Visualization (`可视化`)

Draw if **any** trigger holds; otherwise write `未触发`:

- steps ≥ 3
- multiple parts, branches, loops, or train vs inference are two pipelines
- empirical treatment / control / metric are easy to mix up
- a main theorem depends on several lemmas

Fewest figures. Prefer dataflow / pipeline. Add an I/O box only when the contract must be visible. Empirical: `sample → treatment/control → measure`.

Node ids **must** be `S1`…`Sn`. Mermaid `flowchart LR` or `flowchart TD`. Data movement only. No slogans. No related-work maps.

## 8. Check (`对照`)

Compare section 1 headline result with section 3:

- Is abstract-Y the same object as produced-Y?
- Any input the method cannot run without that was left out of X (pretrained weights, human labels, oracle, simulator, …)?
- Is P an unspoken default the authors treat as given?

Mismatch → **rewrite section 3**. Do not emit two conflicting stories.

This section contains only:

- Check: `一致` (consistent) / `不一致` (inconsistent, where)
- Hidden inputs (`隐含输入`): list, or empty
