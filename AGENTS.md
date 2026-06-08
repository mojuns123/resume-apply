# Agent Instructions for resume-apply

This repository contains a portable AI-agent workflow for assisted resume applications in mainland China job-search workflows. It supports queue-confirmed batch submission for safe jobs, while risky jobs must be paused for manual handling.

## Start Here

1. Read `SKILL.md` for the full workflow.
2. Read `references/matching-rubric.md` before scoring job descriptions.
3. Read `references/channel-workflows.md` before interacting with recruiting platforms or company career pages.
4. Use `scripts/manage_profile.py` and `scripts/application_log.py` only when local command execution is available.

## Tool-Agnostic Rules

- Do not treat this as Codex-only. Any AI agent can follow the workflow.
- Build an application queue first; do not submit jobs before the user confirms the queue.
- After queue confirmation, submit only safe jobs and wait 30 seconds after each submission.
- Mark jobs `needs_manual` when they require extra forms, verification, privacy authorization, tests, page mismatch handling, or new user judgment.
- Pause a platform for the current run after 5 consecutive abnormal items on that platform.
- Do not save recruiting-site passwords, one-time codes, or sensitive credentials.
- Do not bypass CAPTCHA, SMS verification, QR login, anti-bot checks, access controls, or explicit site bans on automation.
- If the current AI tool cannot browse, execute commands, or write files, ask the user to provide the missing input and keep the queue or log in the conversation.
