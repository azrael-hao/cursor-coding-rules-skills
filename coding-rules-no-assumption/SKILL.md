---
name: coding-rules-no-assumption
description: Zero speculation principle. Never guess or assume. Must verify all facts through actual reading and checking.
---

# Zero Speculation Principle

Never make assumptions or guesses. All information must be verified.

## 🚫 NEVER

1. **Assume field/method exists** → Must read code to verify
2. **Assume data structure** → Must check actual schema
3. **Assume error cause** → Must get complete error info
4. **Use uncertainty language** ("should", "might", "probably") → Use definitive statements based on evidence

## ✅ MUST

### Verification Steps
1. **Before accessing fields**: Read entity/DTO/VO code
2. **Before calling methods**: Read service/controller code  
3. **Before querying data**: Check database schema
4. **Before making claims**: Verify with actual evidence

### Evidence-Based Responses
- ✅ "Field X exists in Entity Y (verified in line 10)"
- ❌ "Field X should exist in Entity Y"
- ✅ "Method returns List<DTO> (verified in Service.java:45)"
- ❌ "Method probably returns a list"

## Thinking Self-Check

Before answering/modifying:
```
[ ] Have I read the relevant code?
[ ] Am I making any assumptions?
[ ] Can I cite exact locations for my claims?
[ ] Am I 100% certain about this information?
```

**If any answer is "no" → Go read the code first**

## Related Skills

- `coding-rules-no-inference` - Verification requirements
- `coding-rules-core-enforcement` - Core mandatory checks
