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

## Compression Strategy

### 1. Proactively Inform User
Clearly state at beginning of response:
> "Context approaching capacity limit, compressing to maintain session continuity."

### 2. Generate Structured Summary
Compress current session key information into following structure:
- **Current Task**: One sentence describing what's being done
- **Completed**: List of completed steps
- **To Complete**: List of uncompleted steps
- **Key Files**: File paths involved and their roles
- **Key Decisions**: Technical decisions made and reasons
- **To Confirm**: Issues requiring user confirmation

### 3. Avoid Repeated Reading
After compression, don't re-read already processed file content, only reference file paths. For large data results, only keep statistical summary not raw data.

### 4. Split Large Tasks
If task too large to complete in single session:
- Split remaining work into independently executable sub-steps
- Use TODO list to record progress
- Prioritize script automation (Python/Shell) instead of line-by-line manual operations
- Avoid using subagent to process tasks requiring large text generation

## Preventive Measures

Follow these principles throughout session to slow context consumption:

- When reading files, prioritize using offset/limit parameters, avoid reading over 200 lines at once
- When SSH command output too long, use `head`/`tail` to truncate
- When generating large documents, use Python scripts instead of writing line by line
- When tool call results exceed 100 lines, extract key information and don't reference original output again
- Update TODO list after completing each milestone to ensure progress traceable
