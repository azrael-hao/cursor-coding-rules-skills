---
name: coding-rules-problem-focus
description: For comparison problems, focus on difference analysis rather than known normal parts, quickly locate root cause. Applies to "A works, B doesn't" type problems.
---

# Essential Problem Focus

## Core Concept

**Go straight to differences, don't dwell on the known. Focus on problem root cause, don't waste time analyzing already working parts.**

## Applicability Judgment

### ✅ Comparison Problems (Apply This Principle)
- "Previously worked, now doesn't" / "A environment normal, B environment fails"
- "Old version normal, new version errors" / "Dataset A succeeds, Dataset B fails"
- Description contains transition words like "but", "however", "yet"
- Provided normal and abnormal case comparison

### ❌ Non-Comparison Problems (Don't Apply This Principle)
- Simple error reports: "Runtime error..." (no control group)
- New feature development: "Implement XX feature" (no old version)
- Code understanding: "What does this code mean?" (not problem diagnosis)

### Judgment Process
```
Received user question → Identify comparison words (before/now, old/new, A/B)
├─ Yes → Comparison problem → Apply difference comparison analysis
└─ No → Non-comparison problem → Regular problem diagnosis
```

## Analysis Process for Comparison Problems

1. **Quickly confirm known facts** (don't deep analyze): What's normal?
2. **Immediately focus on differences** (core attention): What's different between new and old?
3. **Analyze how differences cause problem** (locate root cause): Which difference causes the problem?
4. **Directly fix root cause** (precise solution): Fix targeting root cause

## Comparison Dimensions

- **Configuration differences**: Config files, environment variables, parameter settings
- **Version differences**: Dependency versions, tool versions, library versions
- **Environment differences**: Runtime environment, network environment, file system
- **Code differences**: Code changes, logic modifications, API calls
- **Data differences**: Input data, data formats, data states

## Priority Sorting
1. 🔴 High priority: Directly related configuration or code changes
2. 🟡 Medium priority: Indirectly affecting environment or dependency changes
3. 🟢 Low priority: Unlikely to affect minor differences

## Forbidden Inefficient Behaviors

- 🚫 Explain "why old one works" (known facts don't need explanation)
- 🚫 Explain entire system working principles (general knowledge not the point)
- 🚫 List all theoretical possible causes (no targeting)
- 🚫 Ignore user-provided control group (waste valuable clues)
- 🚫 Force finding non-existent comparisons (when user didn't provide control group)

**Remember: First judge scenario, comparison problems focus on differences, non-comparison problems direct diagnosis.**
