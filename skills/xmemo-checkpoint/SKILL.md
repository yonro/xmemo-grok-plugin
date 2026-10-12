---
name: xmemo-checkpoint
description: Preserve a concise XMemo checkpoint after sustained material work, a completed phase, a blocker, an interruption, or a Grok Build stop-hook reminder. Use only when verified project state changed; skip redundant or speculative saves.
---

# Save a verified checkpoint

1. Inspect live workspace evidence and determine whether material state changed since the last checkpoint.
2. If nothing durable changed, state that no checkpoint is needed and stop.
3. Recover the latest scoped state when needed to avoid duplication or regression.
4. Build one concise checkpoint containing:
   - objective and project scope
   - verified current status and evidence
   - completed work
   - settled decisions
   - blocker or uncertainty
   - relevant artifacts
   - remaining work
   - one exact next action
   - provenance and timestamp
5. Use `update_state` to replace stale working state. Use `record_event` only for a significant milestone or handoff, and store durable decisions separately.
6. Return a save receipt. If XMemo is unavailable, say no durable update was made.

Never save transcript content, secrets, hidden reasoning, or unverified claims.

