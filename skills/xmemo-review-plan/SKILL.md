---
name: xmemo-review-plan
description: Review an architecture, implementation, launch, or agent-produced plan against XMemo goals, settled decisions, constraints, lessons, project state, and acceptance criteria. Use when a formal verdict, blocking findings, and approval gate are required.
---

# Review a plan against XMemo

1. Identify the exact plan revision and decision authority.
2. Retrieve only context that can materially affect the verdict.
3. Verify plan assumptions against the live workspace where possible.
4. Check scope, dependency order, evidence, security, reversibility, ownership, validation, and rollback.
5. Classify findings by severity and distinguish contradictions from missing evidence.
6. Return one verdict: `approve`, `approve with conditions`, `revise`, or `reject`.
7. State blocking findings, required changes, risks, acceptance gate, and one exact next action.
8. Save the verdict or approved rationale only after authorization; never save a proposal as implemented state.

For independent review, delegate evidence comparison to `xmemo-context-auditor` and evaluate its findings.

