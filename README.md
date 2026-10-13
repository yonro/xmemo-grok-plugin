# XMemo plugin for Grok Build

XMemo gives Grok Build a user-owned continuity layer for decisions, project context,
verified progress, TODOs, checkpoints, and cross-agent handoffs. It connects through
the hosted XMemo MCP server and keeps the workflow instructions in version-controlled
Skills.

> This is a third-party plugin. It is not authored, operated, or endorsed by xAI.
> The plugin does not claim Marketplace approval until the xAI catalog review is complete.

## Installation

In Grok Build, open `/plugin`, search for **XMemo**, and install it from the marketplace
when the catalog entry is available. During local development, point Grok Build at this
repository using its local plugin flow.

On first MCP connection, Grok opens the XMemo authorization flow in a browser. Review the
XMemo account and consent screen before approving. Do not paste an API key, bearer token,
or OAuth code into chat.

## What the plugin contains

- **XMemo memory steward** — chooses the narrowest safe recall, memory, project-context,
  checkpoint, decision, TODO, and lifecycle operation.
- **Resume work** — recovers a bounded verified checkpoint and reconciles it with the live
  workspace before continuing.
- **Checkpoint** — preserves only verified material progress after a meaningful phase,
  interruption, blocker, or handoff.
- **Handoff work** — prepares and receives evidence-backed cross-agent handoffs.
- **Audit progress** — checks plans and progress claims against current files and evidence.
- **Brainstorm** — keeps options tentative until the user approves a direction.
- **Plan project** — creates evidence-gated project and execution plans.
- **Review plan** — evaluates scope, dependencies, authorization, evidence, rollback, and
  acceptance gates.
- **Distill session** — extracts durable outcomes without storing raw transcripts.

The plugin intentionally ships no lifecycle hook, shell command, binary, or local credential
store. XMemo writes happen only through explicit agent workflows and the authorized MCP
tool surface.

## MCP connection and authentication

The plugin declares one Streamable HTTP-compatible endpoint in `.mcp.json`:

- MCP: `https://xmemo.dev/mcp`
- Authorization-server discovery: `https://xmemo.dev/.well-known/oauth-authorization-server`
- Protected-resource discovery: `https://xmemo.dev/.well-known/oauth-protected-resource`
- OAuth authorization: `https://xmemo.dev/oauth/authorize`
- OAuth token: `https://xmemo.dev/oauth/token`
- Dynamic client registration: `https://xmemo.dev/oauth/register`
- Token revocation: `https://xmemo.dev/oauth/revoke`

Grok Build owns the OAuth browser flow and token storage. The plugin does not hard-code a
client secret or request a fixed tool count; the XMemo service returns the tool profile
available to the signed-in identity and workspace.

## Safety and privacy

- No API keys, OAuth tokens, client secrets, cookies, or user data are committed.
- XMemo memory is user-owned and project-scoped by the service; the plugin never accepts a
  client-supplied owner or tenant claim.
- Retrieved memories are historical context and must be reconciled with live files.
- Raw chat transcripts and hidden reasoning are not written as memories.
- Destructive lifecycle operations require explicit user confirmation in the workflow.
- The only declared network endpoint is the XMemo MCP and its OAuth discovery/authorization
  endpoints listed above.

See [PRIVACY.md](PRIVACY.md) and [SECURITY.md](SECURITY.md).

## Validation

```bash
python scripts/validate_plugin.py
grok plugin validate .
```

The acceptance record separates package checks and endpoint connectivity from the
Grok-specific OAuth, tool discovery, memory read/write, isolation, and revocation tests:
see [docs/acceptance.md](docs/acceptance.md).

## License

MIT, © Yonro.
