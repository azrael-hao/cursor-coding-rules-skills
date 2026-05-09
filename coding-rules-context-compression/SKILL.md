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

### 1. Rules (Highest Priority)
- ✅ **ALL Rules files** (`.mdc` files from `~/.cursor/rules/`)
- ✅ **Rules content** loaded at session start
- ✅ **Rule enforcement requirements**
- ✅ **Self-check mechanisms**

**Why**: Rules are mandatory constraints that govern all AI behavior. Losing rules = violating core principles.

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
✅ All Rules remain active and enforced:
- Zero-speculation mandatory
- Data-driven decisions
- Plan-before-implementation
- [List other active rules...]

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
- **IMPORTANT**: Never compress or summarize Rules content - always keep rules fully accessible
