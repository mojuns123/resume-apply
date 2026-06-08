# resume apply

`resume-apply` is a Codex skill for assisted resume applications in mainland China job-search workflows.

It helps a user choose a dedicated resume folder, analyze resumes, collect job preferences, shortlist matching roles from recruiting platforms and company career pages, and assist with applications only after explicit user confirmation.

## What it does

- Uses a cross-platform resume folder setup instead of hard-coded Windows or macOS paths.
- Stores settings in `~/.codex/resume-apply/settings.json`.
- Reads resumes from the user-selected folder.
- Supports strict, balanced, and broad matching modes.
- Scores job descriptions against resume evidence and user preferences.
- Creates shortlist and application log folders inside the resume folder.
- Requires confirmation before any final application submission.

## Safety boundaries

This skill is intentionally not a hidden auto-submit bot.

- It does not save recruiting-site passwords.
- It does not bypass CAPTCHA, SMS, QR login, anti-bot checks, or access controls.
- It asks the user to log in manually.
- It pauses before final submission.
- It treats resumes and application logs as private personal data.

## Structure

```text
resume-apply/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── channel-workflows.md
│   └── matching-rubric.md
└── scripts/
    ├── application_log.py
    └── manage_profile.py
```

## Typical use

Ask Codex to use `$resume-apply` to shortlist China mainland jobs for your resume and assist applications after you confirm.

On first use, the skill asks you to create and provide a dedicated resume folder. Later runs reuse that folder by default.
