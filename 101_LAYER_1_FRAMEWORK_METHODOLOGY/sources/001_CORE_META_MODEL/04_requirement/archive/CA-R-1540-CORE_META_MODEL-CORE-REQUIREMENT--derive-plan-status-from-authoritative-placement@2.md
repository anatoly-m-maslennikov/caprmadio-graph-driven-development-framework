---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "Atom/Content Role: Plan/Status"
  depends_on:
    - "Atom/Content Role: Plan"
    - "Artifact/Carrier Placement"
version: 2
updated_at: "2026-09-22 14:41:44 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-R-1539", "CA-D-461", "CA-D-466"]}
---
# Derive Plan Status from Authoritative Placement

**every** Plan Atom Revision **must** derive **=1** Status from its own authoritative Carrier Bundle placement under CA-D-461; another field **or** a Hub's Status **must not** independently override that Status.
