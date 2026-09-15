# Hard Gates

These gates override autonomy presets unless the user/organization explicitly changes the policy in a governing configuration.

Default `HUMAN_GATE` actions:

- production or primary-system writes;
- destructive/irreversible actions;
- external communications/publication/submission;
- purchases/financial commitments;
- privileged/admin/elevated changes;
- accessing or revealing secret values/credentials beyond already-scoped tooling;
- changing security controls or bypassing corporate policy;
- moving sensitive data across trust boundaries or external egress;
- deleting source data/evidence;
- physical-world actions requiring a person;
- significant scope expansion;
- accepting material legal/compliance/safety risk;
- changing a locked high-rigor acceptance criterion after seeing results.

A gate request must say:

1. exactly what action is needed;
2. why it is necessary;
3. what will change;
4. the minimum permission/action required;
5. the next step after approval.

Do not create approval fatigue by gating harmless read-only actions individually when the configured environment already authorizes them.
