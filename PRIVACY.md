# XMemo privacy notes for the Grok Build plugin

The plugin package contains workflow instructions and an MCP endpoint declaration. It does
not contain credentials, user memory records, chat transcripts, or an embedded database.

When the user authorizes the connection, Grok Build sends MCP requests to `xmemo.dev` using
the account selected in the browser consent flow. XMemo applies account, project, and
workspace authorization on the service. The plugin does not accept owner or tenant IDs from
model text.

The Skills instruct the agent to store only verified, durable outcomes and to avoid raw
transcripts, secrets, hidden reasoning, and speculative claims. Users can revoke the OAuth
grant through XMemo's authorization controls.

For service-side data retention, account deletion, and legal terms, see the XMemo privacy
policy at <https://xmemo.dev/legal/privacy>.
