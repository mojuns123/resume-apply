---
name: resume-apply
description: Portable AI-agent workflow for China mainland job search assistance. Use when an AI agent such as Codex, Claude Code, or another coding/automation assistant needs to set up or reuse a resume folder, analyze resumes, define job preferences, search mainland China recruiting sites or company career pages, shortlist JD matches, prepare application records, and assist with user-confirmed resume submissions without storing passwords or bypassing verification.
---

# Resume Apply

## Overview

Use this workflow to help a user search and apply for mainland China jobs with a controlled, confirm-before-submit process. Any capable AI agent can use it: Codex can load it as a skill, Claude Code can read `CLAUDE.md`, and other agents can start from `AGENTS.md` or this file.

The workflow reads resumes from a user-chosen folder, matches roles against resume content and user preferences, prepares shortlists and logs, and assists with applications only after explicit user confirmation.

Never fully automate final submission. Never save recruiting-site passwords. Never bypass CAPTCHA, anti-bot checks, paywalls, access controls, or platform rules.

## Agent Compatibility

- **Codex/OpenAI agents**: Use this `SKILL.md` as the primary skill instructions. `agents/openai.yaml` is optional UI metadata for compatible OpenAI surfaces.
- **Claude Code**: Read `CLAUDE.md` first, then follow this `SKILL.md` and the referenced files.
- **Other AI agents**: Read `AGENTS.md` first, then follow this `SKILL.md`. Use the Python scripts only if the environment allows local command execution.
- **Agents without tool execution**: Follow the same decision workflow manually. Ask the user to provide resume folder contents, JD text, and application results when scripts or browsing are unavailable.

## First-Use Setup

1. Check whether a resume folder has already been configured.
   - If command execution is available, run `scripts/manage_profile.py show`.
   - If command execution is not available, ask the user whether they already have a dedicated resume folder.
2. If no resume folder is configured, ask the user to create one dedicated folder for resumes and provide its path.
3. Save the folder after confirming it exists.
   - With command execution: run `scripts/manage_profile.py set-resume-folder <path>`.
   - Without command execution: remember the folder only within the current agent context and ask the user to persist it in their tool if needed.
4. Tell the user to keep current resume files in that folder. Supported files are typically `.pdf`, `.docx`, `.doc`, `.txt`, and `.md`.
5. Create output folders inside the resume folder when possible with `scripts/application_log.py init-dirs <resume-folder>`.

Default configuration location for the bundled scripts is cross-platform and tool-neutral: `~/.resume-apply/settings.json`. Scripts also honor `RESUME_APPLY_CONFIG_DIR` for testing or custom environments, and they can read the legacy Codex path `~/.codex/resume-apply/settings.json` when it already exists.

## Standard Workflow

1. **Load context**
   - Use `scripts/manage_profile.py show` to find the resume folder when commands are available.
   - Use `scripts/manage_profile.py list-resumes` to inspect available resumes when commands are available.
   - If there are multiple resumes, ask which one to optimize for this run.

2. **Collect preferences**
   Ask for or confirm: target roles, cities or remote preference, salary range, industries, company size, seniority, must-have keywords, blocked companies, and channels to use. Ask for matching mode every run: `strict`, `balanced`, or `broad`.

3. **Search channels**
   Search recruiting platforms and company career pages according to the user's channel preference. Use `references/channel-workflows.md` before interacting with a channel.

4. **Match jobs**
   Use `references/matching-rubric.md` to score each JD. Keep a short reason, missing requirements, risk notes, and suggested resume angle for each candidate.

5. **Prepare shortlist**
   Save a shortlist under `<resume-folder>/job-shortlists/` when file access is available. If not, present the shortlist in the conversation with date, channel, company, role, link, score, match reason, risks, and recommended action.

6. **Confirm before applying**
   Show the shortlist and ask the user which jobs to apply to. Before any final submit button, pause and ask for explicit confirmation.

7. **Log outcomes**
   Use `scripts/application_log.py append <resume-folder> ...` after each confirmed application or skipped role when command execution is available. Use `check-duplicate` before applying to avoid repeat submissions. If scripts are unavailable, keep a visible application log in the conversation or in the user's chosen tracking tool.

## Safety Rules

- Do not save or request passwords, one-time codes, ID numbers, or other sensitive credentials for storage.
- User must manually log in to recruiting websites or company systems.
- Stop and ask the user to take over when CAPTCHA, SMS verification, QR login, or anti-automation prompts appear.
- Respect robots, terms, rate limits, and visible site restrictions.
- Do not fabricate application status. If status is unknown, record `unknown`.
- Treat resume files and application logs as private personal data.

## Outputs

Store generated files inside the configured resume folder unless the user asks otherwise:

- `job-shortlists/`: candidate job lists for review.
- `application-logs/`: CSV and JSONL application history.
- `notes/`: optional run notes, company research, or interview follow-up notes.

If the agent cannot write files, output the same information in the conversation and clearly label it for the user to save or transfer.

## References

- Read `references/matching-rubric.md` when scoring or explaining JD fit.
- Read `references/channel-workflows.md` before using recruiting platforms or company career pages.
