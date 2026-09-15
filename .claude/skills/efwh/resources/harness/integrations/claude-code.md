# Claude Code / Sonnet Integration

The harness does not require a Claude-specific file. The simplest launch is to start Claude Code in the workspace and paste `KICKOFF_PROMPT.md`.

## Optional persistent project instruction

If the repository already has `CLAUDE.md`, do not overwrite it. Append/adapt the small snippet in `CLAUDE_SNIPPET.txt` after review.

## MCP / connectors

The orientation phase should inspect the MCP/connectors actually available to that coworker. Do not assume a corporate Confluence, database, or browser connector exists merely because another user had one.

When a relevant connector is unavailable, record it in the orientation summary and ask the user to connect/supply it only if it materially improves the task.

## Subagents

Default off/auto. Use research subagents for independent breadth-heavy branches. Use a fresh evaluator context for R2/high-edge tasks. Do not multiply agents merely because the feature exists.
