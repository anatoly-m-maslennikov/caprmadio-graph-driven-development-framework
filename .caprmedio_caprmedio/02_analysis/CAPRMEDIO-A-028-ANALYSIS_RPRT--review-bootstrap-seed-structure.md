---
subject_scopes:
  - scope-topology
version: 1
updated_at: 2026-08-19 16:35:42
---
# Review Bootstrap Seed structure

## Result

The Bootstrap Seed target is coherent as a CAPRMEDIO-owned METAMODEL → SEMANTICS → GOVERNANCE chain above PROJECT, but the current control tree is a transitional representation rather than a conforming instance of that target. The review found four material remediation groups, two intentional transition groups already owned by later P-020 actions, and one P-025 ownership exception resolved with 99% confidence. No reviewed carrier was changed.

## Bounded source frontier

The review used P-020, P-016, completed P-024 and P-025, and `CAPRMEDIO-A-027-ANALYSIS_RPRT--review-bootstrap-seed-ownership` as its procedural and ownership frontier. Its normative frontier was `CAPRMEDIO-GOAL-001--enable-any-operator-to-build-a-working-system`; all active Project Principles; Project structural Cores `CAPRMEDIO-REQU-031`, `CAPRMEDIO-REQU-032`, `CAPRMEDIO-REQU-045`, and `CAPRMEDIO-REQU-049`; Project topology and authority-mode Requirements `CAPRMEDIO-REQU-706` through `CAPRMEDIO-REQU-712`; META Cores `CAPRMEDIO-META-REQU-085`, `125`, `132`, `151`, `152`, `154`, `157`, `618` through `620`, `643`, `657`, `679`, `706`, and `721` through `725`; and GOV Requirements `CAPRMEDIO-GOV-REQU-344`, `345`, `348` through `350`, `356`, `360`, `364`, `365`, `625`, `626`, `647`, `661`, `662`, `664`, `669`, `676`, `710`, `712` through `714`, `717` through `723`, and `770`.

The reviewed carrier frontier was the P-025 classified set of 1,356 governed carriers plus four structural placeholders. P-026 and this Analysis Report are later Project carriers and are intentionally not retroactively added to that completed P-025 classification; P-020 action 8 owns the replacement frozen inventory. The review inspected `.caprmedio/caprmedio_project_settings.toml`, `.caprmedio/08_implementation/CAPRMEDIO-MAPS-001--project-settings-source-map.yaml`, `caprmedio_framework_settings.toml`, the `000_caprmedio_framework` convenience links, and the live Project Structural-unit directories. It excluded `.f4f`, runtime state, native realization contents, and symlink targets.

## Review criteria

The review tested whether every target unit has one irreducible scope and immediate owner, whether current authority gives each governed claim one owner without repeating independently replaceable obligations, whether role-specific lifecycle placement is valid, whether generated carriers have active source, generator, and currentness authority, and whether native files are either non-Artifacts or expressly admitted and bound without contradicting the control-root boundary.

## Findings

| Finding | Evidence and interpretation | Confidence | Accepted target disposition |
|---|---|---:|---|
| P-025 ownership exception resolves to SEMANTICS | `CAPRMEDIO-META-REQU-723--define-governance-scope` defines the meaning and boundary of GOVERNANCE. `CAPRMEDIO-META-REQU-722--define-semantics-scope` owns meanings and consequences of well-formed constructs, while `CAPRMEDIO-META-REQU-725--define-meta-scope-ownership-chain` and `CAPRMEDIO-REQU-032--assign-immediate-child-scope-ownership` make SEMANTICS the immediate owner of GOVERNANCE scope. GOVERNANCE itself materializes and controls accepted meaning through its downstream carriers. | 99% | Treat META-723 as a governed relocation to target SEMANTICS in action 10. It is not a GOVERNANCE-owned self-definition. |
| The current `600_LAYER_6_EXTNS` placeholder has no accepted target Structural-unit role | `CAPRMEDIO-REQU-706--define-caprmedio-structural-topology` defines only Bootstrap meta units, PROJECT, Project Layers, and Layer-owned Features. `CAPRMEDIO-REQU-707--order-project-layers` lists FRAMEWORK_METHODOLOGY, FRAMEWORK_ENGINE, DOCUMENTATION, RELEASES, and FIELD; it contains no EXTNS Layer. Extensions and Project Adaptations are governed as distinct authority strata by `CAPRMEDIO-REQU-686--separate-canonical-extension-and-project-adaptation-authority` and are applied through FRAMEWORK_METHODOLOGY by `CAPRMEDIO-METHODOLOGY-REQU-690--govern-discipline-extension-and-adaptation-applicability`. | 99% | Action 7 must decide the single owner and representation of the empty EXTNS unit before action 10 relocates, removes, or retains it. It must not be treated as an accepted Project Layer by default. |
| Framework Settings has a native-Atom versus control-root contradiction | `CAPRMEDIO-META-REQU-619--classify-framework-settings-as-an-implementation-atom`, `CAPRMEDIO-GOV-REQU-625--encode-framework-settings-as-a-native-toml-atom`, and `CAPRMEDIO-GOV-REQU-661--register-framework-settings-atom-identity` admit root `caprmedio_framework_settings.toml` as an Implementation Atom with a Work Journal binding. `CAPRMEDIO-GOV-REQU-344--all-governed-artifacts-live-under-caprmedio` simultaneously requires every Atom's current carrier to live under `.caprmedio/` and excludes product roots as current Artifact locations. Both claims cannot govern the same native carrier without an explicit exception or reclassification. | 99% | Action 7 must reconcile the semantic ownership and carrier-boundary rule. Action 8 must record the chosen native-target locator and admitted binding, if any; action 10 applies only the approved carrier disposition. |
| Current Project Settings Projection and Map are stale against live authority | `CAPRMEDIO-GOV-REQU-626--encode-project-settings-as-a-generated-toml-projection`, `647`, `664`, and `669` require generated outputs based on active sources, generator, configuration, and exact frontier. The current TOML and YAML Map name retired sources such as `CAPRMEDIO-GOV-REQU-294--interaction-reporting-mode-setting`, retain removed subtype settings, and name `02_FRAMEWORK_ENGINE/TOOLS/generate_project_settings.py`, while the live native generator is `02_FR_ENGN/TOOLS/generate_project_settings.py`. | 100% | This is generated-state debt, not source authority. Action 14 regenerates both outputs only after actions 7, 8, and 10 stabilize their inputs. Action 8 records their present stale state and declared generation boundary. |
| Seven convenience symlinks are dangling and are not governed Artifacts | `000_caprmedio_framework/01_METHODOLOGY`, `02_TOOLS`, `03_SKILLS`, `04_EXTENSIONS`, `05_ADAPTERS`, `06_EVALUATION`, and `07_DOCUMENTATION` point to absent root paths. `LICENSE`, `README.md`, and `caprmedio_framework_settings.toml` links resolve. P-025 already classifies convenience symlinks as locators rather than governed carriers. | 100% | Action 10 includes these locators in its approved address mapping or removes them as obsolete convenience links. They receive no Atom identity, lifecycle, or owner classification. |
| META-157 combines independently replaceable scope rules | `CAPRMEDIO-META-REQU-157--narrowest-common-scope-ownership` first defines general narrowest-common-scope ownership, then separately inventories Project-scope responsibility already governed by `CAPRMEDIO-REQU-008--define-project-scope-boundary`, and finally adds Concern-placement rules. The latter two can change without changing the first semantic formula. | 98% | Action 7 should retain the general ownership formula in META-157 and move or remove the Project-specific repetition and independently governed Concern-placement rule to their canonical owners. |
| META-132 contains a closed atomicity taxonomy plus separable rules | The role-to-atomicity table in `CAPRMEDIO-META-REQU-132--define-role-specific-atom-atomicity` is one closed taxonomy. Its definition of Claim-bearing roles, split criterion, and whole-Atom replacement rule are independently replaceable semantic and lifecycle obligations beyond that taxonomy. | 97% | Action 7 should preserve the table as one taxonomy and split the non-taxonomy rules to their narrowest existing owner or new irreducible Atom. |
| Active Plan-root lifecycle anomalies are already exclusively owned by P-016 | The five external-review packets and legacy Plan carriers remain in the active Plan root, while `CAPRMEDIO-GOV-REQU-365--place-plans-by-lifecycle` places only active Plans there and P-016 action 4 owns reclassification. P-016 also owns every Plan transition and Plan 012 synchronization. | 100% | Do not duplicate or mutate this lifecycle debt in P-020. P-016 performs its accepted lifecycle work independently; P-020 closure later verifies the result. |

## Intentional transitional debt

The absence of the target `100_BOOTSTRAP_LAYER_1_METAMODEL`, `200_BOOTSTRAP_LAYER_2_SEMANTICS`, and `300_BOOTSTRAP_LAYER_3_GOVERNANCE` directories is not a structural defect at this stage. `CAPRMEDIO-REQU-706--define-caprmedio-structural-topology`, `CAPRMEDIO-META-REQU-721` through `725`, and `CAPRMEDIO-GOV-REQU-770--register-bootstrap-seed-directory-labels` establish the accepted target, while P-020 action 10 owns the approved carrier and directory migration. The legacy `100_LAYER_1_META` and `200_LAYER_2_GOV` directories, legacy filenames, and active historical relation encoding are likewise transition work already reserved to actions 10 and 13 or independent P-015; this review does not misclassify their pre-migration presence as a new defect.

`CAPRMEDIO-GOV-REQU-344--all-governed-artifacts-live-under-caprmedio` is reducible in presentation because its `Primary claim` repeats its opening obligation, but its material conflict with Framework Settings is recorded once above rather than duplicated as a separate finding. The closed taxonomies in `CAPRMEDIO-REQU-706`, `CAPRMEDIO-REQU-707`, and the table in META-132 are not split merely because they enumerate a declared universe.

## Remediation handoff

### P-020 action 7 — semantic remediation

Resolve the EXTNS Structural-unit disposition, reconcile Framework Settings native-Atom status with the `.caprmedio` control-root rule, reduce META-157 to its general formula, and decompose META-132 around its non-taxonomy obligations. Do not change P-016-owned Plan lifecycle carriers or P-015 history work.

### P-020 action 8 — frozen target inventory

Record the resolved META-723 target as SEMANTICS; record the final EXTNS decision; list Framework Settings by stable native locator plus any admitted binding; and capture the current stale Project Settings Projection and Map with their source frontier, generator, configuration, and currentness state.

### P-020 action 10 — deterministic carrier migration

After approval, apply the Bootstrap Seed directory and governed-relocation mapping, update the stale generator locator, and repair or remove the seven dangling convenience symlinks. Do not count target-directory absence or legacy file names as an independent remediation before this action.

### P-020 action 13 — relation repair

After stable carriers exist, rewrite active direct relations to the accepted targets and remove historical active edges. P-015 remains the independent owner of historical replacement-lineage handling.

### P-020 action 14 — self-application and generated state

Regenerate the Project Settings TOML and YAML Map from the final active RMED frontier and registered generator configuration, then determine currentness from the resulting declared frontier rather than preserving the current obsolete source list.
