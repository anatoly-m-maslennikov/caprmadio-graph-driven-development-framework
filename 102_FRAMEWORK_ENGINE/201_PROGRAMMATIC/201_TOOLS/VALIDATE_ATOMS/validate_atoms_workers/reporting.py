"""Deterministic result assembly, independent of check implementation."""

import json
from typing import Any


def diagnostic(code: str, reason: str, path: str | None = None) -> dict[str, Any]:
    return dict(
        code=code,
        severity="error",
        path=path,
        span=None,
        property=None,
        authority=[],
        reason=reason,
        evidence=None,
    )


def canonical(value: Any) -> str:
    return json.dumps(value, sort_keys=True, ensure_ascii=False)


def diagnostic_key(value: dict[str, Any]) -> tuple[Any, ...]:
    span = value["span"]
    positions = (
        (-1,) * 4
        if span is None
        else tuple(span[k] for k in ("start_line", "start_column", "end_line", "end_column"))
    )
    return (
        (value["path"] is not None, value["path"] or ""),
        positions,
        value["code"],
        (value["property"] is not None, value["property"] or ""),
        value["severity"],
        value["reason"],
    )


def ordered_diagnostics(values: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted({canonical(v): v for v in values}.values(), key=diagnostic_key)


def finish(report: dict[str, Any]) -> dict[str, Any]:
    report["findings"] = ordered_diagnostics(report["findings"])
    positions = {canonical(v): n for n, v in enumerate(report["findings"])}
    totals = dict(passed=0, failed=0, not_applicable=0, not_checked=0)
    for carrier in report["carriers"]:
        for outcome in carrier["outcomes"]:
            records = outcome.pop("_findings", [])
            outcome["finding_indexes"] = sorted({positions[canonical(v)] for v in records})
            totals[outcome["outcome"]] += 1
        carrier["outcomes"].sort(key=lambda o: (o["code"], canonical(o["authority"])))
    report["carriers"].sort(key=lambda c: c["path"])
    selection = report["selection"]
    selection["selected"] = sorted(set(selection["selected"]))
    selection["source_roots"] = sorted(selection["source_roots"])
    for key in ("excluded", "unresolved"):
        selection[key] = sorted(
            {canonical(v): v for v in selection[key]}.values(),
            key=lambda v: (v["path"] is not None, v["path"] or "", v["atom_id"] or "", v["reason"]),
        )
    coverage = report["coverage"]
    coverage["outcomes"] = totals
    coverage["targets"] = dict(
        selected=len(selection["selected"]),
        assessed=sum(bool(c["outcomes"]) for c in report["carriers"]),
        excluded=len(selection["excluded"]),
        unresolved=len(selection["unresolved"]),
    )
    coverage["gaps"] = ordered_diagnostics(coverage["gaps"])
    report["execution"]["diagnostics"] = ordered_diagnostics(report["execution"]["diagnostics"])
    for key in ("methodology", "rules"):
        values = report["bindings"][key]
        report["bindings"][key] = sorted(
            {canonical(v): v for v in values}.values(),
            key=lambda v: (v["atom_id"], v["version"], v["path"], v["sha256"]),
        )
    report["bindings"]["context"].sort(key=lambda v: v["path"])
    if report["execution"]["diagnostics"]:
        report["result"] = "error"
    elif (
        coverage["gaps"]
        or selection["unresolved"]
        or not selection["selected"]
        or report["currentness"]["state"] != "unchanged"
    ):
        report["result"] = "incomplete"
    else:
        report["result"] = "invalid" if totals["failed"] else "valid"
    return report
