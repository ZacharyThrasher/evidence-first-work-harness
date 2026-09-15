# Evidence-First Work Harness (EFWH)

A portable file-based operating system for high-quality model-assisted work.

The harness separates four concerns that are often collapsed into one prompt:

1. **Knowledge:** What do we know, and why?
2. **Search space:** What candidate explanations/solutions remain?
3. **Execution:** What is the model allowed to do next?
4. **Evaluation:** What evidence would prove that the step or project succeeded?

Start with `START_HERE.md`, then use `KICKOFF_PROMPT.md` in the agent session.

Core files are model-agnostic. `integrations/` contains optional Claude-specific guidance.
