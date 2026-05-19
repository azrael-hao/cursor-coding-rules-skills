---
name: remote-cleanup
description: 终止任务时必须同时终止远端源头进程，避免服务器资源耗尽。
---

# 远端进程清理

## 核心原则

**当终止本地进程（SSH客户端、数据库客户端等）时，必须同时终止远端服务器上由该连接触发的源头进程。仅终止本地连接会导致服务器资源耗尽甚至宕机。**

## 触发场景

### 1. SSH 连接中断
- `kill` 本地 SSH 进程前，必须先终止远端正在执行的命令
- 如果通过 `docker exec` 执行数据库查询，需先在数据库层面 `KILL` 对应查询

### 2. 数据库查询终止
- 取消本地数据库客户端前，必须先在远端执行 `KILL <process_id>`
- 对于通过 SSH 隧道执行的查询，需通过新连接登录数据库终止残留查询

### 3. 后台任务取消
- 取消本地发起的远端后台任务时，必须确认远端进程已终止
- 不能仅依赖本地 `kill` 来终止远端进程

## 标准清理流程

1. **识别远端进程**：通过 `SHOW PROCESSLIST` 或 `ps aux` 确认远端进程 ID
2. **终止远端进程**：通过新连接执行 `KILL` 命令
3. **验证清理结果**：再次查询确认远端进程已消失
4. **终止本地进程**：确认远端已清理后，再终止本地连接

## MySQL 专用清理

```sql
-- 1. 查看当前活跃查询
SHOW PROCESSLIST;
-- 或更精确：
SELECT id, time, state, LEFT(info, 100) 
FROM information_schema.processlist
WHERE command != 'Sleep' AND time > 30;

-- 2. 终止慢查询
KILL <process_id>;

-- 3. 验证
SHOW PROCESSLIST;
```

## 禁止行为

- ❌ 禁止仅 `kill` 本地进程而不清理远端
- ❌ 禁止假设"断开连接后远端会自动终止"
- ❌ 禁止在未确认远端清理完成时发起新查询

## 预防措施

- 对大表查询设置超时：`SET SESSION max_execution_time = 60000;`
- 避免在远端执行全表扫描或无索引 JOIN
- 对可能耗时的查询，先用 `EXPLAIN` 评估
- 优先使用 `LIMIT` + 采样替代全量扫描
