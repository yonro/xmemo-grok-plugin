# XMemo Grok Build acceptance record

This record separates package validation and XMemo endpoint checks from the
Grok-specific client authorization and marketplace review gates.

## Candidate

- Version: `1.0.0`
- Plugin manifest: `.grok-plugin/plugin.json`
- MCP config: `.mcp.json`
- Endpoint: `https://xmemo.dev/mcp`
- Test date: 2026-10-13 (Asia/Tokyo)

## Results

| Area | Status | Evidence |
| --- | --- | --- |
| Grok plugin manifest | **VERIFIED** | `.grok-plugin/plugin.json` uses `xmemo`, semantic version `1.0.0`, XMemo metadata, and a relative logo. |
| MCP declaration | **VERIFIED** | `.mcp.json` declares exactly one HTTP server at `https://xmemo.dev/mcp`. |
| Skill discovery | **VERIFIED** | Nine `skills/*/SKILL.md` files have matching `name` and `description` frontmatter. |
| Static package validator | **VERIFIED** | `python scripts/validate_plugin.py` passes. |
| Grok CLI manifest validator | **VERIFIED** | Grok CLI `1.0.13` ran `grok plugin validate .` and reported `Plugin manifest is valid`. |
| Endpoint protection | **VERIFIED** | Unauthenticated `GET https://xmemo.dev/mcp` returned HTTP 401. |
| OAuth discovery | **VERIFIED** | XMemo authorization-server and protected-resource metadata returned HTTP 200. |
| Grok local plugin load | **VERIFIED** | `grok plugin install --trust .` installed XMemo and `grok plugin details xmemo` reported the manifest and components. |
| Grok OAuth authorization | **NOT RUN** | Requires a signed-in Grok Build session and an approved browser consent flow. |
| Grok MCP handshake/tools/list | **PARTIAL** | `grok mcp doctor XMemo` completed the handshake and discovered 31 tools, but the duplicate `XMemo` name resolved to an existing `~/.grok/config.toml` server rather than proving plugin-specific OAuth. |
| Grok memory read/write | **NOT RUN** | Requires a Grok-authorized synthetic test record and cleanup. |
| Grok isolation/revocation/resume | **NOT RUN** | Requires Grok-specific authenticated and multi-session evidence. |
| Public source repository | **VERIFIED** | `https://github.com/yonro/xmemo-grok-plugin` is public, MIT licensed, and reachable from GitHub. The Marketplace PR pins the exact tested commit SHA. |
| xAI Marketplace catalog PR | **NOT SUBMITTED** | The catalog entry and generated index must be prepared only after the public source commit exists. |

## Marketplace gate

The official xAI marketplace requires a catalog entry in
`xai-org/plugin-marketplace/.grok-plugin/marketplace.json` with a remote source
URL pinned to a full 40-character commit SHA. The marketplace's generated
`.grok-plugin/plugin-index.json` must then be regenerated and both catalog checks
must pass before opening a PR. This repository does not claim marketplace approval.
