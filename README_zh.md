# Cursor 编码 Skills

优化后的Cursor Skills集合，用于特定任务的能力和工具。

[English Documentation](./README.md)

## ✅ 正确的目录结构

```
skills-cursor/
├── coding-rules-context-compression/SKILL.md   ℹ️ 上下文压缩
├── coding-rules-remote-cleanup/SKILL.md        ℹ️ 远端进程清理
├── coding-rules-github-cli/SKILL.md            🛠️ GitHub CLI指南
└── coding-rules-zh/                            📁 中文版本（备份）
```

## 📋 Skills列表（3个）

### ℹ️ 工作流程工具（2个）
- **coding-rules-context-compression** - 上下文接近容量时的压缩策略
- **coding-rules-remote-cleanup** - 远端进程清理规范

### 🛠️ 工具配置（1个）
- **coding-rules-github-cli** - GitHub CLI配置和使用指南

## 🎯 Skills vs Rules 区分

### Skills（本仓库）
- **目的**：提供能力和方法
- **触发**：用户@引用 或 description触发条件
- **场景**：完成特定任务的技能
- **特点**：工具性、可选性、任务导向
- **示例**：如何分析问题、如何优化性能、如何使用工具

### Rules（另一仓库）
- **目的**：强制约束和规范
- **触发**：`alwaysApply: true` 自动生效
- **场景**：必须遵守的规则，如编码规范
- **特点**：约束性、强制性、全局性
- **仓库**：https://github.com/azrael-hao/cursor-global-rules

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
@coding-rules-context-compression
@coding-rules-remote-cleanup
@coding-rules-github-cli
```

### 查看可用Skills：
在Cursor中输入 `@coding-rules-` 会自动提示所有可用的skills

## 📊 优化记录

- **原始数量**: 11个skill目录
- **优化后**: 4个目录（3个skills + 1个中文备份）
- **精简度**: 64%
- **优化原则**: 
  - 删除了重复内容（Rules中已有）
  - 保留了工具导向、任务特定的skills
  - 将强制性规则分离到Rules仓库

## 🌐 GitHub仓库

- **仓库**: https://github.com/azrael-hao/cursor-coding-rules-skills
- **分支**: main
- **语言**: 英文（默认），中文（在coding-rules-zh/目录）

## ⚡ 快速参考

| Skill名称 | 用途 | 类型 |
|----------|------|------|
| context-compression | 上下文管理策略 | ℹ️ 工作流程 |
| remote-cleanup | 远端进程清理 | ℹ️ 工作流程 |
| github-cli | GitHub CLI使用指南 | 🛠️ 工具 |

## 📝 与Rules的关系

本Skills仓库与Rules仓库互补：
- **Rules**: 强制约束，自动加载（9个规则）
- **Skills**: 可选工具，按需使用（3个技能）
- **分离原则**: 清晰区分，无重复

相关仓库：
- Rules: https://github.com/azrael-hao/cursor-global-rules
- Skills: https://github.com/azrael-hao/cursor-coding-rules-skills（当前）

---

**Made with ❤️ for Cursor AI**

**最后更新**: 2026年4月27日
