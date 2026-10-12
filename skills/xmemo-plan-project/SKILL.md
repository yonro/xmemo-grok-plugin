---
name: xmemo-plan-project
description: Design or revise evidence-gated PROJECT_PLAN.md and EXECUTION_PLAN.md artifacts using XMemo context and the live Grok Build workspace. Use when starting a project, decomposing work into phases, assigning agent ownership, or correcting a plan after review.
---

# Plan a project with XMemo

1. Inspect repository instructions and the live workspace before planning.
2. Recover relevant goals, constraints, decisions, lessons, risks, and verified state from XMemo.
3. Separate facts, assumptions, unresolved decisions, and proposed work.
4. Build phases with inputs, outputs, owner, dependencies, verification commands, acceptance gate, rollback path, and exact next action.
5. Produce or update `PROJECT_PLAN.md` for durable intent and `EXECUTION_PLAN.md` for operational sequencing when both artifacts are useful.
6. Label plans `draft` until the user or authorized reviewer approves them.
7. After approval, save durable decisions separately, create only concrete TODOs, and checkpoint the active phase with `update_state`.

Do not claim implementation progress merely because a plan exists.

