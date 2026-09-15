# Evidence Rules

## Evidence authority examples

From strongest to weaker **for a claim they directly address**:

- direct reproducible observation in the target environment;
- authoritative current internal source/system of record;
- official vendor/standards documentation;
- original peer-reviewed/preprint research with inspectable method;
- well-supported secondary technical source;
- community report/anecdote.

Authority is claim-dependent. A community report can be excellent evidence that a specific person observed a bug, but weak evidence that all systems have that bug.

## Evidence record fields

Recommended metadata:

- `id`
- `timestamp`
- `kind`
- `source_id`
- `authority`
- `instruction_trust`
- `claim_or_question`
- `scope`
- `observation_or_excerpt_summary`
- `supports`
- `refutes`
- `artifact_path_or_url`
- `version/date`
- `hash` when useful
- `limitations`

## Negative evidence

Absence of evidence is not automatically evidence of absence. Failed experiments must record environment/version/preconditions and the precise point of failure.

## Chat statements

User/model statements can seed hypotheses and context but should not silently become `OBSERVED` unless verified or explicitly treated as user-provided requirements/facts.
