---
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Project Scope Unit Graph Projection"
  depends_on:
    - "Project Structure"
    - "Framework Instance Settings"
    - "Authority Mode"
version: 3
updated_at: "2026-09-15 00:13:02 +0000"
relations:
  child_of:
    - "CA-R-1430"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Encode project scope authority modes in the Scope Unit Graph

**if** a Project Scope Unit Graph Projection is retained for compatibility, its `authority_mode` **must** be a derived effective value: an explicit unit override from Project Structure, **otherwise** the applicable Framework Instance Settings selection. it **must not** select **or** own that mode, become a required input **to** a direct Project Structure consumer, **or** require creation of a separate structural Projection.
