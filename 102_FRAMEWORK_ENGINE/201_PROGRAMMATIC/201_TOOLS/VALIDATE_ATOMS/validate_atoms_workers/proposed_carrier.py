"""Finite, source-bound admission for a proposed complete Atom carrier."""

from __future__ import annotations

import hashlib
import json
import tomllib
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .authority import AuthorityContext, Obligation, Record, resolve_context
from .check_operators import load_operators_registry
from .checks import validate_carrier
from .context import load_source
from .read_io import ReadContext
from .settings import CEILINGS
from .support_authority import support_sources
from authoritative_status_models import StatusModelError, resolve_status_model


_REGISTRY_IDS = (
    "CA-D-276", "CA-D-269", "CA-D-268", "CA-D-270", "CA-D-274", "CA-D-446",
    "CA-D-479", "CA-D-482", "CA-D-483",
)
_SUPPORT_IDS = ("CA-D-494", "CA-D-440", "CA-D-441", "CA-D-442", "CA-R-1308", "CA-R-1313", "CA-D-324", "CA-D-466", "CA-D-461")
_CODES = frozenset(
    {
        "frontmatter.common_encoding", "frontmatter.version", "frontmatter.updated_at",
        "frontmatter.author", "author.resolution", "frontmatter.atom_id",
        "frontmatter.subjects", "frontmatter.relations", "frontmatter.claim_target_scope_unit",
        "target.resolution", "frontmatter.status",
        "body.sections",
    }
)


class ProposedCarrierError(ValueError):
    """The finite pre-write carrier boundary is unavailable or failed."""


@dataclass(frozen=True)
class VerifiedSourceContext:
    root: Path
    authority: AuthorityContext
    inputs: Record


def _entry(identifier: str) -> Record:
    registry = json.loads(Path(__file__).with_name("registry.json").read_text(encoding="utf-8"))["sources"]
    return registry.get(identifier) or support_sources().get(identifier) or {}


def _source(root: Path, identifier: str, reader: ReadContext, report: Record) -> Record:
    entry = _entry(identifier)
    path = entry.get("source_path") if isinstance(entry, dict) else None
    version = entry.get("version") if isinstance(entry, dict) else None
    digest = entry.get("sha256") if isinstance(entry, dict) else None
    if not isinstance(path, str) or type(version) is not int or not isinstance(digest, str):
        raise ProposedCarrierError("required source pin is unavailable")
    absolute = root / path
    item = load_source(
        absolute,
        {"atom_id": identifier, "version": version, "sha256": digest, "path": str(absolute)},
        reader,
        report,
    )
    if item is None:
        raise ProposedCarrierError("required source is unreadable, changed, or inactive")
    return item


def source_context_from_project(root: Path) -> VerifiedSourceContext:
    """Load just the finite checked authority closure and selected Project inputs."""

    root = root.resolve()
    reader = ReadContext(roots=[str(root)], limits=dict(CEILINGS))
    report: Record = {"bindings": {}, "coverage": {"gaps": []}}
    sources = [_source(root, identifier, reader, report) for identifier in (*_REGISTRY_IDS, *_SUPPORT_IDS)]
    project_structure = root / ".caprmedio_caprmedio/project_structure.toml"
    operators = root / ".caprmedio_caprmedio/operators_registry.toml"
    try:
        structure = tomllib.loads(reader.read(project_structure).decode("utf-8"))
        operator_raw = reader.read(operators)
    except (OSError, UnicodeError, tomllib.TOMLDecodeError) as error:
        raise ProposedCarrierError("required Project context is unreadable") from error
    inputs: Record = {
        "sources": sources,
        "structure": structure,
        "operators_registry": load_operators_registry(
            {"operators_registry": {"path": str(operators), "sha256": hashlib.sha256(operator_raw).hexdigest()}},
            reader,
        ),
    }
    return VerifiedSourceContext(root, resolve_context(sources), inputs)


def validate_proposed_carrier(
    metadata: Record, body: str, verified_source_context: VerifiedSourceContext, relative_path: Path,
    *, allow_existing_relations: bool = False,
) -> Record:
    """Reject every failed, unresolved, or unsupported finite carrier obligation."""

    selected = tuple(item for item in verified_source_context.authority.obligations if item.code in _CODES)
    if {item.code for item in selected} != _CODES or any(not item.supported for item in selected):
        raise ProposedCarrierError("complete-carrier authority is unsupported or incomplete")
    context = AuthorityContext(
        bindings=verified_source_context.authority.bindings,
        required=len(selected),
        supported=len(selected),
        unsupported=0,
        gaps=[],
        obligations=selected,
        domains=verified_source_context.authority.domains,
        unclassified_sources=False,
    )
    relations = metadata.get("relations", {})
    if not isinstance(relations, dict) or (relations and not allow_existing_relations):
        raise ProposedCarrierError("nonempty relations require bounded graph-target authority")
    result = validate_carrier(metadata, body, context, verified_source_context.inputs)
    if result["findings"] or result["gaps"] or any(item["outcome"] != "passed" for item in result["outcomes"]):
        raise ProposedCarrierError("complete-carrier validation failed or is unresolved")
    try:
        resolve_status_model(verified_source_context.root, metadata, metadata.get("status"))
    except StatusModelError as error:
        raise ProposedCarrierError("status model is missing, ambiguous, or unadmitted") from error
    role = metadata.get("content_role")
    status = metadata.get("status")
    names = {part.lower() for part in relative_path.parts[:-1]}
    source = next((row for row in verified_source_context.inputs["sources"] if row["binding"]["atom_id"] == "CA-D-324"), None)
    if source is None or not isinstance(role, str):
        raise ProposedCarrierError("role-directory authority is unavailable")
    import re
    mapping = dict(re.findall(r"- ([A-Za-z]+): `([0-9]{2}_[a-z_]+)/`;", source["text"]))
    expected_role_directory = mapping.get(role)
    if expected_role_directory is None or expected_role_directory not in names:
        raise ProposedCarrierError("carrier path disagrees with its carried content role")
    owner = metadata.get("current_scope_unit")
    rows = verified_source_context.inputs.get("structure", {}).get("scope_units", [])
    row = next((item for item in rows if item.get("scope_unit_name") == owner), None)
    if not isinstance(row, dict) or not isinstance(row.get("authority_path"), str):
        raise ProposedCarrierError("carrier owner authority is unresolved")
    authority_path = Path(row["authority_path"])
    project_relative_path = Path(".caprmedio_caprmedio") / relative_path
    if not project_relative_path.is_relative_to(authority_path):
        raise ProposedCarrierError("carrier path is outside its carried owner authority")
    expected_status_directory = "" if status == "Active" else status.lower() if isinstance(status, str) else None
    if role == "Plan":
        plan_source = next((item for item in verified_source_context.inputs["sources"] if item["binding"]["atom_id"] == "CA-D-461"), None)
        if plan_source is None:
            raise ProposedCarrierError("Plan placement authority is unavailable")
        plan_mapping = dict(re.findall(r"- ([A-Za-z]+): .*?`([^`]+)`", plan_source["text"]))
        expected_status_directory = "" if status == "Active" else plan_mapping.get(status)
    role_index = relative_path.parts.index(expected_role_directory)
    tail = relative_path.parts[role_index + 1 : -1]
    if len(tail) > 1:
        raise ProposedCarrierError("deeper carrier placement is unsupported")
    actual_status_directory = tail[0] if tail else ""
    if expected_status_directory is None or actual_status_directory != expected_status_directory:
        raise ProposedCarrierError("carrier path disagrees with its carried status")
    return result
