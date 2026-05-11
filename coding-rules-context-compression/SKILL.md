---
name: coding-rules-context-compression
description: When dialogue context approaches capacity limit, automatically perform context compression to maintain session continuity.
---

# Context Compression

## Trigger Conditions

When sensing any of the following signals, context is about to be exhausted, must immediately compress:

1. Dialogue rounds exceeded 20 and contain large number of tool call results
2. Read or generated large code/data segments (cumulative exceeds 2000 lines)
3. Subtask (Task/subagent) execution time exceeds 5 minutes still not complete
4. Feel responses being truncated or unable to generate completely

## 🔴 CRITICAL: What NEVER Gets Compressed

**The following content MUST ALWAYS be preserved and NEVER compressed:**

### 1. Rules (Highest Priority - NEVER COMPRESS)

**🔴 CRITICAL RULES (16个核心规则 - 绝对不可压缩):**

#### 核心执行规则（必须完整保留）
1. ✅ **00-CORE-ENFORCEMENT.mdc** - 核心强制执行规则（最高优先级）
2. ✅ **zero-speculation-mandatory.mdc** - 零臆想强制执行（thinking自检）
3. ✅ **solve-not-suppress.mdc** - 解决问题而非干掉问题
4. ✅ **no-reckless-file-deletion.mdc** - 禁止粗暴删除文件
5. ✅ **plan-approval-mandatory.mdc** - 方案执行前强制确认
6. ✅ **ask-timeout-retry-mandatory.mdc** - AskQuestion超时必须重新提问

#### 用户交互规则（强制使用AskQuestion）
7. ✅ **decision-change-approval.mdc** - 🔴 所有用户选择必须使用AskQuestion工具

#### 核心原则规则
8. ✅ **adaptive-thinking.mdc** - 自适应思考深度控制
9. ✅ **no-assumption-core.mdc** - 零臆想原则
10. ✅ **no-inference-verification-required.mdc** - 禁止推断，必须验证
11. ✅ **data-driven-decisions.mdc** - 数据驱动决策
12. ✅ **task-vs-question-identification.mdc** - 任务与问题识别
13. ✅ **no-report-files.mdc** - 禁止生成报告文档
14. ✅ **plan-before-implementation.mdc** - 计划优先原则

#### 工作流程规则
15. ✅ **essential-problem-focus.mdc** - 本质问题聚焦
16. ✅ **rules-self-check.mdc** - Rules自我监督机制

**Why**: Rules are mandatory constraints that govern all AI behavior. Losing rules = violating core principles.

**ESPECIALLY CRITICAL**:
- 🔴 **decision-change-approval.mdc** must NEVER be compressed (强制AskQuestion使用)
- 🔴 **00-CORE-ENFORCEMENT.mdc** must NEVER be compressed (核心执行规则)
- 🔴 **zero-speculation-mandatory.mdc** must NEVER be compressed (零臆想自检)
- 🔴 **plan-approval-mandatory.mdc** must NEVER be compressed (方案执行确认)
- 🔴 **ask-timeout-retry-mandatory.mdc** must NEVER be compressed (超时重新提问)

### 2. Current Task Context
- ✅ Active task description
- ✅ Uncompleted TODO items
- ✅ User requirements and constraints
- ✅ Critical decisions made

### 3. Error Context
- ✅ Current errors being debugged
- ✅ Error messages and stack traces
- ✅ Root cause analysis

## Compression Strategy

### 1. Proactively Inform User
Clearly state at beginning of response:
> "Context approaching capacity limit, compressing to maintain session continuity. **Note: All Rules remain active and enforced.**"

### 2. Generate Structured Summary
Compress current session key information into following structure:
- **Current Task**: One sentence describing what's being done
- **Completed**: List of completed steps
- **To Complete**: List of uncompleted steps
- **Key Files**: File paths involved and their roles
- **Key Decisions**: Technical decisions made and reasons
- **Active Rules**: Confirm all rules still enforced (reference, don't duplicate)
- **To Confirm**: Issues requiring user confirmation

### 3. Avoid Repeated Reading
After compression, don't re-read already processed file content, only reference file paths. For large data results, only keep statistical summary not raw data.

**EXCEPTION**: If a rule file was modified or added during session, keep the reference visible.

### 4. Split Large Tasks
If task too large to complete in single session:
- Split remaining work into independently executable sub-steps
- Use TODO list to record progress
- Prioritize script automation (Python/Shell) instead of line-by-line manual operations
- Avoid using subagent to process tasks requiring large text generation
- **CRITICAL**: Ensure rule compliance carries over to next session

## What CAN Be Compressed

The following content can be safely compressed:

### ✅ Safe to Compress
- Dialogue history (keep summary only)
- Tool call results (keep conclusions only)
- File contents already processed (keep file paths + summary)
- Long code snippets (keep key changes only)
- Data query results (keep statistics only)
- Log outputs (keep error info only)

### ❌ NEVER Compress
- Rules and rule enforcement
- Current task requirements
- Uncompleted TODO items
- Active error context
- User-provided constraints

## Compression Template

```markdown
## Context Compression Summary

### ⚠️ Rules Status
✅ All 16 Rules remain active and enforced (NEVER compressed):

**🔴 核心执行规则（6个）:**
- 00-CORE-ENFORCEMENT - 核心强制执行
- zero-speculation-mandatory - 零臆想强制执行
- solve-not-suppress - 解决问题而非干掉问题
- no-reckless-file-deletion - 禁止粗暴删除文件
- plan-approval-mandatory - 方案执行前强制确认
- ask-timeout-retry-mandatory - AskQuestion超时必须重新提问

**🔴 用户交互规则（1个）:**
- decision-change-approval - 所有用户选择必须使用AskQuestion工具

**⚠️ 核心原则规则（7个）:**
- adaptive-thinking - 自适应思考
- no-assumption-core - 零臆想原则
- no-inference-verification-required - 禁止推断
- data-driven-decisions - 数据驱动决策
- task-vs-question-identification - 任务识别
- no-report-files - 禁止生成报告
- plan-before-implementation - 计划优先原则

**ℹ️ 工作流程规则（2个）:**
- essential-problem-focus - 本质问题聚焦
- rules-self-check - Rules自我监督机制

### 📋 Current Task
[One sentence description]

### ✅ Completed
1. [Step 1 with key result]
2. [Step 2 with key result]
...

### 🔄 To Complete
1. [Remaining step 1]
2. [Remaining step 2]
...

### 📁 Key Files
- `path/to/file1`: [Role/changes]
- `path/to/file2`: [Role/changes]

### 🎯 Key Decisions
- [Decision 1 + rationale]
- [Decision 2 + rationale]

### ❓ To Confirm
- [Question 1 for user]
- [Question 2 for user]
```

## Preventive Measures

Follow these principles throughout session to slow context consumption:

- When reading files, prioritize using offset/limit parameters, avoid reading over 200 lines at once
- When SSH command output too long, use `head`/`tail` to truncate
- When generating large documents, use Python scripts instead of writing line by line
- When tool call results exceed 100 lines, extract key information and don't reference original output again
- Update TODO list after completing each milestone to ensure progress traceable
- **CRITICAL**: Never compress or summarize Rules content - always keep all 16 rules fully accessible
- **ESPECIALLY**: decision-change-approval (AskQuestion使用), 00-CORE-ENFORCEMENT (核心执行), zero-speculation-mandatory (零臆想), plan-approval-mandatory (方案确认), ask-timeout-retry-mandatory (超时重试) must ALWAYS remain fully loaded
