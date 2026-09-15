# Install EFWH

EFWH installs as a **personal Claude Code Skill**, making `/efwh` available across all of your local Claude Code projects.

## Recommended

From any directory:

```text
npx --yes @zacharythrasher/efwh install
```

That is the complete normal install.

The npm package contains the full canonical `.claude/skills/efwh/` payload, so the installer does **not** clone this repository or fetch individual files from GitHub at runtime. It uses `CLAUDE_CONFIG_DIR` when set; otherwise it installs to `~/.claude/skills/efwh/` (`%USERPROFILE%\.claude\skills\efwh\` on Windows).

If EFWH is already installed and identical, the command is a no-op. If an update/replacement is needed, the installer moves the existing copy to a timestamped backup, installs the bundled payload, and verifies the copied tree byte-for-byte.

Useful commands:

```text
npx --yes @zacharythrasher/efwh install
npx --yes @zacharythrasher/efwh update
npx --yes @zacharythrasher/efwh status
npx --yes @zacharythrasher/efwh uninstall
```

`uninstall` disables EFWH by moving it to a recovery copy. `uninstall --purge` explicitly deletes it.

## Restricted-network / offline fallback

If the npm registry is unavailable on your network, use the self-contained offline bundle:

**Windows**

1. Download/extract `efwh-offline-2.3.0.zip` from the EFWH release or your approved internal mirror.
2. Run `install.cmd` (or `install.ps1`) from the extracted folder.

**macOS / Linux**

1. Download/extract the same bundle.
2. Run:

```bash
./install.sh
```

The offline bundle contains the same canonical Skill payload and requires no Git checkout, no GitHub API access, and no npm registry access.

If Node/npm is available but only the registry is blocked, the release also includes `efwh-2.3.0.tgz`; run it directly from the local file:

```text
npx --yes ./efwh-2.3.0.tgz install
```

## Managed company deployment

For broad organization rollout, prefer your existing Claude Code managed-Skills mechanism and deploy `.claude/skills/efwh/` centrally. The npm/offline installers are intended for personal pilots and unmanaged local installs.

## Scope and safety

Installing EFWH copies one Skill directory. It does **not** grant extra permissions, alter enterprise policy, enable tools, modify MCP configuration, configure credentials, or touch project files.

Claude Code documentation defines personal Skills under `~/.claude/skills/<skill-name>/`, where they are available across projects. EFWH remains explicitly user-invocable with `/efwh`.
