# reasoning.md — Why the Evidence-First Work Harness is structured this way

**Version:** 2.2.0  
**Research refresh:** 2026-09-14  
**Purpose:** explain the design independently of the harness itself, so teams can challenge or simplify the framework instead of treating scaffolding as doctrine.

## Executive rationale

The central design choice is to treat an AI model less like a one-shot oracle and more like a capable but fallible engineer/researcher working across shifts. The useful unit is not the chat transcript. It is a **workspace containing explicit goals, evidence, hypotheses, decisions, tests, state, and handoff artifacts**.

That conclusion is now supported by several converging bodies of practice:

1. Anthropic's long-running-agent work found that models lose continuity across context windows, try to do too much at once, and can prematurely declare work complete. Their effective harness used an initializer, incremental progress, structured artifacts, machine-readable feature state, Git, and explicit end-to-end tests. In 2026 Anthropic extended this into planner/generator/evaluator architectures and emphasized that structured handoffs and task decomposition are load-bearing on hard problems.
2. Anthropic's context-engineering work frames context as a scarce resource with diminishing value. Persisting high-signal artifacts and reloading only relevant pieces is therefore preferable to carrying an ever-growing conversational history.
3. Anthropic's evaluator research found generator self-evaluation to be systematically lenient. Separating generation from evaluation, and defining concrete grading criteria before execution, improved outcomes. Their 2026 harness introduced a “contract” for what done means before work began.
4. OpenAI and Anthropic both emphasize eval-driven development for agents. Agent outputs are nondeterministic; useful evaluation therefore looks at the **actual outcome/environment state**, often across multiple trials, rather than trusting the model's claim that it succeeded.
5. Recent data-agent practice shows that reliable analysis needs access control, links back to raw results, domain context beyond schemas, and continuous regression-style evals. This supports treating production-data analysis as the same general research→experiment→evidence loop, not as a special case.
6. Security guidance from Anthropic, NIST, and OWASP converges on least privilege, hard environmental boundaries, human oversight for high-impact actions, and distrust of external content as instructions. Increasing autonomy should therefore primarily mean expanding a **bounded execution envelope**, not simply suppressing permission prompts.
7. Research-agent benchmarks such as PaperBench and AutoExperiment demonstrate that long-horizon replication remains difficult and that performance falls as more of the work must be reconstructed. This argues for decomposition, repeatable experiments, rubrics, multiple attempts when justified, and preserved failure evidence.
8. OpenAI's 2026 audit of coding benchmarks is an important counterweight: even evaluation suites themselves can be wrong. The harness therefore forbids “passing the eval at all costs”; suspected bad acceptance criteria become an `EVAL_DEFECT` that must be reviewed rather than silently edited.

The framework is intentionally **model-agnostic and file-based**. Claude-specific integration is optional. Anthropic's Agent Skills work similarly emphasizes portable folders of instructions/resources with progressive disclosure, while also warning that harness assumptions should be revisited as models improve.

---

## Design principle 1 — Orient to the actual environment before researching

A weaker model with excellent access to internal artifacts can outperform a stronger model that does not know those artifacts exist. The first operation is therefore an explicit, mostly read-only **capability orientation**.

The agent inventories:

- repository/workspace contents and version-control state;
- local runtimes and test environments;
- internal document/search systems such as Confluence;
- MCP servers and connector/tool surfaces;
- data warehouses/databases and their effective permissions;
- APIs and service documentation;
- browser/web access;
- sandboxes/staging environments;
- domain experts and required human actions;
- security/data-classification boundaries.

The inventory is not “collect everything.” It is a map of **what exists, what it is good for, what permissions it has, and what risks it carries**. Anthropic's tool-design guidance specifically notes that too many overlapping tools can confuse agents; the orientation phase should therefore produce a short recommended tool/source set for the current goal, not flood context with every available interface.

The model must not dump secret values merely to prove it can see them. Capability discovery should inspect names/scopes/metadata and perform minimal read-only probes.

---

## Design principle 2 — Separate instruction trust from evidentiary authority

A Confluence page can be authoritative evidence about an internal process while still being **untrusted as an instruction source** to the agent. A public vendor manual can be strong technical evidence while containing text that should never override the user's goal. A tool result can be correct data and still contain prompt injection.

The harness therefore tracks two independent axes:

- **Instruction trust:** may this source direct agent behavior?
- **Evidence authority:** how much weight should its factual content carry for this claim?

This prevents a common conceptual error: calling a source “trusted” and accidentally granting both epistemic authority and execution authority.

Anthropic's 2026 containment work and OWASP agent-security guidance both treat tool/file/web content as an attack surface and recommend least privilege and deterministic boundaries outside the model.

---

## Design principle 3 — The wiki is a synthesis layer, not a truth store

A wiki page is useful because it compresses scattered research into a form the next session can load quickly. It becomes dangerous when prose loses the provenance and scope of the evidence that produced it.

The harness therefore uses explicit claim states:

- `OBSERVED` — directly measured in the current environment;
- `DOCUMENTED` — supported by a cited authoritative source;
- `INFERRED` — reasoned from evidence but not directly established;
- `HYPOTHESIS` — a testable possibility;
- `DISPROVEN` — contradicted within a stated scope;
- `SUPERSEDED` — replaced by stronger/newer evidence.

Wiki claims link to evidence IDs. Failed experiments remain available. Contradictions are first-class artifacts rather than awkward prose to hide.

This is the generalized lesson from the Bluetooth PAN investigation: “this specific raw socket call fails” is evidence about that path; it is not evidence that the hardware cannot perform Bluetooth PAN when the operating system demonstrably does so.

---

## Design principle 4 — Define “done” before acting

The model should not be allowed to perform work and then invent a success criterion that matches what it happened to produce.

Each meaningful task has a **task contract** written before execution:

- intended outcome;
- scope/non-goals;
- allowed actions;
- expected evidence;
- acceptance criteria;
- evaluation method;
- rollback/recovery path;
- human-gate conditions.

Anthropic's March 2026 long-running application harness used a generator/evaluator contract before each sprint for this reason. OpenAI's eval guidance likewise frames evaluation as `Specify → Measure → Improve`.

For high-rigor work, acceptance criteria are locked after execution starts. If they were flawed, log an `EVAL_DEFECT`; do not rewrite history.

---

## Design principle 5 — Evaluate the outcome, not the agent's story

Agents can say “done” when the environment says otherwise. Anthropic's eval terminology explicitly distinguishes a transcript from the final outcome. A flight agent saying it booked a flight is not evidence that a reservation exists; the database state is.

The harness prefers evaluators in this order:

1. deterministic/environment checks;
2. independent model evaluator using a fresh context and explicit rubric;
3. human/SME review where judgment matters.

A single task can combine all three. Subjective tasks should still turn taste/quality into concrete criteria where possible. The evaluator should not receive the generator's persuasive self-justification unless that rationale is itself part of what is being graded.

For nondeterministic or high-value tasks, multiple trials can be appropriate. Anthropic's eval guidance explicitly treats attempts as trials and recommends multiple trials to obtain stable results.

---

## Design principle 6 — Autonomy and rigor are separate dimensions

The team needs more nuance than “manual” versus “fully autonomous.” A model can have broad freedom inside a disposable sandbox while facing very strict evidence requirements. Conversely, a human can manually approve every action while doing only lightweight exploratory analysis.

The harness therefore exposes:

### Autonomy

- `L0_ADVISORY`
- `L1_GUIDED_RESEARCH`
- `L2_BOUNDED_EXPERIMENT`
- `L3_BOUNDED_BUILDER`
- `L4_AUTONOMOUS_SANDBOX`

### Rigor

- `R0_EXPLORATORY`
- `R1_STANDARD`
- `R2_HIGH_ASSURANCE`
- `R3_ORG_CRITICAL`

Hard gates override all autonomy levels.

This approach is motivated by Anthropic's 2026 finding that repeated permission prompts create approval fatigue (their telemetry showed users approving roughly 93% of prompts) and that containment can be a stronger control than asking a human to approve every low-level action. The framework therefore favors preapproved boundaries plus meaningful gates rather than endless “yes/no” prompts.

---

## Design principle 7 — Default to one agent; specialize only when the task justifies it

The harness can be run by a single Sonnet session. Multi-agent orchestration is optional.

Anthropic's research system showed large gains from parallel agents on breadth-heavy research, but at high token cost; their reported multi-agent research workload used roughly 15× the tokens of ordinary chat. Their broader agent guidance recommends the simplest effective architecture.

So the default policy is:

- use one agent for tightly coupled work;
- use parallel research agents when branches are genuinely independent and breadth matters;
- use a separate evaluator when the task is hard enough that self-grading is risky;
- add specialized planners/evaluators only if traces or evals show they add value.

The harness includes a model-upgrade review specifically to delete scaffolding that is no longer load-bearing.

---

## Design principle 8 — Preserve state outside the conversation

Long-running work must survive:

- context compaction;
- a new Sonnet session;
- a model upgrade;
- a coworker taking over;
- the original researcher being unavailable.

The durable minimum is:

- `GOAL.md` — why the work exists;
- `STATE.json` — machine-readable current position;
- `tasks/CURRENT.md` — immediate work contract;
- `candidates/registry.json` — alternatives and their actual status;
- `evidence/index.json` — provenance map;
- `wiki/` — high-signal synthesis;
- `runs/` — session handoffs and traces/summaries;
- `decisions/` — why important choices were made;
- `evals/` — what success means and whether it passed.

Anthropic's long-running-agent work found this handoff pattern essential across context windows and observed that JSON was harder for agents to casually rewrite than free-form Markdown for machine state. This harness uses JSON for state/registries and Markdown for human-readable reasoning.

---

## Design principle 9 — “Exhausted” must be scoped and earned

Agents are prone to turning one blocked path into a global impossibility statement. The harness therefore treats alternatives as a registry and makes terminal claims depend on that registry.

A candidate can be:

`UNEXPLORED`, `RESEARCHING`, `ACTIVE`, `PROMISING`, `BLOCKED`, `RULED_OUT`, `SELECTED`, `SUPERSEDED`, or `NOT_APPLICABLE`.

`EXHAUSTED` is invalid while a materially relevant candidate is merely unexplored, researching, active, promising, or blocked on an obtainable human action. Every ruled-out candidate must identify the exact scope of the negative evidence.

This is an engineering discipline rather than an AI-specific trick: preserve falsifiability and do not over-generalize from a failed test.

---

## Design principle 10 — Non-code work uses the same loop, different containment

The same architecture fits production-data analysis:

- orientation maps warehouses, semantic layers, lineage/code, dashboards, permissions, and source-of-truth tables;
- research builds a data/domain wiki;
- candidate hypotheses are explicit;
- experiments are read-only queries or analysis scripts against snapshots;
- evidence captures query text, data freshness, row counts, result artifacts, assumptions, and provenance;
- evals compare results against known answers, reconciliation totals, invariants, or SME checks;
- production writes/exports remain hard-gated.

OpenAI's in-house data-agent write-up supports several of these choices: pass-through permissions, raw-result inspectability, continuous evals, fewer non-overlapping tools, and mining pipeline code for business meaning that schemas alone omit.

For pure document research, the “experiment” can be a targeted search, contradiction check, source triangulation, or calculation. For operations work, it can be a dry run or a simulation. The state/evidence/evaluation discipline remains the same.

---

## Known limitations

This harness does not make a weak model infallible. It changes the failure surface:

- it makes unsupported claims easier to detect;
- it reduces context-loss damage;
- it makes negative conclusions more scoped;
- it constrains actions;
- it turns success into something testable;
- it makes a project inspectable by another human or model.

It also adds overhead. On trivial work, do not use the full harness. `R0` exists for this reason. Anthropic's 2026 harness work explicitly recommends removing components when stronger models no longer need them.

Evaluation can also fail. Model graders require calibration, deterministic tests can be brittle, and human reviewers can disagree. The framework therefore supports mixed graders and a first-class `EVAL_DEFECT` path.

Finally, organizational security policy supersedes this framework. `R3_ORG_CRITICAL` is intentionally incomplete: regulated or safety-critical teams must layer their own approval, audit, retention, and validation requirements on top.

---

## Research basis / reading list

Primary and high-value sources consulted for this design:

1. Anthropic, **Building effective agents** (2024-12-19)  
   https://www.anthropic.com/engineering/building-effective-agents
2. Anthropic, **How we built our multi-agent research system** (2025-06-13)  
   https://www.anthropic.com/engineering/multi-agent-research-system
3. Anthropic, **Writing effective tools for AI agents — using AI agents** (2025-09-11)  
   https://www.anthropic.com/engineering/writing-tools-for-agents
4. Anthropic, **Effective context engineering for AI agents** (2025-09-29)  
   https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
5. Anthropic, **Equipping agents for the real world with Agent Skills** (2025-10-16; portability update 2025-12-18)  
   https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
6. Anthropic, **Effective harnesses for long-running agents** (2025-11-26)  
   https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
7. Anthropic, **Demystifying evals for AI agents** (2026-01-09)  
   https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
8. Anthropic, **Harness design for long-running application development** (2026-03-24)  
   https://www.anthropic.com/engineering/harness-design-long-running-apps
9. Anthropic, **How we built Claude Code auto mode: a safer way to skip permissions** (2026-03-25)  
   https://www.anthropic.com/engineering/claude-code-auto-mode
10. Anthropic, **Scaling Managed Agents: Decoupling the brain from the hands** (2026-04-08)  
    https://www.anthropic.com/engineering/managed-agents
11. Anthropic, **How we contain Claude across products** (2026-05-25)  
    https://www.anthropic.com/engineering/how-we-contain-claude
12. Anthropic Claude Cookbook, **Context engineering: memory, compaction, and tool clearing** (2026-03-20)  
    https://platform.claude.com/cookbook/tool-use-context-engineering-context-engineering-tools
13. OpenAI, **How evals drive the next chapter in AI for businesses** (2025-11-19)  
    https://openai.com/index/evals-drive-next-chapter-of-ai/
14. OpenAI, **Inside OpenAI’s in-house data agent** (2026)  
    https://openai.com/index/inside-our-in-house-data-agent/
15. OpenAI, **Separating signal from noise in coding evaluations** (2026-07-08)  
    https://openai.com/index/separating-signal-from-noise-coding-evaluations/
16. OpenAI, **A practical guide to building AI agents**  
    https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/
17. NIST, **AI Risk Management Framework: Generative AI Profile (NIST AI 600-1)** (2024; updated site 2026)  
    https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
18. NIST AI Resource Center / AI RMF Core  
    https://airc.nist.gov/
19. OWASP, **AI Agent Security Cheat Sheet**  
    https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html
20. OWASP, **LLM Prompt Injection Prevention Cheat Sheet**  
    https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html
21. Starace et al., **PaperBench: Evaluating AI's Ability to Replicate AI Research** (2025)  
    https://arxiv.org/abs/2504.01848
22. Kim et al., **From Reproduction to Replication: Evaluating Research Agents with Progressive Code Masking / AutoExperiment** (2025)  
    https://arxiv.org/abs/2506.19724
23. Bragg et al., **AstaBench: Rigorous Benchmarking of AI Agents with a Scientific Research Suite** (2025)  
    https://arxiv.org/abs/2510.21652

The sources are intentionally mixed across model vendors, standards/security organizations, and academic benchmarks. Vendor engineering posts are useful empirical reports, not universal laws. The harness should be periodically re-evaluated against newer models and your organization's own measured outcomes.

---


## Version 2.2 guided-install decision (superseded in 2.3)

Version 2.2 briefly made the preferred personal install path agent-guided rather than shell-first. The user launches an interactive Claude Code session with a short request to install EFWH from the repository; the repository's `INSTALL.md` is the canonical procedure Claude follows. This keeps the human-facing action stable while allowing the repository to evolve environment-specific installation details.

The deterministic `scripts/install.ps1` and `scripts/install.sh` remain available as an auditable fallback. Both resolve the personal Claude configuration root from `CLAUDE_CONFIG_DIR` when set and otherwise use `~/.claude`. The guided path does not expand authority: ordinary Claude Code permission prompts and enterprise policy remain in force.

## Version 2.1 company-release decisions

The company-release form makes the Claude Code Skill the single canonical executable protocol. The previous package duplicated the static harness at the repository root and inside the Skill; that duplication is removed to prevent drift. The auditable protocol remains under `.claude/skills/efwh/resources/harness/`, where Claude loads it progressively.

The Skill is also explicitly **user-invocable only** using `disable-model-invocation: true`. Current Claude Code documentation recommends this control for workflows whose timing should remain a user decision. EFWH changes the operating mode of an investigation and writes durable state, so explicit `/efwh` invocation is the appropriate company default.

Company deployment should prefer managed/enterprise Skills when available. Personal installation is retained for pilots and users outside managed deployment. EFWH deliberately declares no broad `allowed-tools` permissions: the organization's Claude Code permissions, sandbox, auto-mode rules, and external policy remain authoritative.

The repository adds automated structural validation, ownership, contribution rules, a release checklist, security guidance, and a rollout runbook. These are release-engineering controls around EFWH; they do not change the evidence protocol itself.

## Version 2 UX decision — make the workflow a Skill, not a form

The original package asked the user to edit `GOAL.md` and `CONFIG.yaml` before pasting a kickoff prompt. That is explicit and auditable, but it turns adoption friction into part of every investigation.

Version 2 moves initialization into an **Agent Skill**. Anthropic's current Claude Code documentation explicitly positions Skills as the mechanism for reusable multi-step procedures: personal Skills live under `~/.claude/skills/`, project Skills under `.claude/skills/`, and they can be invoked directly as `/skill-name`. Anthropic's broader Agent Skills design uses progressive disclosure: the agent sees only lightweight metadata until the Skill is invoked, then loads detailed resources only when needed. This matches EFWH well because most of its reference material should not occupy the model's context during ordinary work.

The new default user interaction is therefore one line:

```text
/efwh <problem in normal language>
```

The agent writes the project brief, configuration, state, evidence registry, and wiki itself. Autonomy and rigor become optional arguments rather than mandatory form fields. When omitted, the Skill chooses conservative adaptive defaults from the user's intent, the effective permissions, and the available containment boundary. Hard gates remain external constraints and cannot be relaxed merely because the user omitted a configuration choice.

This follows three current design signals:

1. **Anthropic Agent Skills / Claude Code Skills:** reusable workflows should be packaged as discoverable Skills rather than repeatedly pasted prompts or large always-on instruction files. Skills support project, personal, and organization-level distribution and load supporting files progressively.
2. **Anthropic 2026 harness research:** a planner can expand a short user prompt into a useful specification, while overly detailed up-front implementation instructions can cascade early mistakes. EFWH therefore asks the human for the desired outcome and lets orientation/research fill in the rest.
3. **OpenAI's 2026 data-agent lessons:** users should be able to ask natural questions while the agent itself discovers context, tools, lineage, and source-of-truth data. Requiring a human to pre-fill a configuration document works against that goal.

### Why not make the HTML page the runtime?

A browser configurator can make setup pleasant, but it is the wrong source of truth. Browser file APIs vary by policy and browser, and asking people to generate/download configuration files simply replaces Markdown editing with a prettier form. The HTML page in v2 is therefore **education + command composition**, not an execution dependency. EFWH still works if the page is never opened.

### Why explicit `/efwh` instead of invisible automatic behavior?

The framework changes how an agent conducts an entire task and may persist research artifacts. Requiring a short explicit command makes intent legible without imposing meaningful friction. Teams that prefer automatic invocation can relax the Skill's trigger policy later; organization-managed deployment can also make the Skill universally available without asking each user to install it per repository.

### Adaptive autonomy is not permission escalation

The Skill may infer an appropriate working mode from intent—e.g. read-oriented research versus isolated implementation—but it does not infer permission for production writes, destructive actions, secret disclosure, external communications, or other hard-gated behavior. The purpose of adaptive defaults is to remove configuration ceremony, not to broaden authority.

**Additional v2 sources:**

- Claude Code — Extend Claude with skills: https://code.claude.com/docs/en/skills
- Anthropic — Equipping agents for the real world with Agent Skills: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- Anthropic — Harness design for long-running application development: https://www.anthropic.com/engineering/harness-design-long-running-apps
- OpenAI — Inside our in-house data agent: https://openai.com/index/inside-our-in-house-data-agent/


## Version 2.3 distribution decision — deterministic install, agentic use

The earlier guided-install experiment asked Claude Code to interpret a repository URL, discover installation instructions, and copy the Skill itself. In corporate environments this proved unnecessarily variable: an agent could fall back to web-search/MCP retrieval and reconstruct files one-by-one when Git semantics or network access were not obvious. That made installation depend on model behavior even though installation is fundamentally a deterministic filesystem operation.

Version 2.3 therefore moves installation out of the agent loop. The preferred interface is `npx --yes @zacharythrasher/efwh install`. The npm tarball contains the canonical `.claude/skills/efwh/` tree, so the installer does not need GitHub at runtime and does not rely on the model to choose a transport. Existing installs are backed up before replacement and the copied tree is verified.

This intentionally follows a broader design rule: **use deterministic software for deterministic transport and state changes; use the model where interpretation and reasoning are actually required.** The `/efwh` workflow remains agentic, but getting that workflow onto disk is not.

Restricted networks are handled with the same principle. An offline ZIP and local npm tarball carry the identical Skill payload and can be mirrored through an approved internal software channel. The fallback does not weaken enterprise policy or introduce another network path; it simply removes GitHub/npm from the installation transaction once the artifact has been obtained.
