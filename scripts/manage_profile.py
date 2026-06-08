#!/usr/bin/env python3
"""Manage cross-platform profile settings for resume-apply."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Any

RESUME_EXTENSIONS = {".pdf", ".docx", ".doc", ".txt", ".md"}


def config_dir() -> Path:
    override = os.environ.get("RESUME_APPLY_CONFIG_DIR") or os.environ.get("RESUME_AUTO_APPLY_CONFIG_DIR")
    if override:
        return Path(override).expanduser().resolve()
    return Path.home() / ".codex" / "resume-apply"


def settings_path() -> Path:
    return config_dir() / "settings.json"


def load_settings() -> dict[str, Any]:
    path = settings_path()
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def save_settings(settings: dict[str, Any]) -> None:
    path = settings_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(settings, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def normalize_folder(folder: str) -> Path:
    return Path(folder).expanduser().resolve()


def command_show(_: argparse.Namespace) -> int:
    settings = load_settings()
    result = {
        "settings_path": str(settings_path()),
        "resume_folder": settings.get("resume_folder"),
        "resume_folder_exists": bool(settings.get("resume_folder") and Path(settings["resume_folder"]).exists()),
        "preferences": settings.get("preferences", {}),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


def command_set_resume_folder(args: argparse.Namespace) -> int:
    folder = normalize_folder(args.folder)
    if not folder.exists() or not folder.is_dir():
        raise SystemExit(f"Resume folder does not exist or is not a directory: {folder}")
    settings = load_settings()
    settings["resume_folder"] = str(folder)
    settings.setdefault("preferences", {})
    save_settings(settings)
    print(json.dumps({"saved": True, "resume_folder": str(folder), "settings_path": str(settings_path())}, ensure_ascii=False, indent=2))
    return 0


def command_list_resumes(_: argparse.Namespace) -> int:
    settings = load_settings()
    folder_value = settings.get("resume_folder")
    if not folder_value:
        raise SystemExit("No resume folder configured. Ask the user to create one dedicated resume folder, then run set-resume-folder.")
    folder = Path(folder_value)
    if not folder.exists() or not folder.is_dir():
        raise SystemExit(f"Configured resume folder is missing: {folder}")
    resumes = [
        {"name": item.name, "path": str(item), "size_bytes": item.stat().st_size}
        for item in sorted(folder.iterdir())
        if item.is_file() and item.suffix.lower() in RESUME_EXTENSIONS
    ]
    print(json.dumps({"resume_folder": str(folder), "count": len(resumes), "resumes": resumes}, ensure_ascii=False, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Manage resume-apply settings")
    subparsers = parser.add_subparsers(dest="command", required=True)

    show = subparsers.add_parser("show", help="Show current settings")
    show.set_defaults(func=command_show)

    set_folder = subparsers.add_parser("set-resume-folder", help="Save the user's dedicated resume folder")
    set_folder.add_argument("folder")
    set_folder.set_defaults(func=command_set_resume_folder)

    list_resumes = subparsers.add_parser("list-resumes", help="List resume files in the configured folder")
    list_resumes.set_defaults(func=command_list_resumes)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
