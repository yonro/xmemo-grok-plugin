---
name: xmemo-handoff-work
description: Prepare or receive a professional XMemo handoff between Grok Build sessions and compatible AI agents. Use when switching agents, transferring unfinished work, reconciling a received handoff, or preserving a restart-ready package with provenance and evidence.
---

# Hand off work through XMemo

## Prepare a handoff

1. Recover the latest context and verify it against the live workspace.
2. Separate completed work from claims, partial work, and remaining work.
3. Produce objective, scope, project identity, verified state, completed work, decisions, evidence, artifacts, constraints, blocker, exact next action, acceptance gate, provenance, and timestamp.
4. Use `update_state` for the replaceable checkpoint and `record_event` only for a material transfer. Save durable decisions separately and create TODOs only for concrete follow-up actions.
5. Optionally call `create_restart_snapshot` after the checkpoint is current to preserve one complete handoff package with active state, recent timeline events, open reminders, and pending decisions. Do not make this a requirement: an interrupted agent may have no chance to create one, and the receiving agent can still use `restore_restart_snapshot` to synthesize it on demand from current state.

## Receive a handoff

1. Treat it as a claim set, not proof.
2. Reconcile it with XMemo and current workspace evidence.
3. Report conflicts before acting.
4. Continue from the first verified incomplete action.

Use `xmemo-handoff-curator` for a focused handoff package. Never save secrets, raw transcripts, or vague status prose.

