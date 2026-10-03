---
subjects:
  - programmatic-policy
  - method-authority
  - evaluation-coverage
version: 1
updated_at: 2026-08-23 16:05:00
---
# Freeze the PROGRAMMATIC Method and Evaluation target

## Task Scope Resolution

The frozen current-carrier set contains exactly 219 active or draft Method and Evaluation carriers: 31 Methods and 188 Evaluations. It contains 192 active carriers and 27 drafts.

The set is the union of:

1. `.caprmedio/05_method/CA-M-110-CORE-IMPL_METHOD--implement-framework-engine-software-in-python.md`.
2. Every active or draft Method or Evaluation carrier whose Current Scope is `PROGRAMMATIC` or a descendant Scope Unit of `PROGRAMMATIC`, excluding `archive/`, `done/`, and `canceled/`.

The exact resolved carriers, versions, lifecycle states, and dispositions are recorded in the manifest below. Historical `SOFTWARE` terminology in the evidence report is translated to the current `PROGRAMMATIC` Scope; it does not establish a current Scope Unit.

## Current-carrier dispositions

| Disposition | Count | Meaning in this resolution |
|---|---:|---|
| `shared_programmatic_authority` | 1 | Current authority that applies across the Programmatic Feature. |
| `child_scope_specialization` | 218 | Authority or a draft candidate bounded to APPS, TOOLS, or a descendant Scope Unit. |
| `superseded_authority` | 0 | No current carrier is classified as superseded by this resolution. |
| `rejected_candidate` | 0 | No current carrier is rejected by this resolution. |
| `unresolved_operator_decision` | 0 | No current carrier requires this disposition; unresolved report-only candidates are recorded separately. |

CA-M-110 is the only current shared Programmatic Method. Its wording still says `SOFTWARE`; later authoring must update that historical term to `PROGRAMMATIC`. Every other current carrier is a child-scope specialization as written. In particular, the broad TOOLS drafts about deterministic transformations and file or subprocess effects remain TOOLS specializations because their current claims are bounded to Tool managers, workers, or Tool effects. They may inform later shared Methods without already owning shared authority.

No current shared Programmatic Evaluation exists.

## Report-only proposed Method and Evaluation dispositions

These candidates come from `fpf-reports/20260821T161903Z-fpf-sota-harvest-python-engineering-policies.md`. They are evidence-backed candidates, not accepted authority.

| Candidate | Proposed role | Disposition | Receiving use |
|---|---|---|---|
| One supported-Python and tool-configuration boundary | M | unresolved_operator_decision | Decide the supported Python and platform envelope before authoring. |
| Stable current idioms inside the supported boundary | M | shared_programmatic_authority | Author a shared Method after the runtime boundary is decided. |
| Deterministic transformations separated from I/O and lifecycle | M | shared_programmatic_authority | Author a shared Method; retain Tool-specific manager and worker specialization below it. |
| Explicit typed replaceable technical interfaces | M | shared_programmatic_authority | Author a shared Method with conditional applicability at technical boundaries. |
| Planned, validated, bounded, and recoverable file and subprocess effects | M | shared_programmatic_authority | Author a shared Method for Programmatic components that perform those effects. |
| Minimal synchronous Hook work | M | child_scope_specialization | Retain under TOOLS and Hook-specific descendants. |
| Structured contextual logs through one abstraction and schema | M | unresolved_operator_decision | Resolve log ownership against the Work Journal first. |
| Profile and benchmark before accepting performance changes | M | shared_programmatic_authority | Author a shared Method with surface-specific applicability. |
| Ratchet automation and typing without blocking all current work | M | unresolved_operator_decision | Resolve the adoption rule and prerequisite boundary first. |
| Parse, format, lint, and type-check changed Python targets | E | unresolved_operator_decision | Resolve admitted tools, configuration, and changed-code gate behavior first. |
| Evaluate public behavior with applicable unit, integration, property or stateful, and failure cases | E | shared_programmatic_authority | Author shared Evaluation coverage without requiring every form for every component. |
| Use branch coverage as observation rather than correctness proof | E | shared_programmatic_authority | Author a bounded shared Evaluation rule. |
| Evaluate the installed realization across supported Python and platform boundaries | E | unresolved_operator_decision | Resolve those supported boundaries first. |
| Validate log schema, severity, correlation, and secret exclusion | E | unresolved_operator_decision | Resolve the log and Journal boundary first. |
| Benchmark interactive, batch, and background performance separately | E | unresolved_operator_decision | Establish representative workloads and reliance budgets first. |
| Exercise interruption, partial writes, subprocess failure, timeout, and restart where applicable | E | shared_programmatic_authority | Author shared failure-boundary Evaluation coverage. |

## Explicit conflicts and unresolved choices

| Proposal or choice | Disposition | Reason |
|---|---|---|
| Require object-oriented Python universally | rejected_candidate | The admitted evidence supports responsibility-based multi-paradigm Python, not an OOP default. |
| Use objects for owned state, lifecycle, resources, or replaceable adapters and functions for deterministic transformations | shared_programmatic_authority | This is the supported bounded allocation; exact wording remains later authoring work. |
| Make 25-line functions or 200-line files universal correctness gates | rejected_candidate | The thresholds are heuristics, not established quality laws. |
| Use bounded code-size thresholds as warnings or accepted gates with exceptions | unresolved_operator_decision | The Operator must choose their purpose, threshold, gate strength, and exception rule. |
| Require Pydantic as the universal runtime validation mechanism | unresolved_operator_decision | Pydantic was parked by the harvest; admission depends on the third-party prerequisite decision and a capability not already covered. |
| Admit Ruff, mypy, pytest, Hypothesis, coverage, or pyperf as project prerequisites | unresolved_operator_decision | Their evidence roles are distinct, but dependency admission, offline operation, locking, and supply-chain boundaries remain undecided. |
| Keep runtime code standard-library-only | unresolved_operator_decision | This is a viable option, not current accepted shared authority. |
| Separate operational logs from the governed Work Journal | unresolved_operator_decision | The likely split is logs for diagnosis and the Journal for governed action history, but retention, redaction, schema, and correlation ownership are not yet accepted. |
| Establish exact Hook, interactive, batch, and background performance budgets | unresolved_operator_decision | The report supplies measurement methods but no workload-specific thresholds. |

The Operator decisions to resolve in CA-P-071 are therefore: supported Python range; supported platform envelope; third-party prerequisite admission; responsibility-based multi-paradigm wording; warning-versus-gate treatment of code-size heuristics; logging versus Work Journal ownership; typing and automation ratchet; and performance workload budgets.

## Evidence and boundaries

Inputs:

- `fpf-reports/20260821T161903Z-fpf-sota-harvest-python-engineering-policies.md` supplies candidate evidence and open questions.
- `fpf-reports/20260823T080122Z-active-methods-alignment-repair-closure.md` is the closed pre-PROGRAMMATIC baseline.
- `.caprmedio/project_scope_unit_graph.projection.toml` supplies the current PROGRAMMATIC, APPS, MCP, TOOLS, and descendant Scope Unit boundaries.
- The current working-tree carrier bodies and frontmatter supply the exact manifest below.

Excluded:

- Delivery candidates are outside CA-P-070's M/E scope.
- Archived, done, and canceled carriers are not current target members.
- The historical `SOFTWARE` Scope label is evidence vocabulary only.
- No candidate becomes accepted authority merely by appearing in this Analysis.

## Exact current-carrier manifest

| Carrier | Version | Lifecycle | Current Scope | Disposition |
|---|---:|---|---|---|
| `.caprmedio/05_method/CA-M-110-CORE-IMPL_METHOD--implement-framework-engine-software-in-python.md` | 6 | active | PROJECT | shared_programmatic_authority |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/APPS/05_method/drafts/CA-M--IMPL_METHOD-FR_ENGN_APPS--separate-app-state-services-and-operator-interface.md` | 1 | draft | APPS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/APPS/06_evaluation/drafts/CA-E--QA_CASE-FR_ENGN_APPS--operate-the-primary-workflow-by-keyboard.md` | 1 | draft | APPS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/APPS/06_evaluation/drafts/CA-E--QA_CASE-FR_ENGN_APPS--reject-interface-bypass-of-governed-doers.md` | 1 | draft | APPS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/APPS/06_evaluation/drafts/CA-E--QA_CASE-FR_ENGN_APPS--render-untrusted-project-content-only-as-data.md` | 1 | draft | APPS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/APPS/06_evaluation/drafts/CA-E--QA_CASE-FR_ENGN_APPS--restore-app-service-state-after-restart.md` | 1 | draft | APPS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/APPS/AGENT_HOST_PLUGINS/CODEX_PLUGIN/05_method/CA-M-150-CODEX_PLUGIN-CORE-METHOD--select-the-minimal-codex-plugin-shape.md` | 5 | active | CODEX_PLUGIN | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/APPS/AGENT_HOST_PLUGINS/CODEX_PLUGIN/05_method/CA-M-151-CODEX_PLUGIN-CORE-METHOD--package-the-codex-plugin.md` | 4 | active | CODEX_PLUGIN | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/APPS/AGENT_HOST_PLUGINS/CODEX_PLUGIN/05_method/CA-M-152-CODEX_PLUGIN-CORE-METHOD--verify-the-installed-codex-plugin.md` | 4 | active | CODEX_PLUGIN | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/APPS/GRAPH_APP/05_method/CA-M-153-GRAPH_APP-CORE-METHOD--render-and-navigate-active-graph-html.md` | 7 | active | GRAPH_APP | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/APPS/GRAPH_APP/05_method/CA-M-154-GRAPH_APP-CORE-METHOD--serve-live-graph-sources-without-mutation.md` | 6 | active | GRAPH_APP | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/APPS/GRAPH_APP/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-067--interactive-html-graph-view-behavior.md` | 5 | active | GRAPH_APP | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/APPS/GRAPH_APP/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-068--live-graph-source-read-safety-and-freshness.md` | 5 | active | GRAPH_APP | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/05_method/CA-M-087-TOOLS-CORE-IMPL_METHOD--process-one-file-change.md` | 14 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/05_method/CA-M-101-TOOLS-CORE-IMPL_METHOD--build-the-as-is-implementation-inventory.md` | 4 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/05_method/CA-M-102-TOOLS-CORE-IMPL_METHOD--derive-structural-crmed-drafts-from-the-inventory.md` | 3 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/05_method/CA-M-142-TOOLS-CORE-METHOD--isolate-runtime-state-under-caprmedio-runtime.md` | 6 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/05_method/CA-M-143-TOOLS-CORE-METHOD--allocate-one-runtime-folder-per-script.md` | 5 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/05_method/CA-M-144-TOOLS-CORE-METHOD--route-and-invoke-tools-through-the-common-cli.md` | 7 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/05_method/CA-M-145-TOOLS-CORE-METHOD--generate-active-requirement-subject-catalog.md` | 8 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/05_method/CA-M-146-TOOLS-CORE-METHOD--generate-active-requirement-lineage-map.md` | 7 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/05_method/CA-M-147-TOOLS-CORE-METHOD--generate-current-active-atom-snapshot.md` | 5 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/05_method/CA-M-148-TOOLS-CORE-METHOD--generate-active-atom-history.md` | 5 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/05_method/CA-M-149-TOOLS-CORE-METHOD--generate-project-graph-state-from-configuration-authority.md` | 7 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/05_method/drafts/CA-M--IMPL_METHOD-FR_ENGN_TOOLS--advance-predefined-tool-work-through-recoverable-handoffs.md` | 1 | draft | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/05_method/drafts/CA-M--IMPL_METHOD-FR_ENGN_TOOLS--bound-file-and-subprocess-effects.md` | 1 | draft | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/05_method/drafts/CA-M--IMPL_METHOD-FR_ENGN_TOOLS--centralize-tool-decisions-in-one-pure-manager.md` | 2 | draft | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/05_method/drafts/CA-M--IMPL_METHOD-FR_ENGN_TOOLS--control-background-services-with-bounded-lifecycle-and-failure-budgets.md` | 1 | draft | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/05_method/drafts/CA-M--IMPL_METHOD-FR_ENGN_TOOLS--keep-synchronous-hook-work-minimal.md` | 2 | draft | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/05_method/drafts/CA-M--IMPL_METHOD-FR_ENGN_TOOLS--process-automatic-commits-through-durable-single-flight-scheduling.md` | 1 | draft | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/05_method/drafts/CA-M--IMPL_METHOD-FR_ENGN_TOOLS--separate-deterministic-transformations-from-effects-and-lifecycle.md` | 3 | draft | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CA-E-178-EVALUATION-FR_ENGN_TOOLS--produce-equivalent-context-through-both-input-paths.md` | 6 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CA-E-180-EVALUATION-FR_ENGN_TOOLS--commit-one-governed-change-with-all-related-journal-sidecars.md` | 8 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CA-E-182-EVALUATION-FR_ENGN_TOOLS--reject-multiple-file-identities.md` | 3 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CA-E-184-EVALUATION-FR_ENGN_TOOLS--reject-incomplete-relation-kind-metadata.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CA-E-185-EVALUATION-FR_ENGN_TOOLS--store-direct-replaced-by-while-archiving-predecessor.md` | 6 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CA-E-188-EVALUATION-FR_ENGN_TOOLS--reject-non-current-upstream-version.md` | 4 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CA-E-191-EVALUATION-FR_ENGN_TOOLS--roll-journal-part-after-one-hundred-events.md` | 1 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CA-E-192-EVALUATION-FR_ENGN_TOOLS--derive-git-message-from-structured-journal-event.md` | 4 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CA-E-193-EVALUATION-FR_ENGN_TOOLS--append-all-related-journal-records-before-commit.md` | 6 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CA-E-195-EVALUATION-FR_ENGN_TOOLS--retry-without-duplicating-journal-records.md` | 9 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CA-E-198-EVALUATION-FR_ENGN_TOOLS--replay-previous-state-without-before-fields.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CA-E-201-EVALUATION-FR_ENGN_TOOLS--represent-removal-as-result-tombstone.md` | 3 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CA-E-217-QA_CASE-FR_ENGN_TOOLS--report-complete-auto-commit-operational-status.md` | 1 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-065--common-tool-interface-conformance.md` | 5 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-066--requirement-subject-catalog-correctness.md` | 5 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-069--requirement-lineage-map-correctness.md` | 4 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-070--current-active-atom-snapshot-correctness.md` | 3 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-071--active-atom-history-correctness.md` | 3 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-072--accept-a-canonical-active-markdown-atom.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-073--reject-malformed-filename.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-074--reject-unknown-type-prefix.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-075--reject-type-placement.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-076--reject-unknown-structural-scope.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-077--reject-frontmatter-syntax.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-078--reject-unknown-frontmatter-key.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-079--reject-frontmatter-key-grammar.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-080--reject-ambiguous-scalar.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-081--reject-empty-subject-scope.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-082--reject-duplicate-subject-scope.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-083--reject-unknown-subject-scope.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-084--reject-rmed-subject-cardinality.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-085--reject-numeric-tier.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-086--reject-unknown-tier.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-087--reject-role-ineligible-tier.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-088--reject-rmed-priority.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-089--reject-stored-global-tier.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-090--reject-stored-scope-path.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-091--reject-stored-type.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-092--reject-redundant-default.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-093--reject-missing-h1.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-094--reject-multiple-h1.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-095--reject-summary-h1-mismatch.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-096--reject-empty-atom-body.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-097--reject-lifecycle-placement.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-098--reject-carrier-format.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-099--preserve-carrier-bytes-after-validation-failure.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-100--return-deterministic-carrier-diagnostics.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-101--accept-a-conforming-project.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-102--propagate-atom-filename-diagnostics.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-103--reject-duplicate-identity.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-104--reject-missing-relation-target.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-105--reject-ambiguous-relation-target.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-106--reject-inactive-relation-target.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-107--reject-unknown-relation-kind.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-108--reject-relation-source-type.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-109--reject-relation-target-type.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-110--reject-inverse-backlink.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-111--reject-duplicate-relation-target.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-112--reject-self-relation.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-113--reject-non-direct-relation.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-114--accept-a-same-scope-upstream-rmed-parent.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-115--reject-same-scope-tier-direction.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-116--reject-downstream-parent.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-117--accept-an-equal-tier-ancestor-rmed-parent.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-118--reject-cross-branch-authority.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-119--reject-backward-authority.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-120--reject-authority-cycle.md` | 3 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-121--reject-strict-orphan.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-122--reject-a-childless-principle-in-strict-scope.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-123--permit-a-parentless-core-in-casual-scope.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-124--reject-imprecise-relation-in-strict-scope.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-125--permit-the-imprecise-fallback-relation-in-casual-scope.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-126--reject-missing-structural-scope.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-127--reject-unknown-structural-scope.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-128--reject-structural-level-address.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-129--reject-unknown-lifecycle-directory.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-130--accept-registered-control-root-carriers.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-131--reject-finder-metadata-in-the-control-root.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-132--reject-an-editor-swap-file-in-the-control-root.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-133--reject-runtime-authority-boundary.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-134--reject-non-reproducible-settings.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-135--reject-settings-source-address.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-136--reject-stale-projection.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-137--accept-a-current-projection.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-138--reject-journal-syntax.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-139--reject-journal-event-schema.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-140--reject-journal-replay-link.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-141--reject-duplicate-terminal-event.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-142--reject-unresolved-revision.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-143--reject-revision-format.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-144--reject-an-unresolved-artifact-proof-revision.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-145--reject-a-backward-data-stage-dependency.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-146--reject-obsolete-active-identity.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-147--preserve-project-bytes-after-validation-failure.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-148--return-deterministic-project-diagnostics.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-149--reject-a-childless-core-in-strict-scope.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-150--permit-a-parentless-standard-in-casual-scope.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-151--reject-structural-parent-address.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-152--reject-a-temporary-file-in-the-control-root.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-153--reject-a-cache-file-in-the-control-root.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-154--reject-a-backup-file-in-the-control-root.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-155--reject-settings-source-digest.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-156--reject-stale-projection-generator.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-157--reject-revision-sequence.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-158--reject-an-unresolved-implementation-proof-revision.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-159--reject-an-unresolved-configuration-proof-revision.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-160--reject-an-unresolved-evaluator-proof-revision.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-161--reject-an-unresolved-environment-proof-revision.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-162--reject-an-unresolved-material-input-proof-revision.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-163--reject-a-skipped-data-stage.md` | 2 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-164--rebuild-graph-state-and-source-map-from-configuration.md` | 5 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-165--reject-project-settings-contributions-outside-configuration.md` | 5 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-166--restore-direct-graph-state-output-edits.md` | 5 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-167--bind-admitted-graph-state-sources-in-canonical-order.md` | 5 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/CAPRMEDIO-FRAMEWORK-ENGINE-EVAL-168--keep-operator-settings-out-of-graph-state-generator.md` | 5 | active | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/drafts/CA-E--EVAL_APPROACH-FR_ENGN_TOOLS--evaluate-the-installed-toolset-across-supported-boundaries.md` | 1 | draft | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/drafts/CA-E--EVAL_APPROACH-FR_ENGN_TOOLS--evaluate-tool-source-architecture-and-dispatch-conformance.md` | 2 | draft | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/drafts/CA-E--QA_CASE-FR_ENGN_TOOLS--accept-one-codex-event-without-host-delay-or-loss.md` | 1 | draft | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/drafts/CA-E--QA_CASE-FR_ENGN_TOOLS--advance-one-fixed-direct-worker-handoff.md` | 1 | draft | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/drafts/CA-E--QA_CASE-FR_ENGN_TOOLS--complete-one-installed-automatic-commit-end-to-end.md` | 1 | draft | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/drafts/CA-E--QA_CASE-FR_ENGN_TOOLS--deduplicate-one-repeated-queued-completion.md` | 1 | draft | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/drafts/CA-E--QA_CASE-FR_ENGN_TOOLS--keep-one-commit-automation-manager-pure-and-deterministic.md` | 1 | draft | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/drafts/CA-E--QA_CASE-FR_ENGN_TOOLS--keep-one-synchronous-hook-within-its-work-boundary.md` | 2 | draft | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/drafts/CA-E--QA_CASE-FR_ENGN_TOOLS--open-one-service-circuit-at-a-declared-failure-budget.md` | 1 | draft | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/drafts/CA-E--QA_CASE-FR_ENGN_TOOLS--preserve-queued-work-through-service-lifecycle-controls.md` | 1 | draft | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/drafts/CA-E--QA_CASE-FR_ENGN_TOOLS--reconcile-one-missed-external-project-change.md` | 1 | draft | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/drafts/CA-E--QA_CASE-FR_ENGN_TOOLS--reject-an-undeclared-downstream-transition.md` | 1 | draft | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/drafts/CA-E--QA_CASE-FR_ENGN_TOOLS--resume-one-commit-action-from-every-safe-phase.md` | 1 | draft | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/drafts/CA-E--QA_CASE-FR_ENGN_TOOLS--resume-one-queued-plan-after-scheduler-restart.md` | 1 | draft | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/06_evaluation/drafts/CA-E--QA_CASE-FR_ENGN_TOOLS--serialize-concurrent-and-out-of-order-commit-events.md` | 1 | draft | TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/APPEND_CHANGE_RECORDS/06_evaluation/CA-E-181-EVALUATION-FR_ENGN_TOOLS_APPEND_CHANGE_RECORDS--reject-stale-context-before-journal-append.md` | 4 | active | APPEND_CHANGE_RECORDS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/APPEND_CHANGE_RECORDS/06_evaluation/CA-E-183-EVALUATION-FR_ENGN_TOOLS_APPEND_CHANGE_RECORDS--reject-preexisting-unrelated-staged-changes.md` | 4 | active | APPEND_CHANGE_RECORDS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/APPEND_CHANGE_RECORDS/06_evaluation/CA-E-187-EVALUATION-FR_ENGN_TOOLS_APPEND_CHANGE_RECORDS--reject-incomplete-context-before-journal-append.md` | 4 | active | APPEND_CHANGE_RECORDS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/APPEND_CHANGE_RECORDS/06_evaluation/CA-E-197-EVALUATION-FR_ENGN_TOOLS_APPEND_CHANGE_RECORDS--validate-structured-file-change-event-schema.md` | 5 | active | APPEND_CHANGE_RECORDS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/APPEND_CHANGE_RECORDS/06_evaluation/CA-E-200-EVALUATION-FR_ENGN_TOOLS_APPEND_CHANGE_RECORDS--recover-first-prior-result-without-invention.md` | 3 | active | APPEND_CHANGE_RECORDS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/APPEND_CHANGE_RECORDS/06_evaluation/CA-E-205-EVALUATION-FR_ENGN_TOOLS_APPEND_CHANGE_RECORDS--route-by-sealed-journal-date.md` | 1 | active | APPEND_CHANGE_RECORDS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/CLOSE_ATOM/05_method/CA-M-129-CLOSE_ATOM-CORE-IMPL_METHOD--validate-and-describe-one-concern-closure.md` | 2 | active | CLOSE_ATOM | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/CLOSE_ATOM/06_evaluation/CA-E-248-EVALUATION-FR_ENGN_TOOLS_CLOSE_ATOM--reject-unadmitted-concern-closure-application.md` | 2 | active | CLOSE_ATOM | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/COMMIT_CHANGE_SET/06_evaluation/CA-E-179-EVALUATION-FR_ENGN_TOOLS_COMMIT_CHANGE_SET--keep-dry-run-mutation-free.md` | 5 | active | COMMIT_CHANGE_SET | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/COMMIT_CHANGE_SET/06_evaluation/CA-E-196-EVALUATION-FR_ENGN_TOOLS_COMMIT_CHANGE_SET--reject-commit-without-complete-journal-receipts-and-live-lease.md` | 6 | active | COMMIT_CHANGE_SET | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/COMMIT_CHANGE_SET/06_evaluation/CA-E-199-EVALUATION-FR_ENGN_TOOLS_COMMIT_CHANGE_SET--commit-all-and-only-related-journal-sidecars.md` | 3 | active | COMMIT_CHANGE_SET | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/COMMIT_CHANGE_SET/06_evaluation/CA-E-202-EVALUATION-FR_ENGN_TOOLS_COMMIT_CHANGE_SET--reject-context-that-becomes-stale-after-journal-append.md` | 1 | active | COMMIT_CHANGE_SET | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/COMMIT_CHANGE_SET/06_evaluation/CA-E-203-EVALUATION-FR_ENGN_TOOLS_COMMIT_CHANGE_SET--reject-unrelated-staged-change-after-journal-append.md` | 1 | active | COMMIT_CHANGE_SET | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/COMMIT_CHANGE_SET/06_evaluation/CA-E-204-EVALUATION-FR_ENGN_TOOLS_COMMIT_CHANGE_SET--reject-context-corrupted-after-journal-append.md` | 1 | active | COMMIT_CHANGE_SET | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/COMMIT_CHANGE_SET/06_evaluation/CA-E-211-EVALUATION-FR_ENGN_TOOLS_COMMIT_CHANGE_SET--reject-invalid-staged-governed-commit.md` | 1 | active | COMMIT_CHANGE_SET | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/COMMIT_CHANGE_SET/06_evaluation/CA-E-212-EVALUATION-FR_ENGN_TOOLS_COMMIT_CHANGE_SET--reject-noncanonical-governed-commit-message.md` | 1 | active | COMMIT_CHANGE_SET | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/COMMIT_CHANGE_SET/06_evaluation/CA-E-213-EVALUATION-FR_ENGN_TOOLS_COMMIT_CHANGE_SET--observe-created-commit-without-recursion.md` | 2 | active | COMMIT_CHANGE_SET | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/COMMIT_CHANGE_SET/06_evaluation/CA-E-216-QA_CASE-FR_ENGN_TOOLS_COMMIT_CHANGE_SET--reject-installation-and-runtime-state-from-git-index.md` | 2 | active | COMMIT_CHANGE_SET | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/COMMIT_CHANGE_SET/06_evaluation/CA-E-236-QA_CASE-FR_ENGN_TOOLS_COMMIT_CHANGE_SET--commit-one-folder-action-atomically.md` | 1 | active | COMMIT_CHANGE_SET | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/COMMIT_CHANGE_SET/06_evaluation/CA-E-237-QA_CASE-FR_ENGN_TOOLS_COMMIT_CHANGE_SET--commit-each-folder-lifecycle-action.md` | 1 | active | COMMIT_CHANGE_SET | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/COMMIT_CONTEXT/06_evaluation/CA-E-170-EVALUATION-FR_ENGN_TOOLS_COMMIT_CONTEXT--gather-deterministic-context-read-only.md` | 6 | active | COMMIT_CONTEXT | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/COMMIT_CONTEXT/06_evaluation/CA-E-171-EVALUATION-FR_ENGN_TOOLS_COMMIT_CONTEXT--classify-file-creation-as-add.md` | 3 | active | COMMIT_CONTEXT | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/COMMIT_CONTEXT/06_evaluation/CA-E-172-EVALUATION-FR_ENGN_TOOLS_COMMIT_CONTEXT--classify-structural-relocation-as-move.md` | 3 | active | COMMIT_CONTEXT | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/COMMIT_CONTEXT/06_evaluation/CA-E-173-EVALUATION-FR_ENGN_TOOLS_COMMIT_CONTEXT--classify-content-change-as-update.md` | 3 | active | COMMIT_CONTEXT | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/COMMIT_CONTEXT/06_evaluation/CA-E-174-EVALUATION-FR_ENGN_TOOLS_COMMIT_CONTEXT--classify-rename-as-update.md` | 3 | active | COMMIT_CONTEXT | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/COMMIT_CONTEXT/06_evaluation/CA-E-175-EVALUATION-FR_ENGN_TOOLS_COMMIT_CONTEXT--classify-relocation-with-update.md` | 4 | active | COMMIT_CONTEXT | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/COMMIT_CONTEXT/06_evaluation/CA-E-176-EVALUATION-FR_ENGN_TOOLS_COMMIT_CONTEXT--classify-file-removal-as-remove.md` | 4 | active | COMMIT_CONTEXT | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/COMMIT_CONTEXT/06_evaluation/CA-E-177-EVALUATION-FR_ENGN_TOOLS_COMMIT_CONTEXT--reject-a-trigger-with-no-file-change.md` | 3 | active | COMMIT_CONTEXT | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/COMMIT_CONTEXT/06_evaluation/CA-E-189-EVALUATION-FR_ENGN_TOOLS_COMMIT_CONTEXT--default-journal-author-to-full-github-username.md` | 3 | active | COMMIT_CONTEXT | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/COMMIT_CONTEXT/06_evaluation/CA-E-190-EVALUATION-FR_ENGN_TOOLS_COMMIT_CONTEXT--seal-journal-date-in-configured-timezone.md` | 3 | active | COMMIT_CONTEXT | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/COMMIT_CONTEXT/06_evaluation/CA-E-214-QA_CASE-FR_ENGN_TOOLS_COMMIT_CONTEXT--resolve-governed-subject-through-canonical-authority.md` | 2 | active | COMMIT_CONTEXT | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/COMMIT_CONTEXT/06_evaluation/CA-E-218-QA_CASE-FR_ENGN_TOOLS_COMMIT_CONTEXT--resolve-lifecycle-transition-without-activating-inactive-state.md` | 1 | active | COMMIT_CONTEXT | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/COMMIT_CONTEXT/06_evaluation/CA-E-232-QA_CASE-FR_ENGN_TOOLS_COMMIT_CONTEXT--log-a-file-change-despite-graph-defects.md` | 1 | active | COMMIT_CONTEXT | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/COMMIT_CONTEXT/06_evaluation/CA-E-233-QA_CASE-FR_ENGN_TOOLS_COMMIT_CONTEXT--resolve-an-ordinary-project-file-action.md` | 1 | active | COMMIT_CONTEXT | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/COMMIT_TRIGGER/06_evaluation/CA-E-169-EVALUATION-FR_ENGN_TOOLS_COMMIT_TRIGGER--emit-a-trigger-without-mutation.md` | 6 | active | COMMIT_TRIGGER | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/COMMIT_TRIGGER/06_evaluation/CA-E-186-EVALUATION-FR_ENGN_TOOLS_COMMIT_TRIGGER--preserve-existing-hook-behavior.md` | 6 | active | COMMIT_TRIGGER | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/COMMIT_TRIGGER/06_evaluation/CA-E-194-EVALUATION-FR_ENGN_TOOLS_COMMIT_TRIGGER--suppress-recursive-journal-trigger.md` | 4 | active | COMMIT_TRIGGER | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/COMMIT_TRIGGER/06_evaluation/CA-E-215-QA_CASE-FR_ENGN_TOOLS_COMMIT_TRIGGER--reject-custom-git-hooks-path-conflict-without-mutation.md` | 2 | active | COMMIT_TRIGGER | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/COMMIT_TRIGGER/06_evaluation/CA-E-227-QA_CASE-FR_ENGN_TOOLS_COMMIT_TRIGGER--reconcile-a-missed-session-change-at-stop.md` | 1 | active | COMMIT_TRIGGER | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/COMMIT_TRIGGER/06_evaluation/CA-E-234-QA_CASE-FR_ENGN_TOOLS_COMMIT_TRIGGER--emit-one-folder-action.md` | 1 | active | COMMIT_TRIGGER | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/COMMIT_TRIGGER/06_evaluation/CA-E-235-QA_CASE-FR_ENGN_TOOLS_COMMIT_TRIGGER--select-the-project-frontier.md` | 1 | active | COMMIT_TRIGGER | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/INSTALL_TOOLS/05_method/CA-M-103-INSTALL_TOOLS-CORE-IMPL_METHOD--install-one-verified-tool-release.md` | 7 | active | INSTALL_TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/INSTALL_TOOLS/06_evaluation/CA-E-219-QA_CASE-FR_ENGN_TOOLS_INSTALL_TOOLS--resolve-complete-install-dry-run-without-mutation.md` | 1 | active | INSTALL_TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/INSTALL_TOOLS/06_evaluation/CA-E-220-QA_CASE-FR_ENGN_TOOLS_INSTALL_TOOLS--install-one-self-contained-release-and-all-hooks.md` | 5 | active | INSTALL_TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/INSTALL_TOOLS/06_evaluation/CA-E-221-QA_CASE-FR_ENGN_TOOLS_INSTALL_TOOLS--select-a-new-release-and-repoint-managed-carriers.md` | 3 | active | INSTALL_TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/INSTALL_TOOLS/06_evaluation/CA-E-225-QA_CASE-FR_ENGN_TOOLS_INSTALL_TOOLS--reject-drift-in-an-existing-release.md` | 1 | active | INSTALL_TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/INSTALL_TOOLS/06_evaluation/CA-E-226-QA_CASE-FR_ENGN_TOOLS_INSTALL_TOOLS--dispatch-every-codex-task-through-user-hooks.md` | 3 | active | INSTALL_TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/INSTALL_TOOLS/06_evaluation/CA-E-231-QA_CASE-FR_ENGN_TOOLS_INSTALL_TOOLS--rollback-an-unavailable-user-hook-carrier.md` | 1 | active | INSTALL_TOOLS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/MIGRATE_ATOM_IDENTITY/05_method/CA-M-155-TOOLS-CORE-IMPL_METHOD--plan-one-sealed-atom-identity-migration.md` | 1 | active | MIGRATE_ATOM_IDENTITY | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/MIGRATE_ATOM_IDENTITY/06_evaluation/CA-E-251-TOOLS-QA_CASE--evaluate-one-sealed-atom-identity-migration.md` | 1 | active | MIGRATE_ATOM_IDENTITY | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/REBIND_ATOM_RELATIONS/05_method/CA-M-156-TOOLS-CORE-IMPL_METHOD--plan-one-sealed-atom-relation-rebinding.md` | 1 | active | REBIND_ATOM_RELATIONS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/REBIND_ATOM_RELATIONS/06_evaluation/CA-E-252-TOOLS-QA_CASE--evaluate-one-sealed-atom-relation-rebinding.md` | 1 | active | REBIND_ATOM_RELATIONS | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/REPLACE_ATOM/05_method/CA-M-128-REPLACE_ATOM-CORE-IMPL_METHOD--validate-and-describe-one-atom-replacement.md` | 2 | active | REPLACE_ATOM | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/REPLACE_ATOM/06_evaluation/CA-E-247-EVALUATION-FR_ENGN_TOOLS_REPLACE_ATOM--reject-unadmitted-replacement-application.md` | 1 | active | REPLACE_ATOM | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/START_BACKGROUND_SERVICES/05_method/CA-M-104-START_BACKGROUND_SERVICES-CORE-IMPL_METHOD--start-registered-background-services.md` | 2 | active | START_BACKGROUND_SERVICES | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/START_BACKGROUND_SERVICES/06_evaluation/CA-E-222-QA_CASE-FR_ENGN_TOOLS_START_BACKGROUND_SERVICES--accept-an-empty-background-service-registry.md` | 1 | active | START_BACKGROUND_SERVICES | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/START_BACKGROUND_SERVICES/06_evaluation/CA-E-223-QA_CASE-FR_ENGN_TOOLS_START_BACKGROUND_SERVICES--start-each-enabled-service-once.md` | 1 | active | START_BACKGROUND_SERVICES | child_scope_specialization |
| `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/START_BACKGROUND_SERVICES/06_evaluation/CA-E-224-QA_CASE-FR_ENGN_TOOLS_START_BACKGROUND_SERVICES--reject-a-service-dependency-outside-installation.md` | 1 | active | START_BACKGROUND_SERVICES | child_scope_specialization |
