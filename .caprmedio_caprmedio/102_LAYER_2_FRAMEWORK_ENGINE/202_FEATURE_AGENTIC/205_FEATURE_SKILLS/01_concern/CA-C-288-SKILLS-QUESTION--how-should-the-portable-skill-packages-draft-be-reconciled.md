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
updated_at: "2026-09-23 19:41:33 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-D-024", "CA-R-1522", "CA-R-1529", "CA-R-1601", "CAPRMEDIO-FRAMEWORK-ENGINE-REQU-558", "CAPRMEDIO-FRAMEWORK-ENGINE-REQU-559", "CAPRMEDIO-FRAMEWORK-ENGINE-REQU-564"]}
---
# Summary

How should the Portable Skill packages draft be reconciled?

## Claim

how should the identified Draft Atom be reconciled **with** active authority **and** Project Principles **without** losing useful information **or** promoting it?

### Draft under review

- prior Carrier, now archived: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/205_FEATURE_SKILLS/07_delivery/archive/CA-D--DELIVERY-FR_ENGN_SKILLS--provide-thin-portable-skill-packages@1.md`.
- inspected SHA-256: `b6ef738a80842bf1453131ed27f0e6e6931e6884116d27118386c9d99ca07ad8`.
- review point: 79 of 79; campaign `draft-review-8afeac79`.

### Prior review finding

> **Revise/split** — Keep package representation; remove permission to bundle deterministic scripts where thin-wrapper authority requires Tools.
>
> Basis: `CAPRMEDIO-FRAMEWORK-ENGINE-REQU-559`, `CAPRMEDIO-FRAMEWORK-ENGINE-REQU-564`, `CA-M-313`; I7,I8. Reviewer confidence: 99%.

### Authority cited by the prior review

- `CAPRMEDIO-FRAMEWORK-ENGINE-REQU-559@6`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/205_FEATURE_SKILLS/04_requirement/CAPRMEDIO-FRAMEWORK-ENGINE-REQU-559-SKILLS-REQUIREMENT--keep-ca-and-specialist-skills-thin.md`; SHA-256 `2771cca70c4e8f4cbb6613f7fc724165d927565ac8f29135ab6408a96e6aef0e`.
- `CAPRMEDIO-FRAMEWORK-ENGINE-REQU-564@10`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/205_FEATURE_SKILLS/04_requirement/CAPRMEDIO-FRAMEWORK-ENGINE-REQU-564-SKILLS-CORE-REQUIREMENT--use-one-portable-shared-skill-runtime.md`; SHA-256 `3fe6c4e359a897b0ab3013950c633a9a8e3e925c1be255a4e07b18125d525a51`.
- `CA-M-313@1`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-313-CORE_META_MODEL-METHOD--write-delivery-claims-with-the-delivery-cce-profile.md`; SHA-256 `2f7e6adc52588ea7b0be005b3fa0caf446fe814e64a6514ab8227bc8ee1d8fec`.

### Principles to apply

- [CA-M-002](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-002-PRINCIPLE-METHOD--dry-don-t-repeat-yourself.md).
- [CA-M-005](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-005-PRINCIPLE-METHOD--add-complexity-only-when-necessary.md).
- [CA-M-006](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-006-PRINCIPLE-METHOD--keep-the-whole-project-coherent.md).
- [CA-R-1490](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/04_requirement/CA-R-1490-PRINCIPLE-REQUIREMENT--preserve-valuable-information.md).
- [CA-E-001](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/06_evaluation/CA-E-001-PRINCIPLE-EVALUATION--make-governed-commitments-and-results-checkable.md).

### Resolution

resolved for the approved group-13 repair. the Operator confirmed that `ca` is very thin **and** that task-specific instructions arrive through MCP responses for Workflow Steps.

retain package representation **only**. the package contains discovery, bootstrap, response handling, **and** necessary non-executable support; task-specific Action prompts arrive through MCP. remove permission **to** bundle deterministic helpers **or** duplicate prompt/Workflow authority. no new host package schema is selected.

#### Replacement Draft

- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/205_FEATURE_SKILLS/07_delivery/drafts/CA-D--SKILLS-DELIVERY--package-skills-as-bootstrap-and-response-handler-instructions.md`; Version 1; SHA-256 `6d4540790e2c8336fcb4fc6a3853b8fe0dd266ec1fce8529c2bc25e3031237e4`.

#### Active authority alignment

- CAPRMEDIO-FRAMEWORK-ENGINE-REQU-558 **and** CAPRMEDIO-FRAMEWORK-ENGINE-REQU-559 are revised **in** place with their existing Summaries **and** identities. the former delegates entry **to** framework execution through MCP; the latter bounds the standing Skill instructions.
- CA-R-1529 owns the self-contained Agentic Step invocation; CA-R-1522 owns WORKFLOW_ORCHESTRATOR's MCP participation; CA-R-1601 owns ACTION_PROMPTS' Implementation responsibility. no duplicate general Workflow mechanism is added **to** the Core Meta-Model.

#### Preservation and boundary

- exact prior Draft: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/205_FEATURE_SKILLS/07_delivery/archive/CA-D--DELIVERY-FR_ENGN_SKILLS--provide-thin-portable-skill-packages@1.md`; Version 1; SHA-256 `b6ef738a80842bf1453131ed27f0e6e6931e6884116d27118386c9d99ca07ad8`.
- the new Summary starts a new Draft identity under CA-R-1464. no Atom ID is allocated **and** no Draft is promoted.
- original source links **and** candidate alignments remain recoverable **in** the exact archive; they are provenance, **not** a new external-standard adoption.
- DRY, necessary complexity, coherence, preservation, **and** checkability support this separation. the Method is about authoring, the Evaluations check identified active authority, **and** Delivery specifies package representation.
- no implementation, installed Skill, MCP service, runtime, host Hook, Settings, existing O Draft, **or** Projection is changed. the Evaluation Drafts do **not** claim that runtime tests have passed.

#### Current authority checked

- `CA-D-024@9`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/205_FEATURE_SKILLS/07_delivery/CA-D-024-SKILLS-DELIVERY--bind-skills-delivery-place.md`; SHA-256 `cb044363d44694116870ed2ec58662db6aa9a1b1fea421f82efddf110e70fac2`.
- `CA-R-1522@3`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/WORKFLOW_ORCHESTRATOR/04_requirement/CA-R-1522-WORKFLOW_ORCHESTRATOR-REQUIREMENT--provide-workflow-orchestration-from-methodology.md`; SHA-256 `9f005f1244c2d1658576a9cdbb2e68b8d5e48d9935df6fab35c86ae764404d01`.
- `CA-R-1529@1`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1529-CORE_META_MODEL-GENERAL-REQUIREMENT--provide-self-contained-agentic-step-invocations.md`; SHA-256 `dd4642d4a318eb8ee4e49c554ae1a31a4ed2ee40b679850eb5ffbb6bb4382db3`.
- `CA-R-1601@1`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/202_FEATURE_PROMPTS/04_requirement/CA-R-1601-PROMPTS-DEFINES_GOAL_FOR-ACTION_PROMPTS--implement-actions-as-agent-instructions.md`; SHA-256 `b2255af93e223726197f1999f0abe4c0744f278e7d035dd22fc8f97d4cbba748`.
- `CAPRMEDIO-FRAMEWORK-ENGINE-REQU-558@8`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/205_FEATURE_SKILLS/04_requirement/CAPRMEDIO-FRAMEWORK-ENGINE-REQU-558-SKILLS-REQUIREMENT--provide-ca-as-the-universal-entry-skill.md`; SHA-256 `428560b9c514c7e72cb300cedf3c929d53acd6a657f2f2f3373fac3711261cfd`.
- `CAPRMEDIO-FRAMEWORK-ENGINE-REQU-559@7`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/205_FEATURE_SKILLS/04_requirement/CAPRMEDIO-FRAMEWORK-ENGINE-REQU-559-SKILLS-REQUIREMENT--keep-ca-and-specialist-skills-thin.md`; SHA-256 `33aa0496d0451bf63c5399ac5ca80d0cc10e6a2eb1a49bb594522d45226e9668`.
- `CAPRMEDIO-FRAMEWORK-ENGINE-REQU-564@10`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/205_FEATURE_SKILLS/04_requirement/CAPRMEDIO-FRAMEWORK-ENGINE-REQU-564-SKILLS-CORE-REQUIREMENT--use-one-portable-shared-skill-runtime.md`; SHA-256 `3fe6c4e359a897b0ab3013950c633a9a8e3e925c1be255a4e07b18125d525a51`.
