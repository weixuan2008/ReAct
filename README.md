# ReAct: 协同推理与行动的智能体设计模式 (PoC 实现)

本项目是基于 ICLR 2023 论文 [《ReAct: Synergizing Reasoning and Acting in Language Models》](https://arxiv.org/abs/2210.03629) 的一个简单概念验证 (PoC) 实现。

## 什么是 ReAct？

**ReAct** 是 **Reason**（推理）+ **Act**（行动）的缩写。它是一种让大语言模型（LLM）以更智能、更可信的方式解决复杂任务的设计模式。

在传统的 AI 交互中，模型通常要么只是“空想”（Chain-of-Thought，只进行内部推理），要么只是“盲动”（Action-only，直接调用工具而不解释原因）。ReAct 的核心思想是将这两者**协同**起来：

> **“像人类一样思考，像专家一样行动。”**

### ReAct 的工作流程

ReAct 模式引导模型生成一个交替进行的序列：**Thought（思考）** -> **Action（行动）** -> **Observation（观察）**。

1.  **Thought (推理轨迹)**：模型先写下当前对问题的理解、制定的计划或对异常情况的处理逻辑。这相当于模型的“内心独白”。
2.  **Action (交互行动)**：基于推理，模型决定执行一个具体的动作（例如搜索维基百科、查询数据库或调用 API）。
3.  **Observation (外部反馈)**：模型接收动作执行后的结果（如搜索到的网页内容）。
4.  **循环**：模型根据新的观察结果，进入下一轮思考，直到任务完成。

---

## 为什么需要 ReAct？

相比于传统的 Prompt 方式，ReAct 解决了以下核心痛点：

| 特性 | 传统推理 (CoT) | 纯行动模式 | ReAct 模式 |
| :--- | :--- | :--- | :--- |
| **实时性** | 闭门造车，依赖旧知识 | 实时获取外部信息 | **实时获取并逻辑分析** |
| **准确性** | 容易产生“幻觉” | 缺乏逻辑，易误用工具 | **通过推理减少幻觉** |
| **可解释性** | 有推理过程但无行动 | 只有结果，过程黑盒 | **每一步行动都有理有据** |
| **容错性** | 一步错步步错 | 难以处理复杂反馈 | **能根据观察动态调整计划** |

---

## 本项目实现 (PoC)

本项目使用 Python 实现了一个最简化的 ReAct 循环。它展示了如何通过简单的 Prompt 工程，让 LLM 具备：
*   **自我诊断**：意识到自己知识的边界。
*   **工具调用**：自动格式化并触发外部函数。
*   **动态规划**：根据工具返回的结果修正后续步骤。


### 代码结构——ReAct模式

- agent.py：react多轮回复主程序
- llm.py：连接远程的大模型服务器
- prompt.py：react模式的提示词，强制说明需要观察observation和调用工具tool
- tools.py：工具的使用函数，可以调用外部接口
- 
### 核心逻辑示例

```text
Question: 谁是 2023 年奥斯卡最佳男主角得主，他出演过哪部关于物理学家的电影？

Thought 1: 我需要先确认 2023 年奥斯卡最佳男主角是谁。
Action 1: Search[2023 Academy Award Best Actor winner]
Observation 1: 布兰登·费舍 (Brendan Fraser) 凭借《鲸》获得该奖项。

Thought 2: 现在我需要查找布兰登·费舍是否出演过关于物理学家的电影。
Action 2: Search[Brendan Fraser movies about physicists]
Observation 2: 搜索结果显示他并未出演过著名的物理学家传记片。等等，我应该检查一下 2024 年的情况，或者确认问题是否指代错误。
...
```

---

## 快速开始

*(此处可根据您的具体代码结构添加安装和运行指令)*

1. 克隆仓库：
   ```bash
   git clone https://github.com/weixuan2008/ReAct
   ```
2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
3. 运行 Demo：
   ```bash
   python main.py
   ```

---

## 参考文献

- https://arxiv.org/pdf/2210.03629
