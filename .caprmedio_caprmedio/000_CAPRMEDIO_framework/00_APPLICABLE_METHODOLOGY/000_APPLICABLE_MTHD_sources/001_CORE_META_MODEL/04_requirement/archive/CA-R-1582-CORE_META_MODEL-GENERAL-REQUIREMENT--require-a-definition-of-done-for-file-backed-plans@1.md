---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "Atom/Content Role: Plan/Type: Plan/Definition of Done"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
    - "File Carrier"
    - "Directory Carrier"
    - "Hub Atom"
version: 1
updated_at: "2026-09-22 14:41:44 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-R-1581", "CA-D-470", "CA-D-460"]}
---
# Require a Definition of Done for file-backed Plans

**every** Plan Atom with a File Carrier **must** have **=1** Definition of Done, including a Hub whose File Carrier accompanies its Directory Carrier; a folder-only Hub does **not** require a separate file merely **to** state a Definition of Done.
