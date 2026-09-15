# Runs / Session Handoffs

Do not depend on the original chat surviving.

At a natural context/session boundary, write a compact handoff using `SESSION_HANDOFF_TEMPLATE.md`. Store verbose raw transcripts elsewhere if policy permits; the handoff should contain only high-signal state needed to resume.

A fresh model session should be able to resume by reading `GOAL.md`, `CONFIG.yaml`, `STATE.json`, `tasks/CURRENT.md`, relevant wiki pages, and the latest handoff.
