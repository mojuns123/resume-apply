# Matching Rubric

Use this rubric to score jobs consistently. Prefer explainable matches over opaque scores.

## Matching Modes

- `strict`: Recommend only roles with strong title, skill, seniority, location, and compensation fit. Avoid speculative pivots.
- `balanced`: Include strong fits and reasonable adjacent roles where the resume shows transferable evidence.
- `broad`: Include roles that satisfy core constraints even when some skills or industry experience are missing. Label risks clearly.

## Score Bands

- `85-100`: Strong match. Resume evidence directly supports most JD requirements.
- `70-84`: Good match. Some gaps exist, but the role is realistic with tailored positioning.
- `55-69`: Possible stretch. Use only in `balanced` or `broad` mode and call out missing evidence.
- `<55`: Do not recommend unless the user explicitly asks for broad exploration.

## Core Factors

Evaluate each JD against the selected resume and user preferences:

1. Role title and function alignment.
2. Required skills, tools, certificates, and domain experience.
3. Years of experience and seniority level.
4. Industry fit and transferable business context.
5. Company size, stage, and ownership preference.
6. City, remote policy, travel needs, and relocation constraints.
7. Salary range and compensation notes.
8. Hard blockers: required degree, license, language, citizenship, on-site availability, or mandatory background.
9. Negative preferences: blocked companies, unwanted industries, low-quality JD signals, or suspicious postings.

## Output Fields

For each candidate job, record:

- company
- role title
- channel
- job link, for logs even if hidden from the queue confirmation view
- location, for logs even if hidden from the queue confirmation view
- salary if visible
- score
- match mode used
- 2-4 sentence match reason
- missing or uncertain requirements
- risk notes
- selected resume version
- suggested resume/application angle
- queue status: `queued`, `submitted`, `needs_manual`, `skipped`, `failed`, or `paused`
- status reason
- whether the action was triggered by batch confirmation

## Decision Guidance

In `strict` mode, prefer fewer high-quality applications. In `balanced` mode, include adjacent roles only when the resume has concrete proof. In `broad` mode, still exclude obvious mismatches, scams, unpaid roles unless requested, and jobs that violate hard user constraints.

A job can enter the queue only when it satisfies the user's already-confirmed location preferences. The queue confirmation view does not need to repeat city/remote or job link, but logs should keep them when available.
