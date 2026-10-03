"""Resolve source bindings without deriving Atom properties from addresses."""

import hashlib
from pathlib import Path
from typing import Any
import tomllib

from .parsing import CarrierError, parse_carrier
from .read_io import ReadContext
from .reporting import diagnostic
from .settings import bound_file
from .support_authority import matching_pin


def load_sources(
    request: dict[str, Any], reader: ReadContext, report: dict[str, Any]
) -> list[dict[str, Any]]:
    methodology = request["methodology"]
    frontier = {b["path"]: b for b in methodology.get("frontier", [])}
    sources = []
    for path in reader.discover(methodology["roots"]):
        source = load_source(path, frontier.get(str(path)), reader, report)
        if source:
            sources.append(source)
    bindings = [s["binding"] for s in sources]
    report["bindings"]["methodology"] = bindings
    if frontier and {tuple(sorted(b.items())) for b in bindings} != {
        tuple(sorted(b.items())) for b in frontier.values()
    }:
        report["coverage"]["gaps"].append(
            diagnostic(
                "AUTHORITY_FRONTIER",
                "Supplied frontier differs from independently discovered authority.",
            )
        )
    if not sources:
        report["coverage"]["gaps"].append(
            diagnostic("AUTHORITY_MISSING", "No active authority resolved.")
        )
    # A supplied frontier pins revisions, but cannot prove composition completeness.
    report["coverage"]["gaps"].append(
        diagnostic(
            "AUTHORITY_COMPOSITION_UNVERIFIED",
            "Core, Extension and Project Configuration composition needs a registered resolver.",
        )
    )
    bind_action(request, sources, reader, report)
    if "rule_bundle" in request:
        report["coverage"]["gaps"].append(
            diagnostic(
                "RULE_BUNDLE_UNSUPPORTED",
                "Rule bundle reconciliation is not implemented; bundle checks were not executed.",
            )
        )
    return sources


def load_source(
    path: Path, supplied: dict[str, Any] | None, reader: ReadContext, report: dict[str, Any]
) -> dict[str, Any] | None:
    try:
        raw = reader.read(path)
        parsed = parse_carrier(raw, path)
        metadata = parsed.metadata
        # Exact installed support bindings can identify a legacy authority
        # carrier. They do not repair its Status or any validation target.
        supplied = supplied or matching_pin(raw, path)
        if metadata.get("status") not in ("Active", "active"):
            if metadata.get("status") is not None:
                return None
            if supplied is None:
                raise ValueError("Source lacks carried activity classification.")
            report["coverage"]["gaps"].append(
                diagnostic(
                    "AUTHORITY_ACTIVITY_UNVERIFIED",
                    "Pinned source has no carried Status; checks are conditional on its admission.",
                    str(path),
                )
            )
        identifier = metadata.get("atom_id", (supplied or {}).get("atom_id"))
        version = metadata.get("version")
        if (
            not isinstance(identifier, str)
            or not identifier
            or type(version) is not int
            or version < 1
        ):
            raise ValueError(
                "Authority identity cannot be resolved from carried values or binding."
            )
        binding = dict(
            atom_id=identifier,
            version=version,
            path=str(path),
            sha256=hashlib.sha256(raw).hexdigest(),
        )
        if supplied and binding != supplied:
            raise ValueError("Authority does not match supplied binding.")
        return dict(binding=binding, text=parsed.text, metadata=metadata)
    except OSError, ValueError, CarrierError:
        report["coverage"]["gaps"].append(
            diagnostic(
                "AUTHORITY_UNRESOLVED",
                "Authority is unreadable, malformed, inactive, or has an inconsistent binding.",
                str(path),
            )
        )
        return None


def bind_action(
    request: dict[str, Any],
    sources: list[dict[str, Any]],
    reader: ReadContext,
    report: dict[str, Any],
) -> None:
    if "action_binding" in request:
        source = load_source(
            Path(request["action_binding"]["path"]), request["action_binding"], reader, report
        )
        actions = [source["binding"]] if source else []
    else:
        actions = [s["binding"] for s in sources if s["binding"]["atom_id"] == "CA-O-087"]
    if len(actions) == 1 and actions[0]["atom_id"] == "CA-O-087":
        report["bindings"]["action"] = actions[0]
    else:
        report["coverage"]["gaps"].append(
            diagnostic(
                "ACTION_UNRESOLVED",
                "The admitted Check Atoms Action revision could not be resolved exactly once.",
            )
        )


def load_structure(
    request: dict[str, Any], reader: ReadContext, report: dict[str, Any]
) -> dict[str, Any] | None:
    if "project_structure" not in request:
        return None
    try:
        return tomllib.loads(bound_file(reader, request["project_structure"]).decode("utf-8"))
    except OSError, ValueError:
        report["coverage"]["gaps"].append(
            diagnostic("STRUCTURE_UNRESOLVED", "Project Structure binding cannot be resolved.")
        )
        return None
