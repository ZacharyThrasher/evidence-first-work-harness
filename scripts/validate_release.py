#!/usr/bin/env python3
"""Dependency-free structural and distribution validation for EFWH."""
from pathlib import Path
import json
import re
import sys
import tarfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []

required = [
    "README.md",
    "INSTALL.md",
    "QUICKSTART.md",
    "SECURITY.md",
    "CONTRIBUTING.md",
    "SUPPORT.md",
    "CHANGELOG.md",
    "VERSION",
    "package.json",
    "installer/efwh.mjs",
    "scripts/install.ps1",
    "scripts/install.sh",
    "scripts/install.cmd",
    "docs/index.html",
    "docs/quickstart.html",
    "docs/reasoning.html",
    "docs/.nojekyll",
    ".claude/skills/efwh/SKILL.md",
    ".claude/skills/efwh/resources/harness/OPERATING_CONTRACT.md",
    ".claude/skills/efwh/resources/harness/policies/HARD_GATES.md",
    ".claude/skills/efwh/resources/harness/policies/TRUST_MODEL.md",
    ".claude/skills/efwh/resources/harness/environment/ORIENTATION_PROTOCOL.md",
    "reasoning.md",
    "reference/company-rollout.md",
    "reference/architecture.md",
]
for rel in required:
    if not (ROOT / rel).is_file():
        errors.append(f"missing required file: {rel}")

version = (ROOT / "VERSION").read_text(encoding="utf-8").strip() if (ROOT / "VERSION").exists() else ""
skill_root = ROOT / ".claude/skills/efwh"
skill_path = skill_root / "SKILL.md"
skill = skill_path.read_text(encoding="utf-8") if skill_path.exists() else ""
if not skill.startswith("---\n"):
    errors.append("SKILL.md frontmatter must start on line 1")
if "disable-model-invocation: true" not in skill:
    errors.append("SKILL.md must remain explicitly user-invocable")
if "allowed-tools:" in skill:
    errors.append("company default SKILL.md must not grant blanket allowed-tools")
if version and f'version: "{version}"' not in skill:
    errors.append(f"SKILL metadata version does not match VERSION ({version})")

package_path = ROOT / "package.json"
package = {}
if package_path.exists():
    try:
        package = json.loads(package_path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"invalid package.json: {exc}")
if package:
    if package.get("name") != "@zacharythrasher/efwh":
        errors.append("package.json name must be @zacharythrasher/efwh for the public npx install command")
    if package.get("version") != version:
        errors.append("package.json version does not match VERSION")
    if (package.get("bin") or {}).get("efwh") != "installer/efwh.mjs":
        errors.append("package.json must expose efwh -> installer/efwh.mjs")
    if package.get("dependencies"):
        errors.append("installer package should remain dependency-free")

installer = (ROOT / "installer/efwh.mjs").read_text(encoding="utf-8") if (ROOT / "installer/efwh.mjs").exists() else ""
for token in ("CLAUDE_CONFIG_DIR", ".claude", "skills", "efwh", "hashTree", "backup-"):
    if token not in installer:
        errors.append(f"npm installer missing required token: {token}")

install_contract = (ROOT / "INSTALL.md").read_text(encoding="utf-8") if (ROOT / "INSTALL.md").exists() else ""
for token in ("npx --yes @zacharythrasher/efwh install", "CLAUDE_CONFIG_DIR", "offline", "/efwh"):
    if token.lower() not in install_contract.lower():
        errors.append(f"INSTALL.md missing required token: {token}")

for installer_path in (ROOT / "scripts/install.ps1", ROOT / "scripts/install.sh"):
    if installer_path.exists():
        text = installer_path.read_text(encoding="utf-8")
        if "CLAUDE_CONFIG_DIR" not in text:
            errors.append(f"fallback installer does not honor CLAUDE_CONFIG_DIR: {installer_path.relative_to(ROOT)}")
        if version not in text:
            errors.append(f"fallback installer version is stale: {installer_path.relative_to(ROOT)}")

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

site_path = ROOT / "docs/index.html"
site = site_path.read_text(encoding="utf-8") if site_path.exists() else ""
for token in (
    "Created by Zach Thrasher",
    "npx --yes @zacharythrasher/efwh install",
    "Copy install command",
    "Offline install",
    "efwh-offline-",
):
    if token not in site:
        errors.append(f"docs/index.html missing required token: {token}")

old_install_tokens = (
    'claude "Install EFWH from',
    "Copy interactive install",
    "Recommended: guided install",
)
for rel in ("README.md", "INSTALL.md", "QUICKSTART.md", "docs/index.html", "docs/quickstart.html"):
    path = ROOT / rel
    if path.exists():
        text = path.read_text(encoding="utf-8")
        for token in old_install_tokens:
            if token in text:
                errors.append(f"stale agent-guided install UX remains in {rel}: {token}")

# GitHub Pages uses docs/ as a static web root. Do not link site navigation to local Markdown.
for html_path in (ROOT / "docs").glob("*.html"):
    html = html_path.read_text(encoding="utf-8")
    for href in re.findall(r'href=["\']([^"\']+)["\']', html):
        if "://" not in href and href.split("#", 1)[0].lower().endswith(".md"):
            errors.append(f"Pages HTML links to raw local Markdown: {html_path.relative_to(ROOT)} -> {href}")


def normalize_distribution_bytes(data: bytes) -> bytes:
    """Compare text payloads portably while keeping binary payloads byte-exact.

    Git may materialize text files as CRLF on Windows even when release archives
    contain LF. Those are semantically identical and must not make validation
    platform-dependent. UTF-8 text is normalized to LF; binary/non-UTF-8 data
    remains byte-exact.
    """
    if b"\x00" in data:
        return data
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        return data
    return text.replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")


def canonical_skill_bytes() -> dict[str, bytes]:
    out: dict[str, bytes] = {}
    if not skill_root.exists():
        return out
    for p in skill_root.rglob("*"):
        if p.is_file():
            out[p.relative_to(skill_root).as_posix()] = normalize_distribution_bytes(p.read_bytes())
    return out

canonical = canonical_skill_bytes()

tgz_path = ROOT / "docs/downloads" / f"efwh-{version}.tgz"
if not tgz_path.is_file():
    errors.append(f"missing local npm tarball: {tgz_path.relative_to(ROOT)}")
else:
    try:
        with tarfile.open(tgz_path, "r:gz") as tf:
            names = set(tf.getnames())
            for required_name in ("package/installer/efwh.mjs", "package/package.json", "package/.claude/skills/efwh/SKILL.md"):
                if required_name not in names:
                    errors.append(f"npm tarball missing {required_name}")
            for rel, expected in canonical.items():
                name = f"package/.claude/skills/efwh/{rel}"
                try:
                    f = tf.extractfile(name)
                    actual = f.read() if f else b""
                except KeyError:
                    errors.append(f"npm tarball missing canonical Skill file: {rel}")
                    continue
                if normalize_distribution_bytes(actual) != expected:
                    errors.append(f"npm tarball Skill payload differs: {rel}")
    except Exception as exc:
        errors.append(f"invalid npm tarball {tgz_path.name}: {exc}")

offline_path = ROOT / "docs/downloads" / f"efwh-offline-{version}.zip"
if not offline_path.is_file():
    errors.append(f"missing offline ZIP: {offline_path.relative_to(ROOT)}")
else:
    try:
        prefix = f"efwh-offline-{version}/"
        with zipfile.ZipFile(offline_path) as zf:
            names = set(zf.namelist())
            for required_name in (prefix + "install.cmd", prefix + "install.ps1", prefix + "install.sh", prefix + ".claude/skills/efwh/SKILL.md"):
                if required_name not in names:
                    errors.append(f"offline ZIP missing {required_name}")
            for rel, expected in canonical.items():
                name = prefix + ".claude/skills/efwh/" + rel
                try:
                    actual = zf.read(name)
                except KeyError:
                    errors.append(f"offline ZIP missing canonical Skill file: {rel}")
                    continue
                if normalize_distribution_bytes(actual) != expected:
                    errors.append(f"offline ZIP Skill payload differs: {rel}")
    except Exception as exc:
        errors.append(f"invalid offline ZIP {offline_path.name}: {exc}")

if errors:
    print("EFWH release validation FAILED")
    for error in errors:
        print(" -", error)
    sys.exit(1)

print(f"EFWH release validation OK (v{version})")
