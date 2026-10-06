---
atom_id: CA-R-1430
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "Framework Instance Settings/Authority Modes"
  depends_on:
    - "Framework Instance Settings"
    - "Project Structure"
    - "Authority Mode"
    - "Project"
    - "Scope Unit"
    - "Atom"
version: 4
updated_at: "2026-09-15 00:05:45 +0000"
relations:
  child_of:
    - "CA-R-1402"
  relates_to:
    - "CA-M-279"
---
# Select Authority Modes through Framework Instance Settings

Framework Instance Settings **must** select the Project Authority Mode **and** default Scope Unit Authority Mode. a Scope Unit's explicit Authority Mode override **must** be owned **only** by its Project Structure declaration; an omitted override uses the effective Framework Instance setting **without** becoming an authored per-unit value. permitted values are `strict` **and** `casual`; neither changes the authority of active Atoms.
