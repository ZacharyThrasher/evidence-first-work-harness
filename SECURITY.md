# Security policy

EFWH is an instruction/protocol layer. It does not replace Claude Code permissions, sandboxing, identity, access control, data governance, or production change-management systems.

## Security defaults

- `/efwh` is explicitly user-invoked (`disable-model-invocation: true`).
- The Skill grants no blanket `allowed-tools` permissions.
- External/retrieved content is evidence/data by default, not trusted instruction.
- Production writes, destructive changes, privilege changes, secrets disclosure, sensitive-data egress, security-control bypass, external publication/messages, and material legal/compliance/safety acceptance are human gates.
- Organization policy always wins over EFWH autonomy settings.

## Reporting a vulnerability

Do not publish secrets, exploit details, proprietary data, or a live prompt-injection payload in a public issue. Use GitHub private vulnerability reporting if enabled for this repository, or contact the repository owner through an approved private/company channel.

For ordinary logic bugs or overly permissive/overly restrictive behavior that does not expose sensitive information, open a normal issue with the smallest reproducible example.

## Threat model

The framework explicitly considers:

- prompt injection from files, websites, tool output, tickets, documents, and data fields;
- instruction/evidence trust confusion;
- over-broad agent initiative;
- approval fatigue;
- secret leakage and trust-boundary crossing;
- production/destructive side effects;
- false claims of successful execution;
- context loss and stale state;
- incorrect “impossible/exhausted” conclusions.

EFWH reduces these risks through scoped evidence, durable state, hard gates, outcome evaluation, and containment-aware autonomy. It does not claim to eliminate them.
