# Channel Workflows

Use these workflows for mainland China recruiting platforms and company career pages. The goal is queue-confirmed, user-approved application assistance, not hidden automation.

## Universal Rules

- Ask the user which channels to use in this run.
- Let the user log in manually. Do not store credentials.
- Use visible search and filter controls where possible.
- Build a queue before submitting applications.
- Show the queue confirmation view before batch submission.
- After queue confirmation, submit only safe jobs and wait 30 seconds after each submitted job.
- Do not set a fixed per-platform batch size limit.
- Keep browsing pace reasonable. Stop when the site blocks automation or requires verification.
- If one platform has 5 consecutive abnormal items in the current batch, pause that platform for this run.
- If a site explicitly prohibits automation, do not auto-submit on that site. Generate the queue and manual operation guidance only.

## Queue Confirmation View

Show a queue summary before batch submission:

- total jobs
- estimated automatic submissions
- estimated manual items
- estimated skipped items
- filtering conditions
- matching mode

For each job show:

- company
- role title
- visible salary if available
- channel
- match score
- match reason
- key risks or gaps
- selected resume version
- expected action: automatic submission, needs manual handling, or recommended skip

The confirmation view does not need to show city/remote or job links because the user already answered location preferences.

## Recruiting Platforms

Examples include Boss Zhipin, Liepin, 51job, Zhaopin, Lagou, Maimai, and similar sites.

Workflow:

1. User opens or logs into the platform manually when needed.
2. Apply filters from the user's preferences: title, city, salary, industry, company size, experience, and recency.
3. Capture JD text, company information, link, salary, and visible requirements.
4. Score with the matching rubric.
5. Add qualified roles to the queue.
6. Show the queue confirmation view and wait for the user's single queue confirmation.
7. For confirmed safe roles, help fill application fields when allowed by the platform and submit automatically.
8. Wait 30 seconds after each submitted job.
9. Mark risky jobs `needs_manual` and continue with the next safe queued job.

## Company Career Pages

Company pages vary widely, so expect more `needs_manual` items than on stable third-party platforms.

Workflow:

1. Find the official career page from the company website or a reliable search result.
2. Filter by function, city, business unit, and keyword when controls exist.
3. Record the official URL and JD details.
4. If an external ATS is used, follow its visible flow and require user login where needed.
5. Add eligible jobs to the queue.
6. After queue confirmation, attempt only safe submissions.
7. Pause and mark `needs_manual` when the page requires new judgment or extra information.

## When To Mark Needs Manual

Mark the job `needs_manual`, record the reason, and continue with other safe queued jobs if any of these appear:

- CAPTCHA, SMS, QR, or email verification.
- Explicit anti-bot or unusual traffic warning.
- Required privacy authorization beyond ordinary application submission.
- Open-ended questions, expected salary decisions, transfer/adjustment choices, tests, or portfolio uploads.
- Payment request, suspicious data request, or unclear third-party form.
- Page content differs from the queued JD in a meaningful way.
- A site prohibits automation.

## Final Report

After a batch run, report:

- total queued jobs
- submitted count
- needs-manual count
- skipped count
- failed count
- each manual or failed job's reason
- log file location when available
- recommended next actions
