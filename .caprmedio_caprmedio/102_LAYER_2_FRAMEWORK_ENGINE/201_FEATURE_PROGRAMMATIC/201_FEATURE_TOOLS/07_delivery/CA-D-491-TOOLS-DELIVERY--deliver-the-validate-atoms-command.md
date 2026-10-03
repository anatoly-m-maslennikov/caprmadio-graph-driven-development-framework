---
atom_id: CA-D-491
content_role: Delivery
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Tool/VALIDATE_ATOMS/Carrier"
  depends_on:
    - "Tool/VALIDATE_ATOMS"
    - "File Carrier"
    - "Implementation"
version: 3
updated_at: "2026-10-01 21:36:04 +0400"
relations:
  delivery_for:
    - CA-R-1622
    - CA-R-1623
---
# Summary

Deliver the VALIDATE_ATOMS command

## Scope

the `VALIDATE_ATOMS` command Carrier and its delivered test assets in TOOLS.

## Claim

the `VALIDATE_ATOMS` executable Carrier **must** be delivered as `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/VALIDATE_ATOMS/validate_atoms.py`, with its automated tests **in** the adjacent `tests/` directory.

- expose `validate_atoms.py --input <request.json>` **and** `--input -` for standard input.
- emit **=1** JSON result on standard output under CA-D-493-TOOLS-DELIVERY--serialize-atom-validator-results; human execution diagnostics belong on standard error.
- the path identifies an Implementation Artifact inside TOOLS, **not** a newly declared Scope Unit. it carries the implementation bound under CA-R-1622-TOOLS-REQUIREMENT--implement-atom-carrier-validation-in-validate-atoms, **not** another Workflow authority.
- store the end-to-end command tests **in** `VALIDATE_ATOMS/tests/test_validate_atoms_e2e.py` relative **to** the delivered TOOLS directory.
- store mock Markdown Atoms **and** supporting mock context **in** `VALIDATE_ATOMS/tests/fixtures/`, with `good/`, `bad/`, `mixed/`, **and** `context/` groups. fixture files are test inputs, **not** active governing Project Atoms.
- store the case/coverage manifest **in** `VALIDATE_ATOMS/tests/cases.json` **and** independently reviewed expected reports **in** `VALIDATE_ATOMS/tests/expected/<case_id>.json`. **every** manifest case identifies its fixture inputs, request, governing rule identities/Revisions, expected report, **and** expected exit code.

- `cases.json` is a closed object with `schema_version: 1` **and** `cases`: a nonempty array. each case has a unique nonempty `case_id`, `request` path, nonempty `fixture_paths` list, nonempty `authority` list of exact Atom Bindings under CA-D-492-TOOLS-DELIVERY--serialize-atom-validator-requests, nonempty `check_codes` list, `expected_report` path, **and** integer `expected_exit_code` **in** (0, 1, 2, 3). all case paths are relative **to** `tests/`, remain inside it, **and** cannot escape through symlinks. expected reports follow CA-D-493-TOOLS-DELIVERY--serialize-atom-validator-results.
- include positive/negative/exception/boundary coverage for every supported check **and** declared failure class; reusable fixture cases may cover multiple rules. the harness verifies the matrix against the independently resolved obligation inventory, **not** just the list of implemented checks.

## Details
