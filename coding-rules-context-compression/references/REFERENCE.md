# Context Compression - Reference

## Overview

Strategy for managing context limits while preserving all core rules.

## Rule Evolution

### v1.0
- 20 core rules must remain intact
- Context compression triggered manually

### v2.0 (Current)
- 10 core rules (consolidated from 20)
- Automatic trigger conditions
- Structured compression protocol

## 10 Core Rules (Never Compress)

1. **00-CORE-ENFORCEMENT** - Core enforcement with integrated guidelines
2. **zero-speculation-mandatory** - Unified verification principles
3. **user-interaction-mandatory** - Unified user interaction
4. **diagnose-before-action** - Root cause analysis first
5. **solve-not-suppress** - Fix problems, don't hide them
6. **single-turn-resolution** - Complete tasks in one turn
7. **no-unnecessary-divergence** - Stay focused
8. **no-reckless-file-deletion** - Safe deletion protocol
9. **adaptive-thinking** - Complex tasks need thinking
10. **context-compression** - This rule itself

## Trigger Conditions

Compress when any of:
1. Conversation rounds exceed 20 with many tool calls
2. Cumulative code/data blocks exceed 2000 lines
3. Subtask running over 5 minutes
4. Responses truncated or incomplete

## Compression Protocol

### Step 1: Inform User
```
"Context approaching capacity limit, compressing to maintain session continuity."
```

### Step 2: Structured Summary
- **Current Task**: One sentence description
- **Completed**: List of finished steps
- **Pending**: List of remaining steps
- **Key Files**: File paths and roles
- **Key Decisions**: Technical choices made
- **Awaiting Confirmation**: User questions pending

### Step 3: Avoid Repeated Reads
- Reference file paths, don't re-read contents
- Keep statistical summaries, not raw data

### Step 4: Split Large Tasks
- Break into independent sub-steps
- Use TODO list for tracking
- Prefer scripts over manual operations
- Avoid subagents for text-heavy tasks

## Prevention Strategies

### Read Files Efficiently
```bash
# ❌ Wrong
Read entire-large-file.js

# ✅ Correct
Read entire-large-file.js --offset 1 --limit 200
```

### Handle Long Outputs
```bash
# ❌ Wrong
long-running-command  # output fills context

# ✅ Correct
long-running-command | head -50  # truncate
long-running-command > output.txt  # save to file
```

### Generate Documents
```bash
# ❌ Wrong
# Manually write 1000 lines line-by-line

# ✅ Correct
python generate_document.py  # script automation
```

## Forbidden During Compression

❌ **Never Do:**
- Compress or summarize rule content
- Remove rules from context
- Replace rules with summaries

✅ **Must Do:**
- Keep all 10 rules complete
- State "All rules remain intact" in summary

## Example Compression

```
Context approaching capacity limit, compressing to maintain session continuity.

**Current Task**: Integrating rules from 20 to 10 files

**Completed**:
1. ✅ Created Git backup tag
2. ✅ Merged verification rules
3. ✅ Created user-interaction rules
4. ✅ Expanded core enforcement

**Pending**:
1. Update README documentation
2. Create skill structure examples
3. Commit changes

**Key Files**:
- ~/.cursor/rules/*.mdc - Core rules (10 files)
- ~/.cursor/rules/zh/*.mdc - Chinese rules (10 files)

**Key Decisions**:
- Kept execution quality rules independent (not merged)
- Adopted plan recommendation B (10 files)

All rules remain intact.
```
