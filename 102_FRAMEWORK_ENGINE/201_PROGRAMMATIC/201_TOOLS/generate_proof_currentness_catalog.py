#!/usr/bin/env python3
"""Generate the governed proof-currentness Catalog.

Parameters:
    --session-id: session provenance recorded in Work Journal events.
    --apply: publish the Projection and append started/completed Journal events;
        omission is dry-run mode.

Proof carriers without a machine-readable dependency frontier are retained as
`unknown`. Checkable mismatches are `stale`; only fully reproduced frontiers
without unresolved invalidation conditions are `current`.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
import tomllib
import uuid
from dataclasses import dataclass
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve()
REPOSITORY_ROOT = next(parent for parent in SCRIPT_PATH.parents if (parent / ".git").exists())
sys.pycache_prefix = str(REPOSITORY_ROOT / ".caprmedio_tmp/cache/python")
TOOLS_ROOT = SCRIPT_PATH.parent
if str(TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(TOOLS_ROOT))

from artifact_metadata import (  # noqa: E402
    atomic_write,
    current_timestamp,
    one_value,
    repository_root,
    split_frontmatter,
)
from work_journal import append_record, event_record  # noqa: E402


CONTROL_ROOT = Path(".caprmedio")
TARGET = CONTROL_ROOT / "600_LAYER_6_OPS/09_ops/CAPRMEDIO-OPS-CATL-001-ops--proof-currentness.md"
GENERATOR_NAME = "generate_proof_currentness_catalog"
GENERATOR_VERSION = 1
PROOF_TYPES = {"evidence_record", "verification", "verification_record"}
PROJECTION_TYPES = {"catalog", "development_backlog", "hub", "implementation_record", "map", "specification"}
FILE_KINDS = {"file", "configuration", "evaluator", "input"}
ATOM_REF = re.compile(r"^atom:(.+)@(\d+),(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})$")
FILE_REF = re.compile(r"^(file|configuration|evaluator|input):(.+)@sha256:([0-9a-f]{64})$")
ENVIRONMENT_REF = re.compile(r"^environment:(.+)@sha256:([0-9a-f]{64})$")


@dataclass(frozen=True)
class Proof:
    identity: str
    path: Path
    content: bytes
    references: tuple[str, ...]
    invalidation_conditions: tuple[str, ...]


@dataclass(frozen=True)
class Result:
    proof: Proof
    state: str
    reason: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--session-id", required=True)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("root", nargs="?", default=".")
    return parser.parse_args()


def yaml_scalar(frontmatter: str, name: str) -> str | None:
    match = re.search(rf"(?m)^{re.escape(name)}:\s*([^\n]+)$", frontmatter)
    return match.group(1).strip().strip('"') if match else None


def yaml_list(frontmatter: str, name: str) -> tuple[str, ...]:
    match = re.search(rf"(?m)^{re.escape(name)}:\s*\n((?:  - [^\n]+\n?)+)", frontmatter)
    if not match:
        return ()
    return tuple(line.removeprefix("  - ").strip().strip('"') for line in match.group(1).splitlines())


def frontmatter_values(delimiter: str, frontmatter: str) -> tuple[str | None, tuple[str, ...], tuple[str, ...]]:
    if delimiter == "---":
        return (
            yaml_scalar(frontmatter, "artifact_type"),
            yaml_list(frontmatter, "proof_frontier_refs"),
            yaml_list(frontmatter, "invalidation_conditions"),
        )
    data = tomllib.loads(frontmatter)
    references = tuple(str(value) for value in data.get("proof_frontier_refs", []))
    conditions = tuple(str(value) for value in data.get("invalidation_conditions", []))
    return str(data.get("artifact_type")) if data.get("artifact_type") else None, references, conditions


def is_proof(path: Path, artifact_type: str | None) -> bool:
    if artifact_type in PROJECTION_TYPES:
        return False
    return artifact_type in PROOF_TYPES or "EVIDENCE" in path.name or "VERIFICATION" in path.name


def load_proofs(root: Path) -> list[Proof]:
    proofs: list[Proof] = []
    for path in sorted((root / CONTROL_ROOT).rglob("CAPRMEDIO-*.md")):
        if path == root / TARGET or "000_caprmedio_framework" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        if not text.startswith(("---\n", "+++\n")):
            continue
        delimiter, frontmatter, _ = split_frontmatter(text, path)
        artifact_type, references, conditions = frontmatter_values(delimiter, frontmatter)
        if is_proof(path, artifact_type):
            proofs.append(Proof(path.stem, path, text.encode("utf-8"), references, conditions))
    return proofs


def artifact_lookup(root: Path) -> dict[str, list[Path]]:
    lookup: dict[str, list[Path]] = {}
    for path in sorted((root / CONTROL_ROOT).rglob("CAPRMEDIO-*.md")):
        if "000_caprmedio_framework" in path.parts:
            continue
        lookup.setdefault(path.stem, []).append(path)
        short = re.match(r"^(.+?-\d{3})(?:--|-)", path.stem)
        if short:
            lookup.setdefault(short.group(1), []).append(path)
    return lookup


def check_atom(reference: re.Match[str], lookup: dict[str, list[Path]]) -> tuple[str, str]:
    name, expected_version, expected_time = reference.groups()
    paths = list(dict.fromkeys(lookup.get(name, [])))
    if len(paths) != 1:
        return "unknown", f"Atom reference resolves to {len(paths)} carriers"
    text = paths[0].read_text(encoding="utf-8")
    delimiter, frontmatter, _ = split_frontmatter(text, paths[0])
    version = one_value(frontmatter, delimiter, "version")
    updated_at = one_value(frontmatter, delimiter, "updated_at")
    if version == expected_version and updated_at == expected_time:
        return "current", "exact Atom revision matches"
    return "stale", "Atom revision changed"


def check_file(root: Path, reference: re.Match[str]) -> tuple[str, str]:
    kind, locator, expected_digest = reference.groups()
    path = root / locator.split("#", 1)[0]
    if not path.is_file():
        return "stale", f"{kind} dependency is missing"
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    return ("current", f"{kind} digest matches") if digest == expected_digest else ("stale", f"{kind} digest changed")


def evaluate(proof: Proof, root: Path, lookup: dict[str, list[Path]]) -> Result:
    if not proof.references:
        return Result(proof, "unknown", "missing proof_frontier_refs")
    states: list[tuple[str, str]] = []
    for item in proof.references:
        if atom := ATOM_REF.fullmatch(item):
            states.append(check_atom(atom, lookup))
        elif file_reference := FILE_REF.fullmatch(item):
            states.append(check_file(root, file_reference))
        elif ENVIRONMENT_REF.fullmatch(item):
            states.append(("unknown", "environment fingerprint needs a governed checker"))
        else:
            states.append(("unknown", "unrecognized proof frontier reference"))
    if any(state == "stale" for state, _ in states):
        reason = next(reason for state, reason in states if state == "stale")
        return Result(proof, "stale", reason)
    if proof.invalidation_conditions or any(state == "unknown" for state, _ in states):
        reason = "unresolved invalidation condition" if proof.invalidation_conditions else next(
            reason for state, reason in states if state == "unknown"
        )
        return Result(proof, "unknown", reason)
    return Result(proof, "current", "all declared dependencies match")


def source_frontier(root: Path, proofs: list[Proof]) -> str:
    digest = hashlib.sha256()
    for proof in proofs:
        digest.update(proof.path.relative_to(root).as_posix().encode("utf-8"))
        digest.update(b"\0")
        digest.update(proof.content)
        digest.update(b"\0")
    return digest.hexdigest()


def render(results: list[Result], frontier: str, updated_at: str) -> str:
    counts = {state: sum(result.state == state for result in results) for state in ("current", "stale", "unknown")}
    lines = [
        "---",
        "subject_scopes:",
        "  - evaluation",
        f"updated_at: {updated_at}",
        f"generator: {GENERATOR_NAME}",
        f"generator_version: {GENERATOR_VERSION}",
        f"source_count: {len(results)}",
        f"source_frontier_sha256: {frontier}",
        "relations:",
        "  child_of:",
        "    - CA-R-1647--generate-proof-currentness-catalog",
        "---",
        "# Proof currentness Catalog",
        "",
        f"Current: {counts['current']}; stale: {counts['stale']}; unknown: {counts['unknown']}.",
        "",
        "| Proof | State | Reason |",
        "| --- | --- | --- |",
    ]
    for result in sorted(results, key=lambda item: item.proof.identity):
        reason = result.reason.replace("|", "\\|")
        lines.append(f"| `{result.proof.identity}` | `{result.state}` | {reason} |")
    return "\n".join(lines).rstrip() + "\n"


def publish(root: Path, rendered: str, frontier: str, session_id: str, updated_at: str) -> None:
    action_id = str(uuid.uuid4())
    common = {
        "action_id": action_id,
        "kind": "projection_rebuild",
        "scope": "layer:ops",
        "operation": "projection_rebuild",
        "session_id": session_id,
        "subjects": ["CAPRMEDIO-OPS-CATL-001", frontier],
    }
    started = event_record(root=root, event="started", outputs=[], preceding_event=None, details={"generator": GENERATOR_NAME}, **common)
    append_record(root, started)
    try:
        (root / TARGET).parent.mkdir(parents=True, exist_ok=True)
        atomic_write(root / TARGET, rendered)
    except BaseException:
        failed = event_record(root=root, event="failed", outputs=[], preceding_event=str(started["event_id"]), details={}, **common)
        append_record(root, failed)
        raise
    digest = hashlib.sha256(rendered.encode("utf-8")).hexdigest()
    completed = event_record(
        root=root,
        event="completed",
        outputs=[TARGET.as_posix()],
        preceding_event=str(started["event_id"]),
        details={"updated_at": updated_at, "content_sha256": digest},
        **common,
    )
    append_record(root, completed)


def main() -> int:
    args = parse_args()
    root = repository_root(Path(args.root))
    proofs = load_proofs(root)
    frontier = source_frontier(root, proofs)
    target = root / TARGET
    current = target.read_text(encoding="utf-8") if target.is_file() else ""
    current_frontier = yaml_scalar(current.partition("\n---\n")[0], "source_frontier_sha256")
    changed = current_frontier != frontier
    print(f"proofs={len(proofs)} frontier={frontier} changed={changed} apply={args.apply}")
    if args.apply and changed:
        results = [evaluate(proof, root, artifact_lookup(root)) for proof in proofs]
        updated_at = current_timestamp(root)
        publish(root, render(results, frontier, updated_at), frontier, args.session_id, updated_at)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
