---
name: coding-rules-decision-approval
description: All user choices must use AskQuestion tool. Never list options in chat. Distinguish between natural task continuation and user decisions.
---

# Decision Change Approval

All user choices must use AskQuestion tool, not options listed in chat.

## 🚫 NEVER

1. **List options in chat** ("A, B, C" or "1, 2, 3") → Must use AskQuestion
2. **Decide for user** on subjective matters → Must ask
3. **Execute after AskQuestion timeout** → Must re-ask

## ✅ MUST Use AskQuestion

### 8 Mandatory Scenarios

1. **Multiple solutions** - User must choose strategy
2. **Risky operations** - Delete files, major refactoring
3. **Business decisions** - Affects user requirements
4. **Ambiguous requirements** - Need clarification
5. **Plan confirmation** - After creating plan
6. **Previous timeout** - If AskQuestion timed out
7. **Trade-offs** - Performance vs readability, etc.
8. **Incomplete info** - Need user to fill gaps

## ✅ Natural Task Continuation (No AskQuestion)

These scenarios flow naturally, don't need confirmation:

1. **Diagnostic → Fix** - Found bug → Fix it
2. **Validation → Implementation** - Checked feasibility → Implement
3. **Error → Root cause** - Got error → Investigate
4. **Plan → Execution** - ONLY if user explicitly said "execute"

## Judgment Criteria

Ask yourself:
- Does this require **user judgment or preference**? → **Use AskQuestion**
- Is this a **natural next step** everyone would agree on? → **Proceed**

## Timeout Handling

If AskQuestion times out (no response):
1. **Must re-ask** using AskQuestion tool again
2. **Never** proceed without answer
3. **Never** decide for user

## Related Skills

- `coding-rules-core-enforcement` - AskQuestion mandatory scenarios
- `coding-rules-task-identification` - Task vs question distinction
