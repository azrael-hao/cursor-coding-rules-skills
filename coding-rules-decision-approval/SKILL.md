---
name: coding-rules-decision-approval
description: Decision changes and path switches must seek user consent first. Must use AskQuestion tool when choices needed, strictly forbidden to list options in chat.
---

# Decision Change Approval

## Core Principles

### Standard 1: Natural Task Continuation (Highest Priority)

**Natural task continuation → Must execute directly, forbidden to ask**

- verify→fix, analyze→implement, test→fix→retest, find problem→solve
- Key feature: Subsequent steps are the purpose of previous steps
- **Exceptions (need to ask)**: Multiple option choices, high-risk irreversible operations, business decisions

### Standard 2: Certainty Principle

**Can confirm correctly → Execute directly | Uncertain → Must use AskQuestion tool to ask**

🔴 **Mandatory requirement: When user choice needed, must call AskQuestion tool, strictly forbidden to list options in chat**

**Conditions for confirmed correctness (all must be met)**:
1. Task clear (user requirement clear or natural task continuation)
2. Technology certain (only one correct approach)
3. Impact controllable (modification scope clear, no chain impact)
4. Risk acceptable (operation reversible or low risk)

## Judgment Process

```
Step 1: Is it natural task continuation?
  ├─ Yes → Step 2: Any exceptions (multiple options/high risk/business decision)?
  │         ├─ Yes → Use AskQuestion tool
  │         └─ No → Execute directly
  └─ No → Step 3: Meet all 4 certainty conditions?
            ├─ Yes → Execute directly
            └─ No → Use AskQuestion tool
```

## Scenarios Requiring AskQuestion Tool

1. **Path selection**: Multiple technical options need weighing
2. **High-risk operations**: Delete data, force push, DROP TABLE, batch modifications
3. **Business decisions**: Priority sorting, cost weighing, feature trade-offs
4. **Requirement interpretation**: Multiple interpretations, missing key information

## Error Behavior vs Correct Approach

### ❌ Error: List Text Options in Chat
```
"How do you want to proceed?
A. Option 1
B. Option 2
C. Option 3"

This is a serious error! Forbidden!
```

### ✅ Correct: Use AskQuestion Tool
```javascript
AskQuestion({
  title: "Select Handling Approach",
  questions: [{
    id: "approach",
    prompt: "Please select handling method",
    options: [
      { id: "A", label: "Option 1 description" },
      { id: "B", label: "Option 2 description" }
    ],
    allow_multiple: false
  }]
})
```

## Mandatory Requirements

When user choice needed:
1. ✅ Must call AskQuestion tool
2. ❌ Forbidden to list "A, B, C, D" options in chat
3. ❌ Forbidden to use "How do you want to proceed?" followed by text options
4. ✅ Must wait for AskQuestion result before continuing

**Violating this rule is a serious error**

**Remember: When user choice needed, must use AskQuestion tool, forbidden to list options in chat text.**
