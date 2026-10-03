#!/usr/bin/env python3
"""Backfill Global Tier from explicit owning Scope Unit and Local Tier.

The caller supplies a frozen parent map and exact carrier hashes. No filename,
physical nesting, target Scope Unit, or navigational number supplies a tier.
"""
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import sys
from typing import Any

import yaml

import backfill_required_atom_properties as backfill
import remove_retired_atom_properties as safe

KIND = "backfill_global_tier"
PROJECT_TIERS = {"Principle": 0, "Core": 1, "Standard": 2}
UNIT_TIERS = {"Core": 0, "General": 1, "Standard": 2}


def validate_context(context: dict[str, Any]) -> dict[str, int]:
    project, parents = context.get("project"), context.get("parents")
    if not isinstance(project, str) or not isinstance(parents, dict) or parents.get(project, "missing") is not None:
        raise safe.MigrationError("An explicit Project root and parent map are required.")
    operators = context.get("operators", [])
    if (not isinstance(operators, list) or any(not isinstance(x, str) or not x for x in operators)
            or len(operators) != len(set(operators)) or set(operators).intersection(parents)):
        raise safe.MigrationError("Operator identities must be unique and distinct from Scope Units.")
    if not isinstance(context.get("evidence"), str) or not context["evidence"].strip():
        raise safe.MigrationError("The parent map requires a recorded evidence basis.")
    levels = {project: 0}
    for unit in parents:
        trail, cursor = [], unit
        while cursor not in levels:
            if not isinstance(cursor, str) or not cursor or cursor not in parents or cursor in trail:
                raise safe.MigrationError("Missing parent, multiple roots, or cycle in Scope Unit map.")
            trail.append(cursor)
            cursor = parents[cursor]
        for child in reversed(trail):
            levels[child] = levels[parents[child]] + 1
    return levels


def derive_tier(metadata: dict[str, Any], context: dict[str, Any]) -> int:
    levels = validate_context(context)
    owner, local = metadata.get("current_scope_unit"), metadata.get("local_tier")
    if not isinstance(owner, str):
        raise safe.MigrationError("A carried owning Scope Unit or Operator is required.")
    if owner in context.get("operators", []):
        if (metadata.get("content_role") == "Requirement" and metadata.get("type") == "Goal"
                and metadata.get("claim_target_scope_unit") == context["project"]
                and "local_tier" not in metadata):
            return -1
        raise safe.MigrationError("Operator-owned Atom is not an unambiguous tierless Project Goal.")
    if owner not in levels or not isinstance(local, str):
        raise safe.MigrationError("Owner or explicit Local Tier cannot be resolved.")
    admitted = PROJECT_TIERS if levels[owner] == 0 else UNIT_TIERS
    if local not in admitted:
        raise safe.MigrationError("Local Tier is not admitted for this Scope Unit.")
    # Project Standard = 2; every child Core = parent Standard + 1;
    # non-Project General/Standard = Core + 1/+2 (CA-R-1389/1390/1391).
    return admitted[local] + (0 if levels[owner] == 0 else 3 * levels[owner])


def missing_tier(metadata: dict[str, Any], context: dict[str, Any]) -> int | None:
    expected = derive_tier(metadata, context)
    if "global_tier" not in metadata:
        return expected
    if type(metadata["global_tier"]) is not int or metadata["global_tier"] != expected:
        raise safe.MigrationError("Existing Global Tier disagrees; no automatic overwrite.")
    return None


def _metadata(raw: bytes) -> dict[str, Any]:
    _, frontmatter, _ = safe._frontmatter(raw)
    safe._mapping(frontmatter)
    return yaml.safe_load(frontmatter) or {}


def build_plan(request: dict[str, Any], request_path: Path, raw: bytes) -> dict[str, Any]:
    root = safe._absolute(request["source_root"])
    context = request["scope_context"]
    levels = validate_context(context)
    report = {"carriers": request["carriers"], "findings": []}
    evidence: dict[str, Any] = {"carriers": {}}
    errors, counts = [], Counter()
    for binding in request["carriers"]:
        try:
            path, before = safe._report_carrier(binding, root)
            metadata = _metadata(before)
            if str(metadata.get("status", "")).lower() != "active" or "projection" in metadata:
                raise safe.MigrationError("This migration accepts only explicitly Active source Atoms.")
            expected = missing_tier(metadata, context)
            if expected is None:
                continue
            report["findings"].append({"code": "PROPERTY_REQUIRED", "path": str(path), "property": "global_tier"})
            owner, local = metadata["current_scope_unit"], metadata.get("local_tier")
            reason = (f"Explicit owning unit {owner}, level {levels.get(owner, 'external')}, Local Tier {local}; "
                      "CA-R-1388/1389/1390/1391. Claim target and carrier path do not determine Global Tier.")
            evidence["carriers"][str(path)] = {"global_tier": {"value": expected, "evidence": reason}}
            counts[(owner, local, expected)] += 1
        except (ValueError, OSError, yaml.YAMLError) as error:
            errors.append({"path": binding.get("path"), "reason": str(error)})
    inner = backfill.build_plan(report, root, json.dumps(report, sort_keys=True).encode(), evidence)
    inner["blockers"].extend(errors)
    inner["counts"]["blockers"] = len(inner["blockers"])
    return {"schema_version": 1, "kind": KIND, "mode": "dry-run", "request_path": str(request_path),
            "request_sha256": safe._digest(raw), "scope_context": context, "property_plan": inner,
            "counts": inner["counts"], "distribution": [dict(scope_unit=u, local_tier=t, global_tier=g, count=n)
                                                          for (u, t, g), n in sorted(counts.items())]}


def apply_plan(plan: dict[str, Any]) -> dict[str, Any]:
    if plan.get("kind") != KIND or plan.get("schema_version") != 1:
        raise safe.MigrationError("Unsupported Global Tier migration plan.")
    raw, request = safe._json_read(safe._absolute(plan["request_path"]))
    if safe._digest(raw) != plan["request_sha256"] or request["scope_context"] != plan["scope_context"]:
        raise safe.MigrationError("Migration scope context changed after preview.")
    inner = plan["property_plan"]
    if inner["source_root"] != request["source_root"]:
        raise safe.MigrationError("Source root differs from the frozen request.")
    baseline = {row["path"]: row["sha256"] for row in inner["baseline"]}
    if baseline != {row["path"]: row["sha256"] for row in request["carriers"]}:
        raise safe.MigrationError("Selected baseline differs from the frozen request.")
    for change in inner["changes"]:
        fields = change["fields"]
        expected = missing_tier(_metadata(change["before"].encode()), plan["scope_context"])
        if set(fields) != {"global_tier"} or fields["global_tier"]["value"] != expected:
            raise safe.MigrationError("Planned addition disagrees with the Scope Unit and Local Tier.")
    result = backfill.apply_plan(inner, safe._absolute(inner["source_root"]))
    result["kind"] = KIND
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    inputs = parser.add_mutually_exclusive_group(required=True)
    inputs.add_argument("--input", help="Frozen source-root, carrier hashes, and scope_context JSON")
    inputs.add_argument("--apply", metavar="PLAN", help="Apply an already reviewed preview")
    parser.add_argument("--output", required=True, help="New plan/receipt; never overwrites")
    args = parser.parse_args(argv)
    try:
        safe._preflight_output(args.output)
        path = safe._absolute(str(Path(args.apply or args.input).absolute()))
        raw, data = safe._json_read(path)
        result = apply_plan(data) if args.apply else build_plan(data, path, raw)
        safe._output(args.output, result)
        print(json.dumps(result["counts"]))
        return 2 if result["counts"].get("blockers") else 0
    except (ValueError, OSError, KeyError, TypeError, AttributeError, yaml.YAMLError) as error:
        print(json.dumps({"error": str(error), "kind": KIND}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
