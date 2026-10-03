"""Read-only reference and Plan graph checks with exact source-bound rules.

The supplied reference frontier is an execution input, not a new source of rules.
Unknown relation kinds and missing reference evidence remain coverage gaps.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
from functools import lru_cache
from pathlib import Path
from typing import cast

from .authority import Record, diagnostic
from .check_support import Check, _plan, _string, _strings
from .read_io import ReadContext


@lru_cache(maxsize=1)
def _manifest() -> Record:
    return cast(
        Record, json.loads(Path(__file__).with_name("graph_authority.json").read_text())["sources"]
    )


def _inputs(check: Check) -> Record:
    return getattr(check, "inputs", {}) or {}


def _checkpoint(check: Check) -> None:
    reader = _inputs(check).get("reader")
    if isinstance(reader, ReadContext):
        reader.checkpoint()


def _emit(check: Check, code: str, field: str, reason: str, *, gap: bool = False) -> None:
    bindings = list(check.obligation.authority)
    for binding in getattr(check, "_graph_bindings", []):
        if binding not in bindings:
            bindings.append(binding)
    item = diagnostic(code, reason, bindings, field)
    (check.gaps if gap else check.findings).append(item)


def _gap(check: Check, field: str, reason: str) -> None:
    _emit(check, "AUTHORITY_UNSUPPORTED", field, reason, gap=True)


def _fail(check: Check, field: str, reason: str) -> None:
    _emit(check, "RELATION_INVALID", field, reason)


def _pins(check: Check, *atom_ids: str) -> bool:
    """Never execute a reviewed rule against absent, changed or duplicate authority."""
    sources = _inputs(check).get("sources", [])
    checked = getattr(check, "_graph_pins", {})
    setattr(check, "_graph_pins", checked)
    okay = True
    for atom_id in atom_ids:
        _checkpoint(check)
        if atom_id in checked:
            okay = checked[atom_id] and okay
            continue
        entries = [s for s in sources if s.get("binding", {}).get("atom_id") == atom_id]
        pin = _manifest()[atom_id]
        valid = len(entries) == 1
        if valid:
            source = entries[0]
            binding = source["binding"]
            valid = (
                binding.get("version") == pin["version"]
                and binding.get("sha256") == pin["sha256"]
                and isinstance(source.get("text"), str)
                and hashlib.sha256(source["text"].encode()).hexdigest() == pin["sha256"]
            )
        if not valid:
            _gap(
                check,
                check.obligation.code,
                "Required graph authority is absent, changed, or ambiguous: " + atom_id + ".",
            )
            okay = False
        else:
            bindings = getattr(check, "_graph_bindings", [])
            if entries[0]["binding"] not in bindings:
                bindings.append(entries[0]["binding"])
            setattr(check, "_graph_bindings", bindings)
        checked[atom_id] = bool(valid)
    return okay


def _records(check: Check, metadata: Record | None = None) -> list[Record]:
    """Deduplicate the same read locator, never choose the latest Revision by ID."""
    records: dict[str, Record] = {}
    for ref in _inputs(check).get("references", []):
        _checkpoint(check)
        if isinstance(ref.get("metadata"), dict):
            records.setdefault(str(ref.get("path", id(ref))), ref)
    for source in _inputs(check).get("sources", []):
        _checkpoint(check)
        binding = source.get("binding", {})
        if isinstance(source.get("metadata"), dict) and binding.get("path"):
            record = dict(source)
            record["path"] = Path(binding["path"])
            # An explicit, admitted source binding supplies source identity; a
            # filename never supplies a missing target property.
            record["metadata"] = dict(source["metadata"])
            record["metadata"].setdefault("atom_id", binding.get("atom_id"))
            record["metadata"].setdefault("version", binding.get("version"))
            records.setdefault(str(record["path"]), record)
    if metadata is not None and _string(metadata.get("atom_id")):
        path = _inputs(check).get("path")
        records[str(path)] = {"path": path, "metadata": metadata}
    return list(records.values())


def _index(records: list[Record]) -> dict[str, list[Record]]:
    index: dict[str, list[Record]] = {}
    for record in records:
        atom_id = record["metadata"].get("atom_id")
        if _string(atom_id):
            index.setdefault(atom_id, []).append(record)
    return index


def _reference_text(record: Record) -> str | None:
    parsed = record.get("parsed")
    return getattr(parsed, "text", None) if parsed is not None else record.get("text")


def _representations(check: Check, matches: list[Record], field: str) -> list[Record] | None:
    """Coalesce only source-bound copies whose already-read bytes prove fidelity."""
    by_path = {os.path.abspath(str(item.get("path"))): item for item in matches}
    retained = []
    for record in matches:
        _checkpoint(check)
        projection = record["metadata"].get("projection")
        if projection is None:
            retained.append(record)
            continue
        if not _pins(check, "CA-D-305"):
            return None
        if (
            not isinstance(projection, dict)
            or set(projection) != {"source_carrier_path"}
            or not _string(projection.get("source_carrier_path"))
        ):
            _gap(check, field, "Projected target has an invalid source binding.")
            return None
        source_path = os.path.abspath(
            str(Path(record["path"]).parent / projection["source_carrier_path"])
        )
        original = by_path.get(source_path)
        text = _reference_text(record)
        original_text = _reference_text(original) if original else None
        if original is None or not isinstance(text, str) or not isinstance(original_text, str):
            _gap(
                check,
                field,
                "Projected target fidelity requires the already-read original source bytes.",
            )
            return None
        opening = re.match(r"---\r?\n", text)
        closing = re.search(r"(?m)^---\r?\n", text[opening.end() :]) if opening else None
        frontmatter = (
            text[opening.end() : opening.end() + closing.start()] if closing and opening else ""
        )
        block = re.search(r"(?m)^projection:[ \t]*\r?\n(?:[ \t]+[^\r\n]*\r?\n)+", frontmatter)
        if block is None or opening is None:
            _gap(check, field, "Projected target source block cannot be compared faithfully.")
            return None
        unbound = text[: opening.end() + block.start()] + text[opening.end() + block.end() :]
        if unbound != original_text or original["metadata"].get("projection") is not None:
            _gap(
                check,
                field,
                "Projected target does not faithfully represent its original source Revision.",
            )
            return None
    return retained


def _resolve(
    check: Check,
    target: str,
    index: dict[str, list[Record]],
    field: str,
    *,
    active_rmed: bool = False,
) -> Record | None:
    if not _inputs(check).get("reference_complete", False):
        _gap(
            check,
            field,
            "Reference inventory is incomplete; uniqueness cannot be established: " + target + ".",
        )
        return None
    matches = index.get(target, [])
    if active_rmed and len(matches) > 1:
        if not _pins(check, "CA-R-1676"):
            return None
        eligible = [
            item
            for item in matches
            if item["metadata"].get("content_role") not in _RMED
            or item["metadata"].get("status") == "Active"
            or not _string(item["metadata"].get("status"))
        ]
        # The admission rule can disambiguate an applicable Active authority.
        # If none qualifies, retain observed invalid targets for diagnostics.
        if eligible:
            matches = eligible
    canonical = _representations(check, matches, field)
    if canonical is None:
        return None
    if len(canonical) != 1:
        reason = "Missing" if not canonical else "Ambiguous"
        _gap(
            check,
            field,
            reason + " canonical target reference in the bounded context: " + target + ".",
        )
        return None
    resolved = cast(Record, canonical[0]["metadata"])
    version = resolved.get("version")
    if type(version) is not int or version < 1:
        _gap(check, field, "Resolved reference lacks a valid carried Revision: " + target + ".")
        return None
    return resolved


def _relations(metadata: Record, check: Check) -> dict[str, list[str]] | None:
    relations = metadata.get("relations", {})
    if not isinstance(relations, dict):
        _fail(check, "relations", "Relations must be a mapping.")
        return None
    valid: dict[str, list[str]] = {}
    for kind, targets in relations.items():
        _checkpoint(check)
        if not _string(kind) or not _strings(targets) or not targets:
            _fail(
                check, "relations", "Each direct relation requires unique nonempty scalar targets."
            )
        else:
            valid[kind] = targets
            if len(targets) > 1:
                # CA-D-268 requires canonical order but does not select Python's
                # lexical comparator. Neither sorted nor unsorted input proves
                # conformance until a source-bound ordering adapter is admitted.
                _gap(
                    check,
                    "relations." + kind,
                    "Canonical ordering needs a source-bound comparator; lexical sorting "
                    "is not established by the admitted authority. Endpoint and uniqueness "
                    "checks are evaluated independently.",
                )
    return valid


# Endpoint restrictions belong to these individual Relation Kind declarations.
# "one target" describes each direct fact, not the number of distinct facts an
# Atom can author in the serialized relation collection.
_TYPED = {
    "method_for": ("CA-R-1017", "Method", {"Requirement"}),
    "rationale_for": ("CA-R-1016", "Analysis", {"Requirement", "Method", "Evaluation", "Delivery"}),
    "evaluation_for": (
        "CA-R-1018",
        "Evaluation",
        {"Requirement", "Method", "Evaluation", "Delivery", "Operations"},
    ),
    "delivery_for": ("CA-R-1019", "Delivery", {"Requirement", "Method"}),
    "evidence_for": ("CA-R-1021", None, {"Evaluation", "Implementation"}),
}
_INVERSES = {
    "parent_of": "CA-R-879",
    "required_by": "CA-R-1026",
    "implemented_by": "CA-R-1027",
    "decomposes_into": "CA-D-481",
}
_RMED = {"Requirement", "Method", "Evaluation", "Delivery"}


def _role(check: Check, metadata: Record, allowed: set[str], field: str, endpoint: str) -> bool:
    role = metadata.get("content_role")
    if not _string(role):
        _gap(check, field, "Resolved " + endpoint + " lacks its carried Content Role.")
        return False
    if role not in allowed:
        _fail(
            check,
            field,
            "Resolved " + endpoint + " has an inadmissible Content Role: " + str(role) + ".",
        )
        return False
    return True


def _rmed_status(check: Check, owner: Record, target: Record, field: str) -> None:
    if owner.get("content_role") not in _RMED or target.get("content_role") not in _RMED:
        return
    if not _pins(check, "CA-R-1676"):
        return
    if not _string(owner.get("status")) or not _string(target.get("status")):
        _gap(
            check,
            field,
            "RMED endpoint Status is missing; Active-authority applicability is unresolved.",
        )
    elif owner["status"] == "Active" and target["status"] != "Active":
        _fail(check, field, "An Active RMED Atom's RMED relation target must be Active.")


def _typed_rule(metadata: Record, kind: str, check: Check) -> tuple[bool, set[str] | None]:
    pin, owner_role, target_roles = _TYPED[kind]
    if not _pins(check, pin):
        return False, None
    field = "relations." + kind
    if owner_role:
        _role(check, metadata, {owner_role}, field, "owner")
    if kind == "rationale_for" and metadata.get("type") != "Rationale":
        _fail(check, field, "rationale_for must be owned by a Rationale Analysis Atom.")
    if kind == "evidence_for":
        _gap(
            check,
            field,
            "Evidence carrier admission requires explicit supported carrier-class evidence.",
        )
    return True, target_roles


def _other_rule(metadata: Record, kind: str, check: Check) -> tuple[bool, None]:
    pins = {
        "depends_on": ("CA-R-1026",),
        "child_of": ("CA-R-879", "CA-R-796"),
        "implementation_of": ("CA-R-1020", "CA-R-1027"),
        "concern_about": ("CA-R-1022",),
    }
    field = "relations." + kind
    if kind not in pins:
        _gap(check, field, "No exact reviewed Relation Kind admission supports: " + kind + ".")
        return False, None
    if not _pins(check, *pins[kind]):
        return False, None
    if kind == "depends_on" and metadata.get("content_role") == "Plan":
        _fail(check, field, "Plan start dependencies must use blocks, not relations.depends_on.")
    if kind == "implementation_of":
        _role(check, metadata, {"Implementation"}, field, "owner")
        _gap(
            check,
            field,
            "Specification-Atom admission requires a supported specification-target binding.",
        )
    if kind == "concern_about":
        _role(check, metadata, {"Concern"}, field, "owner")
        _gap(
            check,
            field,
            "Affected governed-entity admission cannot be inferred from an Atom ID alone.",
        )
    return True, None


def _tier_parent(check: Check, metadata: Record, target: Record, field: str) -> None:
    owner_scope, target_scope = metadata.get("current_scope_unit"), target.get("current_scope_unit")
    if not _string(owner_scope) or not _string(target_scope):
        _gap(check, field, "Tier-parent scope comparison requires both carried Scope Units.")
    elif owner_scope != target_scope:
        _fail(check, field, "Tier-parent endpoints must share the same Atom Scope.")


def _relation(
    metadata: Record, kind: str, targets: list[str], check: Check, index: dict[str, list[Record]]
) -> None:
    field = "relations." + kind
    if kind in _INVERSES:
        if _pins(check, "CA-R-1040", _INVERSES[kind]):
            _fail(check, field, "An inverse-derived relation must not be authored independently.")
        return
    if kind in {"blocks", "is_decomposition_of"}:
        # Plan adapters check endpoints and graph properties independently.
        if _pins(check, "CA-D-471" if kind == "blocks" else "CA-D-481"):
            _role(check, metadata, {"Plan"}, field, "owner")
        return
    admitted, target_roles = (
        _typed_rule(metadata, kind, check) if kind in _TYPED else _other_rule(metadata, kind, check)
    )
    if not admitted:
        return
    for target_id in targets:
        _checkpoint(check)
        target = _resolve(
            check,
            target_id,
            index,
            field,
            active_rmed=metadata.get("content_role") in _RMED
            and metadata.get("status") == "Active",
        )
        if target is None:
            continue
        if target_roles is not None:
            _role(check, target, target_roles, field, "target " + target_id)
        if kind == "child_of":
            _tier_parent(check, metadata, target, field)
        _rmed_status(check, metadata, target, field)


def relations_resolution(metadata: Record, body: str, check: Check) -> None:
    del body
    if not _pins(check, "CA-D-268"):
        return
    relations = _relations(metadata, check)
    if relations is None:
        return
    index = _index(_records(check, metadata))
    if metadata.get("content_role") == "Evaluation" and metadata.get("local_tier") == "Standard":
        if _pins(check, "CA-R-1018") and not relations.get("evaluation_for"):
            _fail(
                check,
                "relations.evaluation_for",
                "A Standard Evaluation must declare at least one checked-authority target.",
            )
    for kind, targets in relations.items():
        _relation(metadata, kind, targets, check, index)


def _subject_targets(metadata: Record, check: Check) -> list[tuple[str, str]]:
    subjects = metadata.get("subjects")
    if not isinstance(subjects, dict):
        _fail(check, "subjects", "Subjects must carry a canonical governed Subject Path.")
        return []
    if isinstance(subjects.get("governs"), dict) or isinstance(subjects.get("depends_on"), dict):
        _gap(
            check,
            "subjects",
            "Legacy Subject targets require the separately assigned migration's identity evidence.",
        )
        return []
    targets: list[tuple[str, str]] = []
    if _string(subjects.get("governs")):
        targets.append(("subjects.governs", subjects["governs"]))
    else:
        _fail(check, "subjects.governs", "Exactly one scalar canonical Subject Path is required.")
    dependencies = subjects.get("depends_on", [])
    if not _strings(dependencies):
        _fail(
            check,
            "subjects.depends_on",
            "Subject dependencies must be unique scalar Subject Paths.",
        )
    else:
        targets.extend(("subjects.depends_on", path) for path in dependencies)
    return targets


def _subject_declarations(check: Check) -> dict[str, list[Record]]:
    # GOVERNS declarations identify the canonical Entity. A dependent mention, a
    # reusable terminal Term, or several governing Claims does not create another
    # Entity identity. Do not include this candidate merely to prove itself.
    declarations: dict[str, list[Record]] = {}
    for record in _records(check):
        _checkpoint(check)
        data = record["metadata"]
        governed = (
            data.get("subjects", {}).get("governs")
            if isinstance(data.get("subjects"), dict)
            else None
        )
        if _string(governed) and (data.get("status") == "Active" or record.get("binding")):
            declarations.setdefault(str(governed), []).append(record)
    return declarations


def _subject_revision(check: Check, matches: list[Record], field: str, target: str) -> None:
    canonical = _representations(check, matches, field)
    if canonical is None:
        return
    by_id: dict[str, set[tuple[str, str]]] = {}
    for record in canonical:
        _checkpoint(check)
        data = record["metadata"]
        identity = data.get("atom_id")
        if _string(identity):
            by_id.setdefault(str(identity), set()).add(
                (repr(data.get("version")), str(record.get("path")))
            )
    if any(len(revisions) > 1 for revisions in by_id.values()):
        _gap(
            check,
            field,
            "Governing source Revision is ambiguous for canonical Entity: " + target + ".",
        )


def subjects_resolution(metadata: Record, body: str, check: Check) -> None:
    del body
    if not _pins(
        check,
        "CA-D-269",
        "CA-R-1202",
        "CA-R-1194",
        "CA-R-1199",
        "CA-R-1247",
        "CA-R-1248",
        "CA-R-1456",
    ):
        return
    targets = _subject_targets(metadata, check)
    if not _inputs(check).get("reference_complete", False):
        _gap(check, "subjects", "The bounded governed-Entity reference inventory is incomplete.")
        return
    declarations = _subject_declarations(check)
    for field, target in targets:
        matches = declarations.get(target, [])
        if not matches:
            _gap(
                check,
                field,
                "Canonical Entity has no admitted governing declaration in the bounded context: "
                + target
                + ".",
            )
            continue
        _subject_revision(check, matches, field, target)


def subjects_migration(metadata: Record, body: str, check: Check) -> None:
    del body
    if not _pins(check, "CA-D-269"):
        return
    subjects = metadata.get("subjects")
    if not isinstance(subjects, dict):
        _fail(check, "subjects", "Subjects must be a mapping.")
        return
    legacy = [value for value in subjects.values() if isinstance(value, dict)]
    if legacy:
        _gap(
            check,
            "subjects",
            "Legacy temporal Subject encoding requires its explicitly assigned carrier-migration Task and execution evidence; neither is inferred from Status or invented metadata.",
        )
        for branch in legacy:
            if not branch or set(branch) - {"continuant", "occurrent"}:
                _fail(
                    check,
                    "subjects",
                    "Legacy Subject compatibility only admits continuant/occurrent branches.",
                )


def _plan_target(check: Check, target: Record, field: str, identity: str) -> bool:
    if not _role(check, target, {"Plan"}, field, "target " + identity):
        return False
    if target.get("type") != "Plan":
        _gap(
            check,
            field,
            "Plan endpoint Type requires its admitted Plan or subtype authority: " + identity + ".",
        )
        return False
    statuses = check.context.domains.get("domain.status.plan")
    if not statuses:
        _gap(check, field, "Plan endpoint Status requires the selected admitted Plan Status model.")
        return False
    if not _string(target.get("status")):
        _gap(check, field, "Resolved Plan endpoint lacks carried Status: " + identity + ".")
        return False
    if target["status"] not in statuses:
        _fail(check, field, "Plan endpoint has an inadmissible Status: " + target["status"] + ".")
        return False
    return True


def _plan_edges(
    check: Check, metadata: Record, index: dict[str, list[Record]], *, combined: bool
) -> dict[str, set[str]]:
    """Follow reachable prerequisites only; never manufacture a transitive fact."""
    identity = metadata.get("atom_id")
    if not isinstance(identity, str) or not identity.strip():
        _gap(
            check,
            "relations",
            "Plan graph resolution requires the selected Plan's carried identity.",
        )
        return {}
    pending = [identity]
    visited: set[str] = set()
    edges: dict[str, set[str]] = {}
    while pending:
        _checkpoint(check)
        current = pending.pop()
        if current in visited:
            continue
        visited.add(current)
        data = metadata if current == identity else _resolve(check, current, index, "relations")
        if data is None:
            continue
        relation_map = data.get("relations", {})
        if not isinstance(relation_map, dict):
            _gap(
                check,
                "relations",
                "Reachable Plan has malformed relation evidence: " + current + ".",
            )
            continue
        kinds = ("is_decomposition_of", "blocks") if combined else ("is_decomposition_of",)
        for kind in kinds:
            targets = relation_map.get(kind, [])
            if not _strings(targets):
                _gap(
                    check,
                    "relations." + kind,
                    "Reachable Plan relation targets are malformed: " + current + ".",
                )
                continue
            for target_id in targets:
                _checkpoint(check)
                target = (
                    metadata
                    if target_id == identity
                    else _resolve(check, target_id, index, "relations." + kind)
                )
                if target is None or not _plan_target(
                    check, target, "relations." + kind, target_id
                ):
                    continue
                # Both arrows express a completion prerequisite: child -> hub,
                # blocker -> blocked. Reverse the child edge and mixed cycles hide.
                edges.setdefault(current, set()).add(target_id)
                pending.append(target_id)
    return edges


def _cycle_from(check: Check, edges: dict[str, set[str]], identity: str) -> bool:
    active: set[str] = set()
    done: set[str] = set()
    stack: list[tuple[str, bool]] = [(identity, False)]
    while stack:
        _checkpoint(check)
        node, leaving = stack.pop()
        if leaving:
            active.discard(node)
            done.add(node)
        elif node in active:
            return True
        elif node not in done:
            active.add(node)
            stack.append((node, True))
            stack.extend((target, False) for target in sorted(edges.get(node, ()), reverse=True))
    return False


def _placement(check: Check, metadata: Record, records: list[Record]) -> None:
    path = _inputs(check).get("path")
    if path is None:
        _gap(
            check,
            "relations.is_decomposition_of",
            "Plan Carrier placement requires its admitted locator.",
        )
        return
    path = Path(path)
    parents = set(path.parents)
    candidates = []
    for record in records:
        _checkpoint(check)
        other = record.get("path")
        data = record["metadata"]
        if other is None or data.get("content_role") != "Plan" or data.get("type") != "Plan":
            continue
        other = Path(other)
        if other.suffix == ".md" and other.with_suffix("") in parents:
            if data.get("atom_id") != metadata.get("atom_id"):
                candidates.append((len(other.parts), data.get("atom_id")))
    if not candidates:
        return
    nearest = max(depth for depth, _ in candidates)
    owners = {identity for depth, identity in candidates if depth == nearest}
    if len(owners) != 1 or None in owners:
        _gap(
            check,
            "relations.is_decomposition_of",
            "Immediate enclosing Plan Carrier identity is ambiguous.",
        )
        return
    if metadata.get("relations", {}).get("is_decomposition_of", []) != [next(iter(owners))]:
        _fail(
            check,
            "relations.is_decomposition_of",
            "Plan placement inside another Plan's matching Directory Carrier must match its immediate declared decomposition target, across Status containers.",
        )


def _decomposition_placement(check: Check, metadata: Record, records: list[Record]) -> None:
    if not _inputs(check).get("reference_complete", False):
        _gap(
            check,
            "relations.is_decomposition_of",
            "Incomplete reference inventory cannot establish enclosing Plan Carrier placement.",
        )
    else:
        _placement(check, metadata, records)


def plan_resolution(metadata: Record, body: str, check: Check) -> None:
    del body
    if not _plan(metadata, check):
        return
    decomposition = check.obligation.code == "plan.decomposition_resolution"
    field = "relations.is_decomposition_of" if decomposition else "relations.blocks"
    required = (
        ("CA-D-481", "CA-R-1579", "CA-R-1538", "CA-D-460", "CA-D-475")
        if decomposition
        else ("CA-D-471", "CA-R-1580", "CA-R-1592", "CA-R-1579", "CA-D-481")
    )
    if not _pins(check, *required, "CA-R-1539", "CA-R-1593"):
        return
    relations = _relations(metadata, check)
    if relations is None:
        return
    kind = "is_decomposition_of" if decomposition else "blocks"
    targets = relations.get(kind, [])
    if decomposition and len(targets) > 1:
        _fail(check, field, "A Plan can have at most one direct decomposition target.")
    if decomposition and metadata.get("atom_id") in targets:
        _fail(
            check,
            field,
            "Decomposition endpoints must be distinct Plans; a same-bundle directory is not a self-edge.",
        )
    records = _records(check, metadata)
    index = _index(records)
    for target_id in targets:
        target = _resolve(check, target_id, index, field)
        if target is not None:
            _plan_target(check, target, field, target_id)
    edges = _plan_edges(check, metadata, index, combined=not decomposition)
    identity = metadata.get("atom_id")
    if isinstance(identity, str) and _cycle_from(check, edges, identity):
        _fail(
            check,
            field,
            "Plan "
            + ("decomposition" if decomposition else "combined completion-prerequisite")
            + " graph contains a cycle.",
        )
    if decomposition:
        _decomposition_placement(check, metadata, records)


ADAPTERS = {
    "relations.resolution": relations_resolution,
    "subjects.resolution": subjects_resolution,
    "subjects.migration": subjects_migration,
    "plan.blocking_resolution": plan_resolution,
    "plan.decomposition_resolution": plan_resolution,
}
