---
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Atom/Content Role: Plan/Authoritative Carrier Bundle"
  depends_on:
    - "Atom/Content Role: Plan/Type: Objective/Carrier/Stem"
    - "Atom/Content Role: Plan/Type: Task/Carrier/Stem"
    - "File Carrier"
    - "Directory Carrier"
version: 1
updated_at: "2026-09-20 23:55:10 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-R-1533", "CA-D-458", "CA-D-459"]}
---
# Serialize Plan Atom Carrier Bundles

an Objective Atom Carrier Bundle **must** use one canonical stem as a Directory Carrier, a Markdown File Carrier with suffix `.md`, **or** both; a Task Atom Carrier Bundle **must** use one Markdown File Carrier **and may** add one same-stem Directory Carrier for subordinate Tasks. same-stem carriers in one bundle carry one Atom Revision, **not** separate Atoms, **and** their Atom ID, Type, Summary, **and** Status **must** agree.
