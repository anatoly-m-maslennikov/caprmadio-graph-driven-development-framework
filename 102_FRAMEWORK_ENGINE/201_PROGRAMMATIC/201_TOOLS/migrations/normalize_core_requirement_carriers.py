#!/usr/bin/env python3
"""Normalize active Project Requirements and META/GOV Core carriers.

Usage:
    python3 002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/migrations/normalize_core_requirement_carriers.py
    python3 002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/migrations/normalize_core_requirement_carriers.py --apply

The default mode is a read-only dry run. The --apply option writes changed
carriers atomically. Selection excludes drafts, archives, and Projections.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

_PROJECT_TOOLS_ROOT = Path(__file__).resolve().parents[1]
if str(_PROJECT_TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_TOOLS_ROOT))
from project_runtime import atomic_tempfile  # noqa: E402


PROJECT_REQUIREMENTS = Path(".caprmedio/04_requirement")
META_REQUIREMENTS = Path(".caprmedio/100_LAYER_1_META/04_requirement")
GOV_REQUIREMENTS = Path(".caprmedio/200_LAYER_2_GOV/04_requirement")
DERIVED_FRONTMATTER_KEYS = frozenset({"artifact_type", "artifact_id", "scope_path"})
TITLE_TERMS = {
    "caprmedio": "CAPRMEDIO",
    "gov": "GOV",
    "h1": "H1",
    "json": "JSON",
    "llm": "LLM",
    "mece": "MECE",
    "meta": "META",
    "ndjson": "NDJSON",
    "ops": "Ops",
    "rmed": "RMED",
    "spec": "SPEC",
    "toon": "TOON",
    "yaml": "YAML",
}
TOP_LEVEL_KEY = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*):(?:\s*(.*))?$")
NUMBERED_SUMMARY = re.compile(r"-(\d{3})-(.+)$")
LIST_ITEM = re.compile(r"^(?:[-+*]\s+|\d+[.)]\s+)")
CODE_FENCE = chr(96) * 3


class CarrierError(RuntimeError):
    """Reject a carrier whose structure cannot be transformed safely."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write normalized carriers")
    parser.add_argument("root", nargs="?", default=".", help="repository root")
    return parser.parse_args()


def split_frontmatter(text: str, path: Path) -> tuple[list[str], list[str]]:
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise CarrierError(f"{path}: expected leading YAML frontmatter")
    try:
        closing = lines.index("---", 1)
    except ValueError as error:
        raise CarrierError(f"{path}: unterminated YAML frontmatter") from error
    return lines[1:closing], lines[closing + 1 :]


def frontmatter_blocks(lines: list[str], path: Path) -> list[tuple[str, list[str]]]:
    blocks: list[tuple[str, list[str]]] = []
    current_key: str | None = None
    current_lines: list[str] = []
    for line in lines:
        match = TOP_LEVEL_KEY.match(line)
        if match:
            if current_key is not None:
                blocks.append((current_key, current_lines))
            current_key = match.group(1)
            current_lines = [line]
        elif current_key is None:
            raise CarrierError(f"{path}: content before first frontmatter key: {line!r}")
        else:
            current_lines.append(line)
    if current_key is not None:
        blocks.append((current_key, current_lines))
    keys = [key for key, _ in blocks]
    duplicates = sorted({key for key in keys if keys.count(key) > 1})
    if duplicates:
        raise CarrierError(f"{path}: duplicate frontmatter keys: {', '.join(duplicates)}")
    return blocks


def normalize_frontmatter(lines: list[str], path: Path) -> list[str]:
    blocks = frontmatter_blocks(lines, path)
    keys = {key for key, _ in blocks}
    if "subject_scope" in keys and "subject_scopes" in keys:
        raise CarrierError(f"{path}: both subject_scope and subject_scopes are present")
    normalized: list[str] = []
    for key, block in blocks:
        if key in DERIVED_FRONTMATTER_KEYS:
            continue
        if key != "subject_scope":
            normalized.extend(block)
            continue
        if len(block) != 1:
            raise CarrierError(f"{path}: singular subject_scope must be a scalar")
        value = block[0].partition(":")[2].strip()
        if not value:
            raise CarrierError(f"{path}: singular subject_scope is empty")
        normalized.extend(["subject_scopes:", f"  - {value}"])
    if not any(line == "subject_scopes:" for line in normalized):
        raise CarrierError(f"{path}: subject_scopes is required")
    return normalized


def filename_title(path: Path) -> str:
    match = NUMBERED_SUMMARY.search(path.stem)
    if not match:
        raise CarrierError(f"{path}: filename has no numbered summary")
    words = [TITLE_TERMS.get(word, word) for word in match.group(2).split("-")]
    title = " ".join(words)
    return title[:1].upper() + title[1:]


def remove_primary_claim(lines: list[str], path: Path) -> list[str]:
    indexes = [index for index, line in enumerate(lines) if line == "## Primary claim"]
    if not indexes:
        return lines
    if len(indexes) != 1:
        raise CarrierError(f"{path}: expected at most one Primary claim section")
    start = indexes[0]
    end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
    prior_body = [line for line in lines[:start] if line.strip() and not line.startswith("# ")]
    if prior_body:
        return lines[:start] + lines[end:]
    result = lines[:start] + lines[start + 1 :]
    if start > 0 and start < len(result) and result[start - 1] == result[start] == "":
        del result[start]
    return result


def is_prose_line(line: str) -> bool:
    stripped = line.lstrip()
    if not stripped or line != stripped:
        return False
    if stripped.startswith(("#", ">", "|", "<", CODE_FENCE, "~~~")):
        return False
    return LIST_ITEM.match(stripped) is None


def unwrap_prose(lines: list[str]) -> list[str]:
    result: list[str] = []
    paragraph: list[str] = []
    in_fence = False

    def flush() -> None:
        if paragraph:
            result.append(" ".join(part.strip() for part in paragraph))
            paragraph.clear()

    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith((CODE_FENCE, "~~~")):
            flush()
            in_fence = not in_fence
            result.append(line)
        elif in_fence or not is_prose_line(line):
            flush()
            result.append(line)
        else:
            paragraph.append(line)
    flush()
    return result


def normalize_body(lines: list[str], path: Path) -> list[str]:
    h1_indexes = [index for index, line in enumerate(lines) if line.startswith("# ")]
    if len(h1_indexes) != 1:
        raise CarrierError(f"{path}: expected exactly one H1, found {len(h1_indexes)}")
    body = list(lines)
    body[h1_indexes[0]] = f"# {filename_title(path)}"
    body = remove_primary_claim(body, path)
    return unwrap_prose(body)


def is_core(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return False
    frontmatter, _ = split_frontmatter(text, path)
    blocks = dict(frontmatter_blocks(frontmatter, path))
    return blocks.get("tier") == ["tier: core"]


def select_targets(root: Path) -> tuple[list[Path], tuple[int, int, int]]:
    project = sorted((root / PROJECT_REQUIREMENTS).glob("*.md"))
    meta = sorted(
        path
        for path in (root / META_REQUIREMENTS).glob("CAPRMEDIO-REQUIREMENT-*.md")
        if is_core(path)
    )
    gov = sorted(
        path
        for path in (root / GOV_REQUIREMENTS).glob("CAPRMEDIO-REQUIREMENT-*.md")
        if is_core(path)
    )
    targets = project + meta + gov
    if not project or not meta or not gov:
        raise CarrierError("expected non-empty Project, META Core, and GOV Core populations")
    return targets, (len(project), len(meta), len(gov))


def normalize_carrier(path: Path) -> str:
    original = path.read_text(encoding="utf-8")
    frontmatter, body = split_frontmatter(original, path)
    normalized = ["---", *normalize_frontmatter(frontmatter, path), "---"]
    normalized.extend(normalize_body(body, path))
    return "\n".join(normalized).rstrip() + "\n"


def atomic_write(path: Path, text: str) -> None:
    descriptor, temporary_name = atomic_tempfile(path, "migrations")
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
    root = Path(args.root).resolve()
    targets, counts = select_targets(root)
    changes: list[tuple[Path, str]] = []
    for path in targets:
        normalized = normalize_carrier(path)
        if normalized != path.read_text(encoding="utf-8"):
            changes.append((path, normalized))
    print(f"targets={len(targets)} project={counts[0]} meta_core={counts[1]} gov_core={counts[2]}")
    print(f"changes={len(changes)} mode={'apply' if args.apply else 'dry-run'}")
    for path, _ in changes:
        print(path.relative_to(root))
    if args.apply:
        for path, normalized in changes:
            atomic_write(path, normalized)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
