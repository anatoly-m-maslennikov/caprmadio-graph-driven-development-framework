---
subjects:
  governs: "Project Structure"
  depends_on:
    - "Project Settings"
    - "Framework Instance Settings"
    - "Project"
    - "Scope Unit"
    - "Goal"
    - "Carrier"
    - "Applicable Methodology"
version: 12
updated_at: "2026-10-02 20:09:13 +0400"
relations:
  evaluation_for:
    - "CA-R-1483"
    - "CA-R-1484"
    - "CA-R-1485"
    - "CA-R-1738"
    - "CA-R-1402"
    - "CA-R-1052"
    - "CA-R-1429"
    - "CA-R-1430"
    - "CA-R-1739"
    - "CA-R-626"
    - "CA-R-1740"
    - "CA-D-317"
    - "CA-D-318"
    - "CA-D-359"
    - "CA-D-364"
atom_id: "CA-E-446"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "QA Case"
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-446-CORE_META_MODEL-QA_CASE--validate-settings-boundaries-and-observed-project-structure.md
  source_atom_id: CA-E-446
  source_atom_revision: 12
  source_sha256: f5e70780f96e2dcd733fe4895b80c17fca06893d87f62db6f41fa21949cd147c
  original_relations_sha256: 5b513e54cd74d69f9ff194112df4589c8ccd5efc50c0275bc0be2f0582063614
---
# Summary

Validate settings boundaries and observed Project Structure

## Scope

settings boundaries and observed Project Structure across Projects in one repository.

## Claim

settings resolve through their own Project paths **without** cross-Project fallback. Project Settings remain authoritative initialization inputs; Framework Instance Settings remain authoritative instance choices. Core settings Atoms define purpose, content, **and** authority boundaries, General Atoms define independently governable shared settings specifications **when** needed, **and** Standard Atoms define concrete sections **or** fields. the declared unit remains visible with missing Carrier **and** Active Goal findings; the undeclared candidate remains an observation **without** becoming a declaration. explicit unit Authority Mode overrides resolve from Project Structure; omitted values inherit Framework Instance Settings. no structural Projection is required. no Projection edit changes Settings, Project Structure, **or** source Atoms. an unresolved authority-backed value does **not** conceal observed structure.

**every** Framework Instance's Methodology Sources **and** Applicable Methodology output **must** resolve beneath its own Project's `000_CAPRMEDIO_framework/` directory. rebuilding one Project's Applicable Methodology **must not** read, replace, **or** modify another Project's sources, settings, **or** compiled results. a missing selected Project instance **must** be reported rather than resolved through another Project **or** the former repository-shared framework root. nesting the framework directory **must not** change source Atom identity **or** make a projected copy a second authoritative Atom.

## Details

### Test case

create two Projects **in** one repository, **every** Project with its own Project Settings **and** `000_CAPRMEDIO_framework` directory. resolve both settings **before** creating Project Atoms **or** Implementation. select different Authority Modes, installed Extensions, **and** Project Configuration for the two instances. give the two instances distinct Methodology Sources **and** compiled Applicable Methodology results. declare a Scope Unit with no Active Goal **and** no directory; separately add an undeclared candidate Scope Unit directory. include Draft **and** archived Goals as non-active evidence. give a declared unit an explicit Authority Mode override **in** its Project Structure **and** leave another unit's override omitted.
