# Cursor Coding Skills

Optimized Cursor Skills collection for task-specific capabilities and tools.

[中文文档](./README_zh.md)

## ✅ Correct Directory Structure

```
skills-cursor/
├── coding-rules-context-compression/SKILL.md   ℹ️ Context Compression
├── coding-rules-remote-cleanup/SKILL.md        ℹ️ Remote Process Cleanup
├── coding-rules-github-cli/SKILL.md            🛠️ GitHub CLI Guide
└── coding-rules-zh/                            📁 Chinese Versions (Backup)
```

## 📋 Skills List (3 Skills)

### ℹ️ Workflow Tools (2)
- **coding-rules-context-compression** - Context compression strategy when approaching capacity
- **coding-rules-remote-cleanup** - Remote process cleanup specification

### 🛠️ Tool Configuration (1)
- **coding-rules-github-cli** - GitHub CLI configuration and usage guide

## 🎯 Skills vs Rules Distinction

### Skills (This Repository)
- **Purpose**: Provide capabilities and methods
- **Trigger**: User @reference or description conditions
- **Scenario**: Complete specific tasks
- **Characteristics**: Tool-oriented, optional, task-specific
- **Examples**: How to analyze problems, optimize performance, use tools

### Rules (Another Repository)
- **Purpose**: Enforce constraints and standards
- **Trigger**: `alwaysApply: true` automatically effective
- **Scenario**: Must-follow rules like coding standards
- **Characteristics**: Mandatory, automatic, global
- **Repository**: https://github.com/azrael-hao/cursor-global-rules

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
@coding-rules-context-compression
@coding-rules-remote-cleanup
@coding-rules-github-cli
```

### View Available Skills:
Type `@coding-rules-` in Cursor to see all available skills

## 📊 Optimization Record

- **Original Count**: 11 skill directories
- **Optimized**: 4 directories (3 skills + 1 Chinese backup)
- **Reduction**: 64%
- **Optimization Principle**: 
  - Removed duplicates (already exist as Rules)
  - Kept tool-oriented, task-specific skills
  - Separated mandatory rules to Rules repository

## 🌐 GitHub Repository

- **Repository**: https://github.com/azrael-hao/cursor-coding-rules-skills
- **Branch**: main
- **Languages**: English (default), Chinese (in coding-rules-zh/)

## ⚡ Quick Reference

| Skill Name | Purpose | Type |
|-----------|---------|------|
| context-compression | Context management strategy | ℹ️ Workflow |
| remote-cleanup | Remote process cleanup | ℹ️ Workflow |
| github-cli | GitHub CLI usage guide | 🛠️ Tool |

## 📝 Relationship with Rules

This Skills repository complements the Rules repository:
- **Rules**: Mandatory constraints, auto-loaded (9 rules)
- **Skills**: Optional tools, on-demand usage (3 skills)
- **Separation**: Clear distinction, no duplication

Related repositories:
- Rules: https://github.com/azrael-hao/cursor-global-rules
- Skills: https://github.com/azrael-hao/cursor-coding-rules-skills (current)

---

**Made with ❤️ for Cursor AI**

**Last Updated**: April 27, 2026
