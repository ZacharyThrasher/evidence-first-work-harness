#!/usr/bin/env python3
"""Dependency-free structural release validation for EFWH."""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []

required = [
    "README.md",
    "QUICKSTART.md",
    "SECURITY.md",
    "CONTRIBUTING.md",
    "SUPPORT.md",
    "CHANGELOG.md",
    "VERSION",
    "index.html",
    ".claude/skills/efwh/SKILL.md",
    ".claude/skills/efwh/resources/harness/OPERATING_CONTRACT.md",
    ".claude/skills/efwh/resources/harness/policies/HARD_GATES.md",
    ".claude/skills/efwh/resources/harness/policies/TRUST_MODEL.md",
    ".claude/skills/efwh/resources/harness/environment/ORIENTATION_PROTOCOL.md",
    "docs/reasoning.md",
    "docs/company-rollout.md",
    "docs/architecture.md",
]
for rel in required:
    if not (ROOT / rel).is_file():
        errors.append(f"missing required file: {rel}")

version = (ROOT / "VERSION").read_text(encoding="utf-8").strip() if (ROOT / "VERSION").exists() else ""
skill_path = ROOT / ".claude/skills/efwh/SKILL.md"
skill = skill_path.read_text(encoding="utf-8") if skill_path.exists() else ""
if not skill.startswith("---\n"):
    errors.append("SKILL.md frontmatter must start on line 1")
if "disable-model-invocation: true" not in skill:
    errors.append("SKILL.md must remain explicitly user-invocable")
if "allowed-tools:" in skill:
    errors.append("company default SKILL.md must not grant blanket allowed-tools")
if version and f'version: "{version}"' not in skill:
    errors.append(f"SKILL metadata version does not match VERSION ({version})")

for path in ROOT.rglob("*.json"):
    try:
        json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"invalid JSON {path.relative_to(ROOT)}: {exc}")

for legacy in ("claude-skill", "harness"):
    if (ROOT / legacy).exists():
        errors.append(f"legacy duplicate distribution directory present: {legacy}/")

link_re = re.compile(r"\[[^]]+\]\(([^)]+)\)")
for path in ROOT.rglob("*.md"):
    text = path.read_text(encoding="utf-8")
    for raw_target in link_re.findall(text):
        target = raw_target.strip().split("#", 1)[0]
        if not target or "://" in target or target.startswith(("mailto:", "#")):
            continue
        if target.startswith("<") and target.endswith(">"):
            target = target[1:-1]
        resolved = (path.parent / target).resolve()
        try:
            resolved.relative_to(ROOT.resolve())
        except ValueError:
            continue
        if not resolved.exists():
            errors.append(f"broken local link in {path.relative_to(ROOT)} -> {target}")

site_path = ROOT / "index.html"
site = site_path.read_text(encoding="utf-8") if site_path.exists() else ""
for token in (
    "Created by Zach Thrasher",
    ".claude/skills/efwh",
    "ZacharyThrasher/evidence-first-work-harness",
):
    if token not in site:
        errors.append(f"index.html missing required token: {token}")

if errors:
    print("EFWH release validation FAILED")
    for error in errors:
        print(" -", error)
    sys.exit(1)

print(f"EFWH release validation OK (v{version})")
