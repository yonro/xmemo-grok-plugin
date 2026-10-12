---
name: xmemo-distill-session
description: Turn an important Grok Build conversation or work session into concise, retrieval-ready XMemo outcomes. Use to preserve decisions and rationale, stable constraints, TODOs, unresolved questions, milestones, or unfinished progress without archiving the transcript.
---

# Distill a session

1. Extract candidate decisions, stable context, reusable lessons, concrete TODOs, unresolved choices, and working state.
2. Exclude filler, raw transcript text, secrets, hidden reasoning, duplication, and tentative claims.
3. Search for overlapping memories before creating duplicates.
4. Preview judgment-heavy candidates and distinguish approved outcomes from proposals.
5. Route each approved item:
   - new durable concept → `remember`
   - revision → `update_memory`
   - concrete action → `create_memory_todo`
   - replaceable progress → `update_state`
   - significant milestone → `record_event`
6. Return a receipt listing saved, updated, skipped, and still-unresolved items.

