# Cursor Coding Skills

Professional collection of Cursor Agent Skills following official standards from [cursor.com/docs/skills](https://cursor.com/cn/docs/skills).

[中文文档](./README_zh.md)

## Skills Directory Structure

```
skills-cursor/
├── coding-rules-core-enforcement/       🔴 Highest Priority
├── coding-rules-context-compression/    📊 Core Workflow
├── coding-rules-no-assumption/          ⚠️ Core Principles
├── coding-rules-no-inference/           ⚠️ Core Principles  
├── coding-rules-decision-approval/      ⚠️ Core Principles
├── coding-rules-task-identification/    ⚠️ Core Principles
├── coding-rules-problem-focus/          📝 Workflow Tools
├── coding-rules-no-report-files/        📝 Workflow Tools
├── coding-rules-github-cli/             🛠️ Tool Guides
└── coding-rules-remote-cleanup/         🛠️ Tool Guides
```

## Skills List (10 Total)

### 🔴 Highest Priority (1)
- **coding-rules-core-enforcement** - Core mandatory rules, essential summary

### ⚠️ Core Principles (4)
- **coding-rules-no-assumption** - Zero speculation, must verify all facts
- **coding-rules-no-inference** - No inference without verification
- **coding-rules-decision-approval** - All user choices use AskQuestion tool
- **coding-rules-task-identification** - Distinguish tasks vs questions

### 📊 Core Workflow (1)
- **coding-rules-context-compression** - Context compression strategy

### 📝 Workflow Tools (2)
- **coding-rules-problem-focus** - Focus on differences for comparisons
- **coding-rules-no-report-files** - Forbid generating report documents

### 🛠️ Tool Guides (2)
- **coding-rules-github-cli** - GitHub CLI setup and configuration
- **coding-rules-remote-cleanup** - Remote process cleanup specification

## Rules vs Skills

### Rules (Behavioral Constraints)
- **Location**: `~/.cursor/rules/*.mdc`
- **Characteristics**: Mandatory, auto-enabled (alwaysApply: true)
- **Content**: NEVER/MUST principles, prohibitions
- **Repository**: https://github.com/azrael-hao/cursor-global-rules

### Skills (Method Guides) - THIS REPOSITORY
- **Location**: `~/.cursor/skills/skills-cursor/*.md`
- **Characteristics**: On-demand, agent decides when relevant
- **Content**: HOW TO execute, step-by-step guides
- **Repository**: https://github.com/azrael-hao/cursor-coding-rules-skills

## Installation

### Method 1: Git Clone (Recommended)

```bash
cd ~/.cursor/skills/
git clone https://github.com/azrael-hao/cursor-coding-rules-skills.git skills-cursor
```

### Method 2: GitHub Integration (Cursor 2.4+)

1. Open **Cursor Settings** → **Rules**
2. Click **Add Rule** → **Remote Rule (Github)**
3. Enter: `https://github.com/azrael-hao/cursor-coding-rules-skills`

### Method 3: Manual Download

1. Download this repository
2. Extract to:
   - Windows: `%USERPROFILE%\.cursor\skills\skills-cursor\`
   - macOS/Linux: `~/.cursor/skills/skills-cursor/`

## Usage

### Reference Skills in Cursor

Type `@` in chat to see available skills:

```
@coding-rules-core-enforcement
@coding-rules-no-assumption
@coding-rules-decision-approval
```

### Agent Auto-Invocation

Skills are automatically invoked by the agent when relevant. For example:
- User asks comparison → `coding-rules-problem-focus` auto-loads
- Agent needs decision → `coding-rules-decision-approval` auto-loads
- Context filling up → `coding-rules-context-compression` auto-loads

## Official Standards Compliance

Following [Cursor Agent Skills](https://cursor.com/cn/docs/skills) official specification:

- ✅ Flat directory structure (not nested, to ensure auto-discovery)
- ✅ SKILL.md format with YAML frontmatter
- ✅ Concise description field (agent uses for relevance judgment)
- ✅ Name field matches parent folder
- ✅ Lowercase names with hyphens only

## Statistics

- **Total Skills**: 10
- **Total Lines**: ~800 lines
- **Format**: Official SKILL.md standard
- **Languages**: English (primary), Chinese versions available in Rules repo

## Development

### Add New Skill

1. Create folder: `new-skill/`
2. Create file: `new-skill/SKILL.md`
3. Add frontmatter:

```yaml
---
name: new-skill
description: Brief description of when to use this skill.
---

# Skill Title

Detailed instructions for the agent...
```

### Commit and Push

```bash
git add .
git commit -m "feat: add new-skill"
git push origin main
```

## Quick Reference

| Skill | When Agent Invokes | Priority |
|-------|-------------------|----------|
| core-enforcement | Every operation | 🔴 Critical |
| no-assumption | Before accessing fields/methods | ⚠️ High |
| no-inference | Before making claims | ⚠️ High |
| decision-approval | User choice needed | ⚠️ High |
| task-identification | Unclear request type | ⚠️ High |
| context-compression | Context near limit | 📊 Medium |
| problem-focus | Comparison questions | 📝 Medium |
| no-report-files | About to create .md file | 📝 Medium |
| github-cli | Managing rules repo | 🛠️ Low |
| remote-cleanup | Terminating processes | 🛠️ Low |

## Related Resources

- **Rules Repository**: [cursor-global-rules](https://github.com/azrael-hao/cursor-global-rules)
- **Official Docs**: [cursor.com/docs/skills](https://cursor.com/cn/docs/skills)
- **Open Standard**: [agentskills.io](https://agentskills.io)

---

**Optimized for Cursor Agent · Following Official Standards · MIT License**
