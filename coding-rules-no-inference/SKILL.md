---
name: coding-rules-no-inference
description: Forbidden to determine facts through inference, must obtain through actual verification.
---

# No Inference - Mandatory Verification

## Core Principle

**Forbidden to determine any verifiable facts through inference, guessing, or assumptions. All key information must be confirmed through actual query, testing, or inspection.**

**Zero tolerance principle**: For verifiable facts, 0% inference acceptable, 100% must verify.

## Scenarios Requiring Verification

### 1. Database Structure Information
❌ Forbidden to infer: Infer field names based on naming conventions, infer table associations based on business logic  
✅ Must verify: `DESCRIBE table_name`, `SHOW COLUMNS`

### 2. API Interfaces and Function Signatures
❌ Forbidden to infer: Infer parameters based on function names  
✅ Must verify: `help(function)`, `inspect.signature()`

### 3. Config Files and Environment Variables
❌ Forbidden to infer: Assume config items exist  
✅ Must verify: Read actual config files

### 4. File Paths and Resource Locations
❌ Forbidden to infer: Assume files exist at certain locations  
✅ Must verify: `ls`, `find`, `glob` tools

### 5. Code Logic and Business Processes
❌ Forbidden to infer: Assume code executes in standard process  
✅ Must verify: Read actual code, trace call chain

### 6. Dependency Versions and Compatibility
❌ Forbidden to infer: Assume version compatibility  
✅ Must verify: Check `package.json`, `requirements.txt`

## Verification Method Selection

| Scenario | Verification Method |
|----------|---------------------|
| Database structure | SQL query (DESCRIBE/SHOW) |
| Methods/classes/fields in code | Grep search + Read |
| File existence | Glob search or Shell ls |
| API behavior | View docs + actual test |
| Config items | Read config file |
| Table associations | SQL query test JOIN |
| Function call chain | Grep search + layer-by-layer Read |
| Environment variables | Shell echo $VAR |

## Mandatory Verification Process

1. Find needed information → Don't infer
2. Select verification method → Use methods from table above
3. Execute verification → Obtain actual results
4. Base decisions on verification results → Not inference

## Self-Check List

- [ ] Has every field name I use been verified to exist?
- [ ] Has every method I use been confirmed for signature?
- [ ] Have the associations I assume been tested and verified?
- [ ] Have the file paths I reference been confirmed to exist?
- [ ] Have the config items I depend on been read and confirmed?

**Remember: What can be verified must be verified. No exceptions.**
