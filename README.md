# Cursor Coding Rules Skills

这是优化后的Cursor Skills集合，使用扁平目录结构以确保被Cursor自动加载。

## ✅ 正确的目录结构

```
skills-cursor/
├── coding-rules-core-enforcement/SKILL.md       🔴 最高优先级
├── coding-rules-no-assumption/SKILL.md          ⚠️ 核心原则
├── coding-rules-no-inference/SKILL.md           ⚠️ 核心原则
├── coding-rules-task-identification/SKILL.md    ⚠️ 核心原则
├── coding-rules-decision-approval/SKILL.md      ⚠️ 核心原则
├── coding-rules-problem-focus/SKILL.md          ℹ️ 工作流程
├── coding-rules-no-report-files/SKILL.md        ℹ️ 工作流程
├── coding-rules-context-compression/SKILL.md    ℹ️ 工作流程
├── coding-rules-remote-cleanup/SKILL.md         ℹ️ 工作流程
└── coding-rules-github-cli/SKILL.md             ℹ️ 工具配置
```

## 📋 Skills列表

### 🔴 最高优先级
- **coding-rules-core-enforcement**: 核心强制执行规则，所有规则的精华总结

### ⚠️ 核心原则
- **coding-rules-no-assumption**: 零臆想原则，禁止猜测和假设
- **coding-rules-no-inference**: 禁止推断原则，必须验证事实
- **coding-rules-task-identification**: 任务与问题识别
- **coding-rules-decision-approval**: 决策变更审批规则

### ℹ️ 工作流程
- **coding-rules-problem-focus**: 本质问题聚焦（对比型问题）
- **coding-rules-no-report-files**: 禁止生成文档类文件
- **coding-rules-context-compression**: 上下文压缩策略
- **coding-rules-remote-cleanup**: 远端进程清理规范

### 🛠️ 工具配置
- **coding-rules-github-cli**: GitHub CLI配置和使用

## 🎯 为什么使用扁平结构？

Cursor的技能扫描器使用固定的glob模式：
- `*/SKILL.md`
- `*/skills/*/SKILL.md`
- `*/*/*/skills/*/SKILL.md`

**不支持**嵌套结构如 `*/skills/*/*/SKILL.md`

### ❌ 错误的嵌套结构（不会被加载）
```
coding-rules/
  ├── core-enforcement/SKILL.md
  ├── no-assumption/SKILL.md
  └── ...
```

### ✅ 正确的扁平结构（会被自动加载）
```
skills-cursor/
  ├── coding-rules-core-enforcement/SKILL.md
  ├── coding-rules-no-assumption/SKILL.md
  └── ...
```

## 📦 安装方式

### 方式1：Clone到本地
```bash
cd ~/.cursor/
git clone https://github.com/azrael-hao/cursor-coding-rules-skills.git skills-cursor
```

### 方式2：手动下载
1. 下载本仓库
2. 解压到 `~/.cursor/skills-cursor/`（Windows: `%USERPROFILE%\.cursor\skills-cursor\`）

## 🎓 使用方式

### 在Cursor中引用Skills：
```
@coding-rules-core-enforcement
@coding-rules-no-assumption
@coding-rules-decision-approval
```

### 查看可用Skills：
在Cursor中输入 `@coding-rules-` 会自动提示所有可用的skills

## 📊 统计信息

- **Skills数量**: 10个
- **总行数**: 748行
- **优化程度**: 从原始规则压缩15%
- **转换来源**: Cursor全局规则（.mdc格式）

## 🔄 优先级体系

```
coding-rules-core-enforcement 🔴 最高优先级
  ↓
核心原则 Skills ⚠️
  ↓
工作流程 Skills ℹ️
```

## 📝 维护说明

本Skills集合从Cursor全局规则转换而来，保持与规则文件同步更新。

- **原始规则位置**: `~/.cursor/rules/`
- **Skills位置**: `~/.cursor/skills-cursor/`
- **GitHub仓库**: https://github.com/azrael-hao/cursor-coding-rules-skills

## ⚡ 快速参考

| Skill名称 | 用途 | 优先级 |
|----------|------|--------|
| core-enforcement | 核心强制规则（必读） | 🔴 最高 |
| no-assumption | 禁止臆想猜测 | ⚠️ 核心 |
| no-inference | 禁止推断，必须验证 | ⚠️ 核心 |
| task-identification | 区分任务和问题 | ⚠️ 核心 |
| decision-approval | 决策需用户确认 | ⚠️ 核心 |
| problem-focus | 对比型问题聚焦差异 | ℹ️ 流程 |
| no-report-files | 禁止生成报告文档 | ℹ️ 流程 |
| context-compression | 上下文压缩策略 | ℹ️ 流程 |
| remote-cleanup | 远端进程清理 | ℹ️ 流程 |
| github-cli | GitHub CLI配置 | 🛠️ 工具 |

---

**Made with ❤️ for Cursor AI**
