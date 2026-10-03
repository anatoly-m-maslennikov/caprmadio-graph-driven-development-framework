#!/usr/bin/env python3
"""Update CAPRMEDIO Atom or Projection revision metadata.

Parameters:
    path: Markdown carrier to update.
    --kind: atom or projection.
    --new: initialize a newly created Atom instead of revising an existing one.
    --apply: persist the change; omission is dry-run mode.

The tool reads the current project's timestamp timezone from
`.caprmedio_caprmedio/caprmedio_project_settings.toml`, fails closed on malformed or duplicate
metadata, preserves YAML or TOML frontmatter syntax, and writes atomically.
"""

from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import tomllib
from pathlib import Path
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

from project_runtime import atomic_tempfile


SETTINGS_PATH = Path(".caprmedio_caprmedio/caprmedio_project_settings.toml")
TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"
YAML_DELIMITER = "---"
TOML_DELIMITER = "+++"


def project_identity(root: Path) -> dict[str, dict[str, object]]:
    """Read Project identity only from the selected Project Settings Carrier."""
    path = root / SETTINGS_PATH
    if not path.is_file() or path.is_symlink():
        raise ValueError(f"Project Settings Carrier is missing or invalid: {SETTINGS_PATH}")
    try:
        settings = tomllib.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise ValueError(f"invalid Project Settings: {SETTINGS_PATH}") from error
    project = settings.get("project")
    artifacts = settings.get("artifacts")
    identity = artifacts.get("identity") if isinstance(artifacts, dict) else None
    if not isinstance(project, dict) or not isinstance(identity, dict):
        raise ValueError("Project Settings lacks project or artifacts.identity")
    for key in ("key", "name", "repository_slug"):
        value = project.get(key)
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"Project Settings lacks project.{key}")
    if project["name"] != project["name"].strip().lower():
        raise ValueError("Project Settings project.name must be lowercase without surrounding whitespace")
    prefix = identity.get("project_prefix")
    if not isinstance(prefix, str) or not prefix.strip():
        raise ValueError("Project Settings lacks artifacts.identity.project_prefix")
    obsolete = project.get("obsolete_names", [])
    if not isinstance(obsolete, list) or any(not isinstance(name, str) or not name for name in obsolete):
        raise ValueError("Project Settings project.obsolete_names must be a list of names")
    return {"project": dict(project, obsolete_names=obsolete), "identity": identity}


def atom_identifier(filename: str, explicit: str | None = None) -> str:
    """Resolve stable identity without absorbing mutable scope, tier, type, or sequence."""
    if explicit:
        return explicit.strip().strip('\"\'')
    name = Path(filename).name
    canonical = re.match(r"(?:[0-9]+-)?(CA-[CAPRMEDIO]-[0-9]+)(?:-|\.|@|$)", name)
    if canonical:
        return canonical.group(1)
    # Unmigrated legacy identities remain opaque; never allocate or renumber here.
    return name.removesuffix(".md").split("--", 1)[0]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="Markdown carrier")
    parser.add_argument("--kind", choices=("atom", "projection"), required=True)
    parser.add_argument("--new", action="store_true", help="initialize a new Atom")
    parser.add_argument("--apply", action="store_true", help="persist the update")
    return parser.parse_args()


def repository_root(path: Path) -> Path:
    for candidate in (path.resolve(), *path.resolve().parents):
        if (candidate / SETTINGS_PATH).is_file():
            return candidate
    raise RuntimeError(f"cannot locate {SETTINGS_PATH} from {path}")


def configured_timezone(root: Path) -> dt.tzinfo | None:
    settings = tomllib.loads((root / SETTINGS_PATH).read_text(encoding="utf-8"))
    value = settings.get("artifact_timestamps", {}).get("timezone", "local")
    if value == "local":
        return None
    if value == "UTC":
        return dt.UTC
    try:
        return ZoneInfo(value)
    except ZoneInfoNotFoundError as error:
        raise RuntimeError(f"unknown artifact timestamp timezone: {value}") from error


def current_timestamp(root: Path) -> str:
    timezone = configured_timezone(root)
    moment = dt.datetime.now().astimezone() if timezone is None else dt.datetime.now(timezone)
    return moment.strftime(TIMESTAMP_FORMAT)


def split_frontmatter(text: str, path: Path) -> tuple[str, str, str]:
    first_line, separator, remainder = text.partition("\n")
    if not separator or first_line not in {YAML_DELIMITER, TOML_DELIMITER}:
        raise RuntimeError(f"{path}: missing supported frontmatter")
    marker = f"\n{first_line}\n"
    boundary = remainder.find(marker)
    if boundary < 0:
        raise RuntimeError(f"{path}: unterminated frontmatter")
    return first_line, remainder[:boundary], remainder[boundary + len(marker) :]


def property_pattern(delimiter: str, name: str) -> re.Pattern[str]:
    separator = r"\s*:\s*" if delimiter == YAML_DELIMITER else r"\s*=\s*"
    return re.compile(rf"(?m)^{re.escape(name)}{separator}(.+)$")


def property_line(delimiter: str, name: str, value: str | int) -> str:
    if delimiter == YAML_DELIMITER:
        return f"{name}: {value}"
    rendered = str(value) if isinstance(value, int) else f'"{value}"'
    return f"{name} = {rendered}"


def one_value(frontmatter: str, delimiter: str, name: str) -> str | None:
    matches = property_pattern(delimiter, name).findall(frontmatter)
    if len(matches) > 1:
        raise RuntimeError(f"duplicate {name} property")
    return matches[0].strip().strip('"') if matches else None


def insert_properties(frontmatter: str, lines: list[str]) -> str:
    anchor = re.search(r"(?m)^llm_session_ids(?:\s*:|\s*=)", frontmatter)
    if anchor is None:
        return frontmatter.rstrip() + "\n" + "\n".join(lines)
    return frontmatter[: anchor.start()] + "\n".join(lines) + "\n" + frontmatter[anchor.start() :]


def replace_property(frontmatter: str, delimiter: str, name: str, value: str | int) -> str:
    pattern = property_pattern(delimiter, name)
    if len(pattern.findall(frontmatter)) != 1:
        raise RuntimeError(f"expected exactly one {name} property")
    return pattern.sub(property_line(delimiter, name, value), frontmatter, count=1)


def update_atom(frontmatter: str, delimiter: str, timestamp: str, new: bool) -> str:
    version = one_value(frontmatter, delimiter, "version")
    updated_at = one_value(frontmatter, delimiter, "updated_at")
    if new:
        if version is not None or updated_at is not None:
            raise RuntimeError("new Atom already has revision metadata")
        lines = [property_line(delimiter, "version", 1), property_line(delimiter, "updated_at", timestamp)]
        return insert_properties(frontmatter, lines)
    if version is None or updated_at is None:
        raise RuntimeError("existing Atom requires version and updated_at")
    if not version.isdigit() or int(version) < 1:
        raise RuntimeError(f"invalid Atom version: {version}")
    revised = replace_property(frontmatter, delimiter, "version", int(version) + 1)
    return replace_property(revised, delimiter, "updated_at", timestamp)


def update_projection(frontmatter: str, delimiter: str, timestamp: str) -> str:
    if one_value(frontmatter, delimiter, "version") is not None:
        raise RuntimeError("Projection frontmatter must not carry version")
    if one_value(frontmatter, delimiter, "updated_at") is None:
        return insert_properties(frontmatter, [property_line(delimiter, "updated_at", timestamp)])
    return replace_property(frontmatter, delimiter, "updated_at", timestamp)


def atomic_write(path: Path, text: str) -> None:
    descriptor, temporary_name = atomic_tempfile(path, "artifact_metadata")
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary_name, path)
    except BaseException:
        try:
            os.unlink(temporary_name)
        except FileNotFoundError:
            pass
        raise


def main() -> int:
    args = parse_args()
    path = args.path.resolve()
    root = repository_root(path)
    delimiter, frontmatter, body = split_frontmatter(path.read_text(encoding="utf-8"), path)
    timestamp = current_timestamp(root)
    if args.kind == "atom":
        revised_frontmatter = update_atom(frontmatter, delimiter, timestamp, args.new)
    else:
        if args.new:
            raise RuntimeError("--new applies only to Atoms")
        revised_frontmatter = update_projection(frontmatter, delimiter, timestamp)
    revised = f"{delimiter}\n{revised_frontmatter}\n{delimiter}\n{body}"
    print(f"path={path.relative_to(root)} kind={args.kind} updated_at={timestamp} apply={args.apply}")
    if args.apply:
        atomic_write(path, revised)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
