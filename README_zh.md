# Cursor 编程技能集

遵循 [cursor.com/docs/skills](https://cursor.com/cn/docs/skills) 官方标准的专业 Cursor Agent Skills 集合。

[English Docs](./README.md)

## Skills 目录结构

```
skills-cursor/
├── coding-rules-core-enforcement/       🔴 最高优先级
├── coding-rules-context-compression/    📊 核心工作流
├── coding-rules-no-assumption/          ⚠️ 核心原则
├── coding-rules-no-inference/           ⚠️ 核心原则  
├── coding-rules-decision-approval/      ⚠️ 核心原则
├── coding-rules-task-identification/    ⚠️ 核心原则
├── coding-rules-problem-focus/          📝 工作流工具
├── coding-rules-no-report-files/        📝 工作流工具
├── coding-rules-github-cli/             🛠️ 工具指南
└── coding-rules-remote-cleanup/         🛠️ 工具指南
```

## Skills 列表（共10个）

### 🔴 最高优先级（1个）
- **coding-rules-core-enforcement** - 核心强制规则，精华总结

### ⚠️ 核心原则（4个）
- **coding-rules-no-assumption** - 零臆想，必须验证所有事实
- **coding-rules-no-inference** - 禁止推断，必须验证
- **coding-rules-decision-approval** - 所有用户选择使用AskQuestion工具
- **coding-rules-task-identification** - 区分任务与问题

### 📊 核心工作流（1个）
- **coding-rules-context-compression** - 上下文压缩策略

### 📝 工作流工具（2个）
- **coding-rules-problem-focus** - 对比问题聚焦差异
- **coding-rules-no-report-files** - 禁止生成报告文档

### 🛠️ 工具指南（2个）
- **coding-rules-github-cli** - GitHub CLI 安装配置
- **coding-rules-remote-cleanup** - 远程进程清理规范

## Rules vs Skills 区别

### Rules（行为约束）
- **位置**: `~/.cursor/rules/*.mdc`
- **特征**: 强制性，自动生效（alwaysApply: true）
- **内容**: NEVER/MUST 原则，禁止事项
- **仓库**: https://github.com/azrael-hao/cursor-global-rules

### Skills（方法指南）- 本仓库
- **位置**: `~/.cursor/skills/skills-cursor/*.md`
- **特征**: 按需触发，Agent判断相关性
- **内容**: HOW TO 执行，分步指南
- **仓库**: https://github.com/azrael-hao/cursor-coding-rules-skills

## 安装

### 方式一：Git 克隆（推荐）

```bash
cd ~/.cursor/skills/
git clone https://github.com/azrael-hao/cursor-coding-rules-skills.git skills-cursor
```

### 方式二：GitHub 集成（Cursor 2.4+）

1. 打开 **Cursor Settings** → **Rules**
2. 点击 **Add Rule** → **Remote Rule (Github)**
3. 输入：`https://github.com/azrael-hao/cursor-coding-rules-skills`

### 方式三：手动下载

1. 下载本仓库
2. 解压到：
   - Windows: `%USERPROFILE%\.cursor\skills\skills-cursor\`
   - macOS/Linux: `~/.cursor/skills/skills-cursor/`

## 使用

### 在 Cursor 中引用 Skills

在对话中输入 `@` 查看可用技能：

```
@coding-rules-core-enforcement
@coding-rules-no-assumption
@coding-rules-decision-approval
```

### Agent 自动调用

Agent 会在相关时自动调用 Skills。例如：
- 用户问对比问题 → `coding-rules-problem-focus` 自动加载
- Agent 需要决策 → `coding-rules-decision-approval` 自动加载
- 上下文接近容量 → `coding-rules-context-compression` 自动加载

## 符合官方标准

遵循 [Cursor Agent Skills](https://cursor.com/cn/docs/skills) 官方规范：

- ✅ 扁平目录结构（非嵌套，确保自动发现）
- ✅ SKILL.md 格式，带 YAML frontmatter
- ✅ 简洁的 description 字段（Agent用于判断相关性）
- ✅ name 字段与父文件夹一致
- ✅ 仅使用小写字母和连字符

## 统计

- **Skills 总数**: 10
- **总行数**: ~800 行
- **格式**: 官方 SKILL.md 标准
- **语言**: 英文（主要），中文版在 Rules 仓库中

## 开发

### 添加新 Skill

1. 创建文件夹：`new-skill/`
2. 创建文件：`new-skill/SKILL.md`
3. 添加 frontmatter：

```yaml
---
name: new-skill
description: 简要描述何时使用此技能。
---

# 技能标题

为 Agent 提供的详细指令...
```

### 提交和推送

```bash
git add .
git commit -m "feat: add new-skill"
git push origin main
```

## 快速参考

| Skill | Agent 调用时机 | 优先级 |
|-------|---------------|--------|
| core-enforcement | 每次操作 | 🔴 关键 |
| no-assumption | 访问字段/方法前 | ⚠️ 高 |
| no-inference | 做出声明前 | ⚠️ 高 |
| decision-approval | 需要用户选择 | ⚠️ 高 |
| task-identification | 请求类型不明 | ⚠️ 高 |
| context-compression | 上下文接近容量 | 📊 中 |
| problem-focus | 对比问题 | 📝 中 |
| no-report-files | 即将创建.md文件 | 📝 中 |
| github-cli | 管理规则仓库 | 🛠️ 低 |
| remote-cleanup | 终止进程 | 🛠️ 低 |

## 相关资源

- **Rules 仓库**: [cursor-global-rules](https://github.com/azrael-hao/cursor-global-rules)
- **官方文档**: [cursor.com/docs/skills](https://cursor.com/cn/docs/skills)
- **开放标准**: [agentskills.io](https://agentskills.io)

---

**为 Cursor Agent 优化 · 遵循官方标准 · MIT License**
