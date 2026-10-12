#!/usr/bin/env python3
"""Validate the XMemo Grok Build plugin package without network access."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ERRORS: list[str] = []


def load_json(relative: str) -> dict:
    path = ROOT / relative
    if not path.is_file():
        ERRORS.append(f"missing {relative}")
        return {}
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        ERRORS.append(f"invalid JSON in {relative}: {exc}")
        return {}
    if not isinstance(value, dict):
        ERRORS.append(f"{relative} must contain a JSON object")
        return {}
    return value


def check_relative_file(relative: str) -> None:
    path = ROOT / relative
    if not path.is_file():
        ERRORS.append(f"missing {relative}")


manifest = load_json(".grok-plugin/plugin.json")
if manifest.get("name") != "xmemo":
    ERRORS.append("manifest name must be xmemo")
if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", str(manifest.get("name", ""))):
    ERRORS.append("manifest name must be lowercase kebab-case")
if not re.fullmatch(r"0|[1-9]\d*\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?", str(manifest.get("version", ""))):
    ERRORS.append("manifest version must be semantic")
for key in ("description", "author", "homepage", "license", "keywords", "logo"):
    if key not in manifest:
        ERRORS.append(f"manifest missing {key}")
if not isinstance(manifest.get("author"), dict) or not manifest["author"].get("name"):
    ERRORS.append("manifest author.name is required")
if manifest.get("logo"):
    logo = Path(str(manifest["logo"]))
    if logo.is_absolute() or ".." in logo.parts:
        ERRORS.append("manifest logo must be a relative path inside the package")
    else:
        check_relative_file(str(logo).replace("/", "\\"))

mcp = load_json(".mcp.json")
if set(mcp) != {"mcpServers"}:
    ERRORS.append(".mcp.json must contain only mcpServers")
servers = mcp.get("mcpServers")
if not isinstance(servers, dict) or set(servers) != {"xmemo"}:
    ERRORS.append(".mcp.json must declare exactly one server named xmemo")
else:
    server = servers["xmemo"]
    if server.get("type") != "http":
        ERRORS.append("xmemo MCP transport must be http")
    if server.get("url") != "https://xmemo.dev/mcp":
        ERRORS.append("xmemo MCP URL must be https://xmemo.dev/mcp")

skills_root = ROOT / "skills"
if not skills_root.is_dir():
    ERRORS.append("missing skills/")
else:
    skill_dirs = sorted(p for p in skills_root.iterdir() if p.is_dir())
    if len(skill_dirs) != 9:
        ERRORS.append(f"expected 9 skill directories, found {len(skill_dirs)}")
    for directory in skill_dirs:
        skill_file = directory / "SKILL.md"
        if not skill_file.is_file():
            ERRORS.append(f"missing {skill_file.relative_to(ROOT)}")
            continue
        text = skill_file.read_text(encoding="utf-8")
        match = re.match(r"^---\r?\n(.*?)\r?\n---", text, re.S)
        if not match:
            ERRORS.append(f"{skill_file.relative_to(ROOT)} lacks YAML frontmatter")
            continue
        frontmatter = match.group(1)
        if not re.search(r"^name:\s+\S+", frontmatter, re.M):
            ERRORS.append(f"{skill_file.relative_to(ROOT)} lacks name frontmatter")
        if not re.search(r"^description:\s+\S+", frontmatter, re.M):
            ERRORS.append(f"{skill_file.relative_to(ROOT)} lacks description frontmatter")
        if not re.search(rf"^name:\s+{re.escape(directory.name)}\s*$", frontmatter, re.M):
            ERRORS.append(f"skill name mismatch in {skill_file.relative_to(ROOT)}")

for relative in ("README.md", "LICENSE", "PRIVACY.md", "SECURITY.md", "CHANGELOG.md"):
    check_relative_file(relative)

secret_patterns = [
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"\bBearer\s+[A-Za-z0-9._~-]{12,}"),
    re.compile(r"\b(?:XMEMO_KEY|XMEMO_ACCESS_TOKEN)\s*[:=]\s*[\"']?(?!\$|<)[A-Za-z0-9_-]{12,}", re.I),
]
for path in ROOT.rglob("*"):
    if not path.is_file() or ".git" in path.parts:
        continue
    if path.suffix.lower() not in {".json", ".md", ".py", ".yml", ".yaml"}:
        continue
    text = path.read_text(encoding="utf-8", errors="replace")
    for pattern in secret_patterns:
        if pattern.search(text):
            ERRORS.append(f"potential secret pattern in {path.relative_to(ROOT)}")
    if re.search(r"\b[A-Z]:\\Users\\", text, re.I):
        ERRORS.append(f"local absolute Windows path in {path.relative_to(ROOT)}")

if ERRORS:
    for error in ERRORS:
        print(f"ERROR: {error}", file=sys.stderr)
    raise SystemExit(1)

print(f"OK: XMemo Grok plugin {manifest['version']}; 9 Skills, HTTP MCP, and no credential patterns found.")
