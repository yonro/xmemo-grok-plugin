---
name: xmemo-audit-progress
description: Audit implementation or project progress against the approved XMemo plan, last checkpoint, decisions, TODOs, and current workspace evidence. Use to verify another agent's report, detect drift, reconcile conflicting claims, or determine the exact next action.
---

# Audit project progress

1. Establish the approved baseline: plan revision, decisions, acceptance criteria, checkpoint, and known blockers.
2. Inspect current files, diffs, commits, tests, logs, deployments, and explicit user confirmations.
3. Classify every material claim as `verified`, `partial`, `claimed`, `stale`, `conflicting`, or `blocked`.
4. Identify scope drift, missing evidence, regressions, hidden dependencies, and stale TODOs.
5. Return a verdict, evidence matrix, blocking findings, remaining work, risk, and one exact next action.
6. Update XMemo only with verified net-new state: replace the checkpoint, complete proven TODOs, record a material milestone, or preserve a durable lesson.

Never promote an agent's statement to verified status without evidence.

