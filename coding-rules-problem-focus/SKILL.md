---
name: coding-rules-problem-focus
description: For comparison questions, focus on differences. Never waste space on commonalities. Essential problem focus principle.
---

# Essential Problem Focus

When handling comparison questions, focus sharply on differences, not commonalities.

## Core Principle

**User asks comparison = User wants to know DIFFERENCES**

## 🚫 NEVER

1. **List common features** - Wastes space and context
2. **Describe both separately** - User can read docs for that
3. **Generic overviews** - Not answering the question

## ✅ MUST

### Comparison Format

```markdown
## Key Differences

| Aspect | Option A | Option B |
|--------|----------|----------|
| [Difference 1] | ... | ... |
| [Difference 2] | ... | ... |

## Decision Guide

- Choose A if: [specific scenarios]
- Choose B if: [specific scenarios]

## Summary

The critical difference is [1-2 sentence summary]
```

### Focus Areas

For "A vs B" questions, focus on:
1. **Functional differences** - What can A do that B can't?
2. **Performance differences** - Speed, memory, scalability
3. **Use case differences** - When to use each
4. **Trade-offs** - What you gain/lose with each choice

## Examples

**❌ Wrong Response:**
```
A has features X, Y, Z.
B has features X, Y, Z.
Both support caching...
Both are popular...
```

**✅ Correct Response:**
```
Key Differences:

1. Architecture: A uses sync I/O, B uses async
2. Performance: B handles 10x more concurrent requests
3. Complexity: A simpler to configure, B requires expertise

Choose A for: Small apps, simple requirements
Choose B for: High traffic, async workflows

Critical difference: B's async model is essential for high concurrency.
```

## Related Skills

- `coding-rules-core-enforcement` - Comparison problem handling
