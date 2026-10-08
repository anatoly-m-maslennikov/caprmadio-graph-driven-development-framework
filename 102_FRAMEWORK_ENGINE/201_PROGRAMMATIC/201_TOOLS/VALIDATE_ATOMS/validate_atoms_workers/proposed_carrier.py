"""Finite, source-bound admission for a proposed complete Atom carrier."""

from __future__ import annotations

import hashlib
import json
import re
import tomllib
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .authority import AuthorityContext, Obligation, Record, _domain, resolve_context
from .check_operators import load_operators_registry
from .checks import validate_carrier
from .context import load_source
from .read_io import ReadContext
from .settings import CEILINGS
from .support_authority import support_sources
from .check_support import Check
from .check_graph_extended import relations_resolution, plan_resolution
from .proposed_references import ProposedReferenceError, inventory_proposed_references
from .graph_authority_refresh import APPROVED_GRAPH_AUTHORITY_IDS
from authoritative_status_models import StatusModelError, resolve_status_model


_REGISTRY_IDS = (
    "CA-D-276", "CA-D-269", "CA-D-268", "CA-D-270", "CA-D-274", "CA-D-446",
    "CA-D-479", "CA-D-482", "CA-D-483",
)
_SUPPORT_IDS = ("CA-D-494", "CA-D-440", "CA-D-441", "CA-D-442", "CA-R-1308", "CA-R-1313", "CA-D-324", "CA-D-466", "CA-D-461")
_GRAPH_IDS = tuple(sorted(APPROVED_GRAPH_AUTHORITY_IDS))
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


def _entry(identifier: str, *, graph: bool = False) -> Record:
    registry = json.loads(Path(__file__).with_name("registry.json").read_text(encoding="utf-8"))["sources"]
    graph_entries = json.loads(Path(__file__).with_name("graph_authority.json").read_text(encoding="utf-8"))["sources"]
    if graph and identifier in APPROVED_GRAPH_AUTHORITY_IDS:
        return graph_entries.get(identifier) or {}
    return registry.get(identifier) or support_sources().get(identifier) or graph_entries.get(identifier) or {}


def _source(root: Path, identifier: str, reader: ReadContext, report: Record, *, graph: bool = False) -> Record:
    entry = _entry(identifier, graph=graph)
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
    try:
        status_model = resolve_status_model(
            verified_source_context.root, metadata, metadata.get("status")
        )
    except StatusModelError as error:
        raise ProposedCarrierError("status model is missing, ambiguous, or unadmitted") from error
    domains = dict(verified_source_context.authority.domains)
    if metadata.get("content_role") == "Concern":
        domains["domain.status.concern"] = tuple(status_model["statuses"])
    context = AuthorityContext(
        bindings=verified_source_context.authority.bindings,
        required=len(selected),
        supported=len(selected),
        unsupported=0,
        gaps=[],
        obligations=selected,
        domains=domains,
        unclassified_sources=False,
    )
    relations = metadata.get("relations", {})
    if not isinstance(relations, dict):
        raise ProposedCarrierError("relations are malformed")
    role = metadata.get("content_role")
    status = metadata.get("status")
    plan_parts = relative_path.parts
    plan_tail = plan_parts[plan_parts.index("03_plan") + 1 : -1] if "03_plan" in plan_parts else ()
    plan_deep = (
        role == "Plan"
        and "03_plan" in plan_parts
        and len(plan_tail) > (0 if status == "Active" else 1)
    )
    if plan_deep and not relations.get("is_decomposition_of"):
        raise ProposedCarrierError("deep Plan placement requires an admitted decomposition parent")
    plan_source = next(
        (item for item in verified_source_context.inputs["sources"] if item["binding"]["atom_id"] == "CA-D-461"),
        None,
    )
    plan_mapping = (
        dict(re.findall(r"- ([A-Za-z]+): .*?`([^`]+)`", plan_source["text"]))
        if role == "Plan" and plan_source is not None
        else {}
    )
    result = validate_carrier(metadata, body, context, verified_source_context.inputs)
    if result["findings"] or result["gaps"] or any(item["outcome"] != "passed" for item in result["outcomes"]):
        raise ProposedCarrierError("complete-carrier validation failed or is unresolved")
    if relations and (not allow_existing_relations or plan_deep):
        targets = [target for values in relations.values() if isinstance(values, list) for target in values]
        try:
            inventory = inventory_proposed_references(
                verified_source_context.root,
                verified_source_context.inputs["structure"],
                targets,
                candidate_metadata=metadata,
                candidate_path=Path(".caprmedio_caprmedio") / relative_path,
                admitted_plan_status_folders=plan_mapping or None,
            )
        except ProposedReferenceError as error:
            raise ProposedCarrierError("relation targets are missing, inactive, ambiguous, or cyclic") from error
        graph_reader = ReadContext(roots=[str(verified_source_context.root)], limits=dict(CEILINGS))
        graph_report: Record = {"bindings": {}, "coverage": {"gaps": []}}
        graph_sources = [
            _source(verified_source_context.root, identifier, graph_reader, graph_report, graph=True)
            for identifier in _GRAPH_IDS
        ]
        graph_inputs = dict(verified_source_context.inputs)
        graph_inputs.update(
            sources=[
                *[
                    source for source in verified_source_context.inputs["sources"]
                    if source["binding"]["atom_id"] not in APPROVED_GRAPH_AUTHORITY_IDS
                ],
                *graph_sources,
            ],
            reader=graph_reader,
            reference_complete=True,
            path=verified_source_context.root / ".caprmedio_caprmedio" / relative_path,
            references=[
                {"path": verified_source_context.root / item.path, "metadata": item.metadata}
                for item in (*inventory.direct_targets, *inventory.plan_parent_closure)
            ],
        )
        plan_status_source = next(
            (source for source in graph_sources if source["binding"]["atom_id"] == "CA-R-1539"), None
        )
        domains = (
            {"domain.status.plan": _domain(plan_status_source["text"])}
            if plan_status_source is not None
            else {}
        )
        graph_context = AuthorityContext([], 0, 0, 0, [], (), domains, False)
        for code, adapter in (("relations.resolution", relations_resolution), ("plan.decomposition_resolution", plan_resolution)):
            check = Check(Obligation(code, [], True, "verified graph authority"), graph_context, graph_inputs)
            adapter(metadata, body, check)
            if check.findings or check.gaps:
                raise ProposedCarrierError("relation or Plan decomposition admission failed or is unresolved")
    role = metadata.get("content_role")
    status = metadata.get("status")
    names = {part.lower() for part in relative_path.parts[:-1]}
    source = next((row for row in verified_source_context.inputs["sources"] if row["binding"]["atom_id"] == "CA-D-324"), None)
    if source is None or not isinstance(role, str):
        raise ProposedCarrierError("role-directory authority is unavailable")
    mapping = dict(re.findall(r"- ([A-Za-z]+): `([0-9]{2}_[a-z_]+)/`[;.]", source["text"]))
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
    expected_status_directory = (
        "" if isinstance(status, str) and status.casefold() == "active"
        else status.lower() if isinstance(status, str) else None
    )
    if role == "Plan":
        if plan_source is None:
            raise ProposedCarrierError("Plan placement authority is unavailable")
        expected_status_directory = "" if status == "Active" else plan_mapping.get(status)
    role_index = relative_path.parts.index(expected_role_directory)
    tail = relative_path.parts[role_index + 1 : -1]
    if len(tail) > 1 and role != "Plan":
        raise ProposedCarrierError("deeper carrier placement is unsupported")
    actual_status_directory = "" if role == "Plan" and status == "Active" else (tail[-1] if tail else "")
    if expected_status_directory is None or actual_status_directory != expected_status_directory:
        raise ProposedCarrierError("carrier path disagrees with its carried status")
    return result
