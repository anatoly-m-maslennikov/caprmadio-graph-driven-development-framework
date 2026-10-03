#!/usr/bin/env python3
"""Preview/apply missing Atom properties from a reviewed, explicit evidence map.

This is a one-time carrier migration, not a filename-based reader or validator.
Unresolved values remain missing. Existing values are never overwritten.
"""
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import sys
from typing import Any

import yaml

import remove_retired_atom_properties as safe

KIND = "backfill_required_atom_properties"
FIELDS = frozenset({"atom_id", "content_role", "type", "current_scope_unit",
                    "claim_target_scope_unit", "local_tier", "global_tier", "status", "author"})


def add_properties(raw: bytes, additions: dict[str, Any]) -> bytes:
    """Append absent scalar properties without reserializing existing YAML/body."""
    opening, frontmatter, body = safe._frontmatter(raw)
    safe._mapping(frontmatter)
    metadata = yaml.safe_load(frontmatter) or {}
    if not additions:
        return raw
    if set(additions) - FIELDS or set(additions).intersection(metadata):
        raise safe.MigrationError("Only absent, supported properties may be added.")
    for field, value in additions.items():
        valid = type(value) is int if field == "global_tier" else isinstance(value, str) and bool(value.strip())
        if not valid:
            raise safe.MigrationError("Property values must be nonempty strings, or integer global_tier.")
    combined = metadata | additions
    if str(combined.get("status", "")).lower() == "draft" and "atom_id" in combined:
        raise safe.MigrationError("Draft identity must not be backfilled.")
    newline = "\r\n" if opening.endswith("\r\n") else "\n"
    appended = "".join(f"{field}: {json.dumps(value, ensure_ascii=False)}{newline}"
                       for field, value in additions.items())
    result = opening + frontmatter + appended + body
    new_metadata = yaml.safe_load(frontmatter + appended)
    if new_metadata != combined:
        raise safe.MigrationError("Insertion would change an existing YAML value.")
    return result.encode("utf-8")


def _values(fields: dict[str, Any]) -> dict[str, Any]:
    values = {}
    for name, record in fields.items():
        if not isinstance(record.get("evidence"), str) or not record["evidence"].strip():
            raise safe.MigrationError("Each recovered value needs explicit reviewed evidence.")
        values[name] = record["value"]
    return values


def _inputs(report: dict[str, Any], evidence: dict[str, Any]) -> tuple[dict, dict]:
    carriers = {row["path"]: row for row in report["carriers"]}
    if len(carriers) != len(report["carriers"]):
        raise safe.MigrationError("Duplicate report carrier path.")
    selected = report.get("selection", {}).get("selected", list(carriers))
    if len(set(selected)) != len(selected) or set(selected) != set(carriers):
        raise safe.MigrationError("Selection and assessed carriers differ.")
    if set(evidence["carriers"]) - set(carriers):
        raise safe.MigrationError("Evidence contains an unassessed carrier.")
    missing: dict[str, set[str]] = {}
    for finding in report["findings"]:
        if finding.get("code") == "PROPERTY_REQUIRED":
            if finding["path"] not in carriers:
                raise safe.MigrationError("Missing-property finding is outside the assessed carriers.")
            missing.setdefault(finding["path"], set()).add(finding["property"])
    return carriers, missing


def build_plan(report: dict[str, Any], root: Path, report_raw: bytes,
               evidence: dict[str, Any]) -> dict[str, Any]:
    carriers, missing = _inputs(report, evidence)
    baseline, changes, blockers, unresolved = [], [], [], []
    for name, carrier in sorted(carriers.items()):
        fields = evidence["carriers"].get(name, {})
        unresolved.extend({"path": name, "property": key} for key in sorted(missing.get(name, set()) - set(fields)))
        try:
            path, before = safe._report_carrier(carrier, root)
            baseline.append({"path": name, "sha256": safe._digest(before)})
            if set(fields) - missing.get(name, set()):
                raise safe.MigrationError("Backfill values must match reported missing properties.")
            if not fields:
                continue
            after = add_properties(before, _values(fields))
            after, version = safe._revision(after)
            archive = safe._archive_path(path, version)
            safe._archive_exists(archive, before)
            changes.append({"path": name, "before": before.decode(), "after": after.decode(),
                            "before_sha256": safe._digest(before), "after_sha256": safe._digest(after),
                            "fields": fields, "version": version, "after_version": version + 1,
                            "archive": str(archive), "archive_sha256": safe._digest(before)})
        except (ValueError, OSError, yaml.YAMLError) as error:
            blockers.append({"path": name, "reason": str(error)})
    counts = Counter(field for change in changes for field in change["fields"])
    return {"schema_version": 1, "kind": KIND, "source_root": str(root), "mode": "dry-run",
            "report_sha256": safe._digest(report_raw), "baseline": baseline, "changes": changes,
            "blockers": blockers, "unresolved": unresolved,
            "counts": {"selected": len(carriers), "changes": len(changes), "properties": sum(counts.values()),
                       "by_property": dict(counts), "unresolved": len(unresolved), "blockers": len(blockers)}}


def apply_plan(plan: dict[str, Any], root: Path) -> dict[str, Any]:
    if (plan.get("kind") != KIND or plan.get("schema_version") != 1 or plan.get("blockers")
            or plan.get("source_root") != str(root)):
        raise safe.MigrationError("Unsupported, mismatched, or blocked plan.")
    changes = {}
    for change in plan["changes"]:
        path = safe._carrier_path(change["path"], root)
        before, after = change["before"].encode(), change["after"].encode()
        expected, version = safe._revision(add_properties(before, _values(change["fields"])))
        if (not change["fields"] or after != expected or safe._digest(before) != change["before_sha256"]
                or safe._digest(after) != change["after_sha256"] or change["version"] != version
                or change["after_version"] != version + 1 or change["archive_sha256"] != safe._digest(before)
                or change["archive"] != str(safe._archive_path(path, version))):
            raise safe.MigrationError("Plan is not the exact missing-property transformation.")
        if str(path) in changes:
            raise safe.MigrationError("Duplicate plan change path.")
        changes[str(path)] = change
    completed = safe._preflight(plan, root, changes)
    applied = []
    for name, change in changes.items():
        safe._ensure_archive(change)
        if safe._apply_change(change):
            applied.append(name)
        elif name not in completed:
            completed.append(name)
    return {"schema_version": 1, "kind": KIND, "mode": "apply", "source_root": str(root),
            "applied": applied, "already_applied": sorted(completed),
            "counts": {"applied": len(applied), "already_applied": len(completed)}}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report")
    parser.add_argument("--source-root")
    parser.add_argument("--evidence", help="JSON carriers map: path -> field -> {value, evidence}")
    parser.add_argument("--apply", metavar="PLAN")
    parser.add_argument("--output", required=True)
    args = parser.parse_args(argv)
    try:
        safe._preflight_output(args.output)
        if args.apply:
            if args.report or args.evidence or args.source_root:
                raise safe.MigrationError("Apply accepts only a reviewed plan and new receipt path.")
            raw, plan = safe._json_read(safe._absolute(str(Path(args.apply).absolute())))
            result = apply_plan(plan, safe._absolute(plan["source_root"]))
            result["plan_sha256"] = safe._digest(raw)
        else:
            if not args.report or not args.source_root or not args.evidence:
                raise safe.MigrationError("Preview requires report, source-root, and evidence.")
            raw, report = safe._json_read(safe._absolute(str(Path(args.report).absolute())))
            evidence_raw, evidence = safe._json_read(safe._absolute(str(Path(args.evidence).absolute())))
            result = build_plan(report, safe._absolute(str(Path(args.source_root).absolute())), raw, evidence)
            result["evidence_sha256"] = safe._digest(evidence_raw)
        safe._output(args.output, result)
        print(json.dumps(result["counts"]))
        return 2 if result.get("blockers") else 0
    except (ValueError, OSError, KeyError, TypeError, AttributeError, yaml.YAMLError) as error:
        print(json.dumps({"error": str(error), "kind": KIND}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
