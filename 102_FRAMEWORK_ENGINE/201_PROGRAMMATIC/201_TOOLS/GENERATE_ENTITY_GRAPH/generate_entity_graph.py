#!/usr/bin/env python3
"""Build an on-demand Entity Graph from Atom Subjects in any selected folder."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
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
SCHEMA_VERSION = 5
INACTIVE_DIRECTORY_NAMES = {"archive", "drafts", "done", "canceled", "cancelled", "solved", "handled"}
CANONICAL_SUBJECT_KINDS = {"governs": "GOVERNS", "depends_on": "DEPENDS_ON"}
LEGACY_SUBJECT_KINDS = {"declared": "GOVERNS", "prerequisite": "DEPENDS_ON"}
TEMPORAL_FORMS = {"continuant": "CONTINUANT", "occurrent": "OCCURRENT"}


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
class AtomCarrier:
    atom_id: str
    version: int
    cce_form: str
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


def _is_excluded(path: Path, selected_folder: Path) -> bool:
    relative_parts = path.relative_to(selected_folder).parts[:-1]
    return any(part.lower() in INACTIVE_DIRECTORY_NAMES for part in relative_parts)


def discover_atoms(repository: Path, selected_folder: Path) -> tuple[list[AtomCarrier], list[dict[str, object]]]:
    carriers: list[AtomCarrier] = []
    diagnostics: list[dict[str, object]] = []
    for path in sorted(selected_folder.rglob("*.md")):
        if _is_excluded(path, selected_folder):
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
    for line in block:
        kind_match = re.fullmatch(r"  ([a-z_]+):\s*", line)
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
            continue
        form_match = re.fullmatch(r"    ([a-z_]+):\s*(?:\[\])?\s*", line)
        if form_match:
            current_form = form_match.group(1)
            if current_form not in TEMPORAL_FORMS:
                raise EntityGraphError(
                    "subject-temporal-form-invalid",
                    "Atom Carrier has an unknown Subject Temporal Form",
                    path=carrier.carrier_path,
                    temporal_form=current_form,
                )
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
        subject_path = scalar_value(item_match.group(1))
        if not subject_path:
            raise EntityGraphError("subject-path-empty", "Subject Path must not be empty", path=carrier.carrier_path)
        effective_kind = CANONICAL_SUBJECT_KINDS.get(current_kind) or LEGACY_SUBJECT_KINDS[current_kind]
        relations.append(
            SubjectRelation(
                atom_id=carrier.atom_id,
                atom_revision=carrier.version,
                carrier_path=carrier.carrier_path,
                carrier_sha256=carrier.sha256,
                subject_path=subject_path,
                kind=effective_kind,
                temporal_form=TEMPORAL_FORMS[current_form],
                source_schema_key=current_kind,
                cce_form=carrier.cce_form,
            )
        )
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


def dependency_edges(
    relations: Sequence[SubjectRelation],
) -> tuple[
    dict[str, set[str]],
    dict[tuple[str, str], list[dict[str, object]]],
    dict[str, list[SubjectRelation]],
    dict[str, list[SubjectRelation]],
    dict[str, list[SubjectRelation]],
]:
    by_atom: dict[tuple[str, str], list[SubjectRelation]] = defaultdict(list)
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
        for row in governs:
            governed_subjects[row.subject_path].append(row)
            if row.cce_form == "definition":
                declared_terms[terminal_term(row.subject_path)].append(row)
        for row in depends_on:
            depended[row.subject_path].append(row)
        definition_rows_by_atom[atom_key] = [row for row in governs if row.cce_form == "definition"]
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
    graph, edge_evidence, declared, governed, depended = dependency_edges(relations)
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
