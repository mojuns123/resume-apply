# Agent Instructions for resume-apply

This repository contains a portable AI-agent workflow for assisted resume applications in mainland China job-search workflows.

## Start Here

1. Read `SKILL.md` for the full workflow.
2. Read `references/matching-rubric.md` before scoring job descriptions.
3. Read `references/channel-workflows.md` before interacting with recruiting platforms or company career pages.
4. Use `scripts/manage_profile.py` and `scripts/application_log.py` only when local command execution is available.

## Tool-Agnostic Rules

- Do not treat this as Codex-only. Any AI agent can follow the workflow.
- Do not save recruiting-site passwords, one-time codes, or sensitive credentials.
- Do not bypass CAPTCHA, SMS verification, QR login, anti-bot checks, or access controls.
- Require explicit user confirmation before final application submission.
- If the current AI tool cannot browse, execute commands, or write files, ask the user to provide the missing input and keep the shortlist or log in the conversation.
