---
version: 17
updated_at: "2026-09-17 16:03:40 +0000"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  depends_on:
    - CA-R-1430
  child_of:
    - "CA-R-1421"
    - "CA-M-005-PRINCIPLE-METHOD--add-complexity-only-when-necessary"
subjects:
  governs: "Project/authority mode"
  depends_on:
    - "Project"
    - "CAPRMEDIO Framework Instance"
    - "Atom/Content Role: Requirement"
    - "Atom/Content Role: Method"
    - "Atom/Content Role: Evaluation"
    - "Atom/Content Role: Delivery"
    - "Atom/Content Role: Plan"
    - "Atom/Content Role: Operations"
    - "Authority Mode"
    - "Framework Instance Settings"
    - "Project Structure"
    - "Scope Unit"
cce_version: cce_1
cce_form: obligation

---
# Govern each scope by authority mode

the caprmedio Project **must** use the effective Authority Mode for the Project **and** **every** configured Scope Unit under CA-R-1430:

- Framework Instance Settings selects the Project mode **and** the default Scope Unit mode.
- a Scope Unit's explicit override comes **only** from its authoritative Project Structure declaration; an omitted override uses the effective Framework Instance setting.

mode selection **must not** weaken active-authority consistency.
