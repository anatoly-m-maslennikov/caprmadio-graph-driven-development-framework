"""Exact-source-bound checks of carrier schema, never semantic Claim validity.

``plan.model`` checks the common Plan's role/type and one nonempty Objective section.
It does not establish semantic atomicity, boundedness, or intended-work meaning.
Domain entries below are reviewed contributions, not closed universal Type sets.
Unsupported declarations remain gaps instead of guessed extension schemas.
"""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

import yaml
from yaml.nodes import MappingNode, ScalarNode

from .authority import Record, _verified
from .check_sections import _headings, _sections, role_sections, plan_definition
from .check_support import Check, _integer, _string


COMMON_FIELDS = frozenset(
    {
        "atom_id",
        "content_role",
        "type",
        "current_scope_unit",
        "claim_target_scope_unit",
        "local_tier",
        "global_tier",
        "version",
        "updated_at",
        "author",
        "status",
        "subjects",
        "relations",
    }
)
PLAN_FIELDS = {
    "assignee": ("CA-D-473", _string),
    "autonomous_confidence_threshold": ("CA-D-472", _integer),
    "implementation_retry_limit": ("CA-D-447", _integer),
}
BODY_FIELDS = {
    "summary": "Summary",
    "claim": "Claim",
    "details": "Details",
    "objective": "Objective",
    "question": "Question",
    "scope": "Scope",
    "approach": "Approach",
    "results": "Results",
    "tldr": "TLDR",
    "concern": "Concern",
    "evidences": "Evidences",
    "blast_radius": "Blast radius",
    "operation": "Operation",
}
PLAN_BODY_FIELDS = {"definition_of_done": "Definition of Done", "details": "Details"}
FRONTMATTER_TITLES = {
    "Atom Identity",
    "Content Role",
    "Type",
    "Current Scope Unit",
    "Claim Target Scope Unit",
    "Local Tier",
    "Global Tier",
    "Version",
    "Updated At",
    "Author",
    "Status",
    "Subjects",
    "Relations",
    "Assignee",
    "Autonomous Confidence Threshold",
    "Implementation Retry Limit",
    "Priority",
}

# Values transcribed from the named Claims. A contribution is usable only after
# checking its complete source bytes against registry.json/schema_authority.json.
TYPE_CONTRIBUTIONS = {
    "CA-R-1231": ("Concern", ("Question", "Conflict", "Problem")),
    "CA-R-1232": ("Analysis", ("Analysis Report", "Rationale")),
    "CA-R-1574": ("Plan", ("Plan",)),
    "CA-R-1666": ("Plan", ("Action Policy",)),
    "CA-R-1565": ("Operations", ("Action", "Workflow", "Step", "Actor")),
    "CA-R-825": ("Requirement", ("Boundary",)),
    "CA-R-1673": ("Requirement", ("Constraint",)),
    "CA-R-925": ("Requirement", ("Goal",)),
    "CA-R-932": ("Requirement", ("Demand",)),
    "CA-R-1667": ("Method", ("Implementation Method",)),
    "CA-R-1668": ("Method", ("Implementation Decision",)),
    "CA-R-1674": ("Method", ("External Implementation Method",)),
    "CA-R-1675": ("Method", ("Method Binding",)),
    "CA-R-1662": ("Evaluation", ("QA Case", "Evaluation Control")),
    "CAPRMEDIO-R-793": ("Evaluation", ("Evaluation Approach",)),
    "CA-R-1665": ("Delivery", ("Release Definition", "Environment Definition")),
}
CONTENT_ROLES = (
    "Concern",
    "Analysis",
    "Plan",
    "Requirement",
    "Method",
    "Evaluation",
    "Delivery",
    "Implementation",
    "Operations",
)


@lru_cache(maxsize=1)
def _pins() -> Record:
    result = {}
    for name in ("registry.json", "schema_authority.json"):
        result.update(json.loads(Path(__file__).with_name(name).read_text())["sources"])
    return result


def _inputs(check: Check, field: str) -> Record | None:
    inputs = getattr(check, "inputs", None)
    if not isinstance(inputs, dict) or not isinstance(inputs.get("sources"), list):
        check.gap(field, "Schema validation requires the selected raw authority source records.")
        return None
    return inputs


def _source(check: Check, atom_id: str, field: str, *, required: bool = True) -> Record | None:
    inputs = getattr(check, "inputs", {})
    candidates: list[Record] = [
        row for row in inputs.get("sources", []) if row.get("binding", {}).get("atom_id") == atom_id
    ]
    entry = _pins().get(atom_id)
    if entry and len(candidates) == 1 and _verified(candidates[0], entry):
        return candidates[0]
    if required:
        check.gap(field, "Schema authority is absent, changed, or ambiguous: " + atom_id + ".")
    return None


def _governs(row: Record) -> str:
    subjects = row.get("metadata", {}).get("subjects", {})
    value = subjects.get("governs", "") if isinstance(subjects, dict) else ""
    return value if isinstance(value, str) else ""


def _schema_closed(check: Check) -> bool:
    """Close rejection only over an entirely reviewed selected source inventory.

    Missing mandatory schema, changed bytes, and opaque extension declarations
    prevent a whitelist from proving that a new property is forbidden. Syntactic
    mentions in unreviewed prose never grant schema admission.
    """
    required = [atom_id for atom_id, entry in _pins().items() if entry.get("required")]
    selected = [row.get("binding", {}).get("atom_id") for row in check.inputs["sources"]]
    return all(
        _source(check, atom_id, "properties", required=False) for atom_id in {*required, *selected}
    )


def _unknown_property(metadata: Record, field: str, check: Check) -> None:
    del metadata
    if not _schema_closed(check):
        check.gap(
            field,
            "Incomplete or unreviewed source schema prevents deciding admission for " + field + ".",
        )
    else:
        check.fail(
            "PROPERTY_UNADMITTED",
            field,
            "No selected Delivery declaration admits this property location: " + field + ".",
        )


def _admit_plan_field(metadata: Record, field: str, check: Check) -> None:
    role, kind = metadata.get("content_role"), metadata.get("type")
    if not role or (role == "Plan" and not kind):
        check.gap(field, "Conditional field admission needs its carried Content Role and Type.")
    elif role != "Plan":
        check.fail("PROPERTY_UNADMITTED", field, "This encoding belongs to the common Plan model.")
    elif kind != "Plan":
        check.gap(field, "This Plan Type needs its own applicable field declaration.")
    else:
        source_id, predicate = PLAN_FIELDS[field]
        if _source(check, source_id, field):
            check.require(metadata, field, predicate)


def _admit_priority(metadata: Record, check: Check) -> None:
    if "content_role" not in metadata:
        check.gap("priority", "Priority admission requires a carried Content Role.")
    elif _source(check, "CA-D-386", "priority"):
        if metadata["content_role"] != "Concern":
            check.forbid(metadata, "priority")
        else:
            check.require(metadata, "priority", lambda value: value in ("high", "medium", "low"))


def _admit_projection(metadata: Record, check: Check) -> None:
    if not _source(check, "CA-D-305", "projection"):
        return
    block = metadata["projection"]
    if (
        not isinstance(block, dict)
        or set(block) != {"source_carrier_path"}
        or not _string(block.get("source_carrier_path"))
    ):
        check.fail(
            "PROPERTY_UNADMITTED",
            "projection",
            "Projection admits only one source_carrier_path string.",
        )
    path = check.inputs.get("path")
    if path is not None and any(
        str(path) == row.get("binding", {}).get("path") for row in check.inputs["sources"]
    ):
        check.fail(
            "PROPERTY_UNADMITTED",
            "projection",
            "Projection binding metadata must not be authored upstream on its source Atom.",
        )


def _admit_subject_keys(metadata: Record, check: Check) -> None:
    subjects = metadata.get("subjects")
    if isinstance(subjects, dict) and _source(check, "CA-D-269", "subjects"):
        for key in set(subjects) - {"governs", "depends_on"}:
            check.fail(
                "PROPERTY_UNADMITTED",
                "subjects." + str(key),
                "Unadmitted Subject serialization key.",
            )
        if any(isinstance(value, dict) for value in subjects.values()):
            check.gap(
                "subjects",
                "Nested Subject encoding requires separately resolved migration authority.",
            )


def _property_admission(metadata: Record, body: str, check: Check) -> None:
    del body
    if _inputs(check, "properties") is None or _source(check, "CA-D-276", "properties") is None:
        return
    for field in metadata:
        if field in COMMON_FIELDS:
            continue
        if field in {"operators", "identifier", "summary", "claim"}:
            check.fail(
                "PROPERTY_UNADMITTED",
                field,
                "Common carrier authority forbids this frontmatter field.",
            )
        elif field in {"cce_version", "cce_form", "llm_session_ids"}:
            if _source(check, "CA-D-478", field):
                check.fail(
                    "PROPERTY_RETIRED",
                    field,
                    "Retired Atom Properties cannot be admitted by legacy presence.",
                )
        elif field in PLAN_FIELDS:
            _admit_plan_field(metadata, field, check)
        elif field == "priority":
            _admit_priority(metadata, check)
        elif field == "projection":
            _admit_projection(metadata, check)
        else:
            _unknown_property(metadata, field, check)
    _admit_subject_keys(metadata, check)
    # Relation kinds and target semantics have their own source-bound resolver.


def _single_location(metadata: Record, body: str, check: Check) -> None:
    if _inputs(check, "properties") is None or _source(check, "CA-D-478", "properties") is None:
        return
    body_fields = dict(BODY_FIELDS)
    if _source(check, "CA-D-479", "body") is None:
        return
    if metadata.get("content_role") == "Plan" and metadata.get("type") == "Plan":
        if _source(check, "CA-D-470", "body"):
            body_fields.update(PLAN_BODY_FIELDS)
    for field in body_fields:
        if field in metadata:
            check.fail(
                "PROPERTY_LOCATION",
                field,
                "This Property's sole canonical value belongs in its registered body section.",
            )
    if _source(check, "CA-D-276", "body"):
        for level, title, _ in _headings(body):
            if level <= 2 and title in FRONTMATTER_TITLES:
                check.fail(
                    "PROPERTY_LOCATION",
                    title,
                    "This Property belongs in frontmatter, not a body Property section.",
                )


def _additional_properties(metadata: Record, body: str, check: Check) -> None:
    if _inputs(check, "body") is None or _source(check, "CA-D-479", "body") is None:
        return
    layout = role_sections(metadata, check)
    if layout is None:
        return
    expected = set(layout)
    plan = metadata.get("content_role") == "Plan" and metadata.get("type") == "Plan"
    if plan:
        if _source(check, "CA-D-470", "body") is None:
            return
        expected.add((3, "Definition of Done"))
    headings = _headings(body)
    names = {title for _, title in expected}
    for level, title, _ in headings:
        if title in names and (level, title) not in expected:
            check.fail(
                "BODY_SECTION",
                title,
                "Registered body Property has a renamed or ambiguously nested heading.",
            )
        elif level <= 2 and (level, title) not in expected:
            if not _schema_closed(check):
                check.gap(
                    title,
                    "Incomplete or unreviewed source schema prevents deciding body Property admission.",
                )
            else:
                check.fail("BODY_SECTION", title, "Unregistered body Property heading.")
    if plan:
        _sections(body, check, layout)
        plan_definition(body, check)


def _updated_at_quoting(metadata: Record, body: str, check: Check) -> None:
    del metadata, body
    inputs = getattr(check, "inputs", {})
    parsed = inputs.get("parsed")
    if parsed is None or not isinstance(getattr(parsed, "frontmatter", None), str):
        check.gap("updated_at", "Quoted encoding requires the original parsed YAML frontmatter.")
        return
    try:
        root = yaml.compose(parsed.frontmatter, Loader=yaml.SafeLoader)
    except yaml.YAMLError:
        check.gap("updated_at", "Raw frontmatter cannot be inspected safely for quoting.")
        return
    values = (
        [
            value
            for key, value in root.value
            if isinstance(key, ScalarNode) and key.value == "updated_at"
        ]
        if isinstance(root, MappingNode)
        else []
    )
    if (
        len(values) != 1
        or not isinstance(values[0], ScalarNode)
        or values[0].tag != "tag:yaml.org,2002:str"
        or values[0].style not in ("'", '"')
    ):
        check.fail(
            "PROPERTY_ENCODING", "updated_at", "Updated At must be exactly one quoted YAML string."
        )


def _type_values(check: Check, role: str) -> tuple[set[str], bool]:
    values: set[str] = set()
    verified_ids = set()
    unresolved = False
    for atom_id, (contribution_role, contribution) in TYPE_CONTRIBUTIONS.items():
        if contribution_role != role:
            continue
        if _source(check, atom_id, "type", required=False):
            values.update(contribution)
            verified_ids.add(atom_id)
        elif any(
            row.get("binding", {}).get("atom_id") == atom_id for row in check.inputs["sources"]
        ):
            unresolved = True
    prefix = f"Atom/Content Role: {role}/Type"
    for row in check.inputs["sources"]:
        target = _governs(row)
        if (target == prefix or target.startswith(prefix + ": ")) and row.get("binding", {}).get(
            "atom_id"
        ) not in verified_ids:
            # Rules refining an already admitted Type do not introduce another
            # Type; uncertain declarations of new values remain explicit gaps.
            qualified = (
                target[len(prefix + ": ") :].split("/", 1)[0]
                if target.startswith(prefix + ": ")
                else ""
            )
            if qualified not in values and row.get("binding", {}).get("atom_id") != "CA-R-1506":
                unresolved = True
    return values, unresolved


def _model_domains(metadata: Record, body: str, check: Check) -> None:
    del body
    if _inputs(check, "type") is None or _source(check, "CA-D-276", "type") is None:
        return
    if _source(check, "CA-R-1283", "content_role") is None:
        return
    check.require(metadata, "content_role", lambda value: value in CONTENT_ROLES)
    role = metadata.get("content_role")
    if role not in CONTENT_ROLES:
        return
    ordinary = role in ("Requirement", "Method", "Delivery")
    if "type" not in metadata and ordinary:
        # CA-R-1700 is the narrowly governed exception to the otherwise
        # complete role/type coordinate.  A familiar role name or a filename
        # must never manufacture that exception.
        _source(check, "CA-R-1700", "type")
        return
    if not _string(metadata.get("type")):
        check.fail("PROPERTY_TYPE", "type", "Type must be exactly one nonempty string.")
        return
    kind = metadata["type"]
    values, unresolved = _type_values(check, role)
    if role == "Evaluation" and kind in ("Test", "Evaluation"):
        if _source(check, "CA-R-1506", "type"):
            check.fail(
                "PROPERTY_DOMAIN",
                "type",
                "Evaluation mechanism labels are not admitted Evaluation Atom Types.",
            )
        return
    if kind in values:
        return
    if unresolved or not values:
        check.gap(
            "type",
            "The selected methodology does not provide a completely resolved schema for this qualified Type value.",
        )
    else:
        check.fail(
            "PROPERTY_DOMAIN",
            "type",
            "Type is not admitted under the carried Content Role by the selected source declarations.",
        )


def _plan_model(metadata: Record, body: str, check: Check) -> None:
    if "content_role" not in metadata:
        check.gap("content_role", "Plan model applicability requires its carried Content Role.")
        return
    if metadata["content_role"] != "Plan":
        check.applicable = False
        return
    if _inputs(check, "type") is None or _source(check, "CA-R-1574", "type") is None:
        return
    if not _string(metadata.get("type")):
        check.fail(
            "PROPERTY_TYPE",
            "type",
            "Plan model selection requires exactly one nonempty Type string.",
        )
        return
    if metadata.get("type") != "Plan":
        values, _ = _type_values(check, "Plan")
        if metadata.get("type") in values:
            check.applicable = False
        else:
            check.gap(
                "type", "Common Plan applicability needs Plan or a separately resolved Plan Type."
            )
        return
    if _source(check, "CA-D-479", "Objective") is None:
        return
    headings = _headings(body)
    claims = [row for row in headings if row[:2] == (2, "Objective")]
    if len(claims) != 1:
        check.fail(
            "PLAN_MODEL",
            "Objective",
            "The common Plan requires exactly one Objective Property section.",
        )
        return
    start = claims[0][2]
    end = next(
        (index for level, _, index in headings if level <= 2 and index > start),
        len(body.splitlines()),
    )
    if not any(line.strip() for line in body.splitlines()[start + 1 : end]):
        check.fail(
            "PLAN_MODEL", "Objective", "The Plan Objective Property must contain its own value."
        )


ADAPTERS = {
    "property.admission": _property_admission,
    "model.domains": _model_domains,
    "property.single_location": _single_location,
    "body.additional_properties": _additional_properties,
    "frontmatter.updated_at_quoting": _updated_at_quoting,
    "plan.model": _plan_model,
}
