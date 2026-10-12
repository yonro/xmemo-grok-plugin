# XMemo tool routing for Grok Build

Grok Build connects to `https://xmemo.dev/mcp` through interactive OAuth. The server advertises the tool profile available to the signed-in identity and scope. That profile may evolve, so use active discovery rather than a hard-coded tool count.

## Primary workflow routes

| Intent | Preferred tool |
|---|---|
| Verify identity, agent attribution, or scopes | `get_mcp_identity` |
| Save a new durable fact, preference, decision, or lesson | `remember` |
| Replace an active project checkpoint | `update_state` |
| Recover a bounded context pack | `recall_context` |
| Recover known project context | `get_project_context` |
| Take over unfinished work across agents or sessions | `restore_restart_snapshot` |
| Save a complete, optional handoff package | `create_restart_snapshot` |
| Record a milestone or handoff | `record_event` |
| Inspect project chronology | `get_timeline` |
| Focused semantic search or direct memory lookup | `recall` |
| Revise an existing memory | `update_memory` |
| Explain why a memory exists or was retrieved | `explain_memory` |
| Inspect version history | `list_memory_versions` |
| Soft-delete by default; hard-delete only on explicit request | `forget` |
| Restore an eligible soft-deleted memory | `restore_memory` |

## TODO routes

Use `create_memory_todo`, `list_memory_todos`, and `complete_memory_todo` for concrete follow-up actions. Do not turn vague ideas into TODOs.

## Ledger routes

Use `add_expense`, `list_ledger_transactions`, and `get_monthly_ledger_summary` only for explicit personal ledger requests. Never infer or fabricate an amount.

## Advanced proposals

Use `propose_write`, `propose_todo_mutation`, or `propose_profile_mutation` only when the active workflow needs a reviewable proposal rather than a direct authorized mutation.

