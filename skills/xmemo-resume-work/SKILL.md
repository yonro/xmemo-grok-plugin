---
name: xmemo-resume-work
description: Resume a project or unfinished task by recovering XMemo's latest verified checkpoint, relevant decisions, TODOs, blockers, and exact next action. Use at the start of a Grok Build session, after interruption, or when continuing work previously handled by another agent.
---

# Resume work from XMemo

1. Resolve the project and task scope; verify connection identity when ambiguous.
2. Choose the recovery path:
   - For normal continuation by the same agent, prefer `get_project_context` for a known project and `recall_context` for a task-oriented pack. Add focused `recall`, timeline, or TODO reads only to close specific gaps.
   - When another agent or a session on another machine takes over unfinished work, use `restore_restart_snapshot` with the exact project scope. `snapshot_id` and `source_session_id` are optional: the server uses the latest snapshot in that scope, or synthesizes one from the current state if none was created beforehand.
   - A restart snapshot restores active state, recent timeline events, open reminders, and pending decisions. It records `source_session_id` → `target_session_id` provenance and a `session_restart_restored` event; it does not restore a transcript.
3. Inspect current repository state before trusting remembered completion or paths.
4. Reconcile memory with current files, diffs, commits, tests, deployments, and user corrections.
5. Return a Resume Brief with objective, verified state, remembered context, decisions, completed work, blocker, artifacts, remaining work, and one exact next action.
6. Continue only after the next action is evidence-backed and authorized.
7. Update the checkpoint after material verified progress, a new blocker, or a meaningful pause—not every turn.

Resume restores useful context, not the original conversation.

