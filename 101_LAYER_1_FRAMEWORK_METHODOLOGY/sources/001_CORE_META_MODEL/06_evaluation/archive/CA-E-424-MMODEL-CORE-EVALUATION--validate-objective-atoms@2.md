---
atom_id: CA-E-424
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    occurrent:
      - Objective Atom Validation
  depends_on:
    continuant:
      - "Atom/Content Role: Plan/Type: Objective"
      - "Atom/Content Role: Plan/Type: Objective/Carrier/Filename"
      - "Atom/Content Role: Plan/Type: Objective/Carrier/Placement"
      - Epic/Objective
version: 2
updated_at: 2026-09-02 04:15:00 +0400
relations:
  evaluation_for:
    - CA-R-1365
    - CA-R-1367
    - CA-D-350
    - CA-D-351
---
# Validate Objective Atoms

## Claim checked

an Objective Atom states one Epic-wide outcome for **`=1`** Epic, uses the canonical Objective filename, remains outside its target Epic Directory Carrier, **and** is the **`<=1`** Objective Atom for that Epic.

## Test case

create one valid Objective Atom in its Current Scope Owner's `03_plan` folder **and** one Epic with no Objective Atom. **then** create two Objective Atoms for one Epic, omit the target Epic, target multiple Epics, use a noncanonical filename, **and** move the Objective Atom Carrier into its target Epic Directory Carrier.

## Acceptance criteria

**only** the valid Objective Atom **and** the Epic with no Objective Atom pass.

## Failure disposition

record a Concern naming the invalid Objective fact.
