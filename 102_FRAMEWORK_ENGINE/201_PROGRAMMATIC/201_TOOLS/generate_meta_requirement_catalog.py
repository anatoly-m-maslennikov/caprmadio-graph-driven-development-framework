#!/usr/bin/env python3
"""Generate the active META Atom Catalog grouped by Subject scope.

Parameters:
    --session-id: session provenance recorded in Work Journal events.
    --apply: publish the Projection and append started/completed Journal events;
        omission is dry-run mode.

The generator reads active META role folders only, excludes lifecycle
subfolders and Projections, derives identities from filename stems, and fails
closed when an Atom lacks a Subject scope or H1 title.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
import uuid
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve()
REPOSITORY_ROOT = next(parent for parent in SCRIPT_PATH.parents if (parent / ".git").exists())
sys.pycache_prefix = str(REPOSITORY_ROOT / ".caprmedio_tmp/cache/python")
TOOLS_ROOT = SCRIPT_PATH.parent
if str(TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(TOOLS_ROOT))

from artifact_metadata import atomic_write, current_timestamp, repository_root, split_frontmatter  # noqa: E402
from work_journal import append_record, event_record  # noqa: E402


META_ROOT = Path(".caprmedio/100_LAYER_1_META")
TARGET = META_ROOT / "04_requirement/CAPRMEDIO-META-CATL-002--active-atoms-by-subject-scope.md"
ROLE_DIRECTORIES = {
    "01_concern",
    "02_analysis",
    "03_plan",
    "04_requirement",
    "05_method",
    "06_evaluation",
    "07_delivery",
    "09_operations",
}
LIFECYCLE_DIRECTORIES = {"archive", "drafts", "done", "solved", "handled"}
PROJECTION_TYPES = {"catalog", "development_backlog", "hub", "implementation_record", "map", "specification"}
GENERATOR_NAME = "generate_meta_requirement_catalog"
GENERATOR_VERSION = 1


@dataclass(frozen=True)
class Atom:
    identity: str
    title: str
    subject_scopes: tuple[str, ...]
    path: Path
    content: bytes


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--session-id", required=True)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("root", nargs="?", default=".")
    return parser.parse_args()


def yaml_scalar(frontmatter: str, name: str) -> str | None:
    match = re.search(rf"(?m)^{re.escape(name)}:\s*([^\n]+)$", frontmatter)
    return match.group(1).strip().strip('"') if match else None


def yaml_list(frontmatter: str, name: str) -> list[str]:
    match = re.search(rf"(?m)^{re.escape(name)}:\s*\n((?:  - [^\n]+\n?)+)", frontmatter)
    if not match:
        return []
    return [line.removeprefix("  - ").strip().strip('"') for line in match.group(1).splitlines()]


def subject_scopes(frontmatter: str) -> tuple[str, ...]:
    plural = yaml_list(frontmatter, "subject_scopes")
    singular = yaml_scalar(frontmatter, "subject_scope")
    values = plural or ([singular] if singular else [])
    return tuple(values)


def h1_title(body: str, path: Path) -> str:
    match = re.search(r"(?m)^#\s+(.+)$", body)
    if match is None:
        raise RuntimeError(f"{path}: missing H1 title")
    return match.group(1).strip()


def is_active_atom(path: Path, frontmatter: str) -> bool:
    if not any(part in ROLE_DIRECTORIES for part in path.parts):
        return False
    if any(part in LIFECYCLE_DIRECTORIES for part in path.parts):
        return False
    artifact_type = yaml_scalar(frontmatter, "artifact_type")
    return artifact_type not in PROJECTION_TYPES


def load_atoms(root: Path) -> list[Atom]:
    atoms: list[Atom] = []
    meta_root = root / META_ROOT
    for path in sorted(meta_root.rglob("CAPRMEDIO-*.md")):
        if path == root / TARGET:
            continue
        text = path.read_text(encoding="utf-8")
        delimiter, frontmatter, body = split_frontmatter(text, path)
        if delimiter != "---" or not is_active_atom(path, frontmatter):
            continue
        scopes = subject_scopes(frontmatter)
        if not scopes:
            raise RuntimeError(f"{path}: active META Atom lacks Subject scope")
        atoms.append(Atom(path.stem, h1_title(body, path), scopes, path, text.encode("utf-8")))
    return atoms


def source_frontier(root: Path, atoms: list[Atom]) -> str:
    digest = hashlib.sha256()
    for atom in atoms:
        digest.update(atom.path.relative_to(root).as_posix().encode("utf-8"))
        digest.update(b"\0")
        digest.update(atom.content)
        digest.update(b"\0")
    return digest.hexdigest()


def render(atoms: list[Atom], frontier: str, updated_at: str) -> str:
    grouped: dict[str, list[Atom]] = defaultdict(list)
    for atom in atoms:
        for scope in atom.subject_scopes:
            grouped[scope].append(atom)
    lines = [
        "---",
        "subject_scopes:",
        "  - artifact-model",
        f"updated_at: {updated_at}",
        f"generator: {GENERATOR_NAME}",
        f"generator_version: {GENERATOR_VERSION}",
        f"source_count: {len(atoms)}",
        f"source_frontier_sha256: {frontier}",
        "relations:",
        "  child_of:",
        "    - CAPRMEDIO-META-REQU-109--provide-the-active-meta-atom-scope-catalog",
        "---",
        "# META active Atom Catalog by Subject scope",
        "",
    ]
    for scope in sorted(grouped):
        members = sorted(grouped[scope], key=lambda atom: atom.identity)
        lines.extend([f"## `{scope}` ({len(members)})", ""])
        lines.extend(f"- `{atom.identity}` — {atom.title}" for atom in members)
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def journal_record(root: Path, **values: object) -> dict[str, object]:
    return event_record(root=root, **values)  # type: ignore[arg-type]


def publish(root: Path, rendered: str, frontier: str, session_id: str, updated_at: str) -> None:
    action_id = str(uuid.uuid4())
    common = {
        "action_id": action_id,
        "kind": "projection_rebuild",
        "scope": "layer:meta",
        "operation": "projection_rebuild",
        "session_id": session_id,
        "subjects": ["CAPRMEDIO-META-CATL-002--active-atoms-by-subject-scope", frontier],
    }
    started = journal_record(root, event="started", outputs=[], preceding_event=None, details={"generator": GENERATOR_NAME}, **common)
    append_record(root, started)
    try:
        atomic_write(root / TARGET, rendered)
    except BaseException:
        failed = journal_record(root, event="failed", outputs=[], preceding_event=str(started["event_id"]), details={}, **common)
        append_record(root, failed)
        raise
    output_digest = hashlib.sha256(rendered.encode("utf-8")).hexdigest()
    completed = journal_record(
        root,
        event="completed",
        outputs=[TARGET.as_posix()],
        preceding_event=str(started["event_id"]),
        details={"updated_at": updated_at, "content_sha256": output_digest},
        **common,
    )
    append_record(root, completed)


def main() -> int:
    args = parse_args()
    root = repository_root(Path(args.root))
    atoms = load_atoms(root)
    frontier = source_frontier(root, atoms)
    current = (root / TARGET).read_text(encoding="utf-8") if (root / TARGET).is_file() else ""
    current_frontier = yaml_scalar(current.partition("\n---\n")[0], "source_frontier_sha256")
    changed = current_frontier != frontier
    print(f"atoms={len(atoms)} frontier={frontier} changed={changed} apply={args.apply}")
    if args.apply and changed:
        updated_at = current_timestamp(root)
        rendered = render(atoms, frontier, updated_at)
        publish(root, rendered, frontier, args.session_id, updated_at)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
