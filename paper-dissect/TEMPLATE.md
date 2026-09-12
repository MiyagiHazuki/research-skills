# Output template (frozen)

Write TWO files: `paper-dissect/<slug>/dissect.zh.md` (every slot in Chinese) and `paper-dissect/<slug>/dissect.en.md` (every slot in English). Same heading structure, same content, one language per file. Never mix `中：`/`EN:` pairs inside a slot. The two files must not drift apart.

Do not add, delete, rename, or reorder headings. The Chinese block below is canonical; `dissect.en.md` uses the fixed English heading mapping in this file — do not improvise translations.

All math in KaTeX: inline `$...$`, display `$$...$$`, in both files. Plain-text pseudo formulas are forbidden. The section 7 mermaid is written per file in that file's language; node ids stay `S1`…`Sn`.

Primary type is not `其他` → zh `- 子类：无` / en `- Subclass: none`.

If section 7 does not fire, its body is exactly `未触发` (zh) / `Not triggered` (en).

Create `paper-dissect/<slug>/` if it does not exist. Do not write outside the work dir.

Replace `<标题>` with the paper title, kept in the original language in both files.

## Canonical Chinese template

```markdown
# 论文拆解 · <标题>
## 0. 读取
- 来源：PDF
- 读到了什么：
- 残缺页：
- 置信：正常 / 低
## 1. 初始化
### 缺口句
### 主卖对象
### 机制
### 主结果句
## 2. 类型
- 主类型：
- 子类：
- 备注：
## 3. 核心映射
- 一句话：在前提 P 下，把 X 变成 Y
- 输入 X：
- 输出 Y：
- 前提 P：
## 4. 问题为什么重要
- 声称的缺口：
- 谁会痛、痛在哪一步：
- 真实约束 / 包装动机：
## 5. 本质
## 6. 步骤拆解
### S1 <名称>
- 吃什么：
- 做什么：
- 吐什么、交给谁：
## 7. 可视化
未触发 / <图，节点编号与 S1…Sn 一致>
## 8. 对照
- 对照：一致 / 不一致（何处）
- 隐含输入：
```

## English heading mapping (for dissect.en.md)

| Chinese | English |
|---|---|
| `# 论文拆解 · <标题>` | `# Paper Dissect · <title>` |
| `## 0. 读取` | `## 0. Read` |
| `- 来源：PDF` | `- Source: PDF` |
| `- 读到了什么：` | `- What was read:` |
| `- 残缺页：` | `- Failed pages:` |
| `- 置信：正常 / 低` | `- Confidence: normal / low` |
| `## 1. 初始化` | `## 1. Init` |
| `### 缺口句` | `### Gap sentence` |
| `### 主卖对象` | `### Object of sale` |
| `### 机制` | `### Mechanism` |
| `### 主结果句` | `### Headline result` |
| `## 2. 类型` | `## 2. Type` |
| `- 主类型：` | `- Primary type:` |
| `- 子类：` | `- Subclass:` |
| `- 备注：` | `- Remarks:` |
| `## 3. 核心映射` | `## 3. Core map` |
| `- 一句话：在前提 P 下，把 X 变成 Y` | `- One sentence: under premise P, turn X into Y` |
| `- 输入 X：` | `- Input X:` |
| `- 输出 Y：` | `- Output Y:` |
| `- 前提 P：` | `- Premise P:` |
| `## 4. 问题为什么重要` | `## 4. Why the problem matters` |
| `- 声称的缺口：` | `- Claimed gap:` |
| `- 谁会痛、痛在哪一步：` | `- Who hurts, at which step:` |
| `- 真实约束 / 包装动机：` | `- Real constraint / packaging motive:` |
| `## 5. 本质` | `## 5. Essence` |
| `## 6. 步骤拆解` | `## 6. Step breakdown` |
| `### S1 <名称>` | `### S1 <name>` |
| `- 吃什么：` | `- Eats:` |
| `- 做什么：` | `- Does:` |
| `- 吐什么、交给谁：` | `- Emits, hands to:` |
| `## 7. 可视化` | `## 7. Visualization` |
| `## 8. 对照` | `## 8. Check` |
| `- 对照：一致 / 不一致（何处）` | `- Check: consistent / inconsistent (where)` |
| `- 隐含输入：` | `- Hidden inputs:` |

Fixed tokens: `原文不足` → `Source insufficient`; `未触发` → `Not triggered`; `一致`/`不一致` → `consistent`/`inconsistent`; `子类：无` → `Subclass: none`.

Repeat `### S2 <名称>` … as needed. Do not skip from S1 to S3. Do not name steps after chapter titles.
