---
name: github-cli
description: GitHub CLI 安装、代理配置与全局规则仓库同步。
---

# GitHub CLI 连接与全局规则管理

## 环境准备

### 检测与安装
```bash
gh --version  # 检测

# Windows 安装（代理环境）
curl -L -x http://127.0.0.1:7897 -o /tmp/gh_installer.msi \
  "https://github.com/cli/cli/releases/latest/download/gh_<VERSION>_windows_amd64.msi"
powershell -Command "Start-Process msiexec.exe -ArgumentList '/i','C:\Users\admin\AppData\Local\Temp\gh_installer.msi','/quiet','/norestart' -Wait -Verb RunAs"
export PATH="/c/Program Files/GitHub CLI:$PATH"
```

### 代理配置（必须）
```bash
export HTTPS_PROXY=http://127.0.0.1:7897
export HTTP_PROXY=http://127.0.0.1:7897

# 测试代理端口（返回200或302即可用）
curl -s --connect-timeout 3 -x http://127.0.0.1:7890 https://www.google.com -o /dev/null -w "%{http_code}"
```

## GitHub 认证

```bash
export PATH="/c/Program Files/GitHub CLI:$PATH"
export HTTPS_PROXY=http://127.0.0.1:7897
gh auth login --web --git-protocol https
```
在浏览器打开 https://github.com/login/device 输入一次性代码授权。

验证：`gh auth status`

## 全局规则仓库操作

**仓库**: `https://github.com/azrael-hao/cursor-global-rules`  
**本地**: `~/.cursor/rules/`（Windows: `%USERPROFILE%\.cursor\rules\`）

```bash
# 首次加载
cd ~/.cursor/rules/
git init && git remote add origin https://github.com/azrael-hao/cursor-global-rules.git
export HTTPS_PROXY=http://127.0.0.1:7897 && git pull origin master

# 同步更新
cd ~/.cursor/rules/ && export HTTPS_PROXY=http://127.0.0.1:7897 && git pull origin master

# 上传新规则
cd ~/.cursor/rules/ && git add -A && git commit -m "Update rules"
export HTTPS_PROXY=http://127.0.0.1:7897 && git push origin master
```

## 速查命令

```bash
# 一键设置环境
export PATH="/c/Program Files/GitHub CLI:$PATH"
export HTTPS_PROXY=http://127.0.0.1:7897
export HTTP_PROXY=http://127.0.0.1:7897

# 检查 + 同步 + 上传
gh auth status
cd ~/.cursor/rules/ && git pull origin master
cd ~/.cursor/rules/ && git add -A && git commit -m "Update" && git push origin master
```

**记住：所有git/gh操作前必须设置代理环境变量。**
