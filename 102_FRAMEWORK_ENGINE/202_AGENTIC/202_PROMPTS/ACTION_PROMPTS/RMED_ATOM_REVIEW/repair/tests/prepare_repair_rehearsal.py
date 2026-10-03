"""Prepare complete source-bound inputs for four synthetic repair rehearsals.

This builder only prepares candidates, context, resources, permissions, and
reserved identities.  It deliberately produces no evaluator part, merged
evaluation, expected verdict, repair proposal, or source mutation.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
from typing import Any

HERE = Path(__file__).resolve().parent
REVIEW_ROOT = HERE.parents[1]
REPOSITORY_ROOT = REVIEW_ROOT.parents[4]
FIXTURE_ROOT = REVIEW_ROOT / "tests" / "fixtures"
CASE_FILE = HERE / "fixtures" / "rehearsal-cases.json"
sys.path.insert(0, str(REVIEW_ROOT))

from context_builder import body_sections, metadata, prepare_context  # noqa: E402
from evaluation_contract import GROUPS  # noqa: E402
from review_evidence import ReviewContext  # noqa: E402


REPAIR_AUTHORITY_IDS = (
    "CA-O-111", "CA-O-067", "CA-R-1432", "CA-R-1464", "CA-R-1766",
    "CA-R-1700", "CA-D-276", "CA-D-283", "CA-D-496",
)
# These sources make the mock resource carriers inspectable under the same
# live schema used by the production prompts.  They are not a fixture policy
# override and never supply a result for a candidate.
RESOURCE_AUTHORITY_IDS = (
    "CA-D-282", "CA-D-283", "CA-D-284",
    "CA-D-302", "CA-D-359", "CA-D-361", "CA-D-364", "CA-D-366", "CA-D-407", "CA-D-408",
    "CA-D-440", "CA-D-441", "CA-D-442", "CA-D-494", "CA-R-680", "CA-R-1389",
    "CA-R-1390", "CA-R-1391", "CA-R-1442", "CA-R-1484", "CA-R-1488",
    "CA-R-1283", "CA-R-1284", "CA-R-1286", "CA-R-1308", "CA-R-1309", "CA-R-1313",
)
SOURCES_ROOT = REPOSITORY_ROOT / ".caprmedio_caprmedio" / "000_CAPRMEDIO_framework" / "00_APPLICABLE_METHODOLOGY" / "000_APPLICABLE_MTHD_sources"
CASES = tuple(json.loads(CASE_FILE.read_text()))


def digest(raw: str) -> str:
    return hashlib.sha256(raw.encode()).hexdigest()


def bound(path: str, atom_id: str, version: int, raw: str) -> dict[str, Any]:
    return {"binding": {"path": path, "atom_id": atom_id, "version": version,
                         "sha256": digest(raw)}, "text": raw}


def synthetic_authority(
    atom_id: str,
    target: str,
    claim: str,
    *,
    role: str = "Requirement",
    current_scope_unit: str = "SYNTHETIC",
    claim_target_scope_unit: str = "SYNTHETIC",
    local_tier: str = "Standard",
    global_tier: int = 11,
) -> dict[str, Any]:
    type_field = "" if role in ("Requirement", "Method", "Delivery") else f"type: {role}\n"
    raw = (
        "---\nsubjects:\n  governs: " + json.dumps(target) + "\n"
        f"atom_id: {atom_id}\nversion: 1\nupdated_at: \"2026-09-26T00:00:00Z\"\n"
        f"content_role: {role}\ncurrent_scope_unit: \"{current_scope_unit}\"\n"
        f"claim_target_scope_unit: \"{claim_target_scope_unit}\"\nlocal_tier: \"{local_tier}\"\n"
        f"global_tier: {global_tier}\nstatus: \"Active\"\nauthor: \"Synthetic Fixture Operator\"\n"
        + type_field + "---\n# Summary\n\nSynthetic test definition\n\n## Scope\n\n"
        "the closed synthetic repair-rehearsal universe.\n\n## Claim\n\n"
        + claim + "\n\n## Details\n\nThis is fixture-only authority, never real Project authority.\n"
    )
    return bound(f"synthetic/definitions/{atom_id}.md", atom_id, 1, raw)


def rewrite_fixture(spec: dict[str, Any]) -> tuple[str, str]:
    source = FIXTURE_ROOT / spec["fixture"]
    original = source.read_text()
    raw = original
    substitutions = {
        r"(?m)^atom_id: .+$": f"atom_id: {spec['atom_id']}",
        r"(?m)^version: .+$": f"version: {spec['version']}",
        r"(?m)^updated_at: .+$": 'updated_at: "2026-09-26T12:00:00Z"',
        r"(?m)^current_scope_unit: .+$": 'current_scope_unit: SYNTHETIC',
        r"(?m)^claim_target_scope_unit: .+$": 'claim_target_scope_unit: SYNTHETIC',
        r"(?m)^author: .+$": 'author: Synthetic Fixture Operator',
        r"(?m)^\s+depends_on: \[.*\]$": "  depends_on: " + json.dumps(spec["depends_on"]),
    }
    for pattern, replacement in substitutions.items():
        raw, count = re.subn(pattern, replacement, raw, count=1)
        if count != 1:
            raise ValueError(f"cannot rewrite {spec['fixture']}: {pattern}")
    raw, type_count = re.subn(r"(?m)^type: Requirement\n", "", raw, count=1)
    if type_count != 1:
        raise ValueError(f"cannot remove generic Requirement Type from {spec['fixture']}")
    if spec["id"] == "unbold_must_formatting":
        # The inherited corpus case also leaves the Scope predicate unbold and
        # uses a noncanonical uppercase spelling.  Normalize those unrelated
        # CCE defects so this rehearsal has exactly one intentionally unbold
        # lowercase modality operator in Claim.
        raw, scope_count = re.subn(
            r"the Color of a Widget in a public display\.",
            "the Color of a Widget **in** a public display.", raw, count=1)
        raw, claim_count = re.subn(
            r"the Color of a Widget MUST be Blue\.",
            "the Color of a Widget must be Blue.", raw, count=1)
        if scope_count != 1 or claim_count != 1:
            raise ValueError("plain-operator fixture no longer has the expected formatting-only body")
    return original, raw


def bound_active_source(atom_id: str) -> dict[str, Any]:
    """Bind exactly one active source outside the frozen evaluator manifest."""
    matches = []
    for path in SOURCES_ROOT.rglob(f"{atom_id}-*.md"):
        if "archive" in path.parts:
            continue
        raw = path.read_text()
        props = metadata(raw)
        if (props.get("atom_id") == atom_id
                and str(props.get("status", "")).casefold() == "active"
                and isinstance(props.get("version"), int)):
            matches.append(bound(str(path.relative_to(REPOSITORY_ROOT)), atom_id, props["version"], raw))
    if len(matches) != 1:
        raise ValueError(f"expected exactly one active source for {atom_id}, found {len(matches)}")
    return matches[0]


def baseline_sources() -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    manifest = json.loads((REVIEW_ROOT / "source_bindings.json").read_text())
    required = {identifier for group in ("cce", "properties", "coherence")
                for identifier in manifest["evaluators"][group]} | set(REPAIR_AUTHORITY_IDS)
    rows = []
    by_id = {binding["atom_id"]: binding for binding in manifest["sources"]}
    missing = required - set(by_id)
    if missing:
        raise ValueError(f"source_bindings.json lacks required authorities: {sorted(missing)}")
    for binding in manifest["sources"]:
        if binding["atom_id"] not in required:
            continue
        raw = (REPOSITORY_ROOT / binding["path"]).read_text()
        if digest(raw) != binding["sha256"]:
            raise ValueError(f"stale baseline binding: {binding['atom_id']}")
        rows.append({"binding": binding, "text": raw})
    selected = {row["binding"]["atom_id"] for row in rows}
    for identifier in RESOURCE_AUTHORITY_IDS:
        if identifier not in selected:
            rows.append(bound_active_source(identifier))
            selected.add(identifier)
    repair = [next(row["binding"] for row in rows if row["binding"]["atom_id"] == identifier)
              for identifier in REPAIR_AUTHORITY_IDS]
    return rows, repair


def write_resources(output: Path) -> dict[str, str]:
    control_root = output / ".caprmedio_synthetic_project"
    framework_root = control_root / "000_CAPRMEDIO_framework"
    default_root = framework_root / "00_APPLICABLE_METHODOLOGY" / "000_APPLICABLE_MTHD_sources" / "001_CORE_META_MODEL"
    for path in (
        framework_root / "01_SYNTHETIC_ROOT",
        framework_root / "02_SYNTHETIC_MIDDLE",
        framework_root / "03_SYNTHETIC",
        output / "synthetic" / "repair-rehearsal",
        default_root,
    ):
        path.mkdir(parents=True, exist_ok=True)
    values = {
        control_root / "project_structure.toml": """schema_version = 1

[[scope_units]]
scope_unit_name = "SYNTHETIC_ROOT"
parent = "PROJECT"
scope_unit_type = "Unordered"
scope_unit_label = "Synthetic rehearsal root"
structural_level = 1
navigational_order_number = 1
authority_path = ".caprmedio_synthetic_project/000_CAPRMEDIO_framework/01_SYNTHETIC_ROOT"
delivery_path = "synthetic/repair-rehearsal"
authority_mode = "strict"

[[scope_units]]
scope_unit_name = "SYNTHETIC_MIDDLE"
parent = "SYNTHETIC_ROOT"
scope_unit_type = "Ordered"
scope_unit_label = "Synthetic rehearsal middle"
structural_level = 2
local_order = 1
navigational_order_number = 2
authority_path = ".caprmedio_synthetic_project/000_CAPRMEDIO_framework/02_SYNTHETIC_MIDDLE"
delivery_path = "synthetic/repair-rehearsal"
authority_mode = "strict"

[[scope_units]]
scope_unit_name = "SYNTHETIC"
parent = "SYNTHETIC_MIDDLE"
scope_unit_type = "Ordered"
scope_unit_label = "Synthetic rehearsal candidate scope"
structural_level = 3
local_order = 1
navigational_order_number = 3
authority_path = ".caprmedio_synthetic_project/000_CAPRMEDIO_framework/03_SYNTHETIC"
delivery_path = "synthetic/repair-rehearsal"
authority_mode = "strict"
""",
        control_root / "caprmedio_synthetic_project_settings.toml": """[project]
name = "synthetic_project"

[artifacts.identity]
project_prefix = "SYN"
""",
        control_root / "operators_registry.toml": """[[operators]]
name = "Synthetic Fixture Operator"
role = "fixture reviewer"
""",
        framework_root / "caprmedio_framework_settings.toml": """[confidence]
necessary_information_threshold_percent = 99
semantic_resolution_threshold_percent = 99

[authority_modes]
default = "strict"

[interaction]
reporting_mode = "silent"

[artifacts]
creation_strictness = "medium"

[implementation]
retry_limit = 0

[atom_validation]
max_candidates = 4
max_file_bytes = 1048576
max_total_read_bytes = 4194304
timeout_seconds = 60
max_findings = 100

[rmed_review]
max_atoms = 4
target_minutes = 10
""",
        default_root / "caprmedio_framework_default_settings.toml": """[confidence]
necessary_information_threshold_percent = 99
semantic_resolution_threshold_percent = 99

[authority_modes]
default = "strict"

[interaction]
reporting_mode = "silent"

[artifacts]
creation_strictness = "medium"

[implementation]
retry_limit = 0

[atom_validation]
max_candidates = 4
max_file_bytes = 1048576
max_total_read_bytes = 4194304
timeout_seconds = 60
max_findings = 100

[rmed_review]
max_atoms = 4
target_minutes = 10
""",
    }
    for path, text in values.items():
        path.write_text(text)
    return {
        "project_structure": ".caprmedio_synthetic_project/project_structure.toml",
        "project_settings": ".caprmedio_synthetic_project/caprmedio_synthetic_project_settings.toml",
        "operators_registry": ".caprmedio_synthetic_project/operators_registry.toml",
        "framework_instance_settings": ".caprmedio_synthetic_project/000_CAPRMEDIO_framework/caprmedio_framework_settings.toml",
        "default_settings": ".caprmedio_synthetic_project/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/caprmedio_framework_default_settings.toml",
    }


def build(output: Path) -> None:
    if output.exists():
        raise FileExistsError(f"output must be absent: {output}")
    output.mkdir(parents=True)
    resources = write_resources(output)
    candidates = []
    for spec in CASES:
        original, raw = rewrite_fixture(spec)
        props = metadata(raw)
        if props.get("atom_id") != spec["atom_id"] or props.get("version") != spec["version"]:
            raise ValueError(f"safe parser rejected fixture metadata: {spec['fixture']}")
        candidate_path = spec["carrier_path"]
        if not candidate_path.endswith(".md") or ".." in Path(candidate_path).parts:
            raise ValueError(f"unsafe synthetic Carrier path: {candidate_path}")
        carrier = output / candidate_path
        carrier.parent.mkdir(parents=True, exist_ok=True)
        carrier.write_text(raw)
        candidates.append((spec, original, bound(candidate_path, props["atom_id"], props["version"], raw)))
    definitions = [
        synthetic_authority("SYN-DEF-001", "Widget", "a Widget **means** one synthetic display component."),
        synthetic_authority("SYN-DEF-002", "Widget/Color", "Widget/Color **means** the explicit display Color of one Widget."),
        synthetic_authority("SYN-DEF-003", "Widget/Color: Blue", "Widget/Color: Blue **means** the admitted Blue Color value."),
        synthetic_authority("SYN-DEF-004", "Widget/Size", "Widget/Size **means** the explicit display Size of one Widget."),
        synthetic_authority("SYN-DEF-005", "Widget/Size: Large", "Widget/Size: Large **means** the admitted Large Size value."),
        synthetic_authority("SYN-DEF-006", "Widget/Status", "Widget/Status **means** the explicit review Status of one Widget."),
        synthetic_authority("SYN-DEF-007", "Widget/Status: Active", "Widget/Status: Active **means** the admitted Active Status value."),
        synthetic_authority("SYN-DEF-008", "Operator", "an Operator **means** one human reviewing a synthetic Widget."),
    ]
    principle = synthetic_authority(
        "SYN-R-900", "Synthetic Project",
        "the Synthetic Project **must** preserve explicit fixture properties and their stated conditions.",
        current_scope_unit="synthetic_project", claim_target_scope_unit="synthetic_project",
        local_tier="Principle", global_tier=0,
    )
    token_mapping = synthetic_authority(
        "SYN-D-901", "Atom/Scope/Filename Token",
        "the Project Configuration selects SYNTHETIC as the filename token for the Scope Unit named SYNTHETIC.",
        role="Delivery",
    )
    baseline, repair_bindings = baseline_sources()
    candidate_rows = [row for _, _, row in candidates]
    authority = baseline + definitions + [principle, token_mapping]
    context = prepare_context({
        "confidence_threshold": 0.99,
        "sources": authority + candidate_rows,
        "authority_bindings": [row["binding"] for row in authority],
        "principle_admissions": [{"binding": principle["binding"],
            "applicable_to": [row["binding"]["path"] for row in candidate_rows],
            "reason": "Explicit mock Principle for this closed synthetic rehearsal.",
            "provenance": "Fixture declaration; never a real Project admission."}],
        "synthetic_fixture_profile": {
            "name": "fixture-only-repair-rehearsal",
            "project_scope_unit": "PROJECT",
            "candidate_scope_unit": "SYNTHETIC",
            "tier_derivation": {
                "PROJECT": {"principle": 0, "core": 1, "standard": 2},
                "SYNTHETIC_ROOT": {"core": 3, "general": 4, "standard": 5},
                "SYNTHETIC_MIDDLE": {"core": 6, "general": 7, "standard": 8},
                "SYNTHETIC": {"core": 9, "general": 10, "standard": 11},
            },
            "declaration_basis": ["CA-R-1389", "CA-R-1390", "CA-R-1391", "CA-R-1442", "CA-R-1484"],
            "policy_note": "Fixture declarations bind only the synthetic carriers; they do not waive contract checks, supply verdicts, or replace baseline authority.",
        },
        "scope_of_review": "Synthetic repair rehearsal only; no real Project state, carrier, identity, or permission is implied.",
        "prompts": {"cce": (REVIEW_ROOT / "evaluate_cce.prompt.md").read_text(),
                    "properties": (REVIEW_ROOT / "evaluate_properties.prompt.md").read_text(),
                    "coherence": (REVIEW_ROOT / "evaluate_coherence.prompt.md").read_text()},
    }, root=output, resources=resources)
    context_sha = ReviewContext(context).sha256
    (output / "context.json").write_text(json.dumps(context, indent=2) + "\n")
    (output / "packets").mkdir()
    input_cases = []
    for ordinal, (spec, original, candidate) in enumerate(candidates, 1):
        packet = {"ordinal": ordinal, "case_id": spec["id"], "fixture_origin": {
                    "path": str((FIXTURE_ROOT / spec["fixture"]).relative_to(REPOSITORY_ROOT)),
                    "sha256": digest(original)}, "source": candidate["binding"], "raw": candidate["text"],
                  "properties": metadata(candidate["text"]), "body_sections": body_sections(candidate["text"]),
                  "context_sha256": context_sha,
                  "pre_evaluation": {group: {"required_checks": list(GROUPS[group]),
                                      "status": "pending_independent_evaluation", "part": None}
                                     for group in ("cce", "properties", "coherence")}}
        (output / "packets" / f"{ordinal:04}.json").write_text(json.dumps(packet, indent=2) + "\n")
        input_cases.append({"case_id": spec["id"], "source": candidate["binding"],
            "permitted_disposition": spec["disposition"], "permission": {
                "paths": spec["permission_paths"], "dispositions": [spec["disposition"]],
                "provenance": "Synthetic rehearsal preview permission; no mutation authorization."},
            "reserved_successor_ids": spec["reserved_successor_ids"],
            "preservation_requirements": spec["preservation"],
            "evaluation_required": ["cce", "properties", "coherence"]})
    (output / "repair-inputs.json").write_text(json.dumps({
        "purpose": "Complete inputs for rehearsal only; not evaluations, proposals, or source-mutation authority.",
        "context_sha256": context_sha, "repair_authority_bindings": repair_bindings, "cases": input_cases,
    }, indent=2) + "\n")
    (output / "README.md").write_text(
        "# Synthetic repair rehearsal\n\nThis output has real bound baseline prompts and evaluator authorities, "
        "the active repair authorities, explicit mock resources, an admitted mock Principle, permissions, and "
        "reserved successor IDs. Candidate paths use the carried ID and Summary slug and are placed inside the "
        "declared synthetic Scope Unit authority path; exact Project Configuration token mappings remain for the "
        "independent validation/evaluation evidence. It has no verdicts, evaluation parts, merged evaluations, or repair proposals. "
        "Independent reviewers must produce CCE, Properties, and Coherence contract-v4 parts before a fixer can rehearse a proposal.\n")
    print(json.dumps({"output": str(output), "cases": len(input_cases), "context_sha256": context_sha,
                      "preflight": context["preflight"]}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    build(parser.parse_args().output)
