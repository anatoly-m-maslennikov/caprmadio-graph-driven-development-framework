---
atom_id: CA-E-446
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    occurrent:
      - "settings and structure validation"
  depends_on:
    continuant:
      - "Project Settings"
      - "Framework Instance Settings"
      - "Project"
      - "Scope Unit"
      - "Atom"
      - "Projection"
version: 3
updated_at: "2026-09-10 02:19:47 +0400"
relations:
  evaluation_for:
    - "CAPRMEDIO-META-REQU-619"
    - "CA-R-1402"
    - "CA-R-1052"
    - "CA-R-1429"
    - "CA-R-1430"
    - "CAPRMEDIO-META-REQU-620"
    - "CA-R-626"
    - "CAPRMEDIO-META-REQU-627"
    - "CA-D-317"
    - "CA-D-318"
    - "CA-D-359"
    - "CA-D-364"
---
# Validate settings boundaries and observed Project Structure

## Test case

create two Projects in one repository, **every** Project with its own Project Settings **and** `000_CAPRMEDIO_framework` directory. resolve both settings before creating Project Atoms **or** Implementation. select different Authority Modes **and** Extension settings for the two instances. add a Scope Unit directory with no active Goal, a Draft Goal, **and** an archived Goal.

## Acceptance criteria

settings resolve through their own Project paths **without** cross-Project fallback. Project Settings remain authoritative initialization inputs; Framework Instance Settings remain authoritative instance choices. Core settings Atoms define purpose, content, **and** authority boundaries, General Atoms define independently governable shared settings specifications **when** needed, **and** Standard Atoms define concrete sections **or** fields. Project Structure includes the actual Scope Unit **and** reports the missing active Goal **without** promoting Draft **or** archived Claims. no Projection edit changes either Settings Artifact **or** source Atom. an unresolved authority-backed value does **not** conceal observed structure.
