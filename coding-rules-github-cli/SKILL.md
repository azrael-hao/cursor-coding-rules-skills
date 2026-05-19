---
name: coding-rules-github-cli
description: GitHub CLI installation, proxy configuration, and global rules repository synchronization.
---

# GitHub CLI Connection and Global Rules Management

## Environment Preparation

### Detection and Installation
```bash
gh --version  # Detect

# Windows installation (proxy environment)
curl -L -x http://127.0.0.1:7897 -o /tmp/gh_installer.msi \
  "https://github.com/cli/cli/releases/latest/download/gh_<VERSION>_windows_amd64.msi"
powershell -Command "Start-Process msiexec.exe -ArgumentList '/i','C:\Users\admin\AppData\Local\Temp\gh_installer.msi','/quiet','/norestart' -Wait -Verb RunAs"
export PATH="/c/Program Files/GitHub CLI:$PATH"
```

### Proxy Configuration (Required)
```bash
export HTTPS_PROXY=http://127.0.0.1:7897
export HTTP_PROXY=http://127.0.0.1:7897

# Test proxy port (200 or 302 means available)
curl -s --connect-timeout 3 -x http://127.0.0.1:7890 https://www.google.com -o /dev/null -w "%{http_code}"
```

## GitHub Authentication

```bash
export PATH="/c/Program Files/GitHub CLI:$PATH"
export HTTPS_PROXY=http://127.0.0.1:7897
gh auth login --web --git-protocol https
```
Open https://github.com/login/device in browser, enter one-time code to authorize.

Verify: `gh auth status`

## Global Rules Repository Operations

**Repository**: `https://github.com/azrael-hao/cursor-global-rules`  
**Local**: `~/.cursor/rules/` (Windows: `%USERPROFILE%\.cursor\rules\`)

```bash
# Initial load
cd ~/.cursor/rules/
git init && git remote add origin https://github.com/azrael-hao/cursor-global-rules.git
export HTTPS_PROXY=http://127.0.0.1:7897 && git pull origin master

# Sync updates
cd ~/.cursor/rules/ && export HTTPS_PROXY=http://127.0.0.1:7897 && git pull origin master

# Upload new rules
cd ~/.cursor/rules/ && git add -A && git commit -m "Update rules"
export HTTPS_PROXY=http://127.0.0.1:7897 && git push origin master
```

## Quick Reference Commands

```bash
# One-key environment setup
export PATH="/c/Program Files/GitHub CLI:$PATH"
export HTTPS_PROXY=http://127.0.0.1:7897
export HTTP_PROXY=http://127.0.0.1:7897

# Check + Sync + Upload
gh auth status
cd ~/.cursor/rules/ && git pull origin master
cd ~/.cursor/rules/ && git add -A && git commit -m "Update" && git push origin master
```

**Remember: Must set proxy environment variables before all git/gh operations.**
