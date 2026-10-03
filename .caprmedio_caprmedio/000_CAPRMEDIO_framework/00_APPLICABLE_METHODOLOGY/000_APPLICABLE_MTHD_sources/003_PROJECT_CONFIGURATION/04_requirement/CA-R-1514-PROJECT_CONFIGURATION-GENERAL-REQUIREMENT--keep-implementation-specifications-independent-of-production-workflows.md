---
subjects:
  governs: "Spec"
  depends_on:
    - "Project"
    - "Project Configuration"
    - "Core Meta-Model"
    - "Atom/Content Role"
    - "Atom/Content Role: Operations"
    - "Atom/Content Role: Implementation"
    - "Action"
    - "Workflow"
    - "Tool"
version: 6
updated_at: "2026-10-02 23:58:08 +0400"
relations:
  relates_to: [CA-M-002, CA-M-261, CA-R-1516, CA-R-1517, CA-R-1518, CA-R-1519, CA-R-1548]
atom_id: "CA-R-1514"
content_role: "Requirement"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
---
# Summary

Keep Implementation specifications independent of production Workflows

## Scope

the CAPRMEDIO Project's governing RMED for an Implementation.

## Claim

**in** the CAPRMEDIO Project, governing RMED **must** fully specify the required Implementation independently of the Workflow used **to** produce it.

## Details

- conformity depends on the resulting Implementation satisfying its RMED, **not** on following a particular production Workflow. different Workflows, **or** work **without** a formally defined Workflow, **may** produce a conforming Implementation.
- ordinary implementation RMED **must not** leave required behavior specified **only** **in** an O Atom **or** require an O Atom as its production procedure.
- the permitted authority references are the Tool realization binding under CA-R-1516-PROJECT_CONFIGURATION-REQUIREMENT--bind-each-tool-to-one-methodology-action **and** CA-R-1517-PROJECT_CONFIGURATION-REQUIREMENT--keep-tool-operational-authority-outside-its-own-subtree, **and** methodology checks of Action **and** Workflow definitions under CA-R-1518-PROJECT_CONFIGURATION-GENERAL-REQUIREMENT--separate-methodology-and-tool-evaluation-responsibilities. neither exception makes the Workflow used **to** build the Implementation part of its specification.
- a generic executor **may** consume applicable O definitions as runtime inputs under CA-R-1519-CORE_META_MODEL-GENERAL-REQUIREMENT--require-conforming-workflow-execution. its RMED **must** fully specify how it interprets those inputs; the selected Workflow is **not** its production procedure **or** an independently copied part of its Spec.

these are CAPRMEDIO Project Configuration boundaries, **not** a change **to** the reusable Core Meta-Model Content Roles.
