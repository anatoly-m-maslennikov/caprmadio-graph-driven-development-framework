---
subjects:
  governs: "requirement-topology"
  depends_on: []
version: 13
updated_at: "2026-09-09 21:56:59 +0400"
relations:
  child_of:
    - CAPRMEDIO-REQU-037-REQUIREMENT--require-parent-coverage-without-claiming-topology-completeness
    - CAPRMEDIO-META-REQU-744-CORE_META_MODEL-CORE-REQUIREMENT--distinguish-implementation-methods-from-implementation-decisions
---
# Permit orphan Implementation Decisions

`implementation_decision` **must** be registered as orphan-permitted, so an active Implementation Decision **may** have no parent Implementation Method even **in** strict authority mode.
