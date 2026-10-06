---
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Atom/Content Role: Plan/Authoritative Carrier Bundle"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan/Carrier/Stem"
    - "File Carrier"
    - "Directory Carrier"
version: 2
updated_at: "2026-09-22 14:41:44 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-R-1578", "CA-D-469", "CA-D-469"]}
---
# Serialize Plan Atom Carrier Bundles

a Plan Atom Carrier Bundle **must** consist of **=1** Markdown File Carrier, **=1** Directory Carrier, **or** both using the same canonical stem under CA-D-469.

- own work requires a File Carrier; a folder-only Plan **must** be a Hub with direct decomposition under CA-R-1575.
- a matching file **and** directory carry **=1** Atom Revision **and** share its identity, Summary, Label, **and** Status; neither creates another Atom.
- a supplied File Carrier follows CA-D-470, including its mandatory Definition of Done.
- nested Plan Bundles carry independent Atoms; their files are **not** additional Carriers of the Hub Atom Revision.
