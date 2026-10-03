"""Reviewed support-source pins; never admit arbitrary supplied rule parameters."""

from functools import lru_cache
from dataclasses import replace
import hashlib
import json
from pathlib import Path
from typing import Any, cast

from .check_support import Check

MANIFESTS = (
    "schema_authority.json",
    "graph_authority.json",
    "structure_authority.json",
    "context_authority.json",
)


@lru_cache(maxsize=1)
def support_sources() -> dict[str, Any]:
    result: dict[str, Any] = {}
    for name in MANIFESTS:
        path = Path(__file__).with_name(name)
        if not path.is_file():
            continue
        for identifier, entry in json.loads(path.read_text())["sources"].items():
            old = result.get(identifier)
            if old and (old["version"], old["sha256"]) != (entry["version"], entry["sha256"]):
                raise ValueError("Conflicting installed support-source bindings.")
            result[identifier] = entry
    return result


def exact_source(inputs: dict[str, Any], identifier: str) -> dict[str, Any] | None:
    entry = support_sources().get(identifier)
    if entry is None:
        return None
    rows = [
        row
        for row in inputs.get("sources", [])
        if row.get("binding", {}).get("atom_id") == identifier
    ]
    if len(rows) != 1:
        return None
    row = cast(dict[str, Any], rows[0])
    binding = row["binding"]
    if type(binding.get("version")) is not int or (
        binding.get("version"),
        binding.get("sha256"),
    ) != (entry["version"], entry["sha256"]):
        return None
    if hashlib.sha256(row["text"].encode("utf-8")).hexdigest() != entry["sha256"]:
        return None
    return row


def require_sources(check: Check, identifiers: tuple[str, ...]) -> bool:
    missing = [
        identifier for identifier in identifiers if exact_source(check.inputs, identifier) is None
    ]
    if missing:
        check.gap(
            "authority", "Missing or changed supporting authority: " + ", ".join(missing) + "."
        )
        return False
    # Include the dependencies in the check's diagnostic provenance without
    # changing the shared context or the obligation on other targets.
    bindings = list(check.obligation.authority)
    for identifier in identifiers:
        source = exact_source(check.inputs, identifier)
        if source is not None and source["binding"] not in bindings:
            bindings.append(source["binding"])
    check.obligation = replace(check.obligation, authority=bindings)
    return True


def matching_pin(raw: bytes, path: Path) -> dict[str, Any] | None:
    digest = hashlib.sha256(raw).hexdigest()
    found = [
        (identifier, row)
        for identifier, row in support_sources().items()
        if row["sha256"] == digest
    ]
    if len(found) != 1:
        return None
    identifier, row = found[0]
    return dict(atom_id=identifier, version=row["version"], sha256=digest, path=str(path))
