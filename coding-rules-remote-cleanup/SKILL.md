---
name: coding-rules-remote-cleanup
description: When terminating tasks, must simultaneously terminate remote source processes to avoid server resource exhaustion.
---

# Remote Process Cleanup

## Core Principle

**When terminating local processes (SSH client, database client, etc.), must simultaneously terminate source processes on remote server triggered by that connection. Only terminating local connection will cause server resource exhaustion or even crash.**

## Trigger Scenarios

### 1. SSH Connection Interruption
- Before `kill` local SSH process, must first terminate remote executing commands through that connection or new connection
- If SSH executed database query through `docker exec`, need to first `KILL` at database level

### 2. Database Query Termination
- Before canceling local database client, must first execute `KILL <process_id>` on remote
- For queries executed through SSH tunnel, need to login database through new connection to terminate residual queries

### 3. Background Task Cancellation
- When canceling remote background task initiated locally, must confirm remote process terminated
- Cannot rely solely on local `kill` to terminate remote process

## Standard Cleanup Process

1. **Identify Remote Process**: Through `SHOW PROCESSLIST` or `ps aux` confirm remote process ID
2. **Terminate Remote Process**: Execute `KILL` command through new connection
3. **Verify Cleanup Result**: Query again to confirm remote process disappeared
4. **Terminate Local Process**: After confirming remote cleaned, then terminate local connection

## MySQL-Specific Cleanup

```sql
-- 1. View current active queries
SHOW PROCESSLIST;
-- Or more precise:
SELECT id, time, state, LEFT(info, 100) 
FROM information_schema.processlist
WHERE command != 'Sleep' AND time > 30;

-- 2. Terminate slow query
KILL <process_id>;

-- 3. Verify
SHOW PROCESSLIST;
```

## Forbidden Behaviors

- ❌ Forbidden to only `kill` local process without cleaning remote
- ❌ Forbidden to assume "remote will auto-terminate after disconnect"
- ❌ Forbidden to initiate new query without confirming remote cleanup complete

## Preventive Measures

- Set timeout for large table queries: `SET SESSION max_execution_time = 60000;`
- Avoid executing full table scans or no-index JOINs on remote
- For potentially time-consuming queries, first use `EXPLAIN` to evaluate
- Prioritize using `LIMIT` + sampling instead of full scan
