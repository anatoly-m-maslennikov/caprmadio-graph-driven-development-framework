---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Atom"
  depends_on:
    - "Atom/Claim"
    - "Artifact/Revision"
    - "Project"
    - "Operator"
priority: medium
version: 3
updated_at: "2026-09-23 19:20:45 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-D-046", "CA-D-437", "CA-D-489", "CA-D-490", "CA-E-349", "CA-E-350", "CA-E-351", "CA-E-352", "CA-M-153", "CA-M-154", "CA-M-222", "CA-M-302", "CA-R-1076", "CA-R-1077", "CA-R-1100", "CA-R-1522", "CA-R-1523", "CA-R-1524", "CA-R-1603", "CA-R-1604", "CA-R-819", "CAPRMEDIO-META-REQU-158"]}
---
# Summary

How should the Local App runtime draft be reconciled?

## Claim

how should the identified Draft Atom be reconciled **with** active authority **and** Project Principles **without** losing useful information **or** promoting it?

### Draft under review

- prior Carrier, now archived: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/07_delivery/archive/CA-D--DELIVERY-FR_ENGN_APPS--provide-a-separated-local-app-runtime@1.md`.
- inspected SHA-256: `a88d36d5ded0a4694c9ca22b2724f929fbe72c0243ce1b0f87d834dd8f6c120b`.
- review point: 74 of 79; campaign `draft-review-8afeac79`.

### Prior review finding

> **Revise/split** — Keep App carrier/state placement; separate lifecycle, security and keyboard behavior, already checked by active QA.
>
> Basis: `CA-E-349`, `CA-E-350`, `CA-E-351`, `CA-E-352`, `CA-M-313`; I7,I8. Reviewer confidence: 99%.

### Active authority cited by the review

- `CA-E-349@5`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/06_evaluation/CA-E-349-APPS-QA_CASE--operate-the-primary-app-workflow-by-keyboard.md`; SHA-256 `1493f38ff2510eacd49b23139fde733fb5535366daa54c27ff4cccb12fe2db2e`.
- `CA-E-350@6`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/06_evaluation/CA-E-350-APPS-QA_CASE--reject-interface-bypass-of-governed-doers.md`; SHA-256 `db85aacac5b372168197bf2bac551912f11bb3ce5753a898fa671893eb5fc6c6`.
- `CA-E-351@5`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/06_evaluation/CA-E-351-APPS-QA_CASE--render-untrusted-project-content-only-as-data.md`; SHA-256 `a44f395e5ef67aad56284b49b56d87e41bdeea0cadb1e167b0b2dfc88e02c058`.
- `CA-E-352@5`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/06_evaluation/CA-E-352-APPS-QA_CASE--restore-app-service-state-after-restart.md`; SHA-256 `8db521ebe28b76495d638a72658f4408c0de11cd50699e7532073e8ac1733c3d`.
- `CA-M-313@1`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-313-CORE_META_MODEL-METHOD--write-delivery-claims-with-the-delivery-cce-profile.md`; SHA-256 `2f7e6adc52588ea7b0be005b3fa0caf446fe814e64a6514ab8227bc8ee1d8fec`.

### Principles to apply

- [CA-M-002](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-002-PRINCIPLE-METHOD--dry-don-t-repeat-yourself.md).
- [CA-M-005](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-005-PRINCIPLE-METHOD--add-complexity-only-when-necessary.md).
- [CA-M-006](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-006-PRINCIPLE-METHOD--keep-the-whole-project-coherent.md).
- [CA-R-1490](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/04_requirement/CA-R-1490-PRINCIPLE-REQUIREMENT--preserve-valuable-information.md).
- [CA-E-001](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/06_evaluation/CA-E-001-PRINCIPLE-EVALUATION--make-governed-commitments-and-results-checkable.md).

### Resolution

resolved for the approved group-12 repair. the Operator accepted the corrections **and** required the canonical Scope Unit spelling FRAMEWORK_ENGINE.

the combined App Draft is split according **to** CA-R-1100: GRAPH_SERVER owns service/read-model placement, GRAPH_UI owns interface-state placement, **and** WORKFLOW_ORCHESTRATOR owns coordination-state placement. separate Requirement Drafts preserve safe rendering, keyboard operation, **and** shared App lifecycle outcomes. existing CA-E-349 through CA-E-352 remain unchanged; they are check coverage, **not** a reason **to** keep behavioral Claims **in** Delivery. disposable caches move conceptually **to** Project Temporary State under CA-D-437; durable state stays runtime-owned. GRAPH_SERVER remains strictly read-only. the legacy frontend output locator **in** existing active authority is outside this Draft repair; no new locator is inferred **or** migrated.

#### Replacement Drafts

- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/GRAPH_SERVER/07_delivery/drafts/CA-D--GRAPH_SERVER-DELIVERY--separate-graph-service-carriers-from-governed-sources.md`; Version 1; SHA-256 `2ebbd614ef1191f7f130da8e99cffa43198faaf5b3f765d50147b01e80ff5030`.
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/GRAPH_UI/07_delivery/drafts/CA-D--GRAPH_UI-DELIVERY--separate-interface-state-from-governed-sources.md`; Version 1; SHA-256 `03bb970d9bb371a3dc9054bdd59bc2c909b7904e5d241b9a0ad5e26573d1ae75`.
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/WORKFLOW_ORCHESTRATOR/07_delivery/drafts/CA-D--WORKFLOW_ORCHESTRATOR-DELIVERY--place-workflow-coordination-and-recovery-state.md`; Version 1; SHA-256 `11cd0841c0dbae086369f9d0ffd31a20ad0445a7d417ac55c80459064098fd62`.
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/GRAPH_UI/04_requirement/drafts/CA-R--GRAPH_UI-REQUIREMENT--render-untrusted-project-content-only-as-data.md`; Version 1; SHA-256 `fd9c08e78a52c813b1103b7548c21b03f7134e7c890d5bf18507cbac3bff52b0`.
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/GRAPH_UI/04_requirement/drafts/CA-R--GRAPH_UI-REQUIREMENT--make-primary-interface-workflows-keyboard-operable.md`; Version 1; SHA-256 `b35ca9320f32f3f475583be4817429d58b89b5071975a1492a01194c770c1045`.
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/04_requirement/drafts/CA-R--APPS-REQUIREMENT--keep-local-application-lifecycle-bounded-and-observable.md`; Version 1; SHA-256 `f30aa50d51aed28c40047516a6f066bfc5f41c076ce670f688a062aa5f910df5`.

#### Preservation and boundary

- exact prior Draft: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/07_delivery/archive/CA-D--DELIVERY-FR_ENGN_APPS--provide-a-separated-local-app-runtime@1.md`; Version 1; SHA-256 `a88d36d5ded0a4694c9ca22b2724f929fbe72c0243ce1b0f87d834dd8f6c120b`.
- new Summaries start new Draft identities under CA-R-1464; no Atom IDs are allocated **and** nothing is promoted.
- active Principles favor existing authority over duplication, preserve valuable prior content, **and** require explicit role, scope, **and** evidence boundaries. independent Claims are separated under CA-R-918 **and** the R/D profiles CA-M-310 **and** CA-M-313.
- original Drafts **and** prior Question Revisions remain byte-for-byte recoverable. historical review findings are preserved as history, **not** unresolved current decisions.
- no active authority, implementation, runtime, configuration, installed release, Hook, **or** Projection is changed. the replacement Drafts do **not** claim implementation conformance.

#### Active authority checked

- `CA-D-046@6`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/GRAPH_SERVER/07_delivery/CA-D-046-GRAPH_SERVER-DELIVERY--bind-graph-server-delivery-place.md`; SHA-256 `467dc9aef30eb8c55ed8a8e43c03fb69c36bed7bb48925691861c13e58f6c4e3`.
- `CA-D-437@8`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/07_delivery/CA-D-437-PROGRAMMATIC-CORE-DELIVERY--materialize-the-project-temporary-boundary.md`; SHA-256 `6f36d43c22e9da8d595bdb80666aaad96d99412aec2e964c5cf698f2e79666d0`.
- `CA-D-489@1`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/GRAPH_UI/07_delivery/CA-D-489-GRAPH_UI-DELIVERY--bind-graph-ui-delivery-place.md`; SHA-256 `c55434786de8090cfd5f668a5110b8ac0be505e5d38b1a36e28c0f2bfd0406dd`.
- `CA-D-490@1`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/WORKFLOW_ORCHESTRATOR/07_delivery/CA-D-490-WORKFLOW_ORCHESTRATOR-DELIVERY--bind-workflow-orchestrator-delivery-place.md`; SHA-256 `11b6c909e46ba7ef1df252d57d3d1fabb439d588f88a7b86d968a86752003b3d`.
- `CA-E-349@5`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/06_evaluation/CA-E-349-APPS-QA_CASE--operate-the-primary-app-workflow-by-keyboard.md`; SHA-256 `1493f38ff2510eacd49b23139fde733fb5535366daa54c27ff4cccb12fe2db2e`.
- `CA-E-350@6`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/06_evaluation/CA-E-350-APPS-QA_CASE--reject-interface-bypass-of-governed-doers.md`; SHA-256 `db85aacac5b372168197bf2bac551912f11bb3ce5753a898fa671893eb5fc6c6`.
- `CA-E-351@5`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/06_evaluation/CA-E-351-APPS-QA_CASE--render-untrusted-project-content-only-as-data.md`; SHA-256 `a44f395e5ef67aad56284b49b56d87e41bdeea0cadb1e167b0b2dfc88e02c058`.
- `CA-E-352@5`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/06_evaluation/CA-E-352-APPS-QA_CASE--restore-app-service-state-after-restart.md`; SHA-256 `8db521ebe28b76495d638a72658f4408c0de11cd50699e7532073e8ac1733c3d`.
- `CA-M-153@14`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/GRAPH_UI/05_method/CA-M-153-GRAPH_UI-CORE-METHOD--render-and-navigate-active-graph-html.md`; SHA-256 `fc70ec74441e5cf47c58076b7720b60091d4c77dae1b772f3ff17ec5eb799b9a`.
- `CA-M-154@13`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/GRAPH_SERVER/05_method/CA-M-154-GRAPH_SERVER-CORE-METHOD--serve-live-graph-sources-without-mutation.md`; SHA-256 `c082d2dd28fdc663de3eb906c66c4f294ea80dece7581e0462d9486b1ab6b866`.
- `CA-M-222@8`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/05_method/CA-M-222-APPS-CORE-METHOD--bind-an-app-interface-to-declared-backend-services.md`; SHA-256 `973bba46ab38aa7ec21bd27231fb5bcace34d67810e2fffaaa8f99989953c9b8`.
- `CA-M-302@1`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/WORKFLOW_ORCHESTRATOR/05_method/CA-M-302-WORKFLOW_ORCHESTRATOR-METHOD--separate-workflow-coordination-from-action-execution.md`; SHA-256 `d8e1f7eed8bc1d9c3b2f72ff7f14d1a84be21246210634a0e23be0048d41a313`.
- `CA-R-1076@18`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/GRAPH_UI/04_requirement/CA-R-1076-GRAPH_UI-REQUIREMENT--render-interconnected-html-graph-views.md`; SHA-256 `a53a313efd2b613ba1729ef1b06686078689de948744b0f95ee01b98592c0f36`.
- `CA-R-1077@17`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/GRAPH_SERVER/04_requirement/CA-R-1077-GRAPH_SERVER-REQUIREMENT--serve-live-graph-sources-read-only.md`; SHA-256 `4399f8791d83f7c4459f5244e733e9c12c3f53109900ca6305b0859e5592eeea`.
- `CA-R-1100@13`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/04_requirement/CA-R-1100-APPS-CORE-REQUIREMENT--define-the-application-scope-unit-topology.md`; SHA-256 `1da267f1676aed64015aaf4bfd83764b0c591bbd20aa0dba4c8aaa150d554497`.
- `CA-R-1522@3`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/WORKFLOW_ORCHESTRATOR/04_requirement/CA-R-1522-WORKFLOW_ORCHESTRATOR-REQUIREMENT--provide-workflow-orchestration-from-methodology.md`; SHA-256 `9f005f1244c2d1658576a9cdbb2e68b8d5e48d9935df6fab35c86ae764404d01`.
- `CA-R-1523@1`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/WORKFLOW_ORCHESTRATOR/04_requirement/CA-R-1523-WORKFLOW_ORCHESTRATOR-REQUIREMENT--keep-long-running-work-independent-of-client-sessions.md`; SHA-256 `eb7ddf4f4f3e605ecf2b8bce31fd83779c991d9f81b09cea7e14702187778d9c`.
- `CA-R-1524@2`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/WORKFLOW_ORCHESTRATOR/04_requirement/CA-R-1524-WORKFLOW_ORCHESTRATOR-REQUIREMENT--recover-workflow-handoffs-without-repeating-effects.md`; SHA-256 `0bfda77c29dd8a5c2fd1a0c964aa2f6825dd3b7505eaee4b3746cda9c8ba7801`.
- `CA-R-1603@1`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/04_requirement/CA-R-1603-APPS-DEFINES_GOAL_FOR-GRAPH_SERVER--serve-the-derived-graph-headlessly.md`; SHA-256 `1b125cf8cbb4813ea318d3122a93667ba2391b87f8fb1cf5e351c76b569f615a`.
- `CA-R-1604@1`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/04_requirement/CA-R-1604-APPS-DEFINES_GOAL_FOR-GRAPH_UI--provide-an-optional-graph-interface.md`; SHA-256 `287e5d83fd180153bcd11cef0da0d23ad07d96531a2975c54792a6efe372bedd`.
- `CA-R-819@12`: `.caprmedio_caprmedio/04_requirement/CA-R-819-PRINCIPLE-REQUIREMENT--build-what-you-want-without-requiring-proficiency-in-the-craft.md`; SHA-256 `b8cf36427b57922bccea59183b74b95c3dc8d40a66a64822b60b589a6ea393bc`.
- `CAPRMEDIO-META-REQU-158@13`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CAPRMEDIO-META-REQU-158-CORE_META_MODEL-CORE-REQUIREMENT--use-one-project-journal-for-governed-provenance.md`; SHA-256 `d9d05e7eb7c57d770f802812b365559f908a071e9d99fe7b6ccaf10b40b06d31`.
