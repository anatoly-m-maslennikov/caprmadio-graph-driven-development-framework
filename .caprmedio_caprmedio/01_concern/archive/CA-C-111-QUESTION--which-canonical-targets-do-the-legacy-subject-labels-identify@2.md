---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Atom/Subjects"
  depends_on:
    - "Subject Path"
    - "Entity"
    - "Action"
    - "Process"
    - "Term"
    - "Atom/Claim"
version: 2
updated_at: "2026-09-17 02:35:09 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
priority: medium
---
# Which canonical targets do the legacy Subject labels identify?

which canonical Entity, Action, **or** Process does **every** unresolved legacy Subject reference identify, **and** which exact qualified path preserves the Claim's intended target?

## Evidence

the active-source review found **82** unresolved Subject carriers **and** **29** additional Evaluations whose incorrect generic `evaluation` GOVERNS tag was removed under CA-M-125 but whose retained legacy target still needs canonical resolution. examples include `scope-topology` used for both structural rules **and** Delivery bindings, `requirement-topology` used for different authority constraints, **and** `framework-engine-mcp` used for distinct MCP checks. a topic label alone does **not** establish the exact target **or** its registered qualifications.

## Principle check

CA-M-002 requires reuse of existing authority; CA-M-005 rejects unnecessary new Entities; CA-M-006 requires coherent references; CA-R-1490 preserves valuable information. CA-R-1202 **and** CA-M-125 require canonical resolution. these rules prohibit guessing a binding **or** manufacturing an Entity merely **to** make a validation count pass. they do **not** establish the missing target identity for **every** legacy label.

## Disposition

deferred under the Operator's instruction **to** record uncertain repairs as Concerns **and** continue. preserve the affected Claims **and** existing target evidence. resolve **every** listed case against its complete Claim **and** current owning definitions **before** claiming Subject conformance; split **only** **when** the Claim actually governs multiple targets. the list is a bounded review frontier, **not** an authoritative target registry **or** proof that **every** listed Claim is wrong.

## Affected carriers

- `.caprmedio_caprmedio/04_requirement/CA-R-826-BOUNDARY--codex-native-support-only.md`
- `.caprmedio_caprmedio/04_requirement/CAPRMEDIO-REQU-014-REQUIREMENT--support-repository-relative-work-areas.md`
- `.caprmedio_caprmedio/04_requirement/CAPRMEDIO-REQU-025-REQUIREMENT--preserve-higher-tier-authority-in-cross-tier-conflicts.md`
- `.caprmedio_caprmedio/04_requirement/CAPRMEDIO-REQU-030-REQUIREMENT--require-complete-authority-topology-in-strict-mode.md`
- `.caprmedio_caprmedio/04_requirement/CAPRMEDIO-REQU-033-REQUIREMENT--preserve-ancestor-core-authority-across-structural-levels.md`
- `.caprmedio_caprmedio/04_requirement/CAPRMEDIO-REQU-037-REQUIREMENT--require-parent-coverage-without-claiming-topology-completeness.md`
- `.caprmedio_caprmedio/04_requirement/CAPRMEDIO-REQU-038-REQUIREMENT--permit-incomplete-prmedo-topology-in-casual-mode.md`
- `.caprmedio_caprmedio/04_requirement/CAPRMEDIO-REQU-040-REQUIREMENT--permit-only-forward-layer-dependencies.md`
- `.caprmedio_caprmedio/04_requirement/CAPRMEDIO-REQU-041-REQUIREMENT--permit-imprecise-relations-only-in-casual-mode.md`
- `.caprmedio_caprmedio/04_requirement/CAPRMEDIO-REQU-614-REQUIREMENT--separate-layer-names-from-artifact-vocabulary.md`
- `.caprmedio_caprmedio/04_requirement/CAPRMEDIO-REQU-621-REQUIREMENT--use-settings-locations-defined-by-the-core-meta-model.md`
- `.caprmedio_caprmedio/04_requirement/CAPRMEDIO-REQU-633-REQUIREMENT--target-framework-improvement-at-the-operating-framework.md`
- `.caprmedio_caprmedio/04_requirement/CAPRMEDIO-REQU-634-REQUIREMENT--target-project-improvement-at-the-system-being-developed.md`
- `.caprmedio_caprmedio/04_requirement/CAPRMEDIO-REQU-636-REQUIREMENT--repair-the-earliest-inadequate-authority.md`
- `.caprmedio_caprmedio/04_requirement/CAPRMEDIO-REQU-637-REQUIREMENT--establish-recurrence-protection.md`
- `.caprmedio_caprmedio/04_requirement/CAPRMEDIO-REQU-646-REQUIREMENT--project-structure-according-to-the-core-meta-model.md`
- `.caprmedio_caprmedio/04_requirement/CAPRMEDIO-REQU-705-REQUIREMENT--define-framework-composition.md`
- `.caprmedio_caprmedio/04_requirement/CAPRMEDIO-REQU-707-REQUIREMENT--order-project-layers.md`
- `.caprmedio_caprmedio/04_requirement/CAPRMEDIO-REQU-709-REQUIREMENT--classify-project-features-as-unordered-units.md`
- `.caprmedio_caprmedio/04_requirement/CAPRMEDIO-REQU-710-REQUIREMENT--resolve-methodology-authority-modes-from-framework-instance-settings.md`
- `.caprmedio_caprmedio/04_requirement/CAPRMEDIO-REQU-711-REQUIREMENT--use-the-configured-authority-mode-default.md`
- `.caprmedio_caprmedio/04_requirement/CAPRMEDIO-REQU-712-REQUIREMENT--keep-project-layers-as-siblings.md`
- `.caprmedio_caprmedio/04_requirement/CAPRMEDIO-REQU-775-REQUIREMENT--define-field-as-an-unordered-project-child.md`
- `.caprmedio_caprmedio/06_evaluation/CAPRMEDIO-EVAL-001-QA_CASE--canonical-decomposition-conformance.md`
- `.caprmedio_caprmedio/07_delivery/CA-D-013-DELIVERY--bind-caprmedio-delivery-place.md`
- `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/04_requirement/CAPRMEDIO-METHODOLOGY-REQU-491-FRAMEWORK_METHODOLOGY-REQUIREMENT--requirement-provide-the-ca-refactoring-skill.md`
- `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/04_requirement/CAPRMEDIO-METHODOLOGY-REQU-492-FRAMEWORK_METHODOLOGY-REQUIREMENT--default-to-software-application-development.md`
- `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/04_requirement/CAPRMEDIO-METHODOLOGY-REQU-493-FRAMEWORK_METHODOLOGY-REQUIREMENT--support-portable-execution-platforms.md`
- `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/04_requirement/CAPRMEDIO-METHODOLOGY-REQU-494-FRAMEWORK_METHODOLOGY-REQUIREMENT--support-any-operator-language.md`
- `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/04_requirement/CAPRMEDIO-METHODOLOGY-REQU-495-FRAMEWORK_METHODOLOGY-REQUIREMENT--support-any-implementation-language.md`
- `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/04_requirement/CAPRMEDIO-METHODOLOGY-REQU-496-FRAMEWORK_METHODOLOGY-REQUIREMENT--keep-llm-operation-provider-neutral.md`
- `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/04_requirement/CAPRMEDIO-METHODOLOGY-REQU-506-FRAMEWORK_METHODOLOGY-CORE-REQUIREMENT--govern-substrate-neutral-framework-behavior.md`
- `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/04_requirement/CAPRMEDIO-METHODOLOGY-REQU-507-FRAMEWORK_METHODOLOGY-CORE-REQUIREMENT--automatically-initialize-the-session-engine.md`
- `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/04_requirement/CAPRMEDIO-METHODOLOGY-REQU-508-FRAMEWORK_METHODOLOGY-CORE-REQUIREMENT--route-natural-language-through-the-session-engine.md`
- `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/04_requirement/CAPRMEDIO-METHODOLOGY-REQU-509-FRAMEWORK_METHODOLOGY-REQUIREMENT--govern-session-engine-rehydration-behavior.md`
- `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/04_requirement/CAPRMEDIO-METHODOLOGY-REQU-510-FRAMEWORK_METHODOLOGY-CORE-REQUIREMENT--keep-native-implementation-semantically-clean.md`
- `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/04_requirement/CAPRMEDIO-METHODOLOGY-REQU-511-FRAMEWORK_METHODOLOGY-REQUIREMENT--keep-normative-prose-outside-native-implementation.md`
- `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/04_requirement/CAPRMEDIO-METHODOLOGY-REQU-512-FRAMEWORK_METHODOLOGY-REQUIREMENT--keep-caprmedio-references-outside-native-implementation.md`
- `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/04_requirement/CAPRMEDIO-METHODOLOGY-REQU-515-FRAMEWORK_METHODOLOGY-REQUIREMENT--propose-peer-scope-remodeling-for-backward-coupling.md`
- `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/04_requirement/CAPRMEDIO-METHODOLOGY-REQU-516-FRAMEWORK_METHODOLOGY-REQUIREMENT--gate-upstream-framework-proposals.md`
- `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/04_requirement/CAPRMEDIO-METHODOLOGY-REQU-630-FRAMEWORK_METHODOLOGY-CORE-REQUIREMENT--govern-current-non-authoritative-projections.md`
- `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/04_requirement/CAPRMEDIO-METHODOLOGY-REQU-690-FRAMEWORK_METHODOLOGY-CORE-REQUIREMENT--govern-discipline-extension-and-project-adaptation-applicability.md`
- `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/04_requirement/CAPRMEDIO-METHODOLOGY-REQU-692-FRAMEWORK_METHODOLOGY-REQUIREMENT--promote-project-adaptation-to-an-extension.md`
- `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/04_requirement/CAPRMEDIO-METHODOLOGY-REQU-697-FRAMEWORK_METHODOLOGY-REQUIREMENT--govern-the-installed-extension-lifecycle.md`
- `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/05_method/CA-M-141-FRAMEWORK_METHODOLOGY-CORE-METHOD--select-the-least-costly-sufficient-execution-mechanism.md`
- `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/07_delivery/CA-D-017-FRAMEWORK_METHODOLOGY-DELIVERY--bind-framework-methodology-delivery-place.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/04_requirement/CAPRMEDIO-FRAMEWORK-ENGINE-CNTR-002-FRAMEWORK_ENGINE-REQUIREMENT--supply-the-mcp-tool-interface-to-skills.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/04_requirement/CAPRMEDIO-FRAMEWORK-ENGINE-REQU-700-FRAMEWORK_ENGINE-CORE-REQUIREMENT--define-framework-engine-feature-topology.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/07_delivery/CA-D-018-FRAMEWORK_ENGINE-DELIVERY--bind-framework-engine-delivery-place.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/07_delivery/CA-D-251-PROGRAMMATIC-DELIVERY--bind-programmatic-delivery-place.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/302_FEATURE_APPS/07_delivery/CA-D-023-APPS-DELIVERY--bind-apps-delivery-place.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/302_FEATURE_APPS/AGENT_HOST_PLUGINS/07_delivery/CA-D-047-AGENT_HOST_PLUGINS-DELIVERY--bind-agent-host-plugins-delivery-place.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/302_FEATURE_APPS/AGENT_HOST_PLUGINS/CODEX_PLUGIN/07_delivery/CA-D-048-CODEX_PLUGIN-DELIVERY--bind-codex-plugin-delivery-place.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/302_FEATURE_APPS/GRAPH_APP/07_delivery/CA-D-046-GRAPH_APP-DELIVERY--bind-graph-app-delivery-place.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/302_FEATURE_APPS/GRAPH_APP/07_delivery/CAPRMEDIO-FRAMEWORK-ENGINE-DELV-005-GRAPH_APP-DELIVERY--deliver-the-requirement-projection-browser-locally.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/303_FEATURE_MCP/07_delivery/CA-D-049-MCP-DELIVERY--bind-mcp-delivery-place.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/07_delivery/CA-D-252-AGENTIC-DELIVERY--bind-agentic-delivery-place.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/301_FEATURE_SKILLS/04_requirement/CAPRMEDIO-FRAMEWORK-ENGINE-REQU-517-SKILLS-REQUIREMENT--provide-a-deterministic-routing-engine.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/301_FEATURE_SKILLS/04_requirement/CAPRMEDIO-FRAMEWORK-ENGINE-REQU-519-SKILLS-REQUIREMENT--persist-bounded-session-engine-state.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/301_FEATURE_SKILLS/04_requirement/CAPRMEDIO-FRAMEWORK-ENGINE-REQU-558-SKILLS-REQUIREMENT--provide-ca-as-the-universal-entry-skill.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/301_FEATURE_SKILLS/04_requirement/CAPRMEDIO-FRAMEWORK-ENGINE-REQU-559-SKILLS-REQUIREMENT--keep-ca-and-specialist-skills-thin.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/301_FEATURE_SKILLS/04_requirement/CAPRMEDIO-FRAMEWORK-ENGINE-REQU-560-SKILLS-REQUIREMENT--route-operator-added-skills.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/301_FEATURE_SKILLS/04_requirement/CAPRMEDIO-FRAMEWORK-ENGINE-REQU-561-SKILLS-REQUIREMENT--route-generated-data-pipeline-work.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/301_FEATURE_SKILLS/04_requirement/CAPRMEDIO-FRAMEWORK-ENGINE-REQU-562-SKILLS-REQUIREMENT--record-governed-action-lifecycles.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/301_FEATURE_SKILLS/04_requirement/CAPRMEDIO-FRAMEWORK-ENGINE-REQU-563-SKILLS-CORE-REQUIREMENT--calibrate-guidance-to-current-adequacy.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/301_FEATURE_SKILLS/04_requirement/CAPRMEDIO-FRAMEWORK-ENGINE-REQU-564-SKILLS-CORE-REQUIREMENT--use-one-portable-shared-skill-runtime.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/301_FEATURE_SKILLS/04_requirement/CAPRMEDIO-FRAMEWORK-ENGINE-REQU-565-SKILLS-REQUIREMENT--load-durable-authority-only-from-caprmedio.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/301_FEATURE_SKILLS/04_requirement/CAPRMEDIO-FRAMEWORK-ENGINE-REQU-566-SKILLS-REQUIREMENT--analyze-sessions-retrospectively-for-correction-signals.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/301_FEATURE_SKILLS/04_requirement/CAPRMEDIO-FRAMEWORK-ENGINE-REQU-578-SKILLS-REQUIREMENT--initialize-the-session-engine-at-host-context-boundaries.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/301_FEATURE_SKILLS/04_requirement/CAPRMEDIO-FRAMEWORK-ENGINE-REQU-579-SKILLS-REQUIREMENT--preserve-provider-equivalent-session-behavior.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/301_FEATURE_SKILLS/04_requirement/CAPRMEDIO-FRAMEWORK-ENGINE-REQU-580-SKILLS-REQUIREMENT--require-per-run-approval-for-raw-session-access.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/301_FEATURE_SKILLS/04_requirement/CAPRMEDIO-FRAMEWORK-ENGINE-REQU-581-SKILLS-REQUIREMENT--use-repeat-correction-rate-as-the-primary-self-improvement-metric.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/301_FEATURE_SKILLS/04_requirement/CAPRMEDIO-FRAMEWORK-ENGINE-REQU-665-SKILLS-REQUIREMENT--provide-a-project-scope-unit-graph-projection-skill.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/301_FEATURE_SKILLS/04_requirement/CAPRMEDIO-FRAMEWORK-ENGINE-REQU-694-SKILLS-REQUIREMENT--guide-project-adaptation-promotion.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/301_FEATURE_SKILLS/04_requirement/CAPRMEDIO-FRAMEWORK-ENGINE-REQU-699-SKILLS-REQUIREMENT--guide-extension-lifecycle-operations.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/301_FEATURE_SKILLS/07_delivery/CA-D-024-SKILLS-DELIVERY--bind-skills-delivery-place.md`
- `.caprmedio_caprmedio/103_LAYER_3_OPERATOR_DOCUMENTATION/04_requirement/CAPRMEDIO-R-800-OPERATOR_DOCUMENTATION-REQUIREMENT--render-each-principle-in-general-english.md`
- `.caprmedio_caprmedio/103_LAYER_3_OPERATOR_DOCUMENTATION/07_delivery/CA-D-019-OPERATOR_DOCUMENTATION-DELIVERY--bind-operator-documentation-delivery-place.md`
- `.caprmedio_caprmedio/104_LAYER_4_CORE_EXTENSIONS/07_delivery/CA-D-020-CORE_EXTENSIONS-DELIVERY--bind-core-extensions-delivery-place.md`
- `.caprmedio_caprmedio/105_LAYER_5_RELEASES/07_delivery/CA-D-021-RELEASES-DELIVERY--bind-releases-delivery-place.md`
- `.caprmedio_caprmedio/110_FEATURE_COMMUNITY_EXTENSIONS/07_delivery/CA-D-409-COMMUNITY_EXTENSIONS-DELIVERY--bind-community-extensions-delivery-place.md`
- `.caprmedio_caprmedio/110_FEATURE_FIELD/07_delivery/CA-D-022-FIELD-DELIVERY--bind-field-delivery-place.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/302_FEATURE_APPS/06_evaluation/CA-E-314-APPS-QA_CASE--verify-register-the-graph-app-unit.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/302_FEATURE_APPS/06_evaluation/CA-E-349-APPS-QA_CASE--operate-the-primary-app-workflow-by-keyboard.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/302_FEATURE_APPS/06_evaluation/CA-E-350-APPS-QA_CASE--reject-interface-bypass-of-governed-doers.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/302_FEATURE_APPS/06_evaluation/CA-E-351-APPS-QA_CASE--render-untrusted-project-content-only-as-data.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/302_FEATURE_APPS/06_evaluation/CA-E-352-APPS-QA_CASE--restore-app-service-state-after-restart.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/302_FEATURE_APPS/06_evaluation/CA-E-408-APPS-QA_CASE--verify-register-the-agent-host-plugins-unit.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/302_FEATURE_APPS/AGENT_HOST_PLUGINS/06_evaluation/CA-E-315-AGENT_HOST_PLUGINS-QA_CASE--verify-register-the-codex-plugin-unit.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/302_FEATURE_APPS/AGENT_HOST_PLUGINS/CODEX_PLUGIN/06_evaluation/CA-E-288-CODEX_PLUGIN-QA_CASE--select-one-minimal-codex-plugin-shape.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/302_FEATURE_APPS/AGENT_HOST_PLUGINS/CODEX_PLUGIN/06_evaluation/CA-E-289-CODEX_PLUGIN-QA_CASE--reject-one-invalid-codex-plugin-package.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/302_FEATURE_APPS/AGENT_HOST_PLUGINS/CODEX_PLUGIN/06_evaluation/CA-E-290-CODEX_PLUGIN-QA_CASE--prove-one-installed-codex-plugin-workflow.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/302_FEATURE_APPS/AGENT_HOST_PLUGINS/CODEX_PLUGIN/06_evaluation/CA-E-316-CODEX_PLUGIN-QA_CASE--verify-expose-the-current-graph-app-through-codex.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/302_FEATURE_APPS/AGENT_HOST_PLUGINS/CODEX_PLUGIN/06_evaluation/CA-E-317-CODEX_PLUGIN-QA_CASE--verify-route-selected-graph-context-into-governed-codex-work.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/303_FEATURE_MCP/06_evaluation/CA-E-273-MCP-QA_CASE--reject-an-unsealed-or-unacknowledged-atom-mutation.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/303_FEATURE_MCP/06_evaluation/CA-E-274-MCP-QA_CASE--discover-only-current-immediate-tool-units.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/303_FEATURE_MCP/06_evaluation/CA-E-275-MCP-QA_CASE--reject-one-incomplete-tool-invocation-contract.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/303_FEATURE_MCP/06_evaluation/CA-E-276-MCP-QA_CASE--reject-duplicate-mcp-projection-of-one-tool-unit.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/303_FEATURE_MCP/06_evaluation/CA-E-277-MCP-QA_CASE--remove-one-disabled-tool-projection.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/303_FEATURE_MCP/06_evaluation/CA-E-278-MCP-QA_CASE--reject-registry-publication-for-one-invalid-tool-projection.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/303_FEATURE_MCP/06_evaluation/CA-E-279-MCP-QA_CASE--preserve-canonical-tool-ownership-through-one-mcp-call.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/303_FEATURE_MCP/06_evaluation/CA-E-280-MCP-QA_CASE--reject-transport-that-broadens-one-tool-boundary.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/303_FEATURE_MCP/06_evaluation/CA-E-281-MCP-QA_CASE--operate-mcp-headlessly-without-an-app.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/303_FEATURE_MCP/06_evaluation/CA-E-282-MCP-QA_CASE--rebuild-one-unchanged-mcp-registry-identically.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/303_FEATURE_MCP/06_evaluation/CA-E-283-MCP-QA_CASE--reject-one-stale-mcp-project-frontier.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/303_FEATURE_MCP/06_evaluation/CA-E-284-MCP-QA_CASE--reject-one-incompatible-mcp-protocol-initialization.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/303_FEATURE_MCP/06_evaluation/CA-E-285-MCP-QA_CASE--cancel-one-bounded-mcp-request-without-orphaning-work.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/303_FEATURE_MCP/06_evaluation/CA-E-286-MCP-QA_CASE--redact-one-secret-from-an-mcp-result.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/303_FEATURE_MCP/06_evaluation/CA-E-287-MCP-QA_CASE--distinguish-one-protocol-failure-from-one-tool-failure.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/303_FEATURE_MCP/06_evaluation/CA-E-398-MCP-QA_CASE--negotiate-one-supported-mcp-capability-set.md`
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/303_FEATURE_MCP/06_evaluation/CA-E-399-MCP-QA_CASE--reject-one-unauthorized-mcp-capability-call.md`
