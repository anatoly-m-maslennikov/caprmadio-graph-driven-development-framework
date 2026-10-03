---
version: 14
updated_at: "2026-09-09 23:04:14 +0400"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  depends_on:
    - CAPRMEDIO-META-REQU-675
    - CAPRMEDIO-META-REQU-619
    - CA-R-1402
  child_of:
    - "CA-M-002"
    - "CA-R-1421"
cce_version: "cce_1"
cce_form: "obligation"
subjects:
  governs: "Project/settings authority"
  depends_on:
    - "Project"
    - "Framework Instance Settings"
    - "Project Settings"
    - "Artifact"
    - "Atom"
    - "CAPRMEDIO Framework Instance"

---
# Keep selected settings in their authoritative Settings Artifact

the CAPRMEDIO Framework Instance serving caprmedio **must** consume Project Settings **and** Framework Instance Settings according **to** Core Meta-Model authority under CAPRMEDIO-META-REQU-675, **without** redefining their purpose, locations, **or** selected values **in** Project Atoms.
