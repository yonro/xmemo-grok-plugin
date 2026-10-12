---
name: xmemo-memory-steward
description: Coordinate XMemo memory across Grok Build sessions and compatible AI agents. Use when a task mixes recall, durable capture, decisions, TODOs, checkpoints, project context, lifecycle actions, or handoffs and needs the correct XMemo tool and safety policy.
---

# XMemo memory steward

Use XMemo as a user-controlled continuity layer, not as a transcript archive or a replacement for live repository evidence.

## Route the request

- Focused semantic recall: `recall`
- Bounded multi-memory context: `recall_context`
- Known project context: `get_project_context`
- Connection identity and scopes: `get_mcp_identity`
- New durable concept: `remember`
- Existing concept revision: `update_memory`
- Replaceable working checkpoint: `update_state`
- Significant milestone or handoff: `record_event`
- Project history: `get_timeline`
- Memory explanation or provenance: `explain_memory`, `list_memory_versions`
- Recoverable deletion: `forget` with its default soft behavior
- Restore eligible deletion: `restore_memory`

Read [references/tool-routing.md](references/tool-routing.md) when exact routing or current Grok Build surface boundaries matter. Read [references/memory-policy.md](references/memory-policy.md) before consequential writes, lifecycle actions, or automatic checkpoint handling.

## Core workflow

1. Resolve project scope and the user's actual objective.
2. Retrieve the smallest useful context set.
3. Separate remembered context, current evidence, current user corrections, and unresolved claims.
4. Perform the task using live workspace evidence.
5. Preview durable outcomes when judgment is required.
6. Write only approved, retrieval-ready knowledge or verified state.
7. Return a receipt with affected records, scope, provenance, and exact next action.

Do not claim a fixed number of tools. Use only tools advertised by the active signed connection.

