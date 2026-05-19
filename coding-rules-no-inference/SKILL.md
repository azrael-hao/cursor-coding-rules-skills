---
name: coding-rules-no-inference
description: No inference without verification. All deducible facts must be confirmed through actual queries and checks.
---

# No Inference - Must Verify

All deducible information must be verified through actual queries, not inferred.

## 🚫 NEVER

1. **Infer database content** → Must query to check
2. **Infer file existence** → Must use file tools to verify
3. **Infer method behavior** → Must read implementation
4. **Infer configuration values** → Must read config files

## ✅ MUST

### Query Instead of Infer

| ❌ Wrong (Inference)         | ✅ Correct (Verification)        |
|------------------------------|----------------------------------|
| "Table X should have data"   | Query: `SELECT COUNT(*) FROM X`  |
| "File probably exists"       | Tool: Read/Glob to check         |
| "Method likely returns Y"    | Read source code                 |
| "Config is probably default" | Read config file                 |

### Verification Tools

- **Code**: Read tool, Grep tool
- **Database**: SQL query, schema check
- **Files**: Glob, Read, file system commands
- **Configuration**: Read config files, environment variables

## Example Workflow

**Bad:**
```
User: "Is table users empty?"
AI: "Based on the application logic, it's likely populated."
```

**Good:**
```
User: "Is table users empty?"
AI: "Let me verify with a query..."
[Runs: SELECT COUNT(*) FROM users]
AI: "Verified: table users has 150 records."
```

## Thinking Self-Check

```
[ ] Am I inferring anything that can be verified?
[ ] Have I run actual queries/checks?
[ ] Do I have concrete evidence?
```

**Any inference → Stop and verify**

## Related Skills

- `coding-rules-no-assumption` - Zero speculation
- `coding-rules-core-enforcement` - Core verification requirements
