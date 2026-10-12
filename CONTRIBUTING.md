# Contributing

## Development

Run the package validator before opening a change:

```bash
python scripts/validate_plugin.py
```

Keep the plugin limited to the declared XMemo MCP endpoint and evidence-grounded Skills.
Do not add credentials, telemetry, unbounded shell hooks, downloaded executables, or raw
conversation archives.

## Marketplace updates

The xAI marketplace is a separate index repository. A source update must be published at a
public commit first. The marketplace entry then pins that exact 40-character commit SHA and
regenerates its component index before the catalog pull request is opened.
