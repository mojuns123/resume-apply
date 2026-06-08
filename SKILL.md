---
name: resume-apply
description: Portable AI-agent workflow for China mainland job search assistance. Use when an AI agent such as Codex, Claude Code, or another coding/automation assistant needs to set up or reuse a resume folder, analyze resumes, define job preferences, build a user-reviewed application queue, batch-submit safe queued jobs after confirmation, prepare application records, and pause risky jobs for manual handling without storing passwords or bypassing verification.
---

# Resume Apply

## Overview

Use this workflow to help a user search and apply for mainland China jobs with a controlled queue-confirmation process. Any capable AI agent can use it: Codex can load it as a skill, Claude Code can read `CLAUDE.md`, and other agents can start from `AGENTS.md` or this file.

The workflow reads resumes from a user-chosen folder, matches roles against resume content and user preferences, prepares a reviewed application queue, and can batch-submit queue items only after the user confirms the queue.

Never save recruiting-site passwords. Never bypass CAPTCHA, anti-bot checks, paywalls, access controls, platform rules, or explicit site bans on automation.

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
   - If there are multiple resumes, the agent may recommend the best resume version per job, but the queue confirmation view must show the selected resume for every job.

2. **Collect preferences**
   Ask for or confirm: target roles, cities or remote preference, salary range, industries, company size, seniority, must-have keywords, blocked companies, and channels to use. Ask for matching mode every run: `strict`, `balanced`, or `broad`.

3. **Search channels**
   Search recruiting platforms and company career pages according to the user's channel preference. Use `references/channel-workflows.md` before interacting with a channel.

4. **Match jobs**
   Use `references/matching-rubric.md` to score each JD. Keep a short reason, missing requirements, risk notes, and suggested resume angle for each candidate.

5. **Prepare the application queue**
   Create a queue instead of immediately submitting. Queue items must use one of these statuses: `queued`, `submitted`, `needs_manual`, `skipped`, `failed`, or `paused`.

6. **Show the queue confirmation view**
   Before batch submission, show a queue summary: total jobs, estimated automatic submissions, estimated manual items, estimated skipped items, filtering conditions, and matching mode. For each job show: company, role title, visible salary if available, channel, match score, match reason, key risks or gaps, selected resume version, and expected action. Do not require city/remote or job link in the confirmation view because the user already provided location preferences.

7. **Batch-submit only after queue confirmation**
   After the user confirms the queue once, automatically submit only queue items that are safe to submit. Wait 30 seconds after each submitted job. Do not set a fixed per-platform batch size limit.

8. **Pause risky jobs and continue**
   If a job requires extra forms, open-ended answers, salary decisions, transfer/adjustment choices, portfolio upload, privacy authorization, tests, CAPTCHA, SMS, QR login, page content mismatch, or any other new judgment, mark it `needs_manual` with a structured reason and continue with the next safe queue item.

9. **Respect platform limits**
   If a site explicitly prohibits automation, do not auto-submit on that site. Generate the queue and manual operation guidance only. If one platform has 5 consecutive abnormal items in the current batch, pause that platform for the current run while other platforms may continue.

10. **Support pause and stop**
   During the 30-second wait after each job, allow the user to pause or stop when the current AI tool supports interruption. If real-time interruption is unavailable, check for user pause/stop instructions after each job.

11. **Log outcomes and report**
   Use `scripts/application_log.py append <resume-folder> ...` after each queue state change when command execution is available. Use `check-duplicate` before applying to avoid repeat submissions. The final report must include total queued jobs, submitted count, needs-manual count, skipped count, failed count, reasons for manual/failed items, log file location, and next-step recommendations.

## Safety Rules

- Do not save or request passwords, one-time codes, ID numbers, or other sensitive credentials for storage.
- User must manually log in to recruiting websites or company systems.
- User may confirm the queue once for batch submission, but the agent must still pause unsafe jobs and never bypass verification or new judgment points.
- Stop and ask the user to take over when CAPTCHA, SMS verification, QR login, or anti-automation prompts appear.
- Respect robots, terms, rate limits, visible site restrictions, and explicit bans on automation.
- Do not fabricate application status. If status is unknown, record `failed` or `needs_manual` with an honest reason.
- Treat resume files and application logs as private personal data.

## Outputs

Store generated files inside the configured resume folder unless the user asks otherwise:

- `job-shortlists/`: candidate job lists and confirmed application queues.
- `application-logs/`: CSV and JSONL application history.
- `notes/`: optional run notes, company research, or interview follow-up notes.

If the agent cannot write files, output the same information in the conversation and clearly label it for the user to save or transfer.

## References

- Read `references/matching-rubric.md` when scoring or explaining JD fit.
- Read `references/channel-workflows.md` before using recruiting platforms or company career pages.
