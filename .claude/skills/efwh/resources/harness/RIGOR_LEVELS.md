# Rigor Levels

Rigor controls the evidence burden, not permissions.

## R0_EXPLORATORY

For low-stakes reconnaissance. Keep a concise source list and record major assumptions. Predeclared acceptance is recommended but may be lightweight. Suitable for brainstorming and determining whether a deeper investigation is worthwhile.

## R1_STANDARD — default

- provenance for material claims;
- explicit claim status (`OBSERVED`, `DOCUMENTED`, etc.);
- candidate registry;
- task acceptance criteria defined before execution;
- reproducible command/query or enough detail to reconstruct it;
- deterministic verification when feasible;
- preserved failure evidence.

## R2_HIGH_ASSURANCE

Everything in R1 plus:

- contradiction search before major conclusions;
- independent/fresh-context evaluator for nontrivial model-produced work;
- multiple trials for material nondeterministic claims;
- hashes/version identifiers for important inputs/artifacts where practical;
- explicit eval-defect handling;
- SME/human spot-check for high-impact conclusions;
- stronger separation of analysis data from source data.

## R3_ORG_CRITICAL

R2 plus organization-specific governance. Examples may include two-person review, immutable audit storage, formal change control, validated tooling, regulated data handling, statistical review, safety cases, retention policies, or compliance signoff.

The stock harness does not claim to satisfy any regulation or safety standard by itself.
