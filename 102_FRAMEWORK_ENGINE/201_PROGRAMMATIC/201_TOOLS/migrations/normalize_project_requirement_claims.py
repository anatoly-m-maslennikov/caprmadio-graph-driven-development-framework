#!/usr/bin/env python3
"""Normalize active Project Requirement claims and revision metadata.

Usage:
    python3 002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/migrations/normalize_project_requirement_claims.py
    python3 002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/migrations/normalize_project_requirement_claims.py --apply

The default mode is read-only. The migration fails closed on unexpected input,
writes atomically, and is idempotent.
"""

from __future__ import annotations

import argparse
import os
import sys
from dataclasses import dataclass
from pathlib import Path

_PROJECT_TOOLS_ROOT = Path(__file__).resolve().parents[1]
if str(_PROJECT_TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_TOOLS_ROOT))
from project_runtime import atomic_tempfile  # noqa: E402


REQUIREMENTS = Path(".caprmedio/04_requirement")
UPDATED_AT = "2026-08-17 19:22:33"


@dataclass(frozen=True)
class Change:
    pattern: str
    old_version: int | None
    old_updated_at: str | None
    old_claim: str
    new_claim: str


CHANGES = (
    Change(
        "CAPRMEDIO-REQUIREMENT-140-*",
        2,
        "2026-08-17 15:56:56",
        "Whenever it is possible to resolve a governed meaning completely and unambiguously from one canonical owner, CAPRMEDIO stores and maintains that meaning only once. Every other use references, derives, generates, or adapts the canonical owner instead of restating the same governed knowledge.",
        "CAPRMEDIO must store and maintain a governed meaning under one canonical owner whenever that owner can resolve the meaning completely and unambiguously; every other use must reference, derive, generate, or adapt that owner.",
    ),
    Change(
        "CAPRMEDIO-REQUIREMENT-182-*",
        1,
        "2026-08-17 17:24:09",
        "Every CAPRMEDIO governance operation reads or changes the typed graph of governed authority, realization bindings, and their direct relations.",
        "Every CAPRMEDIO governance operation must read or change the typed graph of governed authority, realization bindings, and their direct relations.",
    ),
    Change(
        "CAPRMEDIO-REQUIREMENT-183-*",
        2,
        "2026-08-17 16:39:43",
        "CAPRMEDIO adds or enables a Content role, applicability tier, structural level, scope, automation, or other mechanism only when it is necessary to preserve a material governed distinction or required outcome; otherwise the simpler model remains active.",
        "CAPRMEDIO may add or enable a Content role, applicability tier, structural level, scope, automation, or other mechanism only when it is necessary to preserve a material governed distinction or required outcome.",
    ),
    Change(
        "CAPRMEDIO-REQUIREMENT-185-*",
        2,
        "2026-08-17 16:41:30",
        "The minimum CAPRMEDIO project model is project-scope Requirement authority plus its real Implementation; it requires no Implementation Atom and enables other Atom roles, applicability tiers, structural levels, descendant scopes, or automation only when necessary, including in the framework's self-hosting repository.",
        "CAPRMEDIO must use project-scope Requirement authority plus its real Implementation as the minimum project model, must not require an Implementation Atom, and may enable other Atom roles, applicability tiers, structural levels, descendant scopes, or automation only when necessary.",
    ),
    Change(
        "CAPRMEDIO-REQUIREMENT-186-*",
        None,
        None,
        "CAPRMEDIO records all and only the direct typed relations necessary to trace each governed authority to its real Implementation and material dependents; inverse, transitive, and aggregate relations are derived.",
        "CAPRMEDIO must record all and only the direct typed relations necessary to trace each governed authority to its real Implementation and material dependents; inverse, transitive, and aggregate relations must be derived.",
    ),
    Change(
        "CAPRMEDIO-REQUIREMENT-187-*",
        2,
        "2026-08-17 16:30:52",
        "PROJECT is the structural root of the current project, not a Layer. It owns project Principles, constitutional Cores governing the complete Layer system, concrete Layer scopes, and Contracts between Layers; it does not own META meanings, GOV carrier mechanics, or project behavior assigned to SPEC.",
        "PROJECT must be the structural root of the current project, must own project Principles, constitutional Cores governing the complete Layer system, concrete Layer scopes, and Contracts between Layers, and must exclude META meanings, GOV carrier mechanics, and project behavior assigned to SPEC.",
    ),
    Change(
        "CAPRMEDIO-REQUIREMENT-188-*",
        2,
        "2026-08-17 15:56:56",
        "CAPRMEDIO admits independently evolvable Extensions that add or specialize governed capabilities through explicit extension points without copying or silently redefining canonical authority.",
        "CAPRMEDIO must admit independently evolvable Extensions only through explicit extension points that add or specialize governed capabilities without copying or silently redefining canonical authority.",
    ),
    Change(
        "CAPRMEDIO-REQUIREMENT-189-*",
        2,
        "2026-08-17 15:56:56",
        "CAPRMEDIO lets project-owned configuration select, combine, parameterize, or disable available optional canonical and Extension capabilities without changing their governed meanings.",
        "CAPRMEDIO must permit project-owned configuration to select, combine, parameterize, or disable available optional canonical and Extension capabilities without changing their governed meanings.",
    ),
    Change(
        "CAPRMEDIO-REQUIREMENT-190-*",
        2,
        "2026-08-17 15:54:46",
        "CAPRMEDIO supplies an LLM only the guidance necessary to meet the operator-defined adequacy threshold under the currently observed model, host, task, and risk conditions.",
        "CAPRMEDIO must supply an LLM only the guidance necessary to meet the operator-defined adequacy threshold under the currently observed model, host, task, and risk conditions.",
    ),
    Change(
        "CAPRMEDIO-REQUIREMENT-198-*",
        None,
        None,
        "CAPRMEDIO authority and semantics do not depend on a particular operating system, operator language, programming language, LLM provider or model, or agent host.",
        "CAPRMEDIO must keep its authority and semantics independent of any particular operating system, operator language, programming language, LLM provider or model, or agent host.",
    ),
    Change(
        "CAPRMEDIO-REQUIREMENT-204-*",
        None,
        None,
        "CAPRMEDIO preserves its canonical semantic model across disciplines while Profiles and Extensions adapt terminology, artifact subtypes, Methods, Evaluation, and Implementation to a particular discipline.",
        "CAPRMEDIO must preserve its canonical semantic model across disciplines while Profiles and Extensions adapt terminology, artifact subtypes, Methods, Evaluation, and Implementation to a particular discipline.",
    ),
    Change(
        "CAPRMEDIO-REQUIREMENT-206-*",
        2,
        "2026-08-17 16:30:52",
        "CAPRMEDIO supports either repository-level scope or declared repository-relative Work Areas containing code, services, libraries, documentation, methodology, data, or mixed content without requiring a particular architecture or deployability model.",
        "CAPRMEDIO must support repository-level scope and declared repository-relative Work Areas containing code, services, libraries, documentation, methodology, data, or mixed content without requiring a particular architecture or deployability model.",
    ),
    Change(
        "CAPRMEDIO-REQUIREMENT-208-*",
        2,
        "2026-08-17 16:30:52",
        "META owns the project ontology: canonical vocabulary, semantic axes and distinctions, Content-role and Artifact-form meanings, applicability tiers, relation meanings, structural interpretation, and construct-admission rules; concrete Layer topology, carrier mechanics, project behavior, and realization remain outside its scope.",
        "META must own the project ontology: canonical vocabulary, semantic axes and distinctions, Content-role and Artifact-form meanings, applicability tiers, relation meanings, structural interpretation, and construct-admission rules; it must exclude concrete Layer topology, carrier mechanics, project behavior, and realization.",
    ),
    Change(
        "CAPRMEDIO-REQUIREMENT-209-*",
        2,
        "2026-08-17 16:30:52",
        "GOV owns governed-carrier mechanics: identity, naming, placement, frontmatter, provenance, relation encoding, lifecycle, catalogs, and structural validation; META meanings, project behavior, and realization remain outside its scope.",
        "GOV must own governed-carrier mechanics: identity, naming, placement, frontmatter, provenance, relation encoding, lifecycle, catalogs, and structural validation; it must exclude META meanings, project behavior, and realization.",
    ),
    Change(
        "CAPRMEDIO-REQUIREMENT-211-*",
        2,
        "2026-08-17 16:30:52",
        "IMPLEMENTATION owns the actual source, documentation, configuration, tests, evaluations, and other realized project artifacts together with their traceability to applicable SPEC authority.",
        "IMPLEMENTATION must own the actual source, documentation, configuration, tests, evaluations, and other realized project artifacts together with their traceability to applicable SPEC authority.",
    ),
    Change(
        "CAPRMEDIO-REQUIREMENT-212-*",
        2,
        "2026-08-17 16:30:52",
        "DELIVERY owns packaging, environment, deployment, release, and publication realization of the project.",
        "DELIVERY must own packaging, environment, deployment, release, and publication realization of the project.",
    ),
    Change(
        "CAPRMEDIO-REQUIREMENT-213-*",
        2,
        "2026-08-17 16:30:52",
        "OPS owns post-delivery operation, supportability, runtime investigation, containment, recovery, and factual observation.",
        "OPS must own post-delivery operation, supportability, runtime investigation, containment, recovery, and factual observation.",
    ),
    Change(
        "CAPRMEDIO-REQUIREMENT-238-*",
        1,
        "2026-08-17 19:11:46",
        "An imprecise fallback relation is permitted only within a scope whose effective `authority_mode` is `casual`.",
        "CAPRMEDIO may permit an imprecise fallback relation only within a scope whose effective `authority_mode` is `casual`.",
    ),
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="apply the migration")
    parser.add_argument("root", nargs="?", default=".", help="repository root")
    return parser.parse_args()


def resolve_path(root: Path, pattern: str) -> Path:
    matches = sorted((root / REQUIREMENTS).glob(pattern))
    if len(matches) != 1:
        raise RuntimeError(f"{pattern}: expected one active carrier, found {len(matches)}")
    return matches[0]


def desired_text(path: Path, change: Change) -> tuple[str, str]:
    old = path.read_text(encoding="utf-8")
    if old.count(change.old_claim) != 1:
        if old.count(change.new_claim) == 1:
            return old, old
        raise RuntimeError(f"{path}: expected claim not found exactly once")
    if not old.startswith("---\n") or "\n---\n" not in old[4:]:
        raise RuntimeError(f"{path}: malformed YAML frontmatter")
    expected_version = f"version: {change.old_version}\n" if change.old_version is not None else None
    expected_time = f"updated_at: {change.old_updated_at}\n" if change.old_updated_at is not None else None
    new_version = 1 if change.old_version is None else change.old_version + 1
    if expected_version is None:
        if "\nversion:" in old:
            raise RuntimeError(f"{path}: unexpected version property")
        anchor = "llm_session_ids:\n"
        if old.count(anchor) != 1:
            raise RuntimeError(f"{path}: expected one llm_session_ids property")
        revised = old.replace(anchor, f"version: {new_version}\nupdated_at: {UPDATED_AT}\n{anchor}", 1)
    else:
        if old.count(expected_version) != 1 or old.count(expected_time or "") != 1:
            raise RuntimeError(f"{path}: unexpected revision metadata")
        revised = old.replace(expected_version, f"version: {new_version}\n", 1)
        revised = revised.replace(expected_time or "", f"updated_at: {UPDATED_AT}\n", 1)
    revised = revised.replace(change.old_claim, change.new_claim, 1)
    return old, revised


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
    pending: list[tuple[Path, str]] = []
    for change in CHANGES:
        path = resolve_path(root, change.pattern)
        current, desired = desired_text(path, change)
        if current != desired:
            pending.append((path, desired))
    print(f"targets={len(CHANGES)} pending={len(pending)} state={'pending' if pending else 'applied'}")
    if args.apply:
        for path, desired in pending:
            atomic_write(path, desired)
        if any(desired_text(resolve_path(root, change.pattern), change)[0] != desired_text(resolve_path(root, change.pattern), change)[1] for change in CHANGES):
            raise RuntimeError("post-apply verification failed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
