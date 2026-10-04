---
atom_id: CA-C-374
content_role: Concern
type: Problem
current_scope_unit: caprmedio
claim_target_scope_unit: METHODOLOGY_SOURCES
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
status: active
subjects:
  governs: "Compared F15 source carrier conformance"
  depends_on: ["Markdown Atom Carrier/Structure", Operations, Method]
version: 1
updated_at: "2026-10-04 13:26:54 +0000"
relations:
  concern_about: [CA-O-004, CA-O-009, CA-O-025, CA-O-027, CA-M-301]
  relates_to: [CA-P-1360, CA-A-1078, CA-D-479]
---
# Summary

Normalize the compared F15 source carriers

## Concern

Five fully compared current F15 source carriers fail current registered body-property layout under D479 v6. The issue is narrowly source-carrier conformance, not a reason to broaden research/release authority or rewrite the covered behavior.

## Evidences

Exact authoritative paths, Versions and Updated At values are in A1078. O004 v5/O009 v5/O027 v5 use a title-only layout; O025 v6 uses its title and non-registered level-two Entry conditions/Steps/Transitions/Execution boundaries. All four lack `# Summary`, `## Operation` and `## Details`, required for Operations by current D479 v6.

M301 v6 carries `# Summary`, `## Scope`, `## Claim`, `## Details`, then supporting `## Meaning and context`, `## Structure` and `## Preservation` at the same level. D479 v6 requires supporting headings to be lower-level; a Property section ends at a same/higher-level heading. The support therefore is not nested in registered Details. These are full current-source observations, not projection or historical report diagnoses. The one bounded proof at2026-10-04 13:25:50UTC confirmed the five observed issues and this typed active Concern's strict registered carrier.

## Blast radius

Only O004/O009/O025/O027/M301 are bound. Separately authorized source authoring/review must normalize their registered layout while preserving source-selection/fidelity, optional readiness-not-publication, and citation/meaning-preservation semantics. No global cleanup, O/RMED/code/parent/Git/Journal mutation or publication is authorized here. P1360 may complete the bounded comparison with the actual issue retained; C374 remains active until its narrow source repairs and independent carrier check pass.
