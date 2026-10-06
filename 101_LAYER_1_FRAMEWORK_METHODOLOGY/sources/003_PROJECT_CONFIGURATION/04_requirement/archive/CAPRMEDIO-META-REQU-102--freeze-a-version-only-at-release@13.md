---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "Version/release"
  depends_on:
    - "Version"
    - "Journal/Record"
    - "Artifact/Revision"
    - "Atom/Content Role: Operations"
    - "Atom/Content Role: Implementation"
    - "Atom/Content Role: Delivery"
    - "Atom/Content Role: Evaluation"
    - "Extension"
    - "Project Configuration"
version: 13
updated_at: "2026-09-16 17:31:26 +0000"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  relates_to:
    - "CAPRMEDIO-META-REQU-143"
    - "CAPRMEDIO-GOV-REQU-353"
    - "CA-O-025"
---
# Requirement — Freeze a version only at release

a target Version **must** remain mutable **until** its selected authorized release event succeeds **and** the shared Journal records that outcome for the exact released candidate.

- the release record is a factual Journal Record under CAPRMEDIO-META-REQU-143, **not** an Operations Atom.
- its exact manifest binds the released governing Atom Revisions, Implementation **and** Delivery Revisions, applicable Evaluations **and** evidence, **and** release identifier.
- the selected release policy defines the event boundary. applicable Delivery authority defines the manifest **and** Journal representation; a selected Extension owns mechanism-specific references.
- planning allocation, implementation completion, readiness acceptance, **or** release-candidate naming does **not** freeze the Version **before** the successful event.

this Project Configuration Claim does **not** impose its release Process on **every** Project.
