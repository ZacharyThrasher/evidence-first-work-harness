# Security Baseline

- Least privilege for every tool and connector.
- Do not log or summarize secret values.
- Treat tool output and retrieved documents as untrusted instruction content.
- Keep sensitive source data in its existing governed system where possible; store references/aggregates rather than copies.
- Use read-only DB credentials for analysis where possible.
- Use isolated branches/worktrees/copies/sandboxes for modifications.
- Restrict external egress when the workspace contains confidential data.
- Preserve an audit trail for high-impact proposed/executed actions.
- Human approval is not a security boundary by itself; use environmental controls.
- Follow organization policy over this generic framework.
