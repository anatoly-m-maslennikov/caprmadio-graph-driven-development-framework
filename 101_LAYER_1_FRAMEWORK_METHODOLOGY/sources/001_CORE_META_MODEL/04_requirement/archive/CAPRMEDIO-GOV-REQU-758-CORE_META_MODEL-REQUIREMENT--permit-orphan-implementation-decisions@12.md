---
cce_version: cce_1
cce_form: permission
subjects:
  governs: "requirement-topology"
  depends_on: []
version: 12
updated_at: "2026-09-09 21:56:59 +0400"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
    - CAPRMEDIO-REQU-037-REQUIREMENT--require-parent-coverage-without-claiming-topology-completeness
    - CAPRMEDIO-META-REQU-744-CORE_META_MODEL-CORE-REQUIREMENT--distinguish-implementation-methods-from-implementation-decisions
---
# Permit orphan Implementation Decisions

`implementation_decision` **must** be registered as orphan-permitted, so an active Implementation Decision **may** have no parent Implementation Method even **in** strict authority mode.
