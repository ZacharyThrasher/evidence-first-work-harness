# Terminal States

## COMPLETED

Allowed only when the goal's success criteria are satisfied by evidence and the required evals pass. “The agent believes it is done” is not acceptance evidence.

## HUMAN_GATE

The next useful action requires a human decision/action under the autonomy or hard-gate policy. Record the exact minimal action needed and why.

## BLOCKED_EXTERNAL

Progress depends on an unavailable external dependency that neither the agent nor user can presently resolve (for example a vendor outage or missing entitlement). Record what would unblock it.

## EXHAUSTED

Use only when:

- materially distinct candidates were enumerated;
- all relevant candidates are `RULED_OUT`, `NOT_APPLICABLE`, or truly `BLOCKED_EXTERNAL`;
- each negative conclusion is scoped to concrete evidence;
- no candidate is merely untested because the agent ran out of context/time;
- required contradiction/search checks for the rigor level have been performed.

A human-action dependency is normally `HUMAN_GATE`, not `EXHAUSTED`.

## ABANDONED_BY_USER

The user explicitly stops the project. Preserve state/evidence for possible resumption.
