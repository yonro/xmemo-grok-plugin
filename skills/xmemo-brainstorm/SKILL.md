---
name: xmemo-brainstorm
description: Run a structured brainstorm grounded in XMemo goals, constraints, decisions, lessons, and failed approaches. Use for product ideas, architecture options, strategies, or plans that should remain tentative until the user approves a direction.
---

# XMemo-grounded brainstorm

1. Define the decision question, constraints, and success criteria.
2. Retrieve only relevant context with `recall_context`, `get_project_context`, and focused `recall` queries.
3. Generate at least three meaningfully different options; include a conservative baseline.
4. Stress-test each option for assumptions, evidence gaps, reversibility, cost, risk, and validation method.
5. Compare the options in a compact decision matrix.
6. Recommend a direction while keeping every proposal tentative.
7. Ask for approval before saving a decision. Save durable rationale separately from temporary exploration; use `update_state` only if the exploration will continue later.

Never store discarded brainstorming prose or convert an unapproved option into a settled decision.

