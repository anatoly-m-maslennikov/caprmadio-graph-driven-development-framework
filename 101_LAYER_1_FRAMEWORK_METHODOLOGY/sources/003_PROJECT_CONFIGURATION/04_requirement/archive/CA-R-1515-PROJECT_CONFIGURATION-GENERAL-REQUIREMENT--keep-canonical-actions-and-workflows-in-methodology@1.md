---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "Atom/Content Role: Operations"
  depends_on:
    - "Action"
    - "Workflow"
    - "Methodology"
    - "Methodology Source"
    - "Scope Unit"
    - "Tool"
    - "Core Meta-Model"
    - "Extension"
    - "Project Configuration"
    - "Atom/Content Role: Implementation"
version: 1
updated_at: "2026-09-18 15:44:48 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  relates_to: [CA-M-002, CA-R-1344, CA-R-1222]
---
# Keep canonical Actions and Workflows in methodology

**in** the caprmedio Project, the canonical O definitions of Actions **and** Workflows used by TOOLS **must** belong **to** methodology source Scope Units.

- a Tool references the applicable canonical definition rather than independently defining the same Action **or** Workflow **in** its own Scope Unit.
- the owning methodology source **may** be Core Meta-Model, an admitted Extension, **or** Project Configuration according **to** the definition's actual applicability; this allocation rule does **not** make project-specific behavior universal Core authority.
- Implementation code **and** prompts **may** realize the definition **without** becoming another independently maintained operational definition.
