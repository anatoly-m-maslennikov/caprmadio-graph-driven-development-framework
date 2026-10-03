---
subject_scopes:
  - settings
updated_at: 2026-08-18 01:48:41
generator: generate_project_settings_catalog
generator_version: 1
source_count: 21
source_frontier_sha256: cb0c0eb822340b795362b9834797bdd5f3ed62a022f68628d46cc8f1ec7ddeec
relations:
  child_of:
    - CAPRMEDIO-GOV-REQU-382--generate-one-project-settings-catalog
---
# Project settings

| Setting | Effective value |
| --- | --- |
| `artifact_timestamps.timezone` | `local` |
| `artifacts.creation_strictness` | `medium` |
| `artifacts.enabled_subtypes` | `["requirement:goal","concern:question","concern:problem","concern:risk","concern:opportunity","analysis:rationale","analysis:analysis_report","plan:development_backlog","plan:version_plan","plan:change_plan","plan:refactoring_plan","method:implementation_decision","evaluation:qa_case","evaluation:evaluation_control","delivery:release_definition","delivery:environment_definition","ops:release_record","ops:deployment_record","ops:environment_state","ops:health_record","ops:incident_record"]` |
| `artifacts.enabled_types` | `["concern","external_problem","conflict","analysis","external_analysis_report","conflict_analysis","plan","requirement","constraint","contract","method","external_method","method_binding","evaluation","evaluation_standard","review_protocol","delivery","external_git_commit","pull_request","ops","external_evidence_record","verification_record","catalog","map","hub","implementation_record","work_journal"]` |
| `artifacts.identity.project_prefix` | `CAPRMEDIO` |
| `artifacts.identity.project_prefix_enabled` | `true` |
| `artifacts.identity.scope_path_in_ids` | `true` |
| `artifacts.identity.subtype_in_names` | `false` |
| `artifacts.routing.enabled_governance_loci` | `["internal","external","relation"]` |
| `authority.tiers.default` | `standard` |
| `authority.tiers.external_root` | `goal` |
| `authority.tiers.ordered` | `["principle","core","standard"]` |
| `authority_modes.default` | `casual` |
| `authority_modes.gov` | `strict` |
| `authority_modes.meta` | `strict` |
| `authority_modes.project` | `strict` |
| `confidence.necessary_information_threshold_percent` | `95` |
| `confidence.semantic_resolution_threshold_percent` | `95` |
| `git.commit_each_atom_edit` | `true` |
| `git.initialize_if_missing` | `true` |
| `git.required` | `true` |
| `governance_surfaces.architecture_view` | `false` |
| `governance_surfaces.project_overview` | `false` |
| `governance_surfaces.relation_map` | `false` |
| `governance_surfaces.requirement_catalog` | `false` |
| `governance_surfaces.scope_hub` | `false` |
| `interaction.reporting_mode` | `silent` |
| `paths.control_root` | `.caprmedio` |
| `paths.framework_root` | `.caprmedio/000_caprmedio_framework` |
| `paths.journal_root` | `.caprmedio/010_journals` |
| `paths.runtime_root` | `.caprmedio_runtime` |
| `project.key` | `CAPRMEDIO` |
| `project.name` | `CAPRMEDIO` |
| `project.obsolete_names` | `["DSET","CARMAIO","CARMADIO"]` |
| `project.repository_slug` | `caprmedio-graph-driven-framework` |
| `schema_version` | `2.0` |
| `structure.features.implementation` | `["methodology","tools","skills","profiles","adapters","evaluation","documentation"]` |
| `structure.features.spec` | `["methodology","tools","skills","profiles","adapters","evaluation","documentation"]` |
| `structure.layers` | `["meta","gov","spec","implementation","delivery","ops"]` |

## Governed by

- `CAPRMEDIO-REQU-010--configurability-selects-available-capabilities`
- `CAPRMEDIO-REQU-029--govern-each-scope-by-authority-mode`
- `CAPRMEDIO-REQU-039--define-the-six-layer-project-structure`
- `CAPRMEDIO-REQU-049--use-one-global-tier-number-for-rmed-authority`
- `CAPRMEDIO-REQU-050--auto-resolve-high-confidence-semantic-issues`
- `CAPRMEDIO-REQU-051--use-caprmedio-as-the-canonical-project-name`
- `CAPRMEDIO-META-REQU-162--govern-configuration-semantics`
- `CAPRMEDIO-META-REQU-163--define-configuration-selection-and-precedence`
- `CAPRMEDIO-GOV-REQU-294--interaction-reporting-mode-setting`
- `CAPRMEDIO-GOV-REQU-385--resolve-artifact-routes-from-governed-authority-and-project-settings`
- `CAPRMEDIO-GOV-REQU-302--atomic-admission-and-promotion-gate`
- `CAPRMEDIO-GOV-REQU-303--optional-project-prefix`
- `CAPRMEDIO-GOV-REQU-304--expandable-scope-path-identities`
- `CAPRMEDIO-GOV-REQU-305--optional-governance-surface-activation`
- `CAPRMEDIO-GOV-REQU-362--configure-artifact-timestamp-timezone`
- `CAPRMEDIO-GOV-REQU-373--store-scope-authority-modes-in-project-settings`
- `CAPRMEDIO-GOV-REQU-375--configure-necessary-information-confidence-threshold`
- `CAPRMEDIO-GOV-REQU-380--configure-semantic-resolution-confidence-threshold`
- `CAPRMEDIO-GOV-REQU-382--generate-one-project-settings-catalog`
- `CAPRMEDIO-GOV-REQU-383--register-obsolete-project-names`
