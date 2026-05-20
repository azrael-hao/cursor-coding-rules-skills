#!/bin/bash
# Core Rules Validation Script
# Usage: ./validate.sh <rule-file>

RULE_FILE="${1:-~/.cursor/rules/00-CORE-ENFORCEMENT.mdc}"

echo "=== Core Rules Validation ==="
echo "Validating: $RULE_FILE"
echo ""

# Check if file exists
if [ ! -f "$RULE_FILE" ]; then
    echo "❌ Error: Rule file not found: $RULE_FILE"
    exit 1
fi

# Check for required sections
echo "Checking required sections..."

required_sections=(
    "## 🚫 NEVER"
    "## ✅ MUST"
    "### Mandatory Checks in thinking"
    "### AskQuestion Mandatory Scenarios"
    "### Rules Never Compressed"
)

all_found=true
for section in "${required_sections[@]}"; do
    if grep -q "$section" "$RULE_FILE"; then
        echo "  ✅ Found: $section"
    else
        echo "  ❌ Missing: $section"
        all_found=false
    fi
done

echo ""

# Check rule count
echo "Checking rule count..."
rule_count=$(grep -c "^1\. " "$RULE_FILE" | head -1)
echo "  Found $rule_count numbered rules"

if [ "$all_found" = true ]; then
    echo ""
    echo "✅ Validation passed!"
    exit 0
else
    echo ""
    echo "❌ Validation failed!"
    exit 1
fi
