"""Resolve reviewed, byte-bound obligations independently of installed adapters."""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

Record = dict[str, Any]


def diagnostic(
    code: str, reason: str, authority: list[Record], property_name: str | None = None
) -> Record:
    return {
        "code": code,
        "severity": "error",
        "path": None,
        "span": None,
        "property": property_name,
        "authority": authority,
        "reason": reason,
        "evidence": None,
    }


@dataclass(frozen=True)
class Obligation:
    code: str
    authority: list[Record]
    supported: bool
    reason: str


@dataclass(frozen=True)
class AuthorityContext:
    bindings: list[Record]
    required: int
    supported: int
    unsupported: int
    gaps: list[Record]
    obligations: tuple[Obligation, ...]
    domains: dict[str, tuple[str, ...]]
    unclassified_sources: bool

    @property
    def status_domains(self) -> dict[str, list[str]]:
        """Exact role-qualified values, available only from verified domain sources."""
        return {
            code.rsplit(".", 1)[1].capitalize(): list(values)
            for code, values in self.domains.items()
            if code.startswith("domain.status.")
        }


def _binding_key(binding: Record) -> tuple[str, int, str, str]:
    return (binding["atom_id"], binding["version"], binding["path"], binding["sha256"])


def _verified(source: Record, entry: Record) -> bool:
    binding = source["binding"]
    return bool(
        binding["version"] == entry["version"]
        and binding["sha256"] == entry["sha256"]
        and hashlib.sha256(source["text"].encode("utf-8")).hexdigest() == entry["sha256"]
    )


def _domain(text: str) -> tuple[str, ...]:
    """Extract only the reviewed finite-set syntax, never general prose inference."""
    claim = text.split("---", 2)[-1]
    match = re.search(
        r"\*\*must\*\* be (?:exactly )?\(([^()]+)\)|\*\*must\*\* include \(([^()]+)\)|\*\*in\*\* \(([^()]+)\)",
        claim,
    )
    if match is None:
        return ()
    raw = next(value for value in match.groups() if value is not None)
    return tuple(value.strip().strip("`") for value in raw.split(","))


def _source_obligations(
    atom_id: str, entry: Record, candidates: list[Record], adapters: frozenset[str]
) -> tuple[list[Obligation], list[Record], dict[str, tuple[str, ...]]]:
    bindings = sorted((s["binding"] for s in candidates), key=_binding_key)
    verified = len(candidates) == 1 and _verified(candidates[0], entry)
    reason = "Authority source is absent, changed, or ambiguous: " + atom_id + "."
    domains: dict[str, tuple[str, ...]] = {}
    obligations = []
    for code in entry["obligations"]:
        supported = verified and code in adapters
        if supported and code.startswith("domain."):
            values = _domain(candidates[0]["text"])
            supported = bool(values)
            domains[code] = values
        why = "Verified exact source-bound adapter." if supported else reason
        if verified and not supported:
            why = "No source-bound adapter supports obligation: " + code + "."
        obligations.append(Obligation(code, bindings, supported, why))
    missing = [o.code for o in obligations if not o.supported]
    gaps = []
    if missing:
        why = (
            reason
            if not verified
            else "Unsupported obligations from " + atom_id + ": " + ", ".join(missing) + "."
        )
        gaps.append(diagnostic("AUTHORITY_UNSUPPORTED", why, bindings))
    return obligations, gaps, domains


def resolve_context(sources: list[Record]) -> AuthorityContext:
    # The inventory is loaded before adapter selection. Removing an adapter cannot
    # remove its source obligation, and unknown sources never vanish from coverage.
    registry: Record = json.loads(Path(__file__).with_name("registry.json").read_text())
    from .checks import ADAPTER_CODES
    from .support_authority import support_sources

    grouped: dict[str, list[Record]] = {}
    for source in sources:
        grouped.setdefault(source["binding"]["atom_id"], []).append(source)
    obligations: list[Obligation] = []
    gaps: list[Record] = []
    domains: dict[str, tuple[str, ...]] = {}
    for atom_id, entry in registry["sources"].items():
        candidates = grouped.pop(atom_id, [])
        if not candidates and not entry["required"]:
            continue
        items, missing, values = _source_obligations(atom_id, entry, candidates, ADAPTER_CODES)
        obligations.extend(items)
        gaps.extend(missing)
        domains.update(values)
    # Support definitions are not automatically universal candidate obligations.
    # Changed or ambiguous support sources still remain visibly unclassified.
    for atom_id, entry in support_sources().items():
        candidates = grouped.get(atom_id, [])
        if len(candidates) == 1 and _verified(candidates[0], entry):
            grouped.pop(atom_id)
    for atom_id, candidates in sorted(grouped.items()):
        bindings = sorted((s["binding"] for s in candidates), key=_binding_key)
        why = "Unclassified source obligations require review: " + atom_id + "."
        obligations.append(Obligation("authority.unclassified." + atom_id, bindings, False, why))
        gaps.append(diagnostic("AUTHORITY_UNSUPPORTED", why, bindings))
    obligations.sort(key=lambda item: item.code)
    supported = sum(item.supported for item in obligations)
    bindings = sorted((s["binding"] for s in sources), key=_binding_key)
    return AuthorityContext(
        bindings,
        len(obligations),
        supported,
        len(obligations) - supported,
        gaps,
        tuple(obligations),
        domains,
        bool(grouped),
    )
