---
name: coding-rules-no-report-files
description: Forbidden to generate report, checklist, and guide documents. Summarize key features in response.
---

# Forbidden to Generate Document Files

## Core Principle

**Forbidden to generate report, checklist, guide, and similar document files. After completing work, summarize key features in response, no need to generate independent documents.**

## Forbidden File Types

- **Report types**: `*Report.md`, progress reports, verification reports, analysis reports
- **Checklist types**: `*Checklist.md`, execution checklists, deployment checklists, inspection checklists
- **Guide types**: `*Guide.md`, fix guides, usage guides, operation guides
- **Record types**: `*Record.md`, schema records, type reference tables, field records
- **Summary types**: `Complete*.sql`, `Remaining*.sql`, summary SQL, supplementary SQL

## Correct Output Methods

### ✅ Only Generate Core Executable Files
- Actual code: `.sql`, `.py`, `.js`, `.ts`
- DDL definitions: `PostgreSQL_DDL.sql`
- Config files: `.json`, `.yaml`, `.env`
- Directly runnable scripts

### ✅ Summarize Key Features in Response

**Not just 2-3 sentences, but summarize key features**

Format example:
```
Completed:
- Updated ETL definitions for dim_item, dim_bom
- Key fixes: UUID maintains STRING type, dr changed to INT type

Key Features:
- Supports real-time data sync, latency <5s
- Uses incremental update strategy, 70% performance improvement
- Added data quality validation rules

Notes:
- Requires service restart to take effect
- Compatible with old version data format
```

**Key point: Explain in response, don't generate independent document files**

## Workflow

1. **Query/Analysis**: Directly use tools, don't record query results to files
2. **Fix**: Directly modify target files, don't generate comparison files, guide files
3. **Verification**: Can generate temporary test files, merge to main file after verification and delete
4. **Completion**: Summarize key features in response, don't generate independent summary documents

## Special Cases

Only generate document files when user explicitly requests:
- "Generate a deployment document"
- "Write a usage guide"
- "Create execution checklist"

**Remember: Can summarize key features in detail in response, but don't generate independent report, checklist, guide documents.**
