# Evaluation case — Make DSET self-hosting and skills thin

Accepted qualitative criteria remain owned by their layer plans. This Change
runs them independently from deterministic tests and records disagreements by
case and criterion.

| Owning plan | Applicable Eval IDs |
|---|---|
| `plan-evaluations.md` | `CAPRMEDIO-EVALUATION-CASE-META-008..009` |
| `plan-evaluations.md` | `CAPRMEDIO-EVALUATION-CASE-GOV-007..022`, `CAPRMEDIO-EVALUATION-CASE-GOV-025`, `CAPRMEDIO-GOV-EVAL-012--typed-artifact-relations-evaluation-case`, `CAPRMEDIO-GOV-EVAL-014--verbose-project-settings-evaluation-case..029`, `CAPRMEDIO-GOV-EVAL-018--runtime-boundary-interpretability..034` |
| `plan-evaluations.md` | `CAPRMEDIO-SPEC-TOOLS-EVAL-044--typescript-candidate-evaluation-case..004` |
| `plan-evaluations.md` | `CAPRMEDIO-EVALUATION-CASE-SKILL-002..008`, `CAPRMEDIO-SPEC-SKILLS-EVAL-049--implementation-preparation-modes..011` |
| `plan-evaluations.md` | `CAPRMEDIO-EVALUATION-CASE-OPS-002..003`, `CAPRMEDIO-FIELD-EVAL-058--delivery-artifact-boundaries` |

Connected accepted IDs are `CAPRMEDIO-EVALUATION-CASE-META-008`, `CAPRMEDIO-EVALUATION-CASE-META-009`,
`CAPRMEDIO-EVALUATION-CASE-GOV-007`, `CAPRMEDIO-EVALUATION-CASE-GOV-008`, `CAPRMEDIO-EVALUATION-CASE-GOV-009`,
`CAPRMEDIO-EVALUATION-CASE-GOV-010`, `CAPRMEDIO-EVALUATION-CASE-GOV-011`, `CAPRMEDIO-EVALUATION-CASE-GOV-012`,
`CAPRMEDIO-EVALUATION-CASE-GOV-013`,
`CAPRMEDIO-EVALUATION-CASE-GOV-014`, `CAPRMEDIO-EVALUATION-CASE-GOV-015`, `CAPRMEDIO-EVALUATION-CASE-GOV-016`,
`CAPRMEDIO-EVALUATION-CASE-GOV-017`,
`CAPRMEDIO-EVALUATION-CASE-GOV-018`,
`CAPRMEDIO-GOV-EVAL-011--mece-artifact-classification`,
`CAPRMEDIO-EVALUATION-CASE-GOV-020`, `CAPRMEDIO-EVALUATION-CASE-GOV-021`, `CAPRMEDIO-EVALUATION-CASE-GOV-022`,
`CAPRMEDIO-EVALUATION-CASE-GOV-025`, `CAPRMEDIO-GOV-EVAL-012--typed-artifact-relations-evaluation-case`,
`CAPRMEDIO-SPEC-TOOLS-EVAL-044--typescript-candidate-evaluation-case`,
`CAPRMEDIO-SPEC-TOOLS-EVAL-045--typescript-profile-instantiation-evaluation-case`,
`CAPRMEDIO-EVALUATION-CASE-SKILL-002`,
`CAPRMEDIO-EVALUATION-CASE-SKILL-003`, `CAPRMEDIO-EVALUATION-CASE-SKILL-004`, `CAPRMEDIO-EVALUATION-CASE-SKILL-005`,
`CAPRMEDIO-EVALUATION-CASE-SKILL-006`, `CAPRMEDIO-EVALUATION-CASE-SKILL-007`, `CAPRMEDIO-EVALUATION-CASE-SKILL-008`,
	`CAPRMEDIO-SPEC-SKILLS-EVAL-049--implementation-preparation-modes`, `CAPRMEDIO-EVALUATION-CASE-SKILL-011`,
`CAPRMEDIO-EVALUATION-CASE-OPS-002`, `CAPRMEDIO-EVALUATION-CASE-OPS-003`, and `CAPRMEDIO-FIELD-EVAL-058--delivery-artifact-boundaries`.

## Change-only qualitative proof

| Eval ID | Scenario | Threshold |
|---|---|---|
| `CAPRMEDIO-EVALUATION-CASE-SKILL-009` | Clean declared Claude, Codex, and other-host fixtures use the published installation path. | Every operator installs or links the real skill, confirms discovery, invokes its trigger, reaches local rules, and identifies the stop boundary. |
| `CAPRMEDIO-EVALUATION-CASE-TOOL-005` | Operators run the utility workflow on every declared platform, including spaces, Unicode, failures, and interrupted writes. | Outcomes are equivalent and safe; any narrower applicability is visible before execution. |
| `CAPRMEDIO-EVALUATION-CASE-TOOL-006` | Reviewers assess allowed, denied, unknown-registry, incompatible-license, provenance-drift, and expired-exception dependencies. | Every reviewer reaches the same accept/stop result from the authoritative rule and does not invent approval. |
| `CAPRMEDIO-EVALUATION-CASE-OPS-008` | A cold operator investigates the implementing PR's live GitHub workflow/run/check and protected-target state. | Every operator binds evidence to the actual PR SHA and selects a safe merge, block, or retry action without bypassing protection. |
| `CAPRMEDIO-EVALUATION-CASE-OPS-009` | Projects use shared integration branches and optional isolated worktrees across concurrent Changes and one protected PR. | Every reviewer identifies branch roles, actual workspace mode, and proof owner without requiring a worktree by default, merging Change identities, or creating permanent layer branches. |

Use at least two independent reviewers where interpretation matters. Correct the
earliest ambiguous owner and rerun the failed case; do not average a blocker
into a pass.
