# Sisyphus Skills

[OpenCode](https://github.com/OhMyOpenCode/opencode) 自定义 Agent 技能集。每个技能为特定任务提供专业指令和工作流程。

通过 `skill(name="技能名")` 加载技能，或在 task 调用中使用 `load_skills=[...]`。

---

## 技能索引

| # | 技能 | 领域 | 描述 | 触发词 (EN) | 触发词 (ZH) |
|---|---|---|---|---|---|
| 1 | `archive` | 代码库整理 | 将凌乱的研究项目转化为整洁、文档齐全、可复现的开源仓库。五阶段流程：侦察 → 文档化 → 清理 → 重构 → 验证。 | "archive this repo", "prepare for release", "standardize project structure", "paper repo", `/archive` | "整理项目", "整理成论文仓库", "论文开源" |
| 2 | `caveman` | 通信压缩 | 超压缩输出模式。去除填充词、冠词、客套话，保持完整技术准确性，token 用量降低约 75%。 | "caveman mode", "talk like caveman", "less tokens", "be brief", `/caveman` | — |
| 3 | `caveman-thinking` | 通信压缩 | 同时压缩内部思考/推理和最终输出，使用电报式精简语言。一次加载覆盖两个阶段，可与 `caveman` 安全叠加。 | "caveman thinking", "cave mode", "thought compression", `/caveman-thinking` | "精简思考", "节省token", "压缩思考" |
| 4 | `diagnose` | 调试诊断 | 研究代码 bug 的规范诊断循环：维度/索引错误、数值不稳定、收敛失败、算法实现错误、意图-代码差距。复现 → 假设 → 插桩 → 修复 → 回归测试。 | "diagnose this", "debug this", "algorithm not converging", "NaN/Inf values", "results don't match paper", `/diagnose` | — |
| 5 | `grill-me` | 方案评审 | 对方案/设计进行无死角追问，直至达成共识。遍历决策树的每个分支，逐一解决依赖关系。所有问题批量提交。 | "grill me", "stress-test my plan" | — |
| 6 | `handoff` | 会话管理 | 将当前对话压缩为最小交接块，供新 agent 继续。剥离临时工具输出，保留核心代码和决策，压缩历史。 | "hand off", "continue in new session", `/handoff` | — |
| 7 | `improve-codebase-architecture` | 架构优化 | 在代码库中发现深化机会——将浅模块转化为深模块。暴露架构摩擦，提出可测试性和 AI 可导航性的重构建议。依据项目领域文档（CONTEXT.md、AGENTS.md、ADR）。 | "improve architecture", "find refactoring opportunities", "consolidate modules", `/improve-codebase-architecture` | — |
| 8 | `init-with-grilling` | 研究初始化 | 通过引出精确问题、假设、证据计划、方法、数据来源和可复现约束来初始化研究项目。生成研究章程（AGENTS.md），区分已观察/已计划/已假设的事实。 | "init research project", "new experiment", "paper reproduction", `/init-with-grilling` | — |
| 9 | `tdd` | 测试驱动 | 研究代码的 TDD 红-绿-重构循环。测试验证科学正确性（解析解、不变量、收敛性），而非实现细节。垂直示踪子弹，而非水平批量测试。 | "TDD", "red-green-refactor", "test-first", "verify numerical correctness", `/tdd` | "复现", "数值回归", "收敛验证", "消融实验", "可复现性", "写测试" |
| 10 | `write-a-skill` | 元技能 | 按规范结构（SKILL.md + REFERENCE.md + scripts/）创建新 Agent 技能。渐进式披露、打包资源、评审工作流。 | "write a skill", "create a skill", "build a new skill", `/write-a-skill` | — |
| 11 | `zoom-out` | 代码理解 | 拉远视角，提供更广上下文或更高层视角。用于对某段代码不熟悉，或需要了解其在更大图景中的位置时。 | "zoom out", `/zoom-out` | "有什么用", "干什么的", "怎么实现", "讲解一下", "怎么回事", "是什么", "解释一下", "整体看一下" |

---

## 按场景速查

| 你想做什么？ | 加载 |
|---|---|
| 整理/归档凌乱的研究仓库 | `archive` |
| 节省 token，压缩所有输出 | `caveman` + `caveman-thinking` |
| 调试 NaN/Inf 或不收敛的算法 | `diagnose` |
| 开发前对设计进行压力测试 | `grill-me` |
| 在新会话中继续之前的工作 | `handoff` |
| 重构以优化架构 | `improve-codebase-architecture` |
| 用严谨方法启动新的研究项目 | `init-with-grilling` |
| 为研究代码编写测试 | `tdd` |
| 创建新的可复用技能 | `write-a-skill` |
| 快速理解不熟悉的代码 | `zoom-out` |

---

## 技能目录结构

每个技能遵循以下布局：

```
skill-name/
├── SKILL.md           # 主指令文件（必需）
├── REFERENCE.md       # 详细参考文档
├── EXAMPLES.md        # 使用示例
└── scripts/           # 工具脚本（可选）
```

---

## 安装

技能从 `~/.config/opencode/skills/` 加载。将新技能目录放在此处即可供 agent 使用。
