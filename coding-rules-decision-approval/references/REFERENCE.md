# Decision Approval - Reference

## Overview

This skill ensures all user interactions use AskQuestion tool and plans require approval.

## Integration History

### Before Integration
Three separate rules:
- `decision-change-approval.mdc` - AskQuestion mandatory
- `plan-approval-mandatory.mdc` - Plan execution confirmation
- `ask-timeout-retry-mandatory.mdc` - Timeout retry

### After Integration (v2.0)
- Unified into `user-interaction-mandatory.mdc`
- Consolidated 8 mandatory scenarios
- Clear approval process
- Timeout handling protocol

## AskQuestion Tool Usage

### Correct Usage
```javascript
AskQuestion({
  title: "Choose Implementation Approach",
  questions: [{
    id: "approach",
    prompt: "Which approach do you prefer?",
    options: [
      { id: "A", label: "Merge conflicting rules" },
      { id: "B", label: "Keep rules independent" }
    ],
    allow_multiple: false
  }]
})
```

### ❌ Wrong Usage
```
"Which approach do you prefer?
A. Merge conflicting rules
B. Keep rules independent"
```

## 8 Mandatory AskQuestion Scenarios

1. **Solution selection** - 2+ implementation options
2. **Execution confirmation** - Before making changes
3. **User preference** - Uncertain about user's intent
4. **Timeout re-confirmation** - After AskQuestion timeout
5. **Business decisions** - Priority, cost, feature tradeoffs
6. **Ambiguity clarification** - Multiple interpretations
7. **Path selection** - Multiple next step options
8. **Risk assessment** - High-risk operations

## Plan Approval Process

1. Analyze problem
2. Create detailed plan (steps, impact, risks)
3. **Use AskQuestion for confirmation** (MANDATORY)
4. Execute only after approval

### Scenarios Requiring Approval
- Code modifications
- Database changes
- Architecture adjustments
- File operations (delete/move)
- Dependency changes
- Configuration updates
- Batch operations
- Refactoring

### Exceptions (Direct Execution OK)
- Read-only operations (Read, Grep, Search)
- Plans explicitly approved in current conversation

## Timeout Handling

### Process
1. AskQuestion times out
2. **STOP all operations immediately**
3. Re-ask with "re-confirmation" label
4. Explain timeout context
5. Wait for explicit response

### ❌ Never Do After Timeout
- Guess user intent
- Choose default option
- Continue based on "common sense"
- Assume agreement

## Common Mistakes

### Mistake 1: Listing Options in Chat
```
❌ "Do you want to:
1. Update code
2. Create new file
3. Refactor existing"

✅ Use AskQuestion tool
```

### Mistake 2: Execute Without Approval
```
❌ "I'll update these 5 files..." [starts execution]

✅ "Plan: Update these 5 files... [use AskQuestion]"
```

### Mistake 3: Deciding After Timeout
```
❌ "Since no response, I'll choose option A"

✅ "Previous question timed out. [Re-ask with AskQuestion]"
```
