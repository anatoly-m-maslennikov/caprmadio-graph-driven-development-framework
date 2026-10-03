"""Membership uses carried values; neither names nor location invent facts."""

from pathlib import Path
from typing import Any


def record(path: str | None, metadata: dict[str, Any], reason: str) -> dict[str, Any]:
    value = metadata.get("atom_id")
    return dict(
        path=path, atom_id=value if isinstance(value, str) and value else None, reason=reason
    )


def matching_selectors(
    path: str, metadata: dict[str, Any], selectors: list[dict[str, Any]]
) -> list[int]:
    matches = []
    for index, selector in enumerate(selectors):
        locator = selector.get("carrier_path")
        if locator is not None and locator != path:
            continue
        if any(
            type(metadata.get(k)) is not type(selector[k]) or metadata.get(k) != selector[k]
            for k in ("atom_id", "version")
            if k in selector
        ):
            continue
        matches.append(index)
    return matches


def structural_names(structure: dict[str, Any], name: str, descendants: bool) -> set[str]:
    units = structure.get("scope_units", [])
    if not isinstance(units, list) or not all(isinstance(u, dict) for u in units):
        raise ValueError("Unsupported Project Structure carrier.")
    names = [u.get("scope_unit_name") for u in units]
    if name not in names or len(names) != len(set(names)):
        raise ValueError("Scope Unit must resolve exactly once.")
    selected = {name}
    if descendants:
        while True:
            expanded = selected | {
                u["scope_unit_name"] for u in units if u.get("parent") in selected
            }
            if expanded == selected:
                break
            selected = expanded
    return selected


def filter_candidate(
    metadata: dict[str, Any],
    selection: dict[str, Any],
    names: set[str] | None,
    status_domains: dict[str, list[str]],
) -> tuple[str, str]:
    """Return selected, excluded, or unresolved, with a public bounded reason."""
    for selector, field in [("global_tiers", "global_tier"), ("local_tiers", "local_tier")]:
        if selector not in selection:
            continue
        value = metadata.get(field)
        required_type = int if field == "global_tier" else str
        if type(value) is not required_type:
            return "unresolved", f"Missing or malformed carried {field}."
        if value not in selection[selector]:
            return "excluded", f"Carried {field} is outside the selected values."
    if "scope_unit" in selection:
        if names is None or not isinstance(metadata.get("current_scope_unit"), str):
            return "unresolved", "Scope Unit membership is unresolved."
        if metadata["current_scope_unit"] not in names:
            return "excluded", "Carried Scope Unit is outside the selection."
    return status_filter(metadata, selection, status_domains)


def status_filter(
    metadata: dict[str, Any], selection: dict[str, Any], domains: dict[str, list[str]]
) -> tuple[str, str]:
    requested = selection.get("statuses", "all" if "atoms" in selection else "active")
    if requested == "all":
        return "selected", ""
    role, status = metadata.get("content_role"), metadata.get("status")
    domain = domains.get(role) if isinstance(role, str) else None
    if not domain or not isinstance(status, str):
        return "unresolved", "Status membership requires a complete source-bound Status model."
    if status not in domain:
        return "unresolved", "Carried Status is not admitted by its Status model."
    # These classification spellings are used only within adapter-bound domains.
    selected = (
        [v for v in domain if v in ("Active", "active")] if requested == "active" else requested
    )
    return (
        ("selected", "") if status in selected else ("excluded", "Status filter excludes Carrier.")
    )


def explicitly_excluded(path: Path, exclusions: list[str]) -> bool:
    return any(path == Path(item) or path.is_relative_to(Path(item)) for item in exclusions)
