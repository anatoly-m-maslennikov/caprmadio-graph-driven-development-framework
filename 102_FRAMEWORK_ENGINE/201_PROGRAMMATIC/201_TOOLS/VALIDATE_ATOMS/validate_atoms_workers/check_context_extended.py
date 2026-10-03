"""Exact-source-bound Plan settings and projected-carrier checks."""

from pathlib import Path
import tomllib
from typing import Any, cast

from .check_support import Check, _integer, _plan
from .projection import verify_projection
from .settings import bound_file
from .support_authority import require_sources


def retry_domain(metadata: dict[str, Any], body: str, check: Check) -> None:
    del body
    if not _plan(metadata, check):
        return
    field = "implementation_retry_limit"
    if field not in metadata:
        return  # An omitted optional override is not a stored default.
    if require_sources(check, ("CA-R-1488",)):
        check.require(metadata, field, lambda value: _integer(value) and value >= 0)


def _threshold(value: Any) -> bool:
    return _integer(value) and 0 <= value <= 100


def _parent(metadata: dict[str, Any], check: Check) -> dict[str, Any] | None:
    relations = metadata.get("relations", {})
    if not isinstance(relations, dict):
        check.fail("PROPERTY_TYPE", "relations", "Plan Relations must be a mapping.")
        return None
    targets = relations.get("is_decomposition_of", [])
    if (
        not isinstance(targets, list)
        or len(targets) > 1
        or any(not isinstance(t, str) for t in targets)
    ):
        check.fail(
            "PROPERTY_TYPE", "relations.is_decomposition_of", "Expected at most one Plan parent."
        )
        return None
    if not targets:
        return {}
    if not check.inputs.get("reference_complete", False):
        check.gap(
            "relations.is_decomposition_of",
            "Parent uniqueness requires a complete supplied reference inventory.",
        )
        return None
    candidates = [
        row["metadata"]
        for row in check.inputs.get("references", [])
        if row.get("metadata", {}).get("atom_id") == targets[0]
        and "projection" not in row["metadata"]
    ]
    if len(candidates) != 1:
        check.gap(
            "relations.is_decomposition_of",
            "Current parent Plan is missing or ambiguous; no latest-Version guess is made.",
        )
        return None
    parent = cast(dict[str, Any], candidates[0])
    if parent.get("content_role") != "Plan" or parent.get("type") != "Plan":
        check.fail(
            "RELATION_TARGET",
            "relations.is_decomposition_of",
            "Override ancestor must be an admitted Plan.",
        )
        return None
    return parent


def _settings(check: Check, key: str) -> dict[str, Any] | None:
    binding = check.inputs.get("request", {}).get(key)
    reader = check.inputs.get("reader")
    if binding is None:
        return {}
    if reader is None:
        check.gap(key, "Selected Settings require bounded runtime access.")
        return None
    try:
        return tomllib.loads(bound_file(reader, binding).decode("utf-8"))
    except OSError, ValueError:
        check.gap(key, "Selected Settings are unavailable, changed, or malformed.")
        return None


def _default_thresholds(check: Check) -> None:
    if not require_sources(check, ("CA-M-279", "CA-D-368", "CA-D-369")):
        return
    instance, defaults = (
        _settings(check, "framework_settings"),
        _settings(check, "default_settings"),
    )
    if instance is None or defaults is None:
        return
    sections = [doc.get("confidence", {}) for doc in (instance, defaults)]
    if any(not isinstance(section, dict) for section in sections):
        check.fail(
            "SETTING_VALUE",
            "confidence",
            "Confidence Settings must be tables; invalid explicit values cannot fall back.",
        )
        return
    for field in (
        "necessary_information_threshold_percent",
        "semantic_resolution_threshold_percent",
    ):
        selected = next((section[field] for section in sections if field in section), None)
        if selected is None:
            check.gap(
                "confidence." + field, "No selected confidence default; no value is invented."
            )
        elif not _threshold(selected):
            check.fail(
                "SETTING_VALUE",
                "confidence." + field,
                "Selected confidence default must be an integer percentage from 0 through 100.",
            )
    # This is static carrier validation of available defaults. Direct Operator
    # input is decision-context authority, not a field in the checker request;
    # no execution-specific threshold is selected or stored here.


def confidence_selection(metadata: dict[str, Any], body: str, check: Check) -> None:
    del body
    if not _plan(metadata, check) or not require_sources(check, ("CA-M-271", "CA-R-1427")):
        return
    field = "autonomous_confidence_threshold"
    current = metadata
    seen: set[str] = set()
    for _ in range(len(check.inputs.get("references", [])) + 2):
        reader = check.inputs.get("reader")
        if reader is not None:
            reader.checkpoint()
        identifier = current.get("atom_id")
        if isinstance(identifier, str):
            if identifier in seen:
                check.fail(
                    "RELATION_CYCLE",
                    "relations.is_decomposition_of",
                    "Cyclic Plan inheritance has no unambiguous nearest override.",
                )
                return
            seen.add(identifier)
        if field in current:
            check.require(current, field, _threshold)
            return
        parent = _parent(current, check)
        if parent is None:
            return
        if not parent:
            _default_thresholds(check)
            return
        current = parent
    check.gap(
        "relations.is_decomposition_of", "Inheritance traversal did not reach a resolved source."
    )


def assignee_resolution(metadata: dict[str, Any], body: str, check: Check) -> None:
    """Limit the CA-D-473 carrier obligation to admitted Plan carriers.

    CA-D-473 governs only ``Plan/Type: Plan/Assignee/Carrier``.  Its
    omission rule refers to the effective-assignee semantics in CA-R-1585,
    but this checker has no admitted representation for whether a Plan owns
    work or for the selected AI Agent.  We can therefore classify a non-Plan
    carrier as outside the obligation, while retaining the Plan case as an
    explicit authority gap instead of inferring a default assignee.
    """
    del body
    if not _plan(metadata, check):
        return
    check.gap(
        "assignee",
        "Effective-assignee resolution requires admitted own-work and selected AI Agent evidence; no default is inferred.",
    )


def projection_fidelity(metadata: dict[str, Any], body: str, check: Check) -> None:
    del body
    if "projection" not in metadata:
        check.applicable = False
        return
    parsed, path, reader = (check.inputs.get(key) for key in ("parsed", "path", "reader"))
    if parsed is None or not isinstance(path, Path) or reader is None:
        check.gap(
            "projection", "Projection fidelity requires bounded access to exact source bytes."
        )
        return
    assessment = check.inputs.get("assessment", {})
    try:
        failure = verify_projection(parsed, path, reader, assessment)
    except OSError, ValueError:
        check.gap("projection", "Original source or supported binding encoding is unavailable.")
        return
    if failure:
        check.fail(failure["code"], "projection", failure["reason"])


ADAPTERS = {
    "plan.retry_domain": retry_domain,
    "plan.override_selection": confidence_selection,
    "plan.assignee_resolution": assignee_resolution,
    "projection.fidelity": projection_fidelity,
}
