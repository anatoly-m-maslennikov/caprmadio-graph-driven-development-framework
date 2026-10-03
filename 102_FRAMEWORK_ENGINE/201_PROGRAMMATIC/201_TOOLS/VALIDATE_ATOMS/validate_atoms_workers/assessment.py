"""Assess selected carriers and retain failures when other coverage is incomplete."""

from copy import deepcopy
from pathlib import Path
from typing import Any

from .checks import validate_carrier
from .parsing import CarrierError, ParsedCarrier, parse_carrier
from .projection import verify_projection
from .read_io import ReadContext, LimitReached
from .reporting import diagnostic
from .selection import explicitly_excluded, filter_candidate, matching_selectors, record


def candidates(
    request: dict[str, Any],
    reader: ReadContext,
    report: dict[str, Any],
    names: set[str] | None,
    domains: dict[str, list[str]],
    reference_records: list[dict[str, Any]] | None = None,
) -> list[tuple[Path, Any]]:
    selected: list[tuple[Path, Any]] = []
    selectors = request["selection"].get("atoms", [])
    matches: dict[int, list[tuple[Path, dict[str, Any]]]] = {i: [] for i in range(len(selectors))}
    paths = reader.discover(request["source_roots"])
    for path in paths:
        if explicitly_excluded(path, request.get("exclude_paths", [])):
            report["selection"]["excluded"].append(record(str(path), {}, "Explicitly excluded."))
            continue
        parsed, metadata = read_candidate(reader, path)
        if reference_records is not None:
            reference_records.append(dict(path=path, metadata=metadata, parsed=parsed))
        indices = matching_selectors(str(path), metadata, selectors)
        if selectors and not indices:
            if isinstance(parsed, Exception) and any("atom_id" in s for s in selectors):
                report["selection"]["unresolved"].append(
                    record(
                        str(path),
                        metadata,
                        "Unreadable candidate cannot establish identity-based membership.",
                    )
                )
                continue
            report["selection"]["excluded"].append(
                record(str(path), metadata, "No selector match.")
            )
            continue
        state, reason = filter_candidate(metadata, request["selection"], names, domains)
        if state != "selected":
            report["selection"][state].append(record(str(path), metadata, reason))
            continue
        selected.append((path, parsed))
        for index in indices:
            matches[index].append((path, metadata))
    return resolve_matches(selectors, matches, selected, report)


def read_candidate(
    reader: ReadContext, path: Path
) -> tuple[ParsedCarrier | Exception, dict[str, Any]]:
    try:
        parsed = parse_carrier(reader.read(path), path)
        return parsed, parsed.metadata
    except (OSError, CarrierError) as error:
        return error, {}


def resolve_matches(
    selectors: list[dict[str, Any]],
    matches: dict[int, list[Any]],
    selected: list[tuple[Path, Any]],
    report: dict[str, Any],
) -> list[tuple[Path, Any]]:
    ambiguous: set[Path] = set()
    for index, selector in enumerate(selectors):
        found = matches[index]
        identities = {
            (m.get("atom_id"), m.get("version"))
            for _, m in found
            if isinstance(m.get("atom_id"), str) and type(m.get("version")) is int
        }
        if not found or len(identities) > 1:
            reason = (
                "No selected Carrier matches selector." if not found else "Ambiguous revisions."
            )
            report["selection"]["unresolved"].append(
                record(selector.get("carrier_path"), selector, reason)
            )
            if len(identities) > 1:
                ambiguous.update(p for p, _ in found)
    return [(p, value) for p, value in selected if p not in ambiguous]


def apply_checks(
    path: Path,
    parsed: Any,
    context: Any,
    reader: ReadContext,
    report: dict[str, Any],
    inputs: dict[str, Any] | None = None,
) -> None:
    assessment: dict[str, Any] = dict(
        path=str(path),
        atom_id=None,
        version=None,
        sha256=reader.fingerprints.get(str(path)),
        representation="unresolved",
        source_path=None,
        outcomes=[],
    )
    report["carriers"].append(assessment)
    if isinstance(parsed, Exception):
        if isinstance(parsed, CarrierError) and parsed.code not in (
            "YAML_UNSUPPORTED",
            "CARRIER_UNSUPPORTED",
        ):
            failure = diagnostic(parsed.code, str(parsed), str(path))
            add_check(assessment, "carrier.parse", [failure], report, reader)
        else:
            gap = diagnostic("CARRIER_UNREADABLE", "Carrier cannot be safely assessed.", str(path))
            report["coverage"]["gaps"].append(gap)
        return
    metadata = parsed.metadata
    if "projection" not in metadata:
        assessment["representation"] = "source"
    identity, version = metadata.get("atom_id"), metadata.get("version")
    assessment["atom_id"] = identity if isinstance(identity, str) and identity else None
    assessment["version"] = version if type(version) is int and version > 0 else None
    add_check(assessment, "carrier.parse", [], report, reader)
    supplied = dict(inputs or {})
    supplied.update(path=path, parsed=parsed, reader=reader, assessment=assessment)
    checks = deepcopy(validate_carrier(metadata, parsed.body, context, supplied))
    findings = checks["findings"]
    for finding in findings:
        finding["path"] = str(path)
    for outcome in checks["outcomes"]:
        records = [findings[i] for i in outcome["finding_indexes"]]
        ensure_findings(report, reader, records)
        outcome["_findings"] = records
        assessment["outcomes"].append(outcome)
    for gap in checks["gaps"]:
        gap["path"] = str(path)
        report["coverage"]["gaps"].append(gap)
    if any(outcome["code"] == "projection.fidelity" for outcome in checks["outcomes"]):
        return  # Source-bound adapter already performed (or explicitly withheld) this check.
    try:
        projection_failure = verify_projection(parsed, path, reader, assessment)
        if "projection" in metadata:
            add_check(
                assessment,
                "projection.fidelity",
                [projection_failure] if projection_failure else [],
                report,
                reader,
            )
    except OSError, ValueError:
        report["coverage"]["gaps"].append(
            diagnostic(
                "PROJECTION_UNRESOLVED",
                "Original source or byte-preserving projection adapter is unavailable.",
                str(path),
            )
        )


def ensure_findings(report: dict[str, Any], reader: ReadContext, records: list[Any]) -> None:
    fresh = [r for r in records if r not in report["findings"]]
    if len(report["findings"]) + len(fresh) > reader.limits["max_findings"]:
        raise LimitReached("max_findings")
    report["findings"].extend(fresh)


def add_check(
    assessment: dict[str, Any],
    code: str,
    findings: list[Any],
    report: dict[str, Any],
    reader: ReadContext,
) -> None:
    ensure_findings(report, reader, findings)
    assessment["outcomes"].append(
        dict(
            code=code,
            outcome="failed" if findings else "passed",
            authority=[],
            reason="Carrier check failed." if findings else "Carrier check passed.",
            finding_indexes=[],
            _findings=findings,
        )
    )


def duplicate_sources(report: dict[str, Any], reader: ReadContext) -> None:
    seen: dict[tuple[str, int], dict[str, Any]] = {}
    for carrier in report["carriers"]:
        if (
            carrier["representation"] != "source"
            or not carrier["atom_id"]
            or not carrier["version"]
        ):
            continue
        key = carrier["atom_id"], carrier["version"]
        if key in seen:
            failure = diagnostic(
                "DUPLICATE_SOURCE",
                "Multiple authoritative Carriers claim the same Atom Revision.",
                carrier["path"],
            )
            add_check(carrier, "identity.unique_source", [failure], report, reader)
        seen[key] = carrier
