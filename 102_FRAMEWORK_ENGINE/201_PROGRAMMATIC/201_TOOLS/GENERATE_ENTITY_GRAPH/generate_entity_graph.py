#!/usr/bin/env python3
"""Build an on-demand Entity Graph from Atom Subjects in any selected folder."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import tomllib
from collections import defaultdict
from collections.abc import Iterable, Mapping, Sequence
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from artifact_metadata import atom_identifier
from project_runtime import atomic_tempfile


TOOL_ID = "GENERATE_ENTITY_GRAPH"
TOOL_KIND = "finder"
SCHEMA_VERSION = 6
INACTIVE_DIRECTORY_NAMES = {"archive", "drafts", "done", "canceled", "cancelled", "solved", "handled"}
PROJECTION_DIRECTORY_NAME = "_projection"
JOURNAL_DIRECTORY_NAME = "_journal"
PERSISTED_CONTROL_NON_SOURCE_DIRECTORY_NAMES = {
    PROJECTION_DIRECTORY_NAME,
    JOURNAL_DIRECTORY_NAME,
}
CANONICAL_SUBJECT_KINDS = {"governs": "GOVERNS", "depends_on": "DEPENDS_ON"}
LEGACY_SUBJECT_KINDS = {"declared": "GOVERNS", "prerequisite": "DEPENDS_ON"}
TEMPORAL_FORMS = {"continuant": "CONTINUANT", "occurrent": "OCCURRENT"}
_SECRET_SHAPED = re.compile(r"(?:secret|password|token|credential|api[_-]?key)", re.I)


class EntityGraphError(RuntimeError):
    """A stable Entity Graph generation failure."""

    def __init__(self, code: str, message: str, **details: object) -> None:
        self.code = code
        self.message = message
        self.details = details
        super().__init__(message)

    def record(self) -> dict[str, object]:
        record: dict[str, object] = {"severity": "error", "code": self.code, "message": self.message}
        if self.details:
            record["details"] = self.details
        return record


@dataclass(frozen=True)
class ActualRunRecordingContext:
    """An execution-local proof that this Action has a recorded start.

    This is intentionally not a JSON request shape.  The selected executor
    creates it only after the shared Run session has durably recorded the
    actual Action start; caller-supplied receipt strings cannot impersonate it.
    Terminal evidence is recorded after the projection effect by the same
    shared session.
    """

    workflow_run_id: str
    step_run_id: str
    action_run_id: str
    start_event_receipt: Mapping[str, object]


def actual_run_recording_context(
    workflow_run_id: str,
    step_run_id: str,
    action_run_id: str,
    start_event_receipt: Mapping[str, object],
) -> ActualRunRecordingContext:
    """Build the executor-only graph recording capability.

    Kept as a small constructor so the executor and focused tests share the
    exact structural validation without accepting a caller JSON substitute.
    """

    if not all(isinstance(value, str) and value for value in (workflow_run_id, step_run_id, action_run_id)):
        raise EntityGraphError("recording-context-invalid", "Actual Run recording context is incomplete")
    if not isinstance(start_event_receipt, Mapping):
        raise EntityGraphError("recording-context-invalid", "Actual Action start receipt is unavailable")
    required = {
        "event_id", "action_id", "event_digest", "carrier", "line",
        "previous_carrier_digest", "appended_carrier_digest",
    }
    if set(start_event_receipt) != required:
        raise EntityGraphError("recording-context-invalid", "Actual Action start receipt is invalid")
    if (
        not isinstance(start_event_receipt["event_id"], str)
        or not isinstance(start_event_receipt["action_id"], str)
        or not isinstance(start_event_receipt["carrier"], str)
        or type(start_event_receipt["line"]) is not int
        or start_event_receipt["line"] < 1
        or any(not isinstance(start_event_receipt[key], str) for key in (
            "event_digest", "previous_carrier_digest", "appended_carrier_digest",
        ))
    ):
        raise EntityGraphError("recording-context-invalid", "Actual Action start receipt is invalid")
    return ActualRunRecordingContext(
        workflow_run_id=workflow_run_id,
        step_run_id=step_run_id,
        action_run_id=action_run_id,
        start_event_receipt=dict(start_event_receipt),
    )


@dataclass(frozen=True)
class AtomCarrier:
    atom_id: str
    version: int
    cce_form: str
    content_role: str
    atom_type: str
    status: str
    carrier_path: str
    sha256: str
    frontmatter: str
    body: str

    def evidence(self) -> dict[str, object]:
        return {
            "atom_id": self.atom_id,
            "atom_revision": self.version,
            "carrier_path": self.carrier_path,
            "carrier_sha256": self.sha256,
            "content_role": self.content_role,
            "type": self.atom_type,
            "status": self.status,
        }


@dataclass(frozen=True)
class SubjectRelation:
    atom_id: str
    atom_revision: int
    carrier_path: str
    carrier_sha256: str
    subject_path: str
    kind: str
    temporal_form: str
    source_schema_key: str
    cce_form: str

    def record(self) -> dict[str, object]:
        return {
            "atom_id": self.atom_id,
            "atom_revision": self.atom_revision,
            "carrier_path": self.carrier_path,
            "carrier_sha256": self.carrier_sha256,
            "subject_path": self.subject_path,
            "kind": self.kind,
            "temporal_form": self.temporal_form,
            "source_schema_key": self.source_schema_key,
            "cce_form": self.cce_form,
        }

    def evidence(self) -> dict[str, object]:
        return self.record()


def canonical_json(value: object, *, pretty: bool = False) -> str:
    if pretty:
        return json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n"


def scalar_value(raw: str) -> str:
    value = raw.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        value = value[1:-1]
    return value


def yaml_scalar_or_list(raw: str, *, path: str, field: str) -> list[str]:
    """Read the narrow scalar/inline-list YAML form used by current Subjects."""

    value = raw.strip()
    if not value:
        return []
    if not (value.startswith("[") and value.endswith("]")):
        return [scalar_value(value)]
    body = value[1:-1].strip()
    if not body:
        return []
    values = [scalar_value(item) for item in body.split(",")]
    if any(not item for item in values):
        raise EntityGraphError("subjects-yaml-invalid", "Subject list has an empty value", path=path, field=field)
    return values


def split_frontmatter(data: bytes, path: str) -> str | None:
    if not data.startswith(b"---\n"):
        return None
    boundary = data.find(b"\n---\n", 4)
    if boundary < 0:
        raise EntityGraphError("frontmatter-unterminated", "Markdown frontmatter is unterminated", path=path)
    try:
        return data[4:boundary].decode("utf-8")
    except UnicodeDecodeError as error:
        raise EntityGraphError("carrier-not-utf8", "Markdown Carrier must be UTF-8", path=path) from error


def markdown_body(data: bytes, path: str) -> str:
    boundary = data.find(b"\n---\n", 4)
    if boundary < 0:
        raise EntityGraphError("frontmatter-unterminated", "Markdown frontmatter is unterminated", path=path)
    try:
        return data[boundary + len(b"\n---\n") :].decode("utf-8")
    except UnicodeDecodeError as error:
        raise EntityGraphError("carrier-not-utf8", "Markdown Carrier must be UTF-8", path=path) from error


def top_scalar(frontmatter: str, key: str) -> str | None:
    matches = re.findall(rf"(?m)^{re.escape(key)}:\s*([^\n]+?)\s*$", frontmatter)
    if len(matches) > 1:
        raise EntityGraphError("frontmatter-duplicate-key", "Atom Carrier has a duplicate scalar", key=key)
    return scalar_value(matches[0]) if matches else None


def top_block(frontmatter: str, key: str) -> list[str]:
    lines = frontmatter.splitlines()
    starts = [index for index, line in enumerate(lines) if re.fullmatch(rf"{re.escape(key)}:\s*", line)]
    if len(starts) > 1:
        raise EntityGraphError("frontmatter-duplicate-key", "Atom Carrier has a duplicate block", key=key)
    if not starts:
        return []
    block: list[str] = []
    for line in lines[starts[0] + 1 :]:
        if line and not line[0].isspace():
            break
        block.append(line)
    return block


def _display_path(path: Path, repository: Path) -> str:
    try:
        return path.relative_to(repository).as_posix()
    except ValueError:
        return path.as_posix()


def _is_excluded(path: Path, selected_folder: Path, repository: Path) -> bool:
    relative_parts = path.relative_to(selected_folder).parts[:-1]
    if any(part.lower() in INACTIVE_DIRECTORY_NAMES for part in relative_parts):
        return True
    try:
        control_root = _configured_control_root(repository)
    except EntityGraphError:
        return False
    return any(
        path.is_relative_to(control_root / directory)
        for directory in PERSISTED_CONTROL_NON_SOURCE_DIRECTORY_NAMES
    )


def discover_atoms(repository: Path, selected_folder: Path) -> tuple[list[AtomCarrier], list[dict[str, object]]]:
    carriers: list[AtomCarrier] = []
    diagnostics: list[dict[str, object]] = []
    for path in sorted(selected_folder.rglob("*.md")):
        if _is_excluded(path, selected_folder, repository):
            continue
        display_path = _display_path(path, repository)
        data = path.read_bytes()
        frontmatter = split_frontmatter(data, display_path)
        if frontmatter is None:
            diagnostics.append(
                {
                    "severity": "info",
                    "code": "non-atom-markdown-skipped",
                    "message": "Markdown Carrier without frontmatter was skipped.",
                    "details": {"carrier_path": display_path},
                }
            )
            continue
        subjects = top_block(frontmatter, "subjects")
        if not subjects:
            diagnostics.append(
                {
                    "severity": "info",
                    "code": "non-atom-markdown-skipped",
                    "message": "Markdown Carrier without Atom Subjects was skipped.",
                    "details": {"carrier_path": display_path},
                }
            )
            continue
        atom_id = atom_identifier(path.name, top_scalar(frontmatter, "atom_id"))
        cce_form = (top_scalar(frontmatter, "cce_form") or "").lower()
        content_role = top_scalar(frontmatter, "content_role") or ""
        atom_type = top_scalar(frontmatter, "type") or ""
        status = top_scalar(frontmatter, "status") or ""
        if status and status.lower() != "active":
            diagnostics.append(
                {
                    "severity": "info",
                    "code": "inactive-status-skipped",
                    "message": "Markdown Atom Carrier outside Active status was excluded from the selected frontier.",
                    "details": {"atom_id": atom_id, "carrier_path": display_path, "status": status},
                }
            )
            continue
        raw_version = top_scalar(frontmatter, "version")
        if not raw_version or not raw_version.isdigit() or int(raw_version) < 1:
            raise EntityGraphError(
                "atom-version-invalid",
                "Atom Carrier requires a positive integer version",
                path=display_path,
                value=raw_version,
            )
        carriers.append(
            AtomCarrier(
                atom_id=atom_id,
                version=int(raw_version),
                cce_form=cce_form,
                content_role=content_role,
                atom_type=atom_type,
                status=status or "legacy-unspecified",
                carrier_path=display_path,
                sha256=hashlib.sha256(data).hexdigest(),
                frontmatter=frontmatter,
                body=markdown_body(data, display_path),
            )
        )
    if not carriers:
        raise EntityGraphError(
            "atom-set-empty",
            "Selected folder contains no active Markdown Atom Carriers with Subjects",
            folder=_display_path(selected_folder, repository),
        )
    return carriers, diagnostics


def parse_subject_relations(carrier: AtomCarrier) -> tuple[list[SubjectRelation], list[dict[str, object]]]:
    block = top_block(carrier.frontmatter, "subjects")
    relations: list[SubjectRelation] = []
    diagnostics: list[dict[str, object]] = []
    current_kind: str | None = None
    current_form: str | None = None
    legacy_keys: set[str] = set()

    def append(kind: str, subject_path: str, temporal_form: str, source_schema_key: str) -> None:
        if not subject_path:
            raise EntityGraphError("subject-path-empty", "Subject Path must not be empty", path=carrier.carrier_path)
        relations.append(
            SubjectRelation(
                atom_id=carrier.atom_id,
                atom_revision=carrier.version,
                carrier_path=carrier.carrier_path,
                carrier_sha256=carrier.sha256,
                subject_path=subject_path,
                kind=CANONICAL_SUBJECT_KINDS.get(kind) or LEGACY_SUBJECT_KINDS[kind],
                temporal_form=temporal_form,
                source_schema_key=source_schema_key,
                cce_form=carrier.cce_form,
            )
        )

    for line in block:
        kind_match = re.fullmatch(r"  ([a-z_]+):(?:\s*(.*))?", line)
        if kind_match:
            current_kind = kind_match.group(1)
            current_form = None
            if current_kind in LEGACY_SUBJECT_KINDS:
                legacy_keys.add(current_kind)
            elif current_kind not in CANONICAL_SUBJECT_KINDS:
                raise EntityGraphError(
                    "subject-kind-invalid",
                    "Atom Carrier has an unknown Subject relation kind",
                    path=carrier.carrier_path,
                    kind=current_kind,
                )
            inline_values = yaml_scalar_or_list(
                kind_match.group(2) or "", path=carrier.carrier_path, field=current_kind
            )
            for subject_path in inline_values:
                append(current_kind, subject_path, "CURRENT", current_kind)
            continue
        form_match = re.fullmatch(r"    ([a-z_]+):(?:\s*(.*))?", line)
        if form_match:
            if current_kind is None:
                raise EntityGraphError(
                    "subject-coordinate-missing",
                    "Subject requires one relation kind before a nested value",
                    path=carrier.carrier_path,
                    line=line,
                )
            candidate_form = form_match.group(1)
            if candidate_form in TEMPORAL_FORMS:
                current_form = candidate_form
                for subject_path in yaml_scalar_or_list(
                    form_match.group(2) or "", path=carrier.carrier_path, field=candidate_form
                ):
                    append(current_kind, subject_path, TEMPORAL_FORMS[candidate_form], current_kind)
                continue
            raise EntityGraphError(
                "subject-temporal-form-invalid",
                "Atom Carrier has an unknown legacy Subject Temporal Form",
                path=carrier.carrier_path,
                temporal_form=candidate_form,
            )
        current_item_match = re.fullmatch(r"    -\s*(.+?)\s*", line)
        if current_item_match:
            if current_kind is None or current_form is not None:
                raise EntityGraphError(
                    "subject-coordinate-missing",
                    "Current Subject item requires one relation kind without a legacy Temporal Form",
                    path=carrier.carrier_path,
                    line=line,
                )
            append(current_kind, scalar_value(current_item_match.group(1)), "CURRENT", current_kind)
            continue
        item_match = re.fullmatch(r"      -\s*(.+?)\s*", line)
        if not item_match:
            if line.strip():
                raise EntityGraphError(
                    "subjects-yaml-unsupported",
                    "Atom Carrier uses unsupported subjects YAML",
                    path=carrier.carrier_path,
                    line=line,
                )
            continue
        if current_kind is None or current_form is None:
            raise EntityGraphError(
                "subject-coordinate-missing",
                "Subject requires one relation kind and one Temporal Form",
                path=carrier.carrier_path,
                line=line,
            )
        append(current_kind, scalar_value(item_match.group(1)), TEMPORAL_FORMS[current_form], current_kind)
    if legacy_keys:
        diagnostics.append(
            {
                "severity": "warning",
                "code": "legacy-subject-schema-mapped",
                "message": "Legacy Subject roles were mapped to their current Subject relation kinds for this derived Projection.",
                "details": {
                    "atom_id": carrier.atom_id,
                    "carrier_path": carrier.carrier_path,
                    "mapping": {
                        key: LEGACY_SUBJECT_KINDS[key]
                        for key in sorted(legacy_keys)
                    },
                },
            }
        )
    governed_subjects = [relation for relation in relations if relation.kind == "GOVERNS"]
    if len(governed_subjects) != 1:
        raise EntityGraphError(
            "atom-governs-cardinality",
            "Every Atom must reference exactly one governed Entity through GOVERNS.",
            atom_id=carrier.atom_id,
            carrier_path=carrier.carrier_path,
            governs_count=len(governed_subjects),
        )
    return relations, diagnostics


def _subject_parts(subject_path: str) -> list[tuple[str, str | None]]:
    parts = re.split(r"\s*([/:])\s*", subject_path.strip())
    if not parts or not parts[0]:
        raise EntityGraphError("subject-path-empty", "Subject Path must not be empty")
    if len(parts) % 2 == 0:
        raise EntityGraphError("subject-path-invalid", "Subject Path ends with a separator", subject_path=subject_path)
    result: list[tuple[str, str | None]] = []
    for index in range(0, len(parts), 2):
        segment = parts[index].strip()
        if not segment:
            raise EntityGraphError(
                "subject-path-empty-segment", "Subject Path has an empty segment", subject_path=subject_path
            )
        separator = None if index == 0 else parts[index - 1]
        result.append((segment, separator))
    return result


def terminal_term(subject_path: str) -> str:
    """Return the terminal Term named by one complete Subject Expression."""

    return _subject_parts(subject_path)[-1][0]


def _subject_prefix(parent: str, separator: str, segment: str) -> str:
    return f"{parent}{separator}{' ' if separator == ':' else ''}{segment}"


def _edge_evidence(relation: SubjectRelation) -> dict[str, object]:
    return {
        "atom_id": relation.atom_id,
        "atom_revision": relation.atom_revision,
        "carrier_path": relation.carrier_path,
        "carrier_sha256": relation.carrier_sha256,
        "claim_subject_relation": relation.kind,
        "subject_path": relation.subject_path,
    }


def term_system_edges(
    carriers: Sequence[AtomCarrier], relations: Sequence[SubjectRelation]
) -> list[dict[str, object]]:
    """Derive typed Term-System edges without treating all dependencies as taxonomy."""

    edge_rows: dict[tuple[str, str, str], dict[str, object]] = {}

    def add(
        relation_kind: str,
        source_subject: str,
        source_term: str,
        target_subject: str,
        target_term: str,
        evidence: Mapping[str, object],
    ) -> None:
        key = (relation_kind, source_subject, target_subject)
        row = edge_rows.setdefault(
            key,
            {
                "relation": relation_kind,
                "source_subject": source_subject,
                "source_term": source_term,
                "target_subject": target_subject,
                "target_term": target_term,
                "evidence": [],
            },
        )
        rows = row["evidence"]
        assert isinstance(rows, list)
        candidate = dict(evidence)
        if candidate not in rows:
            rows.append(candidate)

    for relation in relations:
        parts = _subject_parts(relation.subject_path)
        parent_prefix = parts[0][0]
        for segment, separator in parts[1:]:
            assert separator is not None
            child_prefix = _subject_prefix(parent_prefix, separator, segment)
            if separator == "/":
                add(
                    "IS_BORNE_BY",
                    child_prefix,
                    segment,
                    parent_prefix,
                    terminal_term(parent_prefix),
                    _edge_evidence(relation),
                )
            else:
                add(
                    "IS_ALLOWED_VALUE_OF",
                    child_prefix,
                    segment,
                    parent_prefix,
                    terminal_term(parent_prefix),
                    _edge_evidence(relation),
                )
            parent_prefix = child_prefix

    subkind_pattern = re.compile(
        r"(?m)^(?:the Term )?([A-Z][A-Za-z0-9]*(?: [A-Z][A-Za-z0-9]*)*) "
        r"(?:must be (?:a )?)?SUBKIND_OF "
        r"([A-Z][A-Za-z0-9]*(?: [A-Z][A-Za-z0-9]*)*)"
    )
    relations_by_carrier: dict[str, list[SubjectRelation]] = defaultdict(list)
    for relation in relations:
        relations_by_carrier[relation.carrier_path].append(relation)
    for carrier in carriers:
        normalized_body = carrier.body.replace("**", "").replace("`", "")
        for match in subkind_pattern.finditer(normalized_body):
            source_term, target_term = match.groups()
            governed_terms = {
                terminal_term(row.subject_path)
                for row in relations_by_carrier[carrier.carrier_path]
                if row.kind == "GOVERNS"
            }
            depended_terms = {
                terminal_term(row.subject_path)
                for row in relations_by_carrier[carrier.carrier_path]
                if row.kind == "DEPENDS_ON"
            }
            if source_term not in governed_terms or target_term not in depended_terms:
                continue
            add(
                "SUBKIND_OF",
                source_term,
                source_term,
                target_term,
                target_term,
                {**carrier.evidence(), "claim": match.group(0)},
            )

    for row in edge_rows.values():
        evidence = row["evidence"]
        assert isinstance(evidence, list)
        evidence.sort(key=lambda item: canonical_json(item))
    return sorted(
        edge_rows.values(),
        key=lambda row: (str(row["relation"]), str(row["source_subject"]), str(row["target_subject"])),
    )


def term_system_analysis(
    declared_terms: Sequence[str], edges: Sequence[Mapping[str, object]]
) -> dict[str, object]:
    subkind_parents: dict[str, set[str]] = defaultdict(set)
    allowed_value_parents: dict[str, set[str]] = defaultdict(set)
    bearer_parents: dict[str, set[str]] = defaultdict(set)
    subkind_graph: dict[str, set[str]] = defaultdict(set)
    for edge in edges:
        relation_kind = str(edge["relation"])
        source_subject = str(edge["source_subject"])
        source_term = str(edge["source_term"])
        target_subject = str(edge["target_subject"])
        if relation_kind == "SUBKIND_OF":
            subkind_parents[source_term].add(str(edge["target_term"]))
            subkind_graph[source_term].add(str(edge["target_term"]))
        elif relation_kind == "IS_ALLOWED_VALUE_OF":
            allowed_value_parents[source_term].add(target_subject)
        elif relation_kind == "IS_BORNE_BY":
            bearer_parents[source_subject].add(target_subject)

    violations: list[dict[str, object]] = []
    for term, parents in sorted(allowed_value_parents.items()):
        if len(parents) > 1:
            violations.append(
                {
                    "code": "term-allowed-value-parent-cardinality",
                    "term": term,
                    "actual": len(parents),
                    "maximum": 1,
                    "parents": sorted(parents),
                }
            )
    for subject, parents in sorted(bearer_parents.items()):
        if len(parents) != 1:
            violations.append(
                {
                    "code": "dependent-subject-bearer-cardinality",
                    "subject": subject,
                    "actual": len(parents),
                    "required": 1,
                    "parents": sorted(parents),
                }
            )
    subkind_cycles = dependency_cycles(subkind_graph)
    for cycle in subkind_cycles:
        violations.append({"code": "term-subkind-cycle", "cycle": cycle})

    prohibited_type_terms = sorted(
        term for term in declared_terms if term != "Type" and term.endswith(" Type")
    )
    for term in prohibited_type_terms:
        violations.append({"code": "role-specific-type-term", "term": term})

    root_terms = sorted(
        term
        for term in declared_terms
        if not subkind_parents.get(term) and not allowed_value_parents.get(term)
    )
    return {
        "root_terms": root_terms,
        "subkind_cycles": subkind_cycles,
        "prohibited_role_specific_type_terms": prohibited_type_terms,
        "direct_parents": {
            term: {
                "SUBKIND_OF": sorted(subkind_parents.get(term, ())),
                "IS_ALLOWED_VALUE_OF": sorted(allowed_value_parents.get(term, ())),
            }
            for term in sorted(declared_terms)
        },
        "bearer_parents_by_subject_occurrence": {
            subject: sorted(parents) for subject, parents in sorted(bearer_parents.items())
        },
        "violations": violations,
    }


def declared_term_tree(declared: Mapping[str, Sequence[SubjectRelation]]) -> list[dict[str, object]]:
    roots: dict[tuple[str, str | None], dict[str, object]] = {}
    for term in sorted(declared):
        for relation in declared[term]:
            parts = _subject_parts(relation.subject_path)
            current_children = roots
            prefix = ""
            for segment, separator in parts:
                prefix = (
                    segment
                    if separator is None
                    else f"{prefix}{separator}{' ' if separator == ':' else ''}{segment}"
                )
                key = (segment, separator)
                node = current_children.setdefault(
                    key,
                    {
                        "segment": segment,
                        "subject_path": prefix,
                        "relation_from_parent": (
                            None
                            if separator is None
                            else "IS_BORNE_BY"
                            if separator == "/"
                            else "IS_ALLOWED_VALUE_OF"
                        ),
                        "declared": False,
                        "declared_term": None,
                        "declared_by": [],
                        "children": {},
                    },
                )
                current_children = node["children"]
                assert isinstance(current_children, dict)
            node["declared"] = True
            node["declared_term"] = term
            declared_by = node["declared_by"]
            assert isinstance(declared_by, list)
            declared_by.append(relation.evidence())

    def serialize(nodes: Mapping[tuple[str, str | None], Mapping[str, object]]) -> list[dict[str, object]]:
        rendered: list[dict[str, object]] = []
        for key in sorted(nodes, key=lambda item: (str(item[1]), item[0])):
            node = dict(nodes[key])
            children = node.pop("children")
            assert isinstance(children, Mapping)
            node["children"] = serialize(children)
            rendered.append(node)
        return rendered

    return serialize(roots)


def _relation_sort_key(relation: SubjectRelation) -> tuple[object, ...]:
    return (
        relation.kind,
        relation.subject_path,
        relation.temporal_form,
        relation.atom_id,
        relation.atom_revision,
        relation.carrier_path,
    )


def _is_definition_carrier(carrier: AtomCarrier) -> bool:
    """Admit current Definition Type carriers; retain retired CCE-form compatibility."""

    return (
        carrier.atom_type.strip().lower() == "definition"
        or carrier.content_role.strip().lower() == "definition"
        or carrier.cce_form == "definition"
    )


def dependency_edges(
    carriers: Sequence[AtomCarrier],
    relations: Sequence[SubjectRelation],
) -> tuple[
    dict[str, set[str]],
    dict[tuple[str, str], list[dict[str, object]]],
    dict[str, list[SubjectRelation]],
    dict[str, list[SubjectRelation]],
    dict[str, list[SubjectRelation]],
]:
    by_atom: dict[tuple[str, str], list[SubjectRelation]] = defaultdict(list)
    carriers_by_atom = {(carrier.atom_id, carrier.carrier_path): carrier for carrier in carriers}
    for relation in relations:
        by_atom[(relation.atom_id, relation.carrier_path)].append(relation)
    graph: dict[str, set[str]] = defaultdict(set)
    evidence: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    declared_terms: dict[str, list[SubjectRelation]] = defaultdict(list)
    governed_subjects: dict[str, list[SubjectRelation]] = defaultdict(list)
    depended: dict[str, list[SubjectRelation]] = defaultdict(list)
    definition_rows_by_atom: dict[tuple[str, str], list[SubjectRelation]] = {}
    dependency_rows_by_atom: dict[tuple[str, str], list[SubjectRelation]] = {}
    for atom_key, rows in by_atom.items():
        governs = sorted((row for row in rows if row.kind == "GOVERNS"), key=_relation_sort_key)
        depends_on = sorted((row for row in rows if row.kind == "DEPENDS_ON"), key=_relation_sort_key)
        is_definition = _is_definition_carrier(carriers_by_atom[atom_key])
        for row in governs:
            governed_subjects[row.subject_path].append(row)
            if is_definition:
                declared_terms[terminal_term(row.subject_path)].append(row)
        for row in depends_on:
            depended[row.subject_path].append(row)
        definition_rows_by_atom[atom_key] = list(governs) if is_definition else []
        dependency_rows_by_atom[atom_key] = depends_on

    declared_term_names = set(declared_terms)
    for atom_key, definition_terms in definition_rows_by_atom.items():
        depends_on = dependency_rows_by_atom[atom_key]
        for governed in definition_terms:
            governed_term = terminal_term(governed.subject_path)
            for parent in depends_on:
                parent_terminal = terminal_term(parent.subject_path)
                parent_node = parent_terminal if parent_terminal in declared_term_names else parent.subject_path
                graph[governed_term].add(parent_node)
                evidence[(governed_term, parent_node)].append(
                    {
                        "atom_id": governed.atom_id,
                        "atom_revision": governed.atom_revision,
                        "carrier_path": governed.carrier_path,
                        "carrier_sha256": governed.carrier_sha256,
                        "defined_term": governed_term,
                        "definition_subject_path": governed.subject_path,
                        "depends_on_subject_path": parent.subject_path,
                        "depends_on_terminal_term": parent_terminal,
                        "governs_temporal_form": governed.temporal_form,
                        "depends_on_temporal_form": parent.temporal_form,
                        "governs_source_schema_key": governed.source_schema_key,
                        "depends_on_source_schema_key": parent.source_schema_key,
                        "definition_cce_form": governed.cce_form,
                    }
                )
    for rows in declared_terms.values():
        rows.sort(key=_relation_sort_key)
    for rows in governed_subjects.values():
        rows.sort(key=_relation_sort_key)
    for rows in depended.values():
        rows.sort(key=_relation_sort_key)
    for rows in evidence.values():
        rows.sort(key=lambda row: tuple(str(row[key]) for key in sorted(row)))
    return graph, evidence, declared_terms, governed_subjects, depended


def dependency_cycles(graph: Mapping[str, set[str]]) -> list[list[str]]:
    """Return deterministic strongly connected components that contain a cycle."""

    index = 0
    indexes: dict[str, int] = {}
    lowlinks: dict[str, int] = {}
    stack: list[str] = []
    on_stack: set[str] = set()
    components: list[list[str]] = []
    nodes = set(graph)
    for parents in graph.values():
        nodes.update(parents)

    def connect(node: str) -> None:
        nonlocal index
        indexes[node] = index
        lowlinks[node] = index
        index += 1
        stack.append(node)
        on_stack.add(node)
        for parent in sorted(graph.get(node, ())):
            if parent not in indexes:
                connect(parent)
                lowlinks[node] = min(lowlinks[node], lowlinks[parent])
            elif parent in on_stack:
                lowlinks[node] = min(lowlinks[node], indexes[parent])
        if lowlinks[node] == indexes[node]:
            component: list[str] = []
            while True:
                member = stack.pop()
                on_stack.remove(member)
                component.append(member)
                if member == node:
                    break
            component.sort()
            if len(component) > 1 or node in graph.get(node, set()):
                components.append(component)

    for node in sorted(nodes):
        if node not in indexes:
            connect(node)
    return sorted(components, key=lambda component: tuple(component))


def dependency_tree_for(
    term: str,
    graph: Mapping[str, set[str]],
    evidence: Mapping[tuple[str, str], Sequence[Mapping[str, object]]],
    declared_terms: set[str],
    governed_subjects: set[str],
) -> dict[str, object]:
    def expand(node: str, stack: tuple[str, ...]) -> dict[str, object]:
        if node in stack:
            start = stack.index(node)
            return {
                "subject": node,
                "term": node if node in declared_terms else None,
                "is_declared_term": node in declared_terms,
                "is_governed_subject": node in governed_subjects,
                "cycle": True,
                "cycle_path": list(stack[start:] + (node,)),
                "parents": [],
            }
        parents: list[dict[str, object]] = []
        for parent in sorted(graph.get(node, ())):
            branch = expand(parent, stack + (node,))
            branch["relation_evidence"] = [dict(row) for row in evidence.get((node, parent), ())]
            parents.append(branch)
        return {
            "subject": node,
            "term": node if node in declared_terms else None,
            "is_declared_term": node in declared_terms,
            "is_governed_subject": node in governed_subjects or node in declared_terms,
            "parents": parents,
        }

    return expand(term, ())


def frontier_digest(carriers: Sequence[AtomCarrier]) -> str:
    records = [
        {
            "atom_id": carrier.atom_id,
            "atom_revision": carrier.version,
            "carrier_path": carrier.carrier_path,
            "carrier_sha256": carrier.sha256,
        }
        for carrier in carriers
    ]
    encoded = json.dumps(records, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def generate_projection(repository: Path, selected_folder: Path) -> dict[str, object]:
    repository = repository.resolve()
    selected_folder = selected_folder.resolve()
    if not selected_folder.is_dir():
        raise EntityGraphError("folder-missing", "Selected folder does not exist", folder=selected_folder.as_posix())
    carriers, diagnostics = discover_atoms(repository, selected_folder)
    relations: list[SubjectRelation] = []
    for carrier in carriers:
        carrier_relations, carrier_diagnostics = parse_subject_relations(carrier)
        relations.extend(carrier_relations)
        diagnostics.extend(carrier_diagnostics)
    relations.sort(key=_relation_sort_key)
    graph, edge_evidence, declared, governed, depended = dependency_edges(carriers, relations)
    duplicate_definitions = {
        term: rows for term, rows in declared.items() if len(rows) != 1
    }
    definition_conflicts = [
        {
            "term": term,
            "definitions": [row.evidence() for row in duplicate_definitions[term]],
        }
        for term in sorted(duplicate_definitions)
    ]
    for conflict in definition_conflicts:
        diagnostics.append(
            {
                "severity": "warning",
                "code": "governed-term-definition-conflict",
                "message": "A Governed Term resolves to more than one active Definition Atom in the selected source set.",
                "details": conflict,
            }
        )
    declared_terms = sorted(declared)
    governed_subjects = sorted(governed)
    depends_on_subjects = sorted(depended)
    declared_term_names = set(declared_terms)
    depends_on_terminal_terms = {
        terminal_term(subject_path) for subject_path in depends_on_subjects
    }
    terms_in_depends_on = sorted(depends_on_terminal_terms & declared_term_names)
    gaps = sorted(
        subject_path
        for subject_path in depends_on_subjects
        if subject_path not in governed
        and terminal_term(subject_path) not in declared_term_names
    )
    cycles = dependency_cycles(graph)
    dependency_trees = [
        dependency_tree_for(term, graph, edge_evidence, set(declared_terms), set(governed_subjects))
        for term in declared_terms
    ]
    typed_edges = term_system_edges(carriers, relations)
    typed_analysis = term_system_analysis(declared_terms, typed_edges)
    term_system_violations = typed_analysis["violations"]
    assert isinstance(term_system_violations, Sequence)
    for violation in term_system_violations:
        diagnostics.append(
            {
                "severity": "warning",
                "code": str(violation["code"]),
                "message": "The derived Term System violates a current structural invariant.",
                "details": dict(violation),
            }
        )
    diagnostics.sort(
        key=lambda row: (
            str(row.get("severity", "")),
            str(row.get("code", "")),
            str((row.get("details") or {}).get("carrier_path", ""))
            if isinstance(row.get("details"), Mapping)
            else "",
        )
    )
    return {
        "artifact_form": "PROJECTION",
        "authority": "NON_AUTHORITATIVE",
        "projection_kind": "ENTITY_GRAPH",
        "generator": TOOL_ID,
        "generation_procedure": "terminal_terms_typed_term_system_edges_and_claim_subject_relations_from_selected_folder",
        "updated_at": datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %z"),
        "source": {
            "selected_folder": _display_path(selected_folder, repository),
            "atom_count": len(carriers),
            "source_frontier_sha256": frontier_digest(carriers),
            "excluded_nested_directory_names": sorted(INACTIVE_DIRECTORY_NAMES),
        },
        "sets": {
            "declared_term_tree": declared_term_tree(declared),
            "dependency_trees_by_declared_term": dependency_trees,
            "terms_in_depends_on": terms_in_depends_on,
            "depends_on_subjects": depends_on_subjects,
        },
        "term_definitions": [
            {
                "term": term,
                "definition_count": len(declared[term]),
                "definitions": [
                    {
                        "subject_path": relation.subject_path,
                        "defined_by": relation.evidence(),
                    }
                    for relation in declared[term]
                ],
            }
            for term in declared_terms
        ],
        "definition_conflicts": definition_conflicts,
        "declared_terms": declared_terms,
        "governed_subjects": governed_subjects,
        "depends_on_subjects": depends_on_subjects,
        "terms_in_depends_on": terms_in_depends_on,
        "depends_on_without_governs": gaps,
        "dependency_cycles": cycles,
        "term_system": {
            "edges": typed_edges,
            **typed_analysis,
        },
        "claim_subject_relations": [relation.record() for relation in relations],
        "diagnostics": diagnostics,
        "counts": {
            "declared_terms": len(declared_terms),
            "governed_subjects": len(governed_subjects),
            "depends_on_subjects": len(depends_on_subjects),
            "terms_in_depends_on": len(terms_in_depends_on),
            "depends_on_without_governs": len(gaps),
            "dependency_cycles": len(cycles),
            "definition_conflicts": len(definition_conflicts),
            "term_system_edges": len(typed_edges),
            "term_system_violations": len(term_system_violations),
            "root_terms": len(typed_analysis["root_terms"]),
            "claim_subject_relations": len(relations),
            "legacy_schema_atoms": sum(row["code"] == "legacy-subject-schema-mapped" for row in diagnostics),
        },
    }


GRAPH_KINDS = {"entities", "terms"}
STRICT_REQUEST_FIELDS = {
    "graph_kind",
    "source_frontier",
    "selection",
    "display_selection",
    "representation_configuration",
    "output_destination",
    "existing_projection_evidence",
    "capability_permission_evidence",
    "run_recording_context",
}
STRICT_REQUIRED_REQUEST_FIELDS = {
    "graph_kind",
    "source_frontier",
    "selection",
    "representation_configuration",
    "capability_permission_evidence",
    "run_recording_context",
}
PROJECT_SETTINGS_FILENAME = "caprmedio_project_settings.toml"
DEFAULT_GRAPH_OUTPUT_NAMES = {
    "entities": "entities_graph.json",
    "terms": "terms_graph.json",
}


def _mapping(value: object, name: str) -> Mapping[str, object]:
    if not isinstance(value, Mapping):
        raise EntityGraphError("request-field-invalid", f"{name} must be an object", field=name)
    return value


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _structure_frontier(repository: Path) -> dict[str, object] | None:
    try:
        path = _configured_control_root(repository) / "project_structure.toml"
    except EntityGraphError:
        return None
    if not path.is_file():
        return None
    return {
        "carrier_path": _display_path(path, repository),
        "carrier_sha256": _sha256(path),
        "schema_version": 1,
    }


def source_frontier_for(repository: Path, selected_folder: Path) -> dict[str, object]:
    """Seal the current Atom and optional Project Structure source frontier.

    Callers bind this returned value into a strict request.  The builder compares
    it before construction and again immediately before publication, rather than
    accepting a folder path as an implicit moving frontier.
    """

    repository = repository.resolve()
    selected_folder = selected_folder.resolve()
    carriers, _ = discover_atoms(repository, selected_folder)
    result: dict[str, object] = {
        "selected_folder": _display_path(selected_folder, repository),
        "carriers": [carrier.evidence() for carrier in carriers],
        "source_frontier_sha256": frontier_digest(carriers),
    }
    structure = _structure_frontier(repository)
    if structure is not None:
        result["project_structure"] = structure
    return result


def _safe_repository_path(repository: Path, value: str, *, name: str) -> Path:
    candidate = Path(value)
    if candidate.is_absolute() or ".." in candidate.parts:
        raise EntityGraphError("unsafe-path", f"{name} must be a safe repository-relative path", path=value)
    resolved = (repository / candidate).resolve()
    try:
        resolved.relative_to(repository)
    except ValueError as error:
        raise EntityGraphError("unsafe-path", f"{name} escapes the repository", path=value) from error
    return resolved


def _configured_project_roots(repository: Path) -> tuple[Path, Path]:
    """Resolve the Project-owned control and persistent Projection roots from Settings."""

    candidates = sorted(
        path
        for path in repository.glob(f"*/{PROJECT_SETTINGS_FILENAME}")
        if path.is_file() and not path.is_symlink()
    )
    if len(candidates) != 1:
        raise EntityGraphError(
            "project-settings-unavailable",
            "Exactly one Project Settings carrier is required to resolve Projection output.",
            settings_paths=[_display_path(path, repository) for path in candidates],
        )
    settings_path = candidates[0]
    try:
        settings = tomllib.loads(settings_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise EntityGraphError(
            "project-settings-unreadable",
            "Project Settings cannot be read to resolve Projection output.",
            path=_display_path(settings_path, repository),
        ) from error
    paths = settings.get("paths")
    if not isinstance(paths, Mapping):
        raise EntityGraphError("project-settings-invalid", "Project Settings require a paths object")
    control_value = paths.get("control_root")
    if not isinstance(control_value, str) or not control_value:
        raise EntityGraphError("project-settings-invalid", "paths.control_root must be a safe repository-relative path")
    control_root = _safe_repository_path(repository, control_value, name="paths.control_root")
    if control_root != settings_path.parent.resolve():
        raise EntityGraphError(
            "project-settings-invalid",
            "Project Settings must be located directly under paths.control_root.",
            control_root=control_value,
            path=_display_path(settings_path, repository),
        )
    configured_projection = paths.get("projection_root")
    if configured_projection is None:
        projection_root = control_root / PROJECTION_DIRECTORY_NAME
    elif isinstance(configured_projection, str) and configured_projection:
        projection_root = _safe_repository_path(repository, configured_projection, name="paths.projection_root")
    else:
        raise EntityGraphError(
            "project-settings-invalid",
            "paths.projection_root must be a safe repository-relative path when configured.",
        )
    expected_root = control_root / PROJECTION_DIRECTORY_NAME
    if projection_root != expected_root:
        raise EntityGraphError(
            "project-settings-invalid",
            "paths.projection_root must resolve to paths.control_root/_projection.",
            control_root=_display_path(control_root, repository),
            projection_root=_display_path(projection_root, repository),
        )
    return control_root, projection_root


def _configured_control_root(repository: Path) -> Path:
    return _configured_project_roots(repository)[0]


def _configured_projection_root(repository: Path) -> Path:
    return _configured_project_roots(repository)[1]


def _default_publication_path(repository: Path, graph_kind: str) -> Path:
    return _configured_projection_root(repository) / DEFAULT_GRAPH_OUTPUT_NAMES[graph_kind]


def _validate_frontier(
    repository: Path, frontier: Mapping[str, object]
) -> tuple[Path, dict[str, object], list[dict[str, object]]]:
    allowed = {"selected_folder", "carriers", "source_frontier_sha256", "project_structure"}
    unknown = sorted(set(frontier) - allowed)
    if unknown:
        raise EntityGraphError("source-frontier-unknown-field", "Source frontier has unknown fields", fields=unknown)
    selected_folder = frontier.get("selected_folder")
    if not isinstance(selected_folder, str) or not selected_folder:
        raise EntityGraphError("source-frontier-folder-missing", "Source frontier requires selected_folder")
    folder = _safe_repository_path(repository, selected_folder, name="source_frontier.selected_folder")
    if not folder.is_dir():
        raise EntityGraphError("source-frontier-folder-missing", "Selected source frontier folder is unavailable", folder=selected_folder)
    requested_carriers = frontier.get("carriers")
    requested_digest = frontier.get("source_frontier_sha256")
    if not isinstance(requested_carriers, list) or not isinstance(requested_digest, str) or not requested_digest:
        raise EntityGraphError("source-frontier-incomplete", "Source frontier requires carriers and source_frontier_sha256")
    actual = source_frontier_for(repository, folder)
    actual_carriers = actual["carriers"]
    assert isinstance(actual_carriers, list)
    if canonical_json(requested_carriers) != canonical_json(actual_carriers) or requested_digest != actual[
        "source_frontier_sha256"
    ]:
        return folder, actual, [
            {
                "severity": "error",
                "code": "source-frontier-stale",
                "message": "The admitted source frontier no longer matches current source bytes.",
                "details": {"requested": dict(frontier), "actual": actual},
            }
        ]
    requested_structure = frontier.get("project_structure")
    actual_structure = actual.get("project_structure")
    if requested_structure is not None and canonical_json(requested_structure) != canonical_json(actual_structure):
        return folder, actual, [
            {
                "severity": "error",
                "code": "project-structure-stale",
                "message": "The admitted Project Structure evidence no longer matches current bytes.",
                "details": {"requested": requested_structure, "actual": actual_structure},
            }
        ]
    return folder, actual, []


def _frontmatter_properties(carrier: AtomCarrier) -> dict[str, object]:
    properties: dict[str, object] = {}
    for line in carrier.frontmatter.splitlines():
        if line.startswith((" ", "\t")) or ":" not in line:
            continue
        key, raw = line.split(":", 1)
        if key in {"atom_id", "subjects", "relations"}:
            continue
        value = scalar_value(raw)
        # Properties are copied into the derived Entities Graph.  Reject a
        # secret-shaped name or scalar before building any serializable graph
        # shape, and never include the raw name/value in a diagnostic.
        if _SECRET_SHAPED.search(key) or _SECRET_SHAPED.search(value):
            raise EntityGraphError(
                "secret-shaped-property",
                "Selected source contains a secret-shaped Property that cannot be projected.",
                carrier_path=carrier.carrier_path,
            )
        if value:
            properties[key] = value
    properties["atom_revision"] = carrier.version
    properties["cce_form"] = carrier.cce_form
    return dict(sorted(properties.items()))


def _selected_carriers(
    carriers: Sequence[AtomCarrier], selection: Mapping[str, object]
) -> tuple[list[AtomCarrier], list[str]]:
    allowed = {"atom_ids", "scope_unit_names"}
    unknown = sorted(set(selection) - allowed)
    if unknown:
        raise EntityGraphError("selection-unknown-field", "Selection has unknown fields", fields=unknown)
    atom_ids = selection.get("atom_ids")
    if not isinstance(atom_ids, list) or not atom_ids or any(not isinstance(item, str) or not item for item in atom_ids):
        raise EntityGraphError("selection-atoms-invalid", "Selection requires a non-empty atom_ids array")
    if atom_ids != sorted(set(atom_ids)):
        raise EntityGraphError("selection-atoms-ambiguous", "Selection atom_ids must be unique and canonically sorted")
    available = {carrier.atom_id: carrier for carrier in carriers}
    missing = sorted(set(atom_ids) - set(available))
    if missing:
        raise EntityGraphError("selection-atom-unresolved", "Selection names atoms outside the admitted frontier", atom_ids=missing)
    scope_units = selection.get("scope_unit_names", [])
    if not isinstance(scope_units, list) or any(not isinstance(item, str) or not item for item in scope_units):
        raise EntityGraphError("selection-structure-invalid", "scope_unit_names must be an array of names")
    if scope_units != sorted(set(scope_units)):
        raise EntityGraphError("selection-structure-ambiguous", "scope_unit_names must be unique and canonically sorted")
    return [available[atom_id] for atom_id in atom_ids], scope_units


def _selected_structure(
    repository: Path, frontier: Mapping[str, object], scope_unit_names: Sequence[str]
) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    if not scope_unit_names:
        return [], []
    evidence = frontier.get("project_structure")
    if not isinstance(evidence, Mapping):
        return [], [
            {
                "severity": "error",
                "code": "project-structure-unbound",
                "message": "Selected Scope Units require bound Project Structure evidence.",
                "details": {"scope_unit_names": list(scope_unit_names)},
            }
        ]
    path_value = evidence.get("carrier_path")
    if not isinstance(path_value, str):
        raise EntityGraphError("project-structure-invalid", "Project Structure evidence lacks carrier_path")
    path = _safe_repository_path(repository, path_value, name="source_frontier.project_structure.carrier_path")
    try:
        parsed = tomllib.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise EntityGraphError("project-structure-unreadable", "Project Structure source is unreadable", path=path_value) from error
    raw_units = parsed.get("scope_units")
    if not isinstance(raw_units, list):
        raise EntityGraphError("project-structure-invalid", "Project Structure lacks scope_units", path=path_value)
    by_name = {
        unit.get("scope_unit_name"): unit
        for unit in raw_units
        if isinstance(unit, dict) and isinstance(unit.get("scope_unit_name"), str)
    }
    missing = sorted(set(scope_unit_names) - set(by_name))
    diagnostics: list[dict[str, object]] = []
    if missing:
        diagnostics.append(
            {
                "severity": "error",
                "code": "scope-unit-unresolved",
                "message": "Selected Scope Units are not declared by bound Project Structure evidence.",
                "details": {"scope_unit_names": missing, "carrier_path": path_value},
            }
        )
    keys = (
        "scope_unit_name",
        "parent",
        "scope_unit_type",
        "scope_unit_label",
        "structural_level",
        "local_order",
        "navigational_order_number",
        "authority_path",
        "delivery_path",
        "authority_mode",
    )
    rows = []
    for name in scope_unit_names:
        unit = by_name.get(name)
        if unit is None:
            continue
        row = {key: unit[key] for key in keys if key in unit}
        row["source"] = dict(evidence)
        rows.append(row)
    return rows, diagnostics


def _quality(
    *,
    diagnostics: Sequence[Mapping[str, object]],
    current: bool,
    authorized: bool,
    recording_confirmed: bool,
    persistence_valid: bool,
) -> dict[str, str]:
    codes = {str(row.get("code", "")) for row in diagnostics}
    invalid_codes = {
        "term-subkind-cycle",
        "dependency-cycle",
        "self-reference",
        "term-allowed-value-parent-cardinality",
        "dependent-subject-bearer-cardinality",
        "governed-term-definition-conflict",
    }
    incomplete_codes = {
        "term-unresolved",
        "scope-unit-unresolved",
        "project-structure-unbound",
        "carrier-unreadable",
    }
    return {
        "coverage": "fail" if codes & incomplete_codes else "pass",
        "fidelity": "fail" if any(row.get("severity") == "error" and str(row.get("code")) not in invalid_codes | incomplete_codes for row in diagnostics) else "pass",
        "validity": "fail" if codes & invalid_codes else "pass",
        "currentness": "pass" if current else "fail",
        "permission": "pass" if authorized else "fail",
        "persistence": "pass" if persistence_valid else "fail",
        "recording": "pass" if recording_confirmed else "fail",
    }


def _outcome_for(quality: Mapping[str, str], diagnostics: Sequence[Mapping[str, object]]) -> str:
    if quality["currentness"] != "pass":
        return "stale"
    if quality["permission"] != "pass" or quality["recording"] != "pass" or quality["persistence"] != "pass":
        return "blocked"
    if quality["validity"] != "pass":
        return "conflicting"
    if quality["coverage"] != "pass":
        return "incomplete"
    if quality["fidelity"] != "pass":
        return "failed"
    return "built"


def _term_dependencies(
    relations: Sequence[SubjectRelation], terms: set[str]
) -> tuple[dict[str, list[str]], list[dict[str, object]], list[list[str]]]:
    by_atom: dict[tuple[str, str], list[SubjectRelation]] = defaultdict(list)
    for relation in relations:
        by_atom[(relation.atom_id, relation.carrier_path)].append(relation)
    dependency_graph: dict[str, set[str]] = defaultdict(set)
    evidence: list[dict[str, object]] = []
    for rows in by_atom.values():
        governed = [row for row in rows if row.kind == "GOVERNS" and terminal_term(row.subject_path) in terms]
        depended = [row for row in rows if row.kind == "DEPENDS_ON"]
        for source in governed:
            source_term = terminal_term(source.subject_path)
            for target in depended:
                target_term = terminal_term(target.subject_path)
                if target_term in terms:
                    dependency_graph[source_term].add(target_term)
                    evidence.append(
                        {
                            "relation": "DEPENDS_ON",
                            "source": source_term,
                            "target": target_term,
                            "source_lineage": _edge_evidence(target),
                        }
                    )
    for term in terms:
        dependency_graph.setdefault(term, set())
    return (
        {term: sorted(targets) for term, targets in sorted(dependency_graph.items())},
        sorted(evidence, key=lambda row: (str(row["source"]), str(row["target"]))),
        dependency_cycles(dependency_graph),
    )


def _ancestor_sets(parents: Mapping[str, Sequence[str]]) -> tuple[dict[str, list[str]], list[list[str]]]:
    graph = {term: set(values) for term, values in parents.items()}
    cycles = dependency_cycles(graph)
    result: dict[str, list[str]] = {}
    for term in sorted(graph):
        found: set[str] = set()
        pending = list(graph[term])
        while pending:
            parent = pending.pop()
            if parent == term or parent in found:
                continue
            found.add(parent)
            pending.extend(graph.get(parent, ()))
        result[term] = sorted(found)
    return result, cycles


def _publication_path(repository: Path, value: object) -> Path:
    if not isinstance(value, str) or not value:
        raise EntityGraphError("output-destination-invalid", "output_destination must be a non-empty path")
    destination = _safe_repository_path(repository, value, name="output_destination")
    try:
        destination.relative_to(_configured_projection_root(repository))
    except ValueError as error:
        raise EntityGraphError(
            "output-destination-unauthorized",
            "Output destination is outside the configured Project Projection root",
            path=value,
        ) from error
    if destination.suffix != ".json":
        raise EntityGraphError("output-destination-invalid", "Projection output must use a .json Carrier", path=value)
    probe = destination
    while probe != repository:
        if probe.exists() and probe.is_symlink():
            raise EntityGraphError("output-destination-symlink", "Output destination must not traverse a symlink", path=value)
        probe = probe.parent
    return destination


def _strict_error_result(graph_kind: object, error: EntityGraphError) -> dict[str, object]:
    key = "entities_graph" if graph_kind == "entities" else "terms_graph" if graph_kind == "terms" else None
    result: dict[str, object] = {
        "outcome": "failed",
        "source_frontier_evidence": {},
        "selection_evidence": {},
        "lineage": [],
        "quality_dispositions": {name: "unresolved" for name in ("coverage", "fidelity", "validity", "currentness", "permission", "persistence", "recording")},
        "diagnostics": [error.record()],
        "non_authoritative": True,
        "output_effects": {"state": "none", "paths": []},
        "run_receipt_refs": [],
    }
    if key is not None:
        result[key] = {}
    return result


def build_graph(repository: Path, request: Mapping[str, object]) -> dict[str, object]:
    """Build one source-sealed Entities or Terms Graph without source mutation.

    This is the public Tool/Action API for CA-O-134 and CA-O-137.  It accepts
    only the CA-D-539 request fields, returns the common Run-compatible result
    envelope, and leaves Journal persistence to the shared support owner.
    """

    graph_kind: object = request.get("graph_kind") if isinstance(request, Mapping) else None
    try:
        if not isinstance(request, Mapping):
            raise EntityGraphError("request-invalid", "Graph request must be an object")
        unknown = sorted(set(request) - STRICT_REQUEST_FIELDS)
        missing = sorted(STRICT_REQUIRED_REQUEST_FIELDS - set(request))
        if unknown or missing:
            raise EntityGraphError("request-schema-invalid", "Graph request fields are not exact", unknown=unknown, missing=missing)
        graph_kind = request["graph_kind"]
        if graph_kind not in GRAPH_KINDS:
            raise EntityGraphError("graph-kind-invalid", "graph_kind must be entities or terms", graph_kind=graph_kind)
        repository = repository.resolve()
        frontier = _mapping(request["source_frontier"], "source_frontier")
        selection = _mapping(request["selection"], "selection")
        configuration = _mapping(request["representation_configuration"], "representation_configuration")
        permission = _mapping(request["capability_permission_evidence"], "capability_permission_evidence")
        recording = request["run_recording_context"]
        display_selection = request.get("display_selection")
        if display_selection is not None:
            display_selection = dict(_mapping(display_selection, "display_selection"))
        if set(permission) != {"authorized"} or not isinstance(permission["authorized"], bool):
            raise EntityGraphError("permission-evidence-invalid", "Permission evidence must contain only authorized:boolean")
        if not isinstance(recording, ActualRunRecordingContext):
            raise EntityGraphError(
                "recording-context-untrusted",
                "Graph publication requires the actual selected Action start recording context.",
            )
        folder, actual_frontier, frontier_diagnostics = _validate_frontier(repository, frontier)
        if frontier_diagnostics:
            result = _strict_error_result(graph_kind, EntityGraphError("source-frontier-stale", "Admitted source frontier is stale"))
            result["outcome"] = "stale"
            result["source_frontier_evidence"] = actual_frontier
            result["diagnostics"] = frontier_diagnostics
            result["output_effects"] = {"state": "none", "paths": []}
            return result
        carriers, discovery_diagnostics = discover_atoms(repository, folder)
        selected_carriers, scope_unit_names = _selected_carriers(carriers, selection)
        # Validate every serializable source Property before constructing either
        # graph representation.  Terms Graph does not currently expose these
        # values, but a shared fail-closed boundary prevents future drift.
        for carrier in selected_carriers:
            _frontmatter_properties(carrier)
        relations: list[SubjectRelation] = []
        diagnostics: list[dict[str, object]] = list(discovery_diagnostics)
        for carrier in selected_carriers:
            parsed, carrier_diagnostics = parse_subject_relations(carrier)
            relations.extend(parsed)
            diagnostics.extend(carrier_diagnostics)
        relations.sort(key=_relation_sort_key)
        structure_rows, structure_diagnostics = _selected_structure(repository, frontier, scope_unit_names)
        diagnostics.extend(structure_diagnostics)
        graph_payload: dict[str, object]
        if graph_kind == "entities":
            typed_edges = term_system_edges(selected_carriers, relations)
            governed_by_subject: dict[str, list[SubjectRelation]] = defaultdict(list)
            for relation in relations:
                if relation.kind == "GOVERNS":
                    governed_by_subject[relation.subject_path].append(relation)
            property_nodes: list[dict[str, object]] = []
            for carrier in selected_carriers:
                governed = [
                    relation.subject_path
                    for relation in relations
                    if relation.atom_id == carrier.atom_id
                    and relation.carrier_path == carrier.carrier_path
                    and relation.kind == "GOVERNS"
                ]
                for key, value in _frontmatter_properties(carrier).items():
                    property_nodes.append(
                        {
                            "identity": f"{carrier.atom_id}#{key}",
                            "entity_identities": governed,
                            "name": key,
                            "value": value,
                            "source": carrier.evidence(),
                        }
                    )
            graph_payload = {
                "entities": [
                    {
                        "identity": subject_path,
                        "governing_sources": [relation.evidence() for relation in governed_by_subject[subject_path]],
                    }
                    for subject_path in sorted(governed_by_subject)
                ],
                "properties": sorted(property_nodes, key=lambda row: str(row["identity"])),
                "relations": [
                    {
                        "identity": f"{relation.atom_id}:{relation.kind}:{relation.subject_path}",
                        "relation": relation.kind,
                        "source_atom_id": relation.atom_id,
                        "target_entity": relation.subject_path,
                        "temporal_form": relation.temporal_form,
                        "source_lineage": _edge_evidence(relation),
                    }
                    for relation in relations
                ],
                "structural_relations": [
                    {
                        "relation": edge["relation"],
                        "source": edge["source_subject"],
                        "target": edge["target_subject"],
                        "source_term": edge["source_term"],
                        "target_term": edge["target_term"],
                        "evidence": edge["evidence"],
                    }
                    for edge in typed_edges
                    if edge["relation"] in {"IS_BORNE_BY", "IS_ALLOWED_VALUE_OF"}
                ],
                "source_atoms": [
                    {
                        "atom_id": carrier.atom_id,
                        "properties": _frontmatter_properties(carrier),
                        "claim": {"sha256": hashlib.sha256(carrier.body.encode("utf-8")).hexdigest()},
                        "source": carrier.evidence(),
                    }
                    for carrier in selected_carriers
                ],
                "project_structure": structure_rows,
                "external_references": [],
            }
        else:
            _, _, declared, _, depended = dependency_edges(selected_carriers, relations)
            terms = sorted(declared)
            terms_set = set(terms)
            conflicts = {term: rows for term, rows in declared.items() if len(rows) != 1}
            for term, rows in sorted(conflicts.items()):
                diagnostics.append(
                    {
                        "severity": "error",
                        "code": "governed-term-definition-conflict",
                        "message": "A selected Term has conflicting defining Atom evidence.",
                        "details": {"term": term, "definitions": [row.evidence() for row in rows]},
                    }
                )
            typed_edges = term_system_edges(selected_carriers, relations)
            term_edges = [
                {
                    "relation": edge["relation"],
                    "source": edge["source_term"],
                    "target": edge["target_term"],
                    "source_subject": edge["source_subject"],
                    "target_subject": edge["target_subject"],
                    "evidence": edge["evidence"],
                }
                for edge in typed_edges
                if str(edge["source_term"]) in terms_set and str(edge["target_term"]) in terms_set
                and edge["relation"] == "SUBKIND_OF"
            ]
            external_edges = [
                edge
                for edge in typed_edges
                if edge["relation"] == "SUBKIND_OF"
                and (str(edge["source_term"]) not in terms_set or str(edge["target_term"]) not in terms_set)
            ]
            parent_sets: dict[str, list[str]] = {term: [] for term in terms}
            for edge in term_edges:
                if edge["relation"] == "SUBKIND_OF":
                    parent_sets[str(edge["source"])].append(str(edge["target"]))
            parent_sets = {term: sorted(set(values)) for term, values in sorted(parent_sets.items())}
            ancestors, parent_cycles = _ancestor_sets(parent_sets)
            dependencies, dependency_evidence, dependency_cycles_found = _term_dependencies(relations, terms_set)
            unresolved = sorted(
                subject_path
                for subject_path in depended
                if terminal_term(subject_path) not in terms_set
            )
            for subject_path in unresolved:
                diagnostics.append(
                    {
                        "severity": "warning",
                        "code": "term-unresolved",
                        "message": "A selected dependency names no governed Term in the selected frontier.",
                        "details": {"subject_path": subject_path},
                    }
                )
            for cycle in parent_cycles + dependency_cycles_found:
                diagnostics.append(
                    {
                        "severity": "error",
                        "code": "self-reference" if len(cycle) == 1 else "dependency-cycle",
                        "message": "Selected Term relation data contains a cycle.",
                        "details": {"cycle": cycle},
                    }
                )
            graph_payload = {
                "terms": [
                    {
                        "identity": term,
                        "defining_sources": [
                            {"subject_path": row.subject_path, "source": row.evidence()}
                            for row in declared[term]
                        ],
                    }
                    for term in terms
                ],
                "relations": sorted(term_edges + dependency_evidence, key=lambda row: (str(row["relation"]), str(row["source"]), str(row["target"]))),
                "parents_by_term": parent_sets,
                "ancestors_by_term": ancestors,
                "dependencies_by_term": dependencies,
                "unresolved_terms": unresolved,
                "cycles": sorted(parent_cycles + dependency_cycles_found, key=lambda cycle: tuple(cycle)),
                "external_references": external_edges,
            }
        diagnostics.sort(key=lambda row: (str(row.get("severity", "")), str(row.get("code", "")), canonical_json(row.get("details", {}))))
        final_frontier = source_frontier_for(repository, folder)
        current = canonical_json(final_frontier) == canonical_json(frontier)
        authorized = bool(permission["authorized"])
        # The shared session has already durably recorded this Action's start.
        # Its terminal fact necessarily follows effect publication and remains
        # the executor's responsibility, avoiding a circular pre-effect gate.
        recording_confirmed = True
        destination: Path
        persistence_valid = True
        if "output_destination" in request:
            destination = _publication_path(repository, request["output_destination"])
        else:
            assert isinstance(graph_kind, str)
            destination = _default_publication_path(repository, graph_kind)
        quality = _quality(
            diagnostics=diagnostics,
            current=current,
            authorized=authorized,
            recording_confirmed=recording_confirmed,
            persistence_valid=persistence_valid,
        )
        outcome = _outcome_for(quality, diagnostics)
        graph_key = "entities_graph" if graph_kind == "entities" else "terms_graph"
        selection_evidence = {"selection": dict(selection)}
        if display_selection is not None:
            selection_evidence["display_selection"] = display_selection
        settings_digest = hashlib.sha256(
            canonical_json(
                {
                    "graph_kind": graph_kind,
                    "selection_evidence": selection_evidence,
                    "representation_configuration": dict(configuration),
                }
            ).encode("utf-8")
        ).hexdigest()
        result: dict[str, object] = {
            "outcome": outcome,
            graph_key: graph_payload,
            "source_frontier_evidence": final_frontier,
            "selection_evidence": selection_evidence,
            "representation_configuration": dict(configuration),
            "settings_sha256": settings_digest,
            "lineage": [carrier.evidence() for carrier in selected_carriers],
            "quality_dispositions": quality,
            "diagnostics": diagnostics,
            "non_authoritative": True,
            "output_effects": {"state": "none", "paths": []},
            "run_receipt_refs": [str(recording.start_event_receipt["event_id"])],
        }
        if outcome != "built":
            return result
        publication = {
            "schema_version": SCHEMA_VERSION,
            "tool": TOOL_ID,
            "graph_kind": graph_kind,
            graph_key: graph_payload,
            "source_frontier_evidence": final_frontier,
            "selection_evidence": selection_evidence,
            "representation_configuration": dict(configuration),
            "settings_sha256": settings_digest,
            "lineage": result["lineage"],
            "quality_dispositions": quality,
            "diagnostics": diagnostics,
            "non_authoritative": True,
        }
        rendered = canonical_json(publication, pretty=True)
        requested_existing = request.get("existing_projection_evidence")
        if requested_existing is not None:
            existing = _mapping(requested_existing, "existing_projection_evidence")
            expected_digest = existing.get("sha256")
            if not isinstance(expected_digest, str) or not destination.is_file() or _sha256(destination) != expected_digest:
                result["outcome"] = "stale"
                result["quality_dispositions"] = {**quality, "currentness": "fail"}
                result["diagnostics"] = diagnostics + [
                    {
                        "severity": "error",
                        "code": "existing-projection-stale",
                        "message": "Existing Projection evidence does not match the explicit destination.",
                        "details": {"path": _display_path(destination, repository)},
                    }
                ]
                return result
        publication_frontier = source_frontier_for(repository, folder)
        if canonical_json(publication_frontier) != canonical_json(frontier):
            result["outcome"] = "stale"
            result["source_frontier_evidence"] = publication_frontier
            result["quality_dispositions"] = {**quality, "currentness": "fail"}
            result["diagnostics"] = diagnostics + [
                {
                    "severity": "error",
                    "code": "source-frontier-changed-before-publication",
                    "message": "Source bytes changed after construction and before publication.",
                    "details": {"actual": publication_frontier},
                }
            ]
            return result
        if destination.is_file() and destination.read_text(encoding="utf-8") == rendered:
            result["outcome"] = "no_op"
            result["output_effects"] = {"state": "unchanged", "paths": []}
            result["projection_revision"] = _sha256(destination)
            return result
        atomic_write(destination, rendered)
        result["output_effects"] = {
            "state": "created" if not requested_existing else "replaced",
            "paths": [_display_path(destination, repository)],
        }
        result["projection_revision"] = _sha256(destination)
        return result
    except EntityGraphError as error:
        return _strict_error_result(graph_kind, error)


def construct_entities_graph_projection(repository: Path, request: Mapping[str, object]) -> dict[str, object]:
    """CA-O-134 Action adapter for the source graph executor."""

    if request.get("graph_kind", "entities") != "entities":
        return _strict_error_result(
            request.get("graph_kind"),
            EntityGraphError("graph-kind-action-mismatch", "CA-O-134 accepts only an entities graph request"),
        )
    bound = dict(request)
    bound["graph_kind"] = "entities"
    return build_graph(repository, bound)


def construct_terms_graph_projection(repository: Path, request: Mapping[str, object]) -> dict[str, object]:
    """CA-O-137 Action adapter for the source graph executor."""

    if request.get("graph_kind", "terms") != "terms":
        return _strict_error_result(
            request.get("graph_kind"),
            EntityGraphError("graph-kind-action-mismatch", "CA-O-137 accepts only a terms graph request"),
        )
    bound = dict(request)
    bound["graph_kind"] = "terms"
    return build_graph(repository, bound)


ACTION_HANDLERS = {
    "CA-O-134": construct_entities_graph_projection,
    "CA-O-137": construct_terms_graph_projection,
}


def queue_action_handlers(repository: Path) -> dict[str, object]:
    """Return CA-O-134/O-137 adapters in the selected queue's context contract.

    `SelectedExecution` passes one frozen context and requires `result` plus
    optional effect references.  The caller supplies the already-admitted strict
    graph request as `context.parameters`; this adapter never invents a receipt,
    transition, or retry.
    """

    def adapt(action_id: str, graph_kind: str, context: Mapping[str, object]) -> dict[str, object]:
        parameters = context.get("parameters")
        if not isinstance(parameters, Mapping):
            return {
                "result": "blocked",
                "effect_refs": [],
                "graph_result": _strict_error_result(
                    graph_kind,
                    EntityGraphError("queue-parameters-invalid", "Selected queue context lacks a graph request"),
                ),
            }
        request = dict(parameters.get("graph_request", parameters))
        if request.get("graph_kind", graph_kind) != graph_kind:
            result = _strict_error_result(
                request.get("graph_kind"),
                EntityGraphError("graph-kind-action-mismatch", f"{action_id} received the wrong graph kind"),
            )
        else:
            request["graph_kind"] = graph_kind
            result = build_graph(repository, request)
        effects = result.get("output_effects")
        paths = effects.get("paths", []) if isinstance(effects, Mapping) else []
        return {
            "result": result["outcome"],
            "effect_refs": list(paths) if isinstance(paths, list) else [],
            "graph_result": result,
        }

    return {
        "CA-O-134": lambda context: adapt("CA-O-134", "entities", context),
        "CA-O-137": lambda context: adapt("CA-O-137", "terms", context),
    }


def run(repository: Path, request: Mapping[str, object]) -> dict[str, object]:
    """Queue-facing alias; the caller owns workflow continuation and Journal I/O."""

    return build_graph(repository, request)


def _walk_declared_tree(nodes: Sequence[Mapping[str, object]], depth: int = 0) -> Iterable[str]:
    for node in nodes:
        marker = f" [Term: {node['declared_term']}]" if node["declared"] else ""
        relation = "" if node["relation_from_parent"] is None else f" ({node['relation_from_parent']})"
        yield f"{'  ' * depth}- {node['segment']}{relation}{marker}"
        children = node["children"]
        assert isinstance(children, Sequence)
        yield from _walk_declared_tree(children, depth + 1)


def _walk_dependency_tree(node: Mapping[str, object], depth: int = 0) -> Iterable[str]:
    suffix = " [cycle]" if node.get("cycle") else ""
    kind = " [Term]" if node["is_declared_term"] else " [Subject]"
    yield f"{'  ' * depth}- {node['subject']}{kind}{suffix}"
    parents = node["parents"]
    assert isinstance(parents, Sequence)
    for parent in parents:
        assert isinstance(parent, Mapping)
        yield from _walk_dependency_tree(parent, depth + 1)


def markdown_projection(projection: Mapping[str, object]) -> str:
    source = projection["source"]
    counts = projection["counts"]
    sets = projection["sets"]
    assert isinstance(source, Mapping) and isinstance(counts, Mapping) and isinstance(sets, Mapping)
    lines = [
        "# Entity Graph",
        "",
        "this is a non-authoritative, on-demand Projection from Atom Claim-Subject relations.",
        "",
        f"- selected folder: `{source['selected_folder']}`",
        f"- source Atoms: `{source['atom_count']}`",
        f"- source frontier: `{source['source_frontier_sha256']}`",
        f"- declared Terms: `{counts['declared_terms']}`",
        f"- governed Subjects: `{counts['governed_subjects']}`",
        f"- DEPENDS_ON Subjects: `{counts['depends_on_subjects']}`",
        f"- declared Terms in DEPENDS_ON: `{counts['terms_in_depends_on']}`",
        f"- DEPENDS_ON without GOVERNS: `{counts['depends_on_without_governs']}`",
        f"- dependency cycles: `{counts['dependency_cycles']}`",
        f"- Definition conflicts: `{counts['definition_conflicts']}`",
        f"- Term-System edges: `{counts['term_system_edges']}`",
        f"- Term-System violations: `{counts['term_system_violations']}`",
        f"- Root Terms: `{counts['root_terms']}`",
        "",
        "## Set 1 — Declared Term Tree",
        "",
    ]
    declared_tree = sets["declared_term_tree"]
    assert isinstance(declared_tree, Sequence)
    lines.extend(_walk_declared_tree(declared_tree))
    lines.extend(["", "## Set 2 — DEPENDS_ON Parent Trees", ""])
    dependency_trees = sets["dependency_trees_by_declared_term"]
    assert isinstance(dependency_trees, Sequence)
    for tree in dependency_trees:
        assert isinstance(tree, Mapping)
        lines.extend(_walk_dependency_tree(tree))
        lines.append("")
    lines.extend(["## Set 3 — Terms in DEPENDS_ON", ""])
    terms_in_depends_on = sets["terms_in_depends_on"]
    assert isinstance(terms_in_depends_on, Sequence)
    lines.extend(f"- {term}" for term in terms_in_depends_on)
    lines.extend(["", "## All DEPENDS_ON Subject Expressions", ""])
    depends_on_subjects = sets["depends_on_subjects"]
    assert isinstance(depends_on_subjects, Sequence)
    lines.extend(f"- {subject}" for subject in depends_on_subjects)
    gaps = projection["depends_on_without_governs"]
    assert isinstance(gaps, Sequence)
    lines.extend(["", "## Gaps — DEPENDS_ON without GOVERNS", ""])
    lines.extend(f"- {term}" for term in gaps)
    cycles = projection["dependency_cycles"]
    assert isinstance(cycles, Sequence)
    lines.extend(["", "## Dependency Cycles", ""])
    if cycles:
        lines.extend(f"- {' → '.join(cycle)} → {cycle[0]}" for cycle in cycles)
    else:
        lines.append("- none")
    conflicts = projection["definition_conflicts"]
    assert isinstance(conflicts, Sequence)
    lines.extend(["", "## Definition Conflicts", ""])
    if conflicts:
        for conflict in conflicts:
            assert isinstance(conflict, Mapping)
            lines.append(f"- {conflict['term']}: {len(conflict['definitions'])} Definition Atoms")
    else:
        lines.append("- none")
    term_system = projection["term_system"]
    assert isinstance(term_system, Mapping)
    lines.extend(["", "## Typed Term-System Relations", ""])
    typed_edges = term_system["edges"]
    assert isinstance(typed_edges, Sequence)
    if typed_edges:
        lines.extend(
            f"- {edge['source_subject']} —{edge['relation']}→ {edge['target_subject']}"
            for edge in typed_edges
            if isinstance(edge, Mapping)
        )
    else:
        lines.append("- none")
    lines.extend(["", "## Root Terms", ""])
    root_terms = term_system["root_terms"]
    assert isinstance(root_terms, Sequence)
    lines.extend(f"- {term}" for term in root_terms)
    lines.extend(["", "## Term-System Violations", ""])
    violations = term_system["violations"]
    assert isinstance(violations, Sequence)
    if violations:
        lines.extend(f"- {violation['code']}: `{canonical_json(violation).strip()}`" for violation in violations)
    else:
        lines.append("- none")
    return "\n".join(lines) + "\n"


def envelope(
    *, projection: Mapping[str, object] | None = None, error: EntityGraphError | None = None
) -> dict[str, object]:
    return {
        "schema_version": SCHEMA_VERSION,
        "tool": {"capability_id": TOOL_ID, "kind": TOOL_KIND},
        "ok": error is None,
        "mode": "read",
        "diagnostics": [] if error is None else [error.record()],
        "result": {"projection": dict(projection)} if projection is not None else {},
    }


def atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = atomic_tempfile(path, "generate_entity_graph")
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as stream:
            stream.write(content)
        os.replace(temporary, path)
    finally:
        try:
            temporary.unlink()
        except FileNotFoundError:
            pass


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(prog="generate-entity-graph")
    result.add_argument("folder", type=Path, help="Folder whose active Markdown Atoms are the source set")
    result.add_argument("--repository", type=Path, default=Path.cwd(), help="Project repository root")
    result.add_argument("--format", choices=("json", "markdown"), default="json")
    result.add_argument("--output", type=Path, help="Optional Projection Carrier; stdout is the default")
    result.add_argument("--compact", action="store_true", help="Emit compact JSON")
    return result


def main(argv: Sequence[str] | None = None) -> int:
    arguments = parser().parse_args(argv)
    repository = arguments.repository.resolve()
    folder = arguments.folder if arguments.folder.is_absolute() else repository / arguments.folder
    try:
        projection = generate_projection(repository, folder)
        content = (
            markdown_projection(projection)
            if arguments.format == "markdown"
            else canonical_json(envelope(projection=projection), pretty=not arguments.compact)
        )
        if arguments.output:
            output = arguments.output if arguments.output.is_absolute() else repository / arguments.output
            atomic_write(output, content)
        else:
            sys.stdout.write(content)
        return 0
    except EntityGraphError as error:
        sys.stdout.write(canonical_json(envelope(error=error), pretty=not arguments.compact))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
