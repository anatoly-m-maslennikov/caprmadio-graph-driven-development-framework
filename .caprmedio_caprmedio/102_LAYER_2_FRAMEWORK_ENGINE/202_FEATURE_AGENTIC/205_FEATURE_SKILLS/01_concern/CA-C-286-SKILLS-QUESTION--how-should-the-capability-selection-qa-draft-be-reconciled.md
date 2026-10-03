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
relations: {"relates_to": ["CA-R-1522", "CA-R-1529", "CA-R-1601", "CAPRMEDIO-FRAMEWORK-ENGINE-REQU-558", "CAPRMEDIO-FRAMEWORK-ENGINE-REQU-559"]}
---
# Summary

How should the Capability-selection QA draft be reconciled?

## Claim

how should the identified Draft Atom be reconciled **with** active authority **and** Project Principles **without** losing useful information **or** promoting it?

### Draft under review

- prior Carrier, now archived: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/205_FEATURE_SKILLS/06_evaluation/archive/CA-E--QA_CASE-FR_ENGN_SKILLS--select-applicable-methodology-and-capabilities@1.md`.
- inspected SHA-256: `8dc87a5f48db6d9fdf035b5419cda6cc2e33c8515dbca330876e526499431a04`.
- review point: 77 of 79; campaign `draft-review-8afeac79`.

### Prior review finding

> **Retain draft** — Useful selection check; freeze request/authority fixtures and the expected minimal capability set.
>
> Basis: `CA-M-005`, `CAPRMEDIO-FRAMEWORK-ENGINE-REQU-559`, `CA-R-1018`; I8. Reviewer confidence: 97%.

### Authority cited by the prior review

- `CA-M-005@8`: `.caprmedio_caprmedio/05_method/CA-M-005-PRINCIPLE-METHOD--add-complexity-only-when-necessary.md`; SHA-256 `cd4f3ec4fa61d979997600fbcdb2e96865da694ba1f49fcd391232b72664fd1b`.
- `CAPRMEDIO-FRAMEWORK-ENGINE-REQU-559@6`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/205_FEATURE_SKILLS/04_requirement/CAPRMEDIO-FRAMEWORK-ENGINE-REQU-559-SKILLS-REQUIREMENT--keep-ca-and-specialist-skills-thin.md`; SHA-256 `2771cca70c4e8f4cbb6613f7fc724165d927565ac8f29135ab6408a96e6aef0e`.
- `CA-R-1018@12`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1018-CORE_META_MODEL-CORE-REQUIREMENT--register-evaluation-targets.md`; SHA-256 `84d9f7576d66ca3019d5929bd2ce1923154a1342b702cc76924e9eba58b16fda`.

### Principles to apply

- [CA-M-002](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-002-PRINCIPLE-METHOD--dry-don-t-repeat-yourself.md).
- [CA-M-005](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-005-PRINCIPLE-METHOD--add-complexity-only-when-necessary.md).
- [CA-M-006](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-006-PRINCIPLE-METHOD--keep-the-whole-project-coherent.md).
- [CA-R-1490](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/04_requirement/CA-R-1490-PRINCIPLE-REQUIREMENT--preserve-valuable-information.md).
- [CA-E-001](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/06_evaluation/CA-E-001-PRINCIPLE-EVALUATION--make-governed-commitments-and-results-checkable.md).

### Resolution

resolved for the approved group-13 repair. the Operator confirmed that `ca` is very thin **and** that task-specific instructions arrive through MCP responses for Workflow Steps.

the Skill consumes the admitted Step rather than independently selecting **and** sequencing work. check a fixture-defined sufficient capability set **or** admitted alternatives, actual calls, result correlation, **and** executor-owned continuation; do **not** promise a global optimization algorithm.

#### Replacement Draft

- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/205_FEATURE_SKILLS/06_evaluation/drafts/CA-E--SKILLS-QA_CASE--check-skill-use-of-the-selected-workflow-step.md`; Version 1; SHA-256 `95cfd1a4566fc8a5416bc8bae503a4c80f9401ac2a5c8d10a623d540177de84a`.

#### Active authority alignment

- CAPRMEDIO-FRAMEWORK-ENGINE-REQU-558 **and** CAPRMEDIO-FRAMEWORK-ENGINE-REQU-559 are revised **in** place with their existing Summaries **and** identities. the former delegates entry **to** framework execution through MCP; the latter bounds the standing Skill instructions.
- CA-R-1529 owns the self-contained Agentic Step invocation; CA-R-1522 owns WORKFLOW_ORCHESTRATOR's MCP participation; CA-R-1601 owns ACTION_PROMPTS' Implementation responsibility. no duplicate general Workflow mechanism is added **to** the Core Meta-Model.

#### Preservation and boundary

- exact prior Draft: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/205_FEATURE_SKILLS/06_evaluation/archive/CA-E--QA_CASE-FR_ENGN_SKILLS--select-applicable-methodology-and-capabilities@1.md`; Version 1; SHA-256 `8dc87a5f48db6d9fdf035b5419cda6cc2e33c8515dbca330876e526499431a04`.
- the new Summary starts a new Draft identity under CA-R-1464. no Atom ID is allocated **and** no Draft is promoted.
- original source links **and** candidate alignments remain recoverable **in** the exact archive; they are provenance, **not** a new external-standard adoption.
- DRY, necessary complexity, coherence, preservation, **and** checkability support this separation. the Method is about authoring, the Evaluations check identified active authority, **and** Delivery specifies package representation.
- no implementation, installed Skill, MCP service, runtime, host Hook, Settings, existing O Draft, **or** Projection is changed. the Evaluation Drafts do **not** claim that runtime tests have passed.

#### Current authority checked

- `CA-R-1522@3`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/WORKFLOW_ORCHESTRATOR/04_requirement/CA-R-1522-WORKFLOW_ORCHESTRATOR-REQUIREMENT--provide-workflow-orchestration-from-methodology.md`; SHA-256 `9f005f1244c2d1658576a9cdbb2e68b8d5e48d9935df6fab35c86ae764404d01`.
- `CA-R-1529@1`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1529-CORE_META_MODEL-GENERAL-REQUIREMENT--provide-self-contained-agentic-step-invocations.md`; SHA-256 `dd4642d4a318eb8ee4e49c554ae1a31a4ed2ee40b679850eb5ffbb6bb4382db3`.
- `CA-R-1601@1`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/202_FEATURE_PROMPTS/04_requirement/CA-R-1601-PROMPTS-DEFINES_GOAL_FOR-ACTION_PROMPTS--implement-actions-as-agent-instructions.md`; SHA-256 `b2255af93e223726197f1999f0abe4c0744f278e7d035dd22fc8f97d4cbba748`.
- `CAPRMEDIO-FRAMEWORK-ENGINE-REQU-558@8`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/205_FEATURE_SKILLS/04_requirement/CAPRMEDIO-FRAMEWORK-ENGINE-REQU-558-SKILLS-REQUIREMENT--provide-ca-as-the-universal-entry-skill.md`; SHA-256 `428560b9c514c7e72cb300cedf3c929d53acd6a657f2f2f3373fac3711261cfd`.
- `CAPRMEDIO-FRAMEWORK-ENGINE-REQU-559@7`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/205_FEATURE_SKILLS/04_requirement/CAPRMEDIO-FRAMEWORK-ENGINE-REQU-559-SKILLS-REQUIREMENT--keep-ca-and-specialist-skills-thin.md`; SHA-256 `33aa0496d0451bf63c5399ac5ca80d0cc10e6a2eb1a49bb594522d45226e9668`.
