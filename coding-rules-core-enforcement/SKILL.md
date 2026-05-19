---
name: coding-rules-core-enforcement
description: Core enforcement rules with highest priority. All operations must comply. Includes mandatory checks in thinking.
---

# Core Enforcement Rules

**Highest priority rules. Essential summary of all coding standards. Must check before every operation.**

## 🚫 NEVER

### Speculation and Guessing
- ❌ NEVER assume fields/methods/files exist → MUST verify
- ❌ NEVER guess error causes → MUST get complete information
- ❌ NEVER use "should", "might", "probably" → MUST base on evidence

### Document Generation
- ❌ NEVER generate `*report.md`, `*list.md`, `*doc.md`
- ✅ MUST summarize in response (can be detailed, but no files)

### Options Display
- ❌ NEVER list "A, B, C, D" options in chat
- ✅ MUST use AskQuestion tool (when user choice needed)

### Verification
- ❌ NEVER read only first 100 lines → MUST read completely
- ❌ NEVER execute when uncertain → MUST ask first

## ✅ MUST

### 1. Pre-execution Checks (Before Any Operation)
- [ ] Root cause 100% identified
- [ ] Solution fully verified
- [ ] Impact scope comprehensively assessed
- [ ] User rules completely followed

### 2. Task vs Question Identification
- **Execution tasks** (create, modify, delete, optimize) → MUST use tools
- **Answer questions** (what, why, how) → MUST answer directly

### 3. AskQuestion Mandatory Scenarios
Use AskQuestion tool in these cases:
1. User needs to choose from multiple options
2. Plan needs confirmation before execution
3. Risky operations (delete, major refactor)
4. User judgment required
5. Multiple valid solutions
6. Ambiguous requirements
7. Previous AskQuestion timeout
8. Task dependency involves user decision

### 4. Comparison Problems
When user asks "compare A and B":
- ✅ MUST focus on **differences** (what's different)
- ❌ NEVER waste space on commonalities
- Format: Differences table + key difference summary

### 5. Thinking Self-Check
Every thinking block must check:
```
1. [ ] Based on unverified assumptions?
2. [ ] Execution task or answer question?
3. [ ] Root cause diagnosed before fixing?
4. [ ] User choice involved? → Use AskQuestion
5. [ ] Created plan? → Confirm with AskQuestion
6. [ ] AskQuestion timeout? → Re-ask
7. [ ] Compressing context? → Keep all 20 rules
8. [ ] Answer focused? No unnecessary divergence?
9. [ ] Task fully resolved in one turn?
10. [ ] Generating report file? → Forbidden
11. [ ] Verified all information?
12. [ ] 100% certain?
```

**Any "no" or "uncertain" → STOP and recheck**

## Related Skills

- `coding-rules-no-assumption` - Zero speculation principle
- `coding-rules-no-inference` - Verification requirements
- `coding-rules-decision-approval` - AskQuestion usage
- `coding-rules-problem-focus` - Comparison problem handling
- `coding-rules-no-report-files` - Document generation rules
