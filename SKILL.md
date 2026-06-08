---
name: resume-apply
description: Cross-platform workflow for China mainland job search assistance. Use when the user wants to set up or reuse a resume folder, analyze resumes, define job preferences, search mainland China recruiting sites or company career pages, shortlist JD matches, prepare application records, and assist with user-confirmed resume submissions without storing passwords or bypassing verification.
---

# Resume Apply

## Overview

Use this skill to help a user search and apply for mainland China jobs with a controlled, confirm-before-submit workflow. The skill reads resumes from a user-chosen folder, matches roles against resume content and user preferences, prepares shortlists and logs, and assists with applications only after explicit user confirmation.

Never fully automate final submission. Never save recruiting-site passwords. Never bypass CAPTCHA, anti-bot checks, paywalls, access controls, or platform rules.

## First-Use Setup

1. Check the saved profile with `scripts/manage_profile.py show`.
2. If no resume folder is configured, ask the user to create one dedicated folder for resumes and provide its path.
3. Save the folder with `scripts/manage_profile.py set-resume-folder <path>` after confirming it exists.
4. Tell the user to keep current resume files in that folder. Supported files are typically `.pdf`, `.docx`, `.doc`, `.txt`, and `.md`.
5. Create output folders inside the resume folder with `scripts/application_log.py init-dirs <resume-folder>`.

Default configuration location is cross-platform: `~/.codex/resume-apply/settings.json`. Scripts also honor `RESUME_APPLY_CONFIG_DIR` for testing or custom environments.

## Standard Workflow

1. **Load context**
   - Run `scripts/manage_profile.py show` to find the resume folder.
   - Run `scripts/manage_profile.py list-resumes` to inspect available resumes.
   - If there are multiple resumes, ask which one to optimize for this run.

2. **Collect preferences**
   Ask for or confirm: target roles, cities or remote preference, salary range, industries, company size, seniority, must-have keywords, blocked companies, and channels to use. Ask for matching mode every run: `strict`, `balanced`, or `broad`.

3. **Search channels**
   Search recruiting platforms and company career pages according to the user's channel preference. Use `references/channel-workflows.md` before interacting with a channel.

4. **Match jobs**
   Use `references/matching-rubric.md` to score each JD. Keep a short reason, missing requirements, risk notes, and suggested resume angle for each candidate.

5. **Prepare shortlist**
   Save a shortlist under `<resume-folder>/job-shortlists/` with date, channel, company, role, link, score, match reason, risks, and recommended action.

6. **Confirm before applying**
   Show the shortlist and ask the user which jobs to apply to. Before any final submit button, pause and ask for explicit confirmation.

7. **Log outcomes**
   Use `scripts/application_log.py append <resume-folder> ...` after each confirmed application or skipped role. Use `check-duplicate` before applying to avoid repeat submissions.

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

## References

- Read `references/matching-rubric.md` when scoring or explaining JD fit.
- Read `references/channel-workflows.md` before using recruiting platforms or company career pages.
