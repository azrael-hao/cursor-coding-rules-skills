---
name: coding-rules-task-identification
description: Accurately identify user intent - distinguish between tasks that need execution and questions that only need answers, avoiding over-execution or just providing explanations.
---

# Task vs Question Identification

## Core Principle

**Accurately determine user intent, complete execution tasks with tools, answer questions directly with explanations.**

## Identification Process

```
User Input → Analyze Intent Features
├─ Execution Task → Use Tools to Execute → Brief Summary
└─ Answer Question → Answer Directly (Query if necessary)
```

## Execution Tasks (Need to Use Tools)

### Feature Identification
**Clear action words**: create, modify, delete, update, add, implement, develop, write, generate, fix, optimize, refactor, deploy, configure, install, run, execute, test

**Implicit execution intent**:
- "Help me XX", "Give me XX" (followed by specific operation)
- Provided specific modification content or requirements
- Has file/code reference (@file) + improvement description

### Handling Method
1. Use tools to execute (Read, Write, StrReplace, Shell, etc.)
2. Brief summary after completion
3. Forbid only providing plan without execution (unless needs user decision)

### Examples
- "Modify config file port to 8080" ✅ Execute
- "Create user login API" ✅ Execute
- "Optimize this code performance" ✅ Execute

## Answer Questions (Only Need to Answer)

### Feature Identification
**Question words**: what is, why, how, have/has, can/can't, will/won't

**Information query intent**:
- Asking about principles, concepts, definitions, best practices
- Asking about possibilities, feasibility, reasons, explanations
- No clear execution action requirement

### Handling Method
1. Answer directly, provide clear explanation
2. Use Read/Grep to query information if necessary
3. Forbid proactively modifying or creating files

### Examples
- "What does this code mean?" ✅ Answer
- "Why does this error occur?" ✅ Answer
- "What are the optimization options?" ✅ Answer

## Ambiguous Scenario Judgment

### "How to XX" Type Questions
- Has specific code/file reference → Tends toward execution
- No specific context → Tends toward answering methods

### "Can/Can't XX" Type Questions
- Has file reference + task background → Tends toward execution
- Pure inquiry tone → Tends toward answering feasibility

### Judgment Strategy
**Signals tending toward execution**:
- Provided file path or @file reference
- Has clear task background
- Firm tone, instructional

**Signals tending toward answer**:
- Pure theoretical, conceptual inquiry
- No specific context
- Exploratory, consultative tone

## Avoiding Error Behaviors

### ❌ Over-Execution
User: "What's wrong with this code?"
- Wrong: Directly modify code ❌
- Right: Analyze problem, explain reason ✅

### ❌ Only Talk, Don't Do
User: "Modify config file port to 8080"
- Wrong: Only explain how to modify ❌
- Right: Directly modify, brief summary ✅

**Remember: Tasks need execution, questions need answers, clarify intent when uncertain.**
