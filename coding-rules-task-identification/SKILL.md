---
name: coding-rules-task-identification
description: Distinguish execution tasks from answer questions. Tasks use tools, questions get direct answers.
---

# Task vs Question Identification

Correctly identify whether user request is an execution task or an answer question.

## Two Categories

### Execution Tasks
**Characteristics:**
- Create, modify, delete, optimize, refactor
- Change system state
- Produce artifacts (code, files, data)

**Action:** Use tools to execute

**Examples:**
- "Add a new API endpoint"
- "Optimize this query"
- "Refactor the UserService"
- "Fix the bug in checkout"

### Answer Questions
**Characteristics:**
- Ask about how/what/why
- Seek understanding
- Request information

**Action:** Directly answer

**Examples:**
- "How does authentication work?"
- "What's the difference between X and Y?"
- "Why is this method deprecated?"
- "Can you explain this error?"

## Decision Matrix

| User Says | Type | Action |
|-----------|------|--------|
| "Add...", "Create...", "Implement..." | Task | Execute with tools |
| "Fix...", "Optimize...", "Refactor..." | Task | Execute with tools |
| "How does...", "What is...", "Why..." | Question | Answer directly |
| "Explain...", "Describe..." | Question | Answer directly |
| "Show me..." | Depends | Show existing = answer, create new = task |

## Gray Areas

### "Can you..."
- "Can you add X?" → Task (they want you to do it)
- "Can X be done?" → Question (asking about possibility)

### "Should I..."
- Seeking advice → Answer question
- Asking you to decide and do → Use AskQuestion tool

## Thinking Check

```
[ ] Is user asking for information? → Answer
[ ] Is user asking to change something? → Execute
[ ] Unclear? → Ask for clarification
```

## Related Skills

- `coding-rules-core-enforcement` - Task vs question rules
- `coding-rules-decision-approval` - When to ask user
