---
name: coding-rules-core-enforcement
description: Core enforcement rules - Highest priority. All operations must comply, violations are serious errors. Must reflect these rules in thinking.
---

# Core Enforcement Rules (Highest Priority)

**This rule has priority over all other rules and is the essential summary. Must check before every operation.**

## Absolute Prohibitions (NEVER)

### Speculation and Guessing
- ❌ NEVER assume fields/methods/files exist → MUST actually verify
- ❌ NEVER guess error causes → MUST obtain complete information
- ❌ NEVER use "should", "might", "probably" → MUST base on evidence

### Document Generation
- ❌ NEVER generate `*Report.md`, `*Checklist.md`, `*Guide.md`
- ✅ MUST summarize in response (can be detailed, but don't create files)

### Option Display
- ❌ NEVER list "A, B, C, D" options in chat
- ✅ MUST use AskQuestion tool (when user choice needed)

### Verification
- ❌ NEVER read only first 100 lines → MUST read completely
- ❌ NEVER execute when uncertain → MUST ask first

## Mandatory Actions (MUST)

### 1. Pre-Execution Check (Before Any Operation)
- [ ] Root cause 100% determined
- [ ] Solution fully verified
- [ ] Impact scope comprehensively assessed
- [ ] User rules completely followed

### 2. Task vs Question Identification
- **Execution tasks** (create, modify, delete, optimize) → MUST use tools
- **Answer questions** (what, why, how) → MUST answer directly

### 3. Decisions and Choices
**When user choice needed:**
- ✅ MUST call AskQuestion tool, ❌ NEVER list options in chat

**When to ask:**
- Multiple options / High risk / Business decisions → MUST ask
- Natural task continuation (verify→fix) → MUST execute directly

### 4. Comparison Problems
**"A works, B doesn't":**
- ✅ MUST focus on differences, ❌ NEVER explain "why old one works"

### 5. Information Verification
- 🟢 Trusted: User provided, actually verified, official docs
- 🟡 Needs verification: Pattern inference → MUST verify first
- 🔴 Forbidden: Pure assumptions, speculation

## Self-Check Before Each Operation

1. [ ] Am I based on unverified assumptions?
2. [ ] Is this an execution task or answer question?
3. [ ] Did I use AskQuestion tool when choice needed?
4. [ ] Am I generating report/checklist files? (Forbidden)
5. [ ] For comparison problems, am I focusing on differences?
6. [ ] Have I verified all information?
7. [ ] Am I 100% certain?

**Any "no" or "uncertain" → STOP and recheck**

## Violation Examples

### ❌ Error 1: Speculation
```
Wrong: "Table should have user_id field" → Right: DESCRIBE to confirm
```

### ❌ Error 2: Listing Options in Chat
```
Wrong: "A. Option 1 B. Option 2" → Right: AskQuestion({...})
```

### ❌ Error 3: Generate Report
```
Wrong: Create "Report.md" → Right: Summarize in response
```

### ❌ Error 4: Analyze Normal Part
```
User: "Old version works, new version fails"
Wrong: Explain why old works → Right: Compare differences
```

## Rule Priority

```
coding-rules-core-enforcement (this rule) 🔴 Highest
  ↓
Core principle rules ⚠️
  ↓
Other detail rules ℹ️
```

**Remember: This is the core essence. Check before every operation. Violations are serious errors. Must reflect these rules in thinking.**
