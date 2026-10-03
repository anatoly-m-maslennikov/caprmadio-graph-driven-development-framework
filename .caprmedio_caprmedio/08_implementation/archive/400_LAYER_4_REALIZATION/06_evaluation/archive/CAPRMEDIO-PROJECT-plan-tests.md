# Test case — Make DSET self-hosting and skills thin

Accepted deterministic claims remain owned by the layer plans below. This
Change executes and records their applicable proof; it does not redefine them.

| Owning plan | Applicable Test IDs |
|---|---|
| `plan-tests.md` | `CAPRMEDIO-TEST-CASE-META-007`, `CAPRMEDIO-TEST-CASE-META-010..011` |
| `plan-tests.md` | `CAPRMEDIO-TEST-CASE-GOV-014..032`, `CAPRMEDIO-TEST-CASE-GOV-035..036`, `CAPRMEDIO-GOV-EVAL-027--canonical-settings-selections-test-case`, `CAPRMEDIO-GOV-EVAL-030--all-toml-carrier-migration-test-case..044`, `CAPRMEDIO-GOV-EVAL-036--control-runtime-and-scratch-boundaries-test-case..050` |
| `plan-tests.md` | `CAPRMEDIO-TEST-CASE-TOOL-005`, `CAPRMEDIO-TEST-CASE-TOOL-018..019`, `CAPRMEDIO-SPEC-TOOLS-EVAL-047--typescript-candidate-test-case..022` |
| `plan-tests.md` | `CAPRMEDIO-TEST-CASE-SKILL-001..010`, `CAPRMEDIO-SPEC-SKILLS-EVAL-051--lazy-implementation-preparation..013` |
| `plan-tests.md` | `CAPRMEDIO-TEST-CASE-OPS-003..007`, `CAPRMEDIO-FIELD-EVAL-059--delivery-release-role-boundaries` |

Connected accepted IDs are `CAPRMEDIO-TEST-CASE-META-007`, `CAPRMEDIO-TEST-CASE-META-010`,
`CAPRMEDIO-TEST-CASE-META-011`, `CAPRMEDIO-TEST-CASE-GOV-014`, `CAPRMEDIO-TEST-CASE-GOV-015`,
`CAPRMEDIO-TEST-CASE-GOV-016`, `CAPRMEDIO-TEST-CASE-GOV-017`, `CAPRMEDIO-TEST-CASE-GOV-018`,
`CAPRMEDIO-TEST-CASE-GOV-019`, `CAPRMEDIO-TEST-CASE-GOV-020`, `CAPRMEDIO-TEST-CASE-GOV-021`,
`CAPRMEDIO-TEST-CASE-GOV-022`, `CAPRMEDIO-TEST-CASE-GOV-023`, `CAPRMEDIO-TEST-CASE-TOOL-005`,
`CAPRMEDIO-TEST-CASE-GOV-024`, `CAPRMEDIO-TEST-CASE-GOV-025`, `CAPRMEDIO-TEST-CASE-GOV-026`,
`CAPRMEDIO-TEST-CASE-GOV-027`,
`CAPRMEDIO-TEST-CASE-GOV-028`,
`CAPRMEDIO-GOV-EVAL-023--delivery-artifact-classification`,
`CAPRMEDIO-TEST-CASE-GOV-030`, `CAPRMEDIO-TEST-CASE-GOV-031`, `CAPRMEDIO-TEST-CASE-GOV-032`,
`CAPRMEDIO-TEST-CASE-GOV-035`, `CAPRMEDIO-GOV-EVAL-024--typed-artifact-relations-test-case`,
`CAPRMEDIO-GOV-EVAL-027--canonical-settings-selections-test-case`, `CAPRMEDIO-GOV-EVAL-030--all-toml-carrier-migration-test-case`, `CAPRMEDIO-GOV-EVAL-031--complete-toml-cutover-test-case`,
`CAPRMEDIO-TEST-CASE-TOOL-018`, `CAPRMEDIO-TEST-CASE-TOOL-019`,
`CAPRMEDIO-SPEC-TOOLS-EVAL-047--typescript-candidate-test-case`,
`CAPRMEDIO-SPEC-TOOLS-EVAL-048--typescript-profile-instantiation-test-case`,
`CAPRMEDIO-TEST-CASE-SKILL-001`, `CAPRMEDIO-TEST-CASE-SKILL-002`, `CAPRMEDIO-TEST-CASE-SKILL-003`,
`CAPRMEDIO-TEST-CASE-SKILL-004`, `CAPRMEDIO-TEST-CASE-SKILL-005`,
`CAPRMEDIO-TEST-CASE-SKILL-006`, `CAPRMEDIO-TEST-CASE-SKILL-007`, `CAPRMEDIO-TEST-CASE-SKILL-008`,
`CAPRMEDIO-TEST-CASE-SKILL-009`, `CAPRMEDIO-TEST-CASE-SKILL-010`,
	`CAPRMEDIO-SPEC-SKILLS-EVAL-051--lazy-implementation-preparation`, `CAPRMEDIO-TEST-CASE-SKILL-013`,
`CAPRMEDIO-TEST-CASE-OPS-003`, `CAPRMEDIO-TEST-CASE-OPS-004`,
`CAPRMEDIO-TEST-CASE-OPS-005`, `CAPRMEDIO-TEST-CASE-OPS-006`, `CAPRMEDIO-TEST-CASE-OPS-007`, and
`CAPRMEDIO-FIELD-EVAL-059--delivery-release-role-boundaries`.

## Change-only deterministic proof

| Test ID | Contract/Requirement | Assertion |
|---|---|---|
| `CAPRMEDIO-TEST-CASE-SKILL-011` | `CAPRMEDIO-CONTRACT-SKILL-001` | Install/link every declared host-native skill in a clean host fixture and prove discovery, load, invocation, local resolution, handoff, and stop behavior. |
| `CAPRMEDIO-TEST-CASE-TOOL-016` | `CAPRMEDIO-CONTRACT-TOOL-001` | Exercise path, process, shell, encoding, temporary-file, write-safety, and exit behavior on every declared platform or prove honest narrower applicability before execution. |
| `CAPRMEDIO-TEST-CASE-TOOL-017` | `CAPRMEDIO-CONTRACT-TOOL-002` | Enforce dependency registry/version/license/provenance, lockfile authority, allow/deny policy, and bounded unexpired exceptions. |
| `CAPRMEDIO-TEST-CASE-OPS-014` | `CAPRMEDIO-CONTRACT-OPS-001` | Bind real GitHub workflow/run/check evidence to the actual implementing PR head and protected-target disposition. |
| `CAPRMEDIO-TEST-CASE-OPS-015` | `CAPRMEDIO-REQUIREMENT-OPS-012`, `CAPRMEDIO-CONTRACT-OPS-002` | Require integration-branch default scaffolding, accept explicit worktree isolation, allow shared integration branches/PRs, preserve isolated-branch uniqueness, and require head/candidate equality only at verified or archive-ready states. |

Add a failing deterministic proof before repairing every reproducible defect.
