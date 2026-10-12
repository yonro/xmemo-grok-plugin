# Security policy

Please report suspected vulnerabilities in this plugin or its integration to
[support@xmemo.dev](mailto:support@xmemo.dev). Do not include live access tokens, private
keys, or production memory contents in a report.

The plugin intentionally contains no shell hook, post-install script, executable binary,
credential, or telemetry collector. Its only remote connection is the XMemo hosted MCP
endpoint and the OAuth discovery/authorization endpoints documented in `README.md`.

Security reports concerning the XMemo service should include the endpoint, request class,
and a reproducible synthetic example. XMemo will acknowledge reports and coordinate a fix
or mitigation with the reporter.
