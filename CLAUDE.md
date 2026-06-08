# Claude Code Instructions for resume-apply

Use this repository as a portable workflow, not a Codex-only skill.

1. Read `SKILL.md` first and follow its standard workflow.
2. Use `references/matching-rubric.md` when evaluating JD fit.
3. Use `references/channel-workflows.md` before any recruiting-site or company-career-page interaction.
4. Run the Python scripts only if the local environment allows command execution and the user has approved any needed file access.
5. Build a queue before submitting. After the user confirms the queue once, submit only safe jobs, wait 30 seconds after each submission, and mark risky jobs `needs_manual` instead of forcing them through.

Safety is part of the feature: do not save passwords, do not bypass verification, respect sites that prohibit automation, and pause a platform after 5 consecutive abnormal items in one run.
