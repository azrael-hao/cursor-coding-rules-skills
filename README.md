# Cursor Coding Rules Skills

Optimized Cursor Skills collection using flat directory structure to ensure automatic loading by Cursor.

[中文文档](./README_zh.md)

## ✅ Correct Directory Structure

```
skills-cursor/
├── coding-rules-core-enforcement/SKILL.md       🔴 Highest Priority
├── coding-rules-no-assumption/SKILL.md          ⚠️ Core Principles
├── coding-rules-no-inference/SKILL.md           ⚠️ Core Principles
├── coding-rules-task-identification/SKILL.md    ⚠️ Core Principles
├── coding-rules-decision-approval/SKILL.md      ⚠️ Core Principles
├── coding-rules-problem-focus/SKILL.md          ℹ️ Workflow
├── coding-rules-no-report-files/SKILL.md        ℹ️ Workflow
├── coding-rules-context-compression/SKILL.md    ℹ️ Workflow
├── coding-rules-remote-cleanup/SKILL.md         ℹ️ Workflow
├── coding-rules-github-cli/SKILL.md             ℹ️ Tool Config
└── coding-rules-zh/                             📁 Chinese Versions
```

## 📋 Skills List

### 🔴 Highest Priority
- **coding-rules-core-enforcement**: Core enforcement rules, essential summary of all rules

### ⚠️ Core Principles
- **coding-rules-no-assumption**: Zero speculation principle, no guessing or assumptions
- **coding-rules-no-inference**: No inference principle, must verify facts
- **coding-rules-task-identification**: Task vs question identification
- **coding-rules-decision-approval**: Decision change approval rules

### ℹ️ Workflow
- **coding-rules-problem-focus**: Essential problem focus (comparison problems)
- **coding-rules-no-report-files**: Forbidden to generate document files
- **coding-rules-context-compression**: Context compression strategy
- **coding-rules-remote-cleanup**: Remote process cleanup specification

### 🛠️ Tool Configuration
- **coding-rules-github-cli**: GitHub CLI configuration and usage

## 🎯 Why Flat Structure?

Cursor's skill scanner uses fixed glob patterns:
- `*/SKILL.md`
- `*/skills/*/SKILL.md`
- `*/*/*/skills/*/SKILL.md`

**Does NOT support** nested structures like `*/skills/*/*/SKILL.md`

### ❌ Wrong Nested Structure (Won't Load)
```
coding-rules/
  ├── core-enforcement/SKILL.md
  ├── no-assumption/SKILL.md
  └── ...
```

### ✅ Correct Flat Structure (Will Auto-Load)
```
skills-cursor/
  ├── coding-rules-core-enforcement/SKILL.md
  ├── coding-rules-no-assumption/SKILL.md
  └── ...
```

## 📦 Installation

### Method 1: Clone Locally
```bash
cd ~/.cursor/
git clone https://github.com/azrael-hao/cursor-coding-rules-skills.git skills-cursor
```

### Method 2: Manual Download
1. Download this repository
2. Extract to `~/.cursor/skills-cursor/` (Windows: `%USERPROFILE%\.cursor\skills-cursor\`)

## 🎓 Usage

### Reference Skills in Cursor:
```
@coding-rules-core-enforcement
@coding-rules-no-assumption
@coding-rules-decision-approval
```

### View Available Skills:
Type `@coding-rules-` in Cursor to see all available skills

## 📊 Statistics

- **Skills Count**: 10
- **Total Lines**: 748 lines
- **Optimization**: Compressed 15% from original rules
- **Source**: Converted from Cursor global rules (.mdc format)
- **Languages**: English (default), Chinese (in coding-rules-zh/)

## 🔄 Priority System

```
coding-rules-core-enforcement 🔴 Highest Priority
  ↓
Core Principle Skills ⚠️
  ↓
Workflow Skills ℹ️
```

## 📝 Maintenance Notes

This Skills collection is converted from Cursor global rules, maintained in sync with rule files.

- **Original Rules Location**: `~/.cursor/rules/`
- **Skills Location**: `~/.cursor/skills-cursor/`
- **GitHub Repository**: https://github.com/azrael-hao/cursor-coding-rules-skills

## ⚡ Quick Reference

| Skill Name | Purpose | Priority |
|-----------|---------|----------|
| core-enforcement | Core mandatory rules (must read) | 🔴 Highest |
| no-assumption | No speculation or guessing | ⚠️ Core |
| no-inference | No inference, must verify | ⚠️ Core |
| task-identification | Distinguish tasks vs questions | ⚠️ Core |
| decision-approval | Decisions need user confirmation | ⚠️ Core |
| problem-focus | Focus on differences for comparison | ℹ️ Workflow |
| no-report-files | No report document generation | ℹ️ Workflow |
| context-compression | Context compression strategy | ℹ️ Workflow |
| remote-cleanup | Remote process cleanup | ℹ️ Workflow |
| github-cli | GitHub CLI configuration | 🛠️ Tool |

---

**Made with ❤️ for Cursor AI**
