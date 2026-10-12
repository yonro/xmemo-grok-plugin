# XMemo memory policy

## Save automatically only when safe

An automatic checkpoint may preserve verified working state after sustained material work. It must not turn every response into a write.

## Preview before judgment-heavy writes

Preview proposed decisions, inferred preferences, broad summaries, superseding updates, and destructive lifecycle actions. The user should be able to correct scope or wording before persistence.

## Never save

- raw transcripts or message dumps
- passwords, tokens, keys, cookies, or private credentials
- hidden reasoning or chain-of-thought
- speculative facts or unverified completion claims
- rejected or tentative options as approved decisions
- redundant checkpoints that add no new verified state

## Precedence

1. current explicit user instruction
2. current verified workspace or deployment evidence
3. approved durable decisions
4. latest verified checkpoint
5. older memory and agent reports

## Deletion

Use recoverable soft deletion by default. Use hard deletion only after an explicit request and confirmation that identifies the exact target and consequence.

