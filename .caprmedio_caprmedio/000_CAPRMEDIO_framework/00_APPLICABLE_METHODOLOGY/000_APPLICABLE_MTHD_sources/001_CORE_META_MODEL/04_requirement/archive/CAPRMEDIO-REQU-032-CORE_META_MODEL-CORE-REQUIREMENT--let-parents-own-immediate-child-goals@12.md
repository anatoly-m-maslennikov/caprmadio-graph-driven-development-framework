---
version: 12
updated_at: "2026-09-14 23:34:13 +0000"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
    - CA-M-001
subjects:
  governs: "Atom/Content Role: Requirement/Type: Goal"
  depends_on:
    - "Scope Unit"
    - "Atom"
    - "Owned Atoms"
    - "Targeting Atoms"
cce_version: cce_1
cce_form: obligation

---
# Let Parents Own Immediate Child Goals

**every** parent Scope Unit **must** own the Goal Atoms for its immediate child Scope Units under CA-R-926; those Goal Atoms belong **to** the parent's Owned Atoms **and** the child's Targeting Atoms **without** transferring their ownership.
