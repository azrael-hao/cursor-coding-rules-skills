---
name: coding-rules-no-report-files
description: Forbidden to generate report documents. Must summarize in chat response instead. No *.md, *.txt report files.
---

# No Report Files

Forbidden to generate document files. Summarize in chat response instead.

## 🚫 NEVER Generate

File patterns that are forbidden:
- `*报告.md` / `*report.md`
- `*清单.md` / `*list.md`
- `*说明.md` / `*doc.md`  
- `*总结.md` / `*summary.md`
- `*分析.md` / `*analysis.md`
- `*验证.txt` / `*validation.txt`

## ✅ MUST Do Instead

### Summarize in Response
- ✅ Detailed summary in chat (can be long)
- ✅ Use markdown formatting in response
- ✅ Include tables, code blocks, lists
- ✅ Multiple paragraphs okay

### Allowed Files
- ✅ Source code files (.java, .ts, .py)
- ✅ Config files (.yaml, .json, .properties)
- ✅ SQL scripts (.sql)
- ✅ Shell scripts (.sh)
- ✅ Documentation in code comments

## Exception

**ONLY** create report files when:
- User **explicitly requests** a file
- User says "create a document" or "save to file"

Otherwise, **always** summarize in chat response.

## Example

**❌ Wrong:**
```
Let me create a validation report...
[Creates: validation_report.md]
```

**✅ Correct:**
```
Validation Results:

1. Schema Validation: ✅ Passed
   - All tables exist
   - Indexes properly configured

2. Data Validation: ⚠️ Issues Found
   - Table X: 3 orphaned records
   - Table Y: 5 duplicate keys

Recommendation: Clean orphaned records before deployment.
```

## Related Skills

- `coding-rules-core-enforcement` - Document generation rules
