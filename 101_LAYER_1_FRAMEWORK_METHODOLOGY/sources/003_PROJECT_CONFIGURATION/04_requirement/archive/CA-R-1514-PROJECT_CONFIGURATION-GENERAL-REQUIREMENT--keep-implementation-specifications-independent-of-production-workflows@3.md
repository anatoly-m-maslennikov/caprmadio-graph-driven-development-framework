---
cce_version: cce_1
cce_form: obligation
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
version: 3
updated_at: "2026-09-21 00:39:50 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  relates_to: [CA-M-261, CA-M-002, CA-R-1548, CA-R-1516, CA-R-1517, CA-R-1518, CA-R-1519]
---
# Keep Implementation specifications independent of production Workflows

**in** the caprmedio Project, governing RMED **must** fully specify the required Implementation independently of the Workflow used **to** produce it.

- conformity depends on the resulting Implementation satisfying its RMED, **not** on following a particular production Workflow. different Workflows, **or** work **without** a formally defined Workflow, **may** produce a conforming Implementation.
- ordinary implementation RMED **must not** leave required behavior specified **only** **in** an O Atom **or** require an O Atom as its production procedure.
- the permitted authority references are the Tool realization binding under CA-R-1516 **and** CA-R-1517, **and** methodology checks of Action **and** Workflow definitions under CA-R-1518. neither exception makes the Workflow used **to** build the Implementation part of its specification.
- a generic executor **may** consume applicable O definitions as runtime inputs under CA-R-1519. its RMED **must** fully specify how it interprets those inputs; the selected Workflow is **not** its production procedure **or** an independently copied part of its Spec.

these are caprmedio Project Configuration boundaries, **not** a change **to** the reusable Core Meta-Model Content Roles.
