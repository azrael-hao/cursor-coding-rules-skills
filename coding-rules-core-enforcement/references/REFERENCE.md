# Core Enforcement Rules - Reference

## Overview

This skill provides comprehensive enforcement of core coding rules with highest priority.

## Rule Evolution History

### v1.0 (Initial)
- Created as standalone core enforcement rule
- 20 separate rule files

### v2.0 (Current - Integration)
- Consolidated to 10 core rules
- Integrated 5 auxiliary guidelines as sub-sections
- Improved structure and maintainability

## Related Rules

### Primary Rules
- `00-CORE-ENFORCEMENT.mdc` - Core enforcement with integrated guidelines
- `zero-speculation-mandatory.mdc` - Unified verification principles
- `user-interaction-mandatory.mdc` - Unified user interaction rules

### Integrated Guidelines
- Task identification (execution vs answer)
- Essential problem focus (comparison questions)
- No report files (summarize in response)
- Rules self-check (compliance monitoring)
- Plan before implementation (complex tasks)

## Usage Examples

### Scenario 1: Task Identification
```
User: "What is git rebase?"
Action: Answer directly (not execution task)

User: "Rebase my feature branch"
Action: Use tools to execute
```

### Scenario 2: Comparison Questions
```
User: "Function A works but B doesn't"
Focus: Why B doesn't work (not why A works)
```

## Best Practices

1. **Always verify before acting** - Read, Grep, DESCRIBE first
2. **Use AskQuestion for all user interactions** - Never list options in chat
3. **Complete tasks in one turn** - No partial work requiring "continue"
4. **Diagnose before fixing** - Identify exact root cause first

## Common Violations

### ❌ Wrong
- Assuming file/method exists without verification
- Listing options in chat as "A. B. C."
- Executing plan without user confirmation
- Leaving partial work unfinished

### ✅ Correct
- Verify existence with Read/Grep
- Use AskQuestion tool for choices
- Get approval before executing plans
- Complete tasks fully in one turn
