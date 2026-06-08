#!/usr/bin/env python3
"""Create output folders and maintain application queue logs."""

from __future__ import annotations

import argparse
import csv
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

STATUS_CHOICES = ["queued", "submitted", "needs_manual", "skipped", "failed", "paused", "applied", "saved", "unknown"]
STATUS_ALIASES = {
    "applied": "submitted",
    "saved": "queued",
    "unknown": "failed",
}

FIELDNAMES = [
    "timestamp",
    "status",
    "status_reason",
    "company",
    "role",
    "channel",
    "job_link",
    "resume_file",
    "score",
    "batch_confirmed",
    "batch_id",
    "notes",
]


def resolve_resume_folder(folder: str) -> Path:
    path = Path(folder).expanduser().resolve()
    if not path.exists() or not path.is_dir():
        raise SystemExit(f"Resume folder does not exist or is not a directory: {path}")
    return path


def normalize_status(status: str) -> str:
    return STATUS_ALIASES.get(status, status)


def output_dirs(folder: Path) -> dict[str, Path]:
    return {
        "application_logs": folder / "application-logs",
        "job_shortlists": folder / "job-shortlists",
        "notes": folder / "notes",
    }


def init_dirs(folder: Path) -> dict[str, str]:
    dirs = output_dirs(folder)
    for path in dirs.values():
        path.mkdir(parents=True, exist_ok=True)
    return {name: str(path) for name, path in dirs.items()}


def csv_path(folder: Path) -> Path:
    return folder / "application-logs" / "applications.csv"


def jsonl_path(folder: Path) -> Path:
    return folder / "application-logs" / "applications.jsonl"


def read_rows(folder: Path) -> list[dict[str, str]]:
    path = csv_path(folder)
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_row(folder: Path, row: dict[str, Any]) -> None:
    init_dirs(folder)
    cpath = csv_path(folder)
    exists = cpath.exists()
    normalized = {field: str(row.get(field, "")) for field in FIELDNAMES}
    with cpath.open("a", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDNAMES)
        if not exists:
            writer.writeheader()
        writer.writerow(normalized)
    with jsonl_path(folder).open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(normalized, ensure_ascii=False) + "\n")


def command_init_dirs(args: argparse.Namespace) -> int:
    folder = resolve_resume_folder(args.resume_folder)
    print(json.dumps(init_dirs(folder), ensure_ascii=False, indent=2))
    return 0


def command_append(args: argparse.Namespace) -> int:
    folder = resolve_resume_folder(args.resume_folder)
    status = normalize_status(args.status)
    row = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "status": status,
        "status_reason": args.status_reason or "",
        "company": args.company,
        "role": args.role,
        "channel": args.channel,
        "job_link": args.job_link,
        "resume_file": args.resume_file or "",
        "score": args.score or "",
        "batch_confirmed": "true" if args.batch_confirmed else "false",
        "batch_id": args.batch_id or "",
        "notes": args.notes or "",
    }
    write_row(folder, row)
    print(json.dumps({"logged": True, "row": row, "csv": str(csv_path(folder))}, ensure_ascii=False, indent=2))
    return 0


def command_check_duplicate(args: argparse.Namespace) -> int:
    folder = resolve_resume_folder(args.resume_folder)
    rows = read_rows(folder)
    matches = [row for row in rows if row.get("job_link") == args.job_link]
    print(json.dumps({"duplicate": bool(matches), "matches": matches}, ensure_ascii=False, indent=2))
    return 0


def command_summary(args: argparse.Namespace) -> int:
    folder = resolve_resume_folder(args.resume_folder)
    rows = read_rows(folder)
    if args.batch_id:
        rows = [row for row in rows if row.get("batch_id") == args.batch_id]
    counts: dict[str, int] = {}
    manual_or_failed = []
    for row in rows:
        status = row.get("status", "")
        counts[status] = counts.get(status, 0) + 1
        if status in {"needs_manual", "failed"}:
            manual_or_failed.append({
                "company": row.get("company", ""),
                "role": row.get("role", ""),
                "status": status,
                "status_reason": row.get("status_reason", ""),
            })
    result = {
        "total": len(rows),
        "counts": counts,
        "manual_or_failed": manual_or_failed,
        "csv": str(csv_path(folder)),
        "jsonl": str(jsonl_path(folder)),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Manage resume application queue logs")
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_cmd = subparsers.add_parser("init-dirs", help="Create output directories inside the resume folder")
    init_cmd.add_argument("resume_folder")
    init_cmd.set_defaults(func=command_init_dirs)

    append = subparsers.add_parser("append", help="Append an application queue log row")
    append.add_argument("resume_folder")
    append.add_argument("--status", required=True, choices=STATUS_CHOICES)
    append.add_argument("--status-reason")
    append.add_argument("--company", required=True)
    append.add_argument("--role", required=True)
    append.add_argument("--channel", required=True)
    append.add_argument("--job-link", required=True)
    append.add_argument("--resume-file")
    append.add_argument("--score")
    append.add_argument("--batch-confirmed", action="store_true")
    append.add_argument("--batch-id")
    append.add_argument("--notes")
    append.set_defaults(func=command_append)

    duplicate = subparsers.add_parser("check-duplicate", help="Check whether a job link was already logged")
    duplicate.add_argument("resume_folder")
    duplicate.add_argument("--job-link", required=True)
    duplicate.set_defaults(func=command_check_duplicate)

    summary = subparsers.add_parser("summary", help="Summarize application queue logs")
    summary.add_argument("resume_folder")
    summary.add_argument("--batch-id")
    summary.set_defaults(func=command_summary)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
