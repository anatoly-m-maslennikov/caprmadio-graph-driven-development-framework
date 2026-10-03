#!/usr/bin/env python3
"""Split combined Project Layer boundary Atoms into scopes and Contracts.

Usage:
    python3 002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/migrations/split_layer_scope_contract_atoms.py
    python3 002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/migrations/split_layer_scope_contract_atoms.py --apply

The default mode is read-only. The migration fails closed on mixed states,
preserves the six source carriers byte-for-byte in archive, and is idempotent.
"""

from __future__ import annotations

import argparse
import os
import sys
from dataclasses import dataclass
from pathlib import Path

_PROJECT_TOOLS_ROOT = Path(__file__).resolve().parents[1]
if str(_PROJECT_TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_TOOLS_ROOT))
from project_runtime import atomic_tempfile  # noqa: E402


PROJECT_REQUIREMENTS = Path(".caprmedio/04_requirement")
PROJECT_ARCHIVE = PROJECT_REQUIREMENTS / "archive"
GOV_REQUIREMENTS = Path(".caprmedio/200_LAYER_2_GOV/04_requirement")
SESSION_ID = "codex:019f591f-04f6-70f2-8de7-828b7cccc69d"
PROJECT_PARENT = "CAPRMEDIO-REQU-073--assign-feature-scope-ownership-to-each-layer"
RELATION_PARENT = "CAPRMEDIO-META-REQU-084--relational-artifacts-declare-endpoints"
GOV_CARRIER_PARENT = "CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully"
LAYER_TITLES = {
    "meta": "META",
    "gov": "GOV",
    "spec": "SPEC",
    "implementation": "implementation",
    "delivery": "delivery",
    "ops": "Ops",
}


@dataclass(frozen=True)
class Layer:
    key: str
    old_id: int
    requirement_id: int
    scope_summary: str
    scope_claim: str
    providers: tuple[str, ...]

    @property
    def old_stem(self) -> str:
        return f"CAPRMEDIO-REQUIREMENT-{self.old_id:03d}-define-{self.key}-layer-scope-and-contracts"

    @property
    def scope_stem(self) -> str:
        return f"CAPRMEDIO-REQUIREMENT-{self.requirement_id:03d}-{self.scope_summary}"


LAYERS = (
    Layer(
        "meta",
        175,
        208,
        "define-meta-layer-scope",
        "META owns the project ontology: canonical vocabulary, semantic axes and distinctions, Content-role and Artifact-form meanings, applicability tiers, relation meanings, structural interpretation, and construct-admission rules; concrete Layer topology, carrier mechanics, project behavior, and realization remain outside its scope.",
        ("project",),
    ),
    Layer(
        "gov",
        176,
        209,
        "define-gov-layer-scope",
        "GOV owns governed-carrier mechanics: identity, naming, placement, frontmatter, provenance, relation encoding, lifecycle, catalogs, and structural validation; META meanings, project behavior, and realization remain outside its scope.",
        ("project", "meta_layer"),
    ),
    Layer(
        "spec",
        177,
        210,
        "define-spec-layer-scope",
        "SPEC owns the applicable Requirement, Method, Evaluation, and Delivery authority that defines what and how the project must realize; realized project artifacts remain outside its scope.",
        ("project", "meta_layer", "gov_layer"),
    ),
    Layer(
        "implementation",
        178,
        211,
        "define-implementation-layer-scope",
        "IMPLEMENTATION owns the actual source, documentation, configuration, tests, evaluations, and other realized project artifacts together with their traceability to applicable SPEC authority.",
        ("project", "meta_layer", "gov_layer", "spec_layer"),
    ),
    Layer(
        "delivery",
        179,
        212,
        "define-delivery-layer-scope",
        "DELIVERY owns packaging, environment, deployment, release, and publication realization of the project.",
        ("project", "meta_layer", "gov_layer", "spec_layer", "implementation_layer"),
    ),
    Layer(
        "ops",
        180,
        213,
        "define-ops-layer-scope",
        "OPS owns post-delivery operation, supportability, runtime investigation, containment, recovery, and factual observation.",
        (
            "project",
            "meta_layer",
            "gov_layer",
            "spec_layer",
            "implementation_layer",
            "delivery_layer",
        ),
    ),
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="apply the migration")
    parser.add_argument("root", nargs="?", default=".", help="repository root")
    return parser.parse_args()


def relations_block(replacements: tuple[str, ...]) -> str:
    replacement_lines = "\n".join(f"    - {stem}" for stem in replacements)
    return (
        "relations:\n"
        "  child_of:\n"
        f"    - {PROJECT_PARENT}\n"
        "  replacement_of:\n"
        f"{replacement_lines}\n"
    )


def requirement_carrier(layer: Layer) -> str:
    title = f"Define {LAYER_TITLES[layer.key]} layer scope"
    return (
        "---\n"
        "subject_scopes:\n"
        "  - scope-topology\n"
        "llm_session_ids:\n"
        f"  - {SESSION_ID}\n"
        f"{relations_block((layer.old_stem,))}"
        "---\n"
        f"# {title}\n\n"
        f"{layer.scope_claim}\n"
    )


def contract_stem(contract_id: int, layer: Layer) -> str:
    return f"CAPRMEDIO-CONTRACT-{contract_id:03d}-supply-cumulative-authority-to-{layer.key}"


def contract_carrier(contract_id: int, layer: Layer) -> str:
    endpoints = "".join(
        "  - role: provider\n"
        f"    identity: {provider}\n"
        "    origin: internal\n"
        for provider in layer.providers
    )
    endpoints += (
        "  - role: consumer\n"
        f"    identity: {layer.key}_layer\n"
        "    origin: internal\n"
    )
    providers = ", ".join(provider.replace("_layer", "").upper() for provider in layer.providers)
    replacements = tuple(
        item.old_stem
        for item in LAYERS
        if item.key == layer.key or f"{item.key}_layer" in layer.providers
    )
    title = f"Supply cumulative authority to {LAYER_TITLES[layer.key]}"
    claim = (
        f"{layer.key.upper()} consumes the complete applicable upstream authority set from "
        f"{providers} through the layer_authority_input Contract."
    )
    return (
        "---\n"
        "subject_scopes:\n"
        "  - scope-topology\n"
        "llm_session_ids:\n"
        f"  - {SESSION_ID}\n"
        f"{relations_block(replacements)}"
        "relation_kind: layer_authority_input\n"
        "endpoints:\n"
        f"{endpoints}"
        "---\n"
        f"# {title}\n\n"
        f"{claim}\n"
    )


def ops_feedback_carrier() -> str:
    return (
        "---\n"
        "subject_scopes:\n"
        "  - scope-topology\n"
        "llm_session_ids:\n"
        f"  - {SESSION_ID}\n"
        f"{relations_block((LAYERS[-1].old_stem,))}"
        "relation_kind: ops_feedback\n"
        "endpoints:\n"
        "  - role: provider\n"
        "    identity: ops_layer\n"
        "    origin: internal\n"
        "  - role: consumer\n"
        "    identity: project_exploration\n"
        "    origin: internal\n"
        "---\n"
        "# Route Ops feedback to project exploration\n\n"
        "OPS may submit factual findings to PROJECT Exploration Mode without gaining authority to rewrite any earlier Layer.\n"
    )


def gov_relation_carrier(
    requirement_id: int,
    summary: str,
    relation_kind: str,
    claim: str,
) -> str:
    title = summary.replace("-", " ").capitalize()
    return (
        "---\n"
        "subject_scopes:\n"
        "  - relation-model\n"
        "llm_session_ids:\n"
        f"  - {SESSION_ID}\n"
        "relations:\n"
        "  child_of:\n"
        f"    - {RELATION_PARENT}\n"
        f"    - {GOV_CARRIER_PARENT}\n"
        "---\n"
        f"# {title}\n\n"
        f"GOV registers {relation_kind} as {claim}.\n"
    )


def desired_files(root: Path) -> dict[Path, str]:
    files: dict[Path, str] = {}
    for contract_id, layer in enumerate(LAYERS, start=2):
        files[root / PROJECT_REQUIREMENTS / f"{layer.scope_stem}.md"] = requirement_carrier(layer)
        stem = contract_stem(contract_id, layer)
        files[root / PROJECT_REQUIREMENTS / f"{stem}.md"] = contract_carrier(contract_id, layer)
    files[root / PROJECT_REQUIREMENTS / "CAPRMEDIO-CNTR-008--route-ops-feedback-to-project-exploration.md"] = ops_feedback_carrier()
    files[root / GOV_REQUIREMENTS / "CAPRMEDIO-GOV-REQU-485--register-layer-authority-input-relation-kind.md"] = gov_relation_carrier(
        188,
        "register-layer-authority-input-relation-kind",
        "layer_authority_input",
        "the cumulative upstream-authority Contract between one Layer consumer and every direct provider declared by PROJECT",
    )
    files[root / GOV_REQUIREMENTS / "CAPRMEDIO-GOV-REQU-352--register-ops-feedback-relation-kind.md"] = gov_relation_carrier(
        189,
        "register-ops-feedback-relation-kind",
        "ops_feedback",
        "the factual feedback Contract from OPS to PROJECT Exploration Mode without backward authority",
    )
    return files


def source_pairs(root: Path) -> list[tuple[Path, Path]]:
    return [
        (
            root / PROJECT_REQUIREMENTS / f"{layer.old_stem}.md",
            root / PROJECT_ARCHIVE / f"{layer.old_stem}.md",
        )
        for layer in LAYERS
    ]


def detect_state(root: Path, desired: dict[Path, str]) -> str:
    pairs = source_pairs(root)
    before = all(source.is_file() and not archive.exists() for source, archive in pairs)
    after = all(not source.exists() and archive.is_file() for source, archive in pairs)
    desired_absent = all(not path.exists() for path in desired)
    desired_exact = all(path.is_file() and path.read_text(encoding="utf-8") == text for path, text in desired.items())
    if before and desired_absent:
        return "pending"
    if after and desired_exact:
        return "applied"
    raise RuntimeError("mixed or unexpected migration state")


def atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = atomic_tempfile(path, "migrations")
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary_name, path)
    except BaseException:
        try:
            os.unlink(temporary_name)
        except FileNotFoundError:
            pass
        raise


def apply_migration(root: Path, desired: dict[Path, str]) -> None:
    preserved = {source: source.read_bytes() for source, _ in source_pairs(root)}
    for path, text in desired.items():
        atomic_write(path, text)
    (root / PROJECT_ARCHIVE).mkdir(parents=True, exist_ok=True)
    for source, archive in source_pairs(root):
        os.replace(source, archive)
        if archive.read_bytes() != preserved[source]:
            raise RuntimeError(f"archived carrier changed: {archive}")


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    desired = desired_files(root)
    state = detect_state(root, desired)
    changes = 0 if state == "applied" else len(desired) + len(LAYERS)
    print(f"state={state} desired={len(desired)} archived={len(LAYERS)} changes={changes}")
    if args.apply and state == "pending":
        apply_migration(root, desired)
        if detect_state(root, desired) != "applied":
            raise RuntimeError("post-apply verification failed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
