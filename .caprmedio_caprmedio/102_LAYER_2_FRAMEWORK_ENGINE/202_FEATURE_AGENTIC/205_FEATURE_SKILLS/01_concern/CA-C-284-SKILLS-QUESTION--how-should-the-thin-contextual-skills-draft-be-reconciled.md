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
relations: {"relates_to": ["CA-R-1111", "CA-R-1522", "CA-R-1527", "CA-R-1529", "CA-R-1552", "CA-R-1601", "CA-R-852", "CAPRMEDIO-FRAMEWORK-ENGINE-REQU-558", "CAPRMEDIO-FRAMEWORK-ENGINE-REQU-559", "CAPRMEDIO-FRAMEWORK-ENGINE-REQU-564"]}
---
# Summary

How should the Thin contextual Skills draft be reconciled?

## Claim

how should the identified Draft Atom be reconciled **with** active authority **and** Project Principles **without** losing useful information **or** promoting it?

### Draft under review

- prior Carrier, now archived: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/205_FEATURE_SKILLS/05_method/archive/CA-M--IMPL_METHOD-FR_ENGN_SKILLS--keep-skills-thin-contextual-and-methodology-faithful@1.md`.
- inspected SHA-256: `d778031dad1eb337a4aa2d77ab3c552415b00eced9044e3c4253eed03832cc5f`.
- review point: 75 of 79; campaign `draft-review-8afeac79`.

### Prior review finding

> **Revise/split** — Preserve progressive disclosure and capability selection; separate reusable delegation behavior and avoid duplicate Skill authority.
>
> Basis: `CAPRMEDIO-FRAMEWORK-ENGINE-REQU-559`, `CAPRMEDIO-FRAMEWORK-ENGINE-REQU-564`, `CA-R-852`; I7,I8. Reviewer confidence: 98%.

### Authority cited by the prior review

- `CAPRMEDIO-FRAMEWORK-ENGINE-REQU-559@6`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/205_FEATURE_SKILLS/04_requirement/CAPRMEDIO-FRAMEWORK-ENGINE-REQU-559-SKILLS-REQUIREMENT--keep-ca-and-specialist-skills-thin.md`; SHA-256 `2771cca70c4e8f4cbb6613f7fc724165d927565ac8f29135ab6408a96e6aef0e`.
- `CAPRMEDIO-FRAMEWORK-ENGINE-REQU-564@10`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/205_FEATURE_SKILLS/04_requirement/CAPRMEDIO-FRAMEWORK-ENGINE-REQU-564-SKILLS-CORE-REQUIREMENT--use-one-portable-shared-skill-runtime.md`; SHA-256 `3fe6c4e359a897b0ab3013950c633a9a8e3e925c1be255a4e07b18125d525a51`.
- `CA-R-852@13`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-852-CORE_META_MODEL-GENERAL-REQUIREMENT--encode-bounded-ai-agent-delegation.md`; SHA-256 `37e56f18015f6cfc55c513b94203aaaaa00814e75d778de267331e3ccf3ab776`.

### Principles to apply

- [CA-M-002](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-002-PRINCIPLE-METHOD--dry-don-t-repeat-yourself.md).
- [CA-M-005](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-005-PRINCIPLE-METHOD--add-complexity-only-when-necessary.md).
- [CA-M-006](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-006-PRINCIPLE-METHOD--keep-the-whole-project-coherent.md).
- [CA-R-1490](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/04_requirement/CA-R-1490-PRINCIPLE-REQUIREMENT--preserve-valuable-information.md).
- [CA-E-001](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/06_evaluation/CA-E-001-PRINCIPLE-EVALUATION--make-governed-commitments-and-results-checkable.md).

### Resolution

resolved for the approved group-13 repair. the Operator confirmed that `ca` is very thin **and** that task-specific instructions arrive through MCP responses for Workflow Steps.

retain a Skill-authoring Method, **not** a session execution procedure. the Operator selected a very thin `ca` whose task instructions arrive **in** current-Step MCP responses. reuse CA-R-1529 **and** CA-R-1522; preserve the existing group-9 O Drafts **without** duplication **or** promotion.

#### Replacement Draft

- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/205_FEATURE_SKILLS/05_method/drafts/CA-M--SKILLS-METHOD--write-very-thin-skills-for-mcp-delivered-step-instructions.md`; Version 1; SHA-256 `d8ad314edf4441cb0ad26b32e8038f2041704d8d5f04e307c4e25dd2891cd91f`.

#### Active authority alignment

- CAPRMEDIO-FRAMEWORK-ENGINE-REQU-558 **and** CAPRMEDIO-FRAMEWORK-ENGINE-REQU-559 are revised **in** place with their existing Summaries **and** identities. the former delegates entry **to** framework execution through MCP; the latter bounds the standing Skill instructions.
- CA-R-1529 owns the self-contained Agentic Step invocation; CA-R-1522 owns WORKFLOW_ORCHESTRATOR's MCP participation; CA-R-1601 owns ACTION_PROMPTS' Implementation responsibility. no duplicate general Workflow mechanism is added **to** the Core Meta-Model.

#### Preservation and boundary

- exact prior Draft: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/205_FEATURE_SKILLS/05_method/archive/CA-M--IMPL_METHOD-FR_ENGN_SKILLS--keep-skills-thin-contextual-and-methodology-faithful@1.md`; Version 1; SHA-256 `d778031dad1eb337a4aa2d77ab3c552415b00eced9044e3c4253eed03832cc5f`.
- the new Summary starts a new Draft identity under CA-R-1464. no Atom ID is allocated **and** no Draft is promoted.
- original source links **and** candidate alignments remain recoverable **in** the exact archive; they are provenance, **not** a new external-standard adoption.
- DRY, necessary complexity, coherence, preservation, **and** checkability support this separation. the Method is about authoring, the Evaluations check identified active authority, **and** Delivery specifies package representation.
- no implementation, installed Skill, MCP service, runtime, host Hook, Settings, existing O Draft, **or** Projection is changed. the Evaluation Drafts do **not** claim that runtime tests have passed.

#### Current authority checked

- `CA-R-1111@10`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP/04_requirement/CA-R-1111-MCP-REQUIREMENT--delegate-mcp-calls-to-canonical-tools.md`; SHA-256 `f3bd57e26ac8d6c2e457fb40a5119a173f03f16ec1dc572931755bbb2c9f33a4`.
- `CA-R-1522@3`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/WORKFLOW_ORCHESTRATOR/04_requirement/CA-R-1522-WORKFLOW_ORCHESTRATOR-REQUIREMENT--provide-workflow-orchestration-from-methodology.md`; SHA-256 `9f005f1244c2d1658576a9cdbb2e68b8d5e48d9935df6fab35c86ae764404d01`.
- `CA-R-1527@1`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1527-CORE_META_MODEL-GENERAL-REQUIREMENT--define-agentic-step-execution-context.md`; SHA-256 `7fd3caf7dcc8ea77c401aaef4644bdffe2d76ebfeb1d397d8115e3d372b237ea`.
- `CA-R-1529@1`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1529-CORE_META_MODEL-GENERAL-REQUIREMENT--provide-self-contained-agentic-step-invocations.md`; SHA-256 `dd4642d4a318eb8ee4e49c554ae1a31a4ed2ee40b679850eb5ffbb6bb4382db3`.
- `CA-R-1552@1`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1552-CORE_META_MODEL-CORE-REQUIREMENT--require-active-delegation-for-ai-agent-actions.md`; SHA-256 `e9f1d839060998a968f332ae81a5bcf2aaba0f3855321af049298c646079171b`.
- `CA-R-1601@1`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/202_FEATURE_PROMPTS/04_requirement/CA-R-1601-PROMPTS-DEFINES_GOAL_FOR-ACTION_PROMPTS--implement-actions-as-agent-instructions.md`; SHA-256 `b2255af93e223726197f1999f0abe4c0744f278e7d035dd22fc8f97d4cbba748`.
- `CA-R-852@13`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-852-CORE_META_MODEL-GENERAL-REQUIREMENT--encode-bounded-ai-agent-delegation.md`; SHA-256 `37e56f18015f6cfc55c513b94203aaaaa00814e75d778de267331e3ccf3ab776`.
- `CAPRMEDIO-FRAMEWORK-ENGINE-REQU-558@8`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/205_FEATURE_SKILLS/04_requirement/CAPRMEDIO-FRAMEWORK-ENGINE-REQU-558-SKILLS-REQUIREMENT--provide-ca-as-the-universal-entry-skill.md`; SHA-256 `428560b9c514c7e72cb300cedf3c929d53acd6a657f2f2f3373fac3711261cfd`.
- `CAPRMEDIO-FRAMEWORK-ENGINE-REQU-559@7`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/205_FEATURE_SKILLS/04_requirement/CAPRMEDIO-FRAMEWORK-ENGINE-REQU-559-SKILLS-REQUIREMENT--keep-ca-and-specialist-skills-thin.md`; SHA-256 `33aa0496d0451bf63c5399ac5ca80d0cc10e6a2eb1a49bb594522d45226e9668`.
- `CAPRMEDIO-FRAMEWORK-ENGINE-REQU-564@10`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/205_FEATURE_SKILLS/04_requirement/CAPRMEDIO-FRAMEWORK-ENGINE-REQU-564-SKILLS-CORE-REQUIREMENT--use-one-portable-shared-skill-runtime.md`; SHA-256 `3fe6c4e359a897b0ab3013950c633a9a8e3e925c1be255a4e07b18125d525a51`.
