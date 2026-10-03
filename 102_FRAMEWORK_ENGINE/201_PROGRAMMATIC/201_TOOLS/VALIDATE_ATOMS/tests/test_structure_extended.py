"""Acceptance cases for source-bound structure, tier, status and address checks."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import sys
from typing import ClassVar
import unittest

HERE = Path(__file__).resolve().parent
TOOL = HERE.parent
sys.path.insert(0, str(TOOL))

from validate_atoms_workers.authority import AuthorityContext, Obligation, Record  # noqa: E402
from validate_atoms_workers.check_support import Check  # noqa: E402
from validate_atoms_workers.check_structure_extended import ADAPTERS  # noqa: E402
from validate_atoms_workers.parsing import parse_carrier  # noqa: E402


def sources() -> list[Record]:
    rows: dict[str, tuple[Record, Path]] = {}
    for name, fixture_folder in (
        ("registry.json", "authority_checks"),
        ("structure_authority.json", "structure_authority"),
        ("schema_authority.json", "schema_authority"),
    ):
        manifest = json.loads((TOOL / "validate_atoms_workers" / name).read_text())["sources"]
        rows.update(
            {
                identifier: (entry, HERE / "fixtures" / fixture_folder / f"{identifier}.md")
                for identifier, entry in manifest.items()
            }
        )
    found: list[Record] = []
    for identifier, (entry, path) in rows.items():
        raw = path.read_bytes()
        if hashlib.sha256(raw).hexdigest() != entry["sha256"]:
            raise AssertionError("Fixture must match its exact authority pin: " + identifier)
        found.append(
            dict(
                binding=dict(
                    atom_id=identifier,
                    version=entry["version"],
                    path=str(path),
                    sha256=hashlib.sha256(raw).hexdigest(),
                ),
                text=raw.decode(),
                metadata=parse_carrier(raw, path).metadata,
            )
        )
    return found


def unit(name: str = "CORE", parent: str = "PROJECT", level: int = 1) -> Record:
    return dict(
        scope_unit_name=name,
        parent=parent,
        scope_unit_type="Unordered",
        scope_unit_label="Layer",
        structural_level=level,
        navigational_order_number=level,
        authority_path=f".caprmedio_demo/{name}",
        delivery_path=f"src/{name}",
    )


class StructureExtendedTest(unittest.TestCase):
    authorities: ClassVar[list[Record]]

    @classmethod
    def setUpClass(cls) -> None:
        cls.authorities = sources()

    def setUp(self) -> None:
        self.metadata: Record = dict(
            atom_id="EX-R-1",
            content_role="Requirement",
            type="Requirement",
            current_scope_unit="CORE",
            claim_target_scope_unit="CORE",
            local_tier="Core",
            global_tier=3,
            status="Active",
            version=1,
        )
        self.structure: Record = dict(schema_version=1, scope_units=[unit()])
        self.path = Path(
            "/example/.caprmedio_demo/CORE/04_requirement/EX-R-1-CORE-CORE-REQUIREMENT--test-claim.md"
        )
        self.body = "# Summary\n\nTest claim\n\n## Claim\n\nA requirement.\n"

    def check(
        self,
        code: str,
        *,
        metadata: Record | None = None,
        inputs: Record | None = None,
        sources_override: list[Record] | None = None,
        unclassified: bool = False,
    ) -> Check:
        context = AuthorityContext(
            bindings=[],
            required=0,
            supported=0,
            unsupported=0,
            gaps=[],
            obligations=(),
            domains={
                "domain.status.requirement": ("Draft", "Active", "Archived"),
                "domain.status.method": ("Draft", "Active", "Archived"),
                "domain.status.evaluation": ("Draft", "Active", "Archived"),
                "domain.status.delivery": ("Draft", "Active", "Archived"),
                "domain.status.concern": ("draft", "active", "resolved", "canceled"),
                "domain.status.plan": ("Active", "Backlog", "Done", "Canceled", "Archived"),
            },
            unclassified_sources=unclassified,
        )
        check = Check(Obligation(code, [], True, "test"), context)
        check.inputs = dict(
            path=self.path,
            structure=self.structure,
            request={
                "project_structure": {"path": "/example/.caprmedio_demo/project_structure.toml"}
            },
            sources=self.authorities if sources_override is None else sources_override,
            references=[],
            reference_complete=True,
        )
        if inputs:
            check.inputs.update(inputs)
        ADAPTERS[code](self.metadata if metadata is None else metadata, self.body, check)
        return check

    def test_owner_resolves_declared_scope_independently_of_author(self) -> None:
        self.assertFalse(self.check("owner.resolution").gaps)

        # Structural Scope Unit ownership does not borrow Actor/Author identity.
        known = self.check(
            "owner.resolution", metadata={**self.metadata, "author": "Different Operator"}
        )
        self.assertFalse(known.gaps)

    def test_unknown_owner_requires_identity_but_stays_unresolved_without_external_admission(self) -> None:
        bad = self.check(
            "owner.resolution",
            metadata={
                **self.metadata,
                "current_scope_unit": "Test Operator",
                "author": "Test Operator",
            },
            inputs={"operators_registry": {"names": frozenset({"Test Operator"}), "error": None}},
        )
        self.assertTrue(bad.gaps)  # Registry identity alone cannot prove external placement.
        self.assertFalse(bad.findings)
        self.assertFalse(any(gap["property"] == "authority" for gap in bad.gaps))

    def test_unknown_owner_requires_exact_author_and_registered_operator(self) -> None:
        for author, registry in (
            ("Other Operator", frozenset({"Test Operator", "Other Operator"})),
            ("Test Operator", frozenset({"Other Operator"})),
            (None, frozenset({"Test Operator"})),
        ):
            with self.subTest(author=author, registry=registry):
                checked = self.check(
                    "owner.resolution",
                    metadata={
                        **self.metadata,
                        "current_scope_unit": "Test Operator",
                        "author": author,
                    },
                    inputs={"operators_registry": {"names": registry, "error": None}},
                )
                self.assertTrue(checked.gaps)
                self.assertFalse(checked.findings)

    def test_owner_missing_or_list_is_not_recovered_from_path(self) -> None:
        for owner in (None, ["CORE"], ""):
            bad = self.check(
                "owner.resolution", metadata={**self.metadata, "current_scope_unit": owner}
            )
            self.assertTrue(bad.findings)

    def test_structure_missing_duplicate_or_cycle_is_a_gap(self) -> None:
        for structure in (
            None,
            {"schema_version": 1, "scope_units": [unit(), unit()]},
            {"schema_version": 1, "scope_units": [unit(parent="CORE")]},
            {"schema_version": True, "scope_units": [unit()]},
        ):
            self.assertTrue(self.check("owner.resolution", inputs={"structure": structure}).gaps)

    def test_structure_path_escape_is_not_followed(self) -> None:
        row = unit()
        row["authority_path"] = "../../outside"
        check = self.check(
            "owner.resolution", inputs={"structure": dict(schema_version=1, scope_units=[row])}
        )
        self.assertTrue(check.gaps)

    def test_target_resolves_and_requires_relational_admission(self) -> None:
        self.assertFalse(self.check("target.resolution").gaps)
        self.structure["scope_units"].append(unit("OTHER"))
        bad = self.check(
            "target.resolution", metadata={**self.metadata, "claim_target_scope_unit": "OTHER"}
        )
        self.assertTrue(bad.findings)
        good = self.check(
            "target.resolution",
            metadata={**self.metadata, "type": "Demand", "claim_target_scope_unit": "OTHER"},
        )
        self.assertFalse(good.findings)
        self.assertFalse(good.gaps)

    def test_target_is_not_inferred_from_scope_body_or_file_address(self) -> None:
        self.body = "# Summary\nTarget rule\n## Scope\nCORE\n## Claim\nA rule.\n## Details\n"
        for value in (None, "", ["CORE"]):
            checked = self.check("target.resolution", metadata={
                **self.metadata, "claim_target_scope_unit": value})
            self.assertTrue(checked.findings)
        # Prose applicability is not a structural name and need not equal it.
        self.body = "# Summary\nTarget rule\n## Scope\nAll active Markdown Atoms.\n## Claim\nA rule.\n## Details\n"
        checked = self.check("target.resolution")
        self.assertFalse(checked.findings)
        self.assertFalse(checked.gaps)

    def test_v7_target_rule_is_source_bound_and_rejects_duplicate_property(self) -> None:
        authority = next(row for row in self.authorities if row["binding"]["atom_id"] == "CA-D-482")
        self.assertEqual(authority["binding"]["version"], 7)
        checked = self.check("target.resolution", metadata={**self.metadata, "claim_scope": "CORE"})
        self.assertTrue(checked.findings)

    def test_unknown_target_and_implicit_project_are_gaps(self) -> None:
        for value in ("UNKNOWN", "demo", "PROJECT"):
            self.assertTrue(
                self.check(
                    "target.resolution",
                    metadata={**self.metadata, "claim_target_scope_unit": value},
                ).gaps
            )

    def test_tier_uses_declared_parent_depth(self) -> None:
        self.assertFalse(self.check("tier.resolution").gaps)
        for value in (0, 4, True):
            self.assertTrue(
                self.check(
                    "tier.resolution", metadata={**self.metadata, "global_tier": value}
                ).findings
            )
        self.structure["scope_units"].append(unit("CHILD", "CORE", 2))
        child = {
            **self.metadata,
            "current_scope_unit": "CHILD",
            "local_tier": "Standard",
            "global_tier": 8,
        }
        self.assertFalse(self.check("tier.resolution", metadata=child).findings)

    def test_tier_requires_carried_value_and_restricts_change_roles(self) -> None:
        self.assertTrue(
            self.check("tier.resolution", metadata={**self.metadata, "local_tier": None}).findings
        )
        self.assertTrue(
            self.check(
                "tier.resolution", metadata={**self.metadata, "content_role": "Plan"}
            ).findings
        )
        self.assertTrue(
            self.check("tier.resolution", metadata={**self.metadata, "type": "Goal"}).gaps
        )

    def test_status_is_case_exact_and_qualified(self) -> None:
        self.assertFalse(self.check("status.resolution").gaps)
        self.assertTrue(
            self.check("status.resolution", metadata={**self.metadata, "status": "active"}).findings
        )
        self.assertTrue(
            self.check("status.resolution", metadata={**self.metadata, "type": None}).gaps
        )
        concern = {
            **self.metadata,
            "content_role": "Concern",
            "type": "Question",
            "status": "active",
        }
        self.assertFalse(self.check("status.resolution", metadata=concern).findings)
        self.assertFalse(self.check("status.resolution", metadata=concern).gaps)

    def test_ordinary_rmd_without_type_keeps_status_and_tier_resolved(self) -> None:
        for role in ("Requirement", "Method", "Delivery"):
            with self.subTest(role=role):
                metadata = {key: value for key, value in self.metadata.items() if key != "type"}
                metadata["content_role"] = role
                self.assertFalse(self.check("status.resolution", metadata=metadata).gaps)
                self.assertFalse(self.check("tier.resolution", metadata=metadata).gaps)

    def test_status_unknown_specific_model_does_not_pass(self) -> None:
        self.assertTrue(
            self.check("status.resolution", metadata={**self.metadata, "type": "New Type"}).gaps
        )

    def test_evaluation_approach_uses_admitted_evaluation_role_status_domain(self) -> None:
        approach = {
            **self.metadata,
            "content_role": "Evaluation",
            "type": "Evaluation Approach",
        }
        for status in ("Draft", "Active", "Archived"):
            with self.subTest(status=status):
                check = self.check("status.resolution", metadata={**approach, "status": status})
                self.assertFalse(check.findings)
                self.assertFalse(check.gaps)
        bad = self.check("status.resolution", metadata={**approach, "status": "Deprecated"})
        self.assertTrue(bad.findings)
        self.assertFalse(bad.gaps)

    def test_evaluation_approach_requires_exact_type_admission(self) -> None:
        approach = {
            **self.metadata,
            "content_role": "Evaluation",
            "type": "Evaluation Approach",
        }
        sources = [
            source
            for source in self.authorities
            if source["binding"]["atom_id"] != "CAPRMEDIO-R-793"
        ]
        check = self.check("status.resolution", metadata=approach, sources_override=sources)
        self.assertTrue(check.gaps)
        self.assertFalse(check.findings)

    def test_evaluation_approach_blocks_unresolved_exact_narrower_status_source(self) -> None:
        approach = {
            **self.metadata,
            "content_role": "Evaluation",
            "type": "Evaluation Approach",
        }
        source: Record = dict(
            binding={"atom_id": "EXT-R-1"},
            metadata={
                "subjects": {
                    "governs": "Atom/Content Role: Evaluation/Type: Evaluation Approach/Status"
                }
            },
        )
        check = self.check(
            "status.resolution",
            metadata=approach,
            sources_override=[*self.authorities, source],
            unclassified=True,
        )
        self.assertTrue(check.gaps)
        self.assertFalse(check.findings)

    def test_status_placement_checks_carried_state(self) -> None:
        self.assertTrue(self.check("status.placement").gaps)
        archived = {**self.metadata, "status": "Archived"}
        self.assertFalse(self.check("status.placement", metadata=archived).findings)
        good = self.check(
            "status.placement",
            metadata=archived,
            inputs={"path": self.path.parent / "archived" / self.path.name},
        )
        self.assertFalse(good.findings)
        self.assertTrue(good.gaps)  # No more-specific Type placement registry is supplied.

    def test_plan_placement_uses_specific_mapping(self) -> None:
        plan = {**self.metadata, "content_role": "Plan", "type": "Plan", "status": "Backlog"}
        path = self.path.parents[1] / "03_plan/001_backlog/EX-P-1-PLAN--test-claim.md"
        good = self.check("status.placement", metadata=plan, inputs={"path": path})
        self.assertFalse(good.findings)
        self.assertFalse(good.gaps)
        bad = self.check(
            "status.placement", metadata=plan, inputs={"path": path.parent.parent / path.name}
        )
        self.assertTrue(bad.findings)
        nested = {**plan, "relations": {"is_decomposition_of": ["EX-P-9"]}}
        self.assertTrue(self.check("status.placement", metadata=nested, inputs={"path": path}).gaps)

    def test_matching_plan_bundle_directory_is_not_a_parent_plan(self) -> None:
        plan = {**self.metadata, "content_role": "Plan", "type": "Plan", "status": "Active"}
        stem = "EX-P-1--test-claim"
        path = self.path.parents[1] / "03_plan" / stem / (stem + ".md")
        check = self.check("status.placement", metadata=plan, inputs={"path": path})
        self.assertFalse(check.findings)
        self.assertFalse(check.gaps)

    def test_projected_representations_do_not_use_authored_address_rules(self) -> None:
        metadata = {**self.metadata, "projection": {"source_carrier_path": "../../source.md"}}
        for code in ("status.placement", "address.consistency"):
            check = self.check(
                code, metadata=metadata, inputs={"path": Path("/projection/other.md")}
            )
            self.assertFalse(check.findings)
            self.assertTrue(check.gaps)

    def test_unclassified_status_context_is_scoped_by_qualified_path(self) -> None:
        source: Record = dict(
            binding={"atom_id": "EXT-R-1"}, metadata={"subjects": {"governs": "Rendering/Color"}}
        )
        check = self.check(
            "status.resolution", sources_override=[*self.authorities, source], unclassified=True
        )
        self.assertFalse(check.gaps)
        source["metadata"]["subjects"]["governs"] = (
            "Atom/Content Role: Requirement/Type: Requirement/Status"
        )
        check = self.check(
            "status.resolution", sources_override=[*self.authorities, source], unclassified=True
        )
        self.assertTrue(check.gaps)

    def test_unclassified_generic_status_authority_does_not_override_role_domain(self) -> None:
        source: Record = dict(
            binding={"atom_id": "EXT-R-1"},
            metadata={"subjects": {"governs": "Artifact/Revision/Status"}},
        )
        check = self.check(
            "status.resolution", sources_override=[*self.authorities, source], unclassified=True
        )
        self.assertFalse(check.gaps)

    def test_address_detects_identity_and_slug_mismatches_without_repair(self) -> None:
        before = copy.deepcopy(self.metadata)
        check = self.check(
            "address.consistency",
            inputs={"path": self.path.with_name("EX-R-2-CORE-CORE-REQUIREMENT--wrong.md")},
        )
        self.assertTrue(any(f["property"] == "atom_id" for f in check.findings))
        self.assertTrue(any(f["property"] == "Summary" for f in check.findings))
        self.assertEqual(before, self.metadata)

    def test_address_unsupported_scope_token_registry_remains_gap(self) -> None:
        check = self.check("address.consistency")
        self.assertFalse(check.findings)
        self.assertTrue(check.gaps)

    def test_address_does_not_require_a_filename_type_segment_when_type_is_omitted(self) -> None:
        metadata = {key: value for key, value in self.metadata.items() if key != "type"}
        path = self.path.with_name("EX-R-1-CORE-CORE--test-claim.md")
        check = self.check("address.consistency", metadata=metadata, inputs={"path": path})
        self.assertFalse(check.findings)
        self.assertTrue(check.gaps)  # Scope-token Configuration is intentionally not inferred.
        self.assertFalse(any(gap["property"] == "type" for gap in check.gaps))

    def test_source_absent_or_changed_cannot_pass(self) -> None:
        changed = copy.deepcopy(self.authorities)
        source = next(s for s in changed if s["binding"]["atom_id"] == "CA-D-442")
        source["text"] += "\nchanged\n"
        for values in ([], changed):
            self.assertTrue(self.check("owner.resolution", sources_override=values).gaps)

    def test_duplicate_authority_is_a_gap(self) -> None:
        duplicate = next(s for s in self.authorities if s["binding"]["atom_id"] == "CA-D-442")
        check = self.check("owner.resolution", sources_override=[*self.authorities, duplicate])
        self.assertTrue(check.gaps)

    def test_unknown_structure_fields_and_wrong_depth_are_not_ignored(self) -> None:
        for changes in (
            {"structural_level": 99},
            {"node_id": "unadmitted"},
            {"authority_path": ".caprmedio_other/CORE"},
        ):
            row = {**unit(), **changes}
            check = self.check(
                "address.consistency",
                inputs={"structure": dict(schema_version=1, scope_units=[row])},
            )
            self.assertTrue(check.gaps)

    def test_no_adapter_reads_or_mutates_candidate(self) -> None:
        class NoRead:
            def read(self, path: Path) -> bytes:
                raise AssertionError("Adapter must use supplied context, not unbound reads")

        for code in ADAPTERS:
            before = copy.deepcopy(self.metadata)
            self.check(code, inputs={"reader": NoRead()})
            self.assertEqual(before, self.metadata)


if __name__ == "__main__":
    unittest.main()
