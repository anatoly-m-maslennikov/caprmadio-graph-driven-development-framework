---
atom_id: CA-D-491
content_role: Delivery
type: Delivery
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
author: Anatoly Maslennikov
status: Active
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Tool/VALIDATE_ATOMS/Carrier"
  depends_on:
    - "Tool/VALIDATE_ATOMS"
    - "File Carrier"
    - "Implementation"
version: 3
updated_at: "2026-09-24 14:07:30 +0000"
relations:
  delivery_for:
    - CA-R-1622
    - CA-R-1623
---
# Summary

Deliver the VALIDATE_ATOMS command

## Claim

the `VALIDATE_ATOMS` executable Carrier **must** be delivered as `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/VALIDATE_ATOMS/validate_atoms.py`, with its automated tests **in** the adjacent `tests/` directory.

- expose `validate_atoms.py --input <request.json>` **and** `--input -` for standard input.
- emit **=1** JSON result on standard output under CA-D-493; human execution diagnostics belong on standard error.
- the path identifies an Implementation Artifact inside TOOLS, **not** a newly declared Scope Unit. it carries the implementation bound under CA-R-1622, **not** another Workflow authority.
- store the end-to-end command tests **in** `VALIDATE_ATOMS/tests/test_validate_atoms_e2e.py` relative **to** the delivered TOOLS directory.
- store mock Markdown Atoms **and** supporting mock context **in** `VALIDATE_ATOMS/tests/fixtures/`, with `good/`, `bad/`, `mixed/`, **and** `context/` groups. fixture files are test inputs, **not** active governing Project Atoms.
- store the case/coverage manifest **in** `VALIDATE_ATOMS/tests/cases.json` **and** independently reviewed expected reports **in** `VALIDATE_ATOMS/tests/expected/<case_id>.json`. **every** manifest case identifies its fixture inputs, request, governing rule identities/Revisions, expected report, **and** expected exit code.

- `cases.json` is a closed object with `schema_version: 1` **and** `cases`: a nonempty array. each case has a unique nonempty `case_id`, `request` path, nonempty `fixture_paths` list, nonempty `authority` list of exact Atom Bindings under CA-D-492, nonempty `check_codes` list, `expected_report` path, **and** integer `expected_exit_code` **in** (0, 1, 2, 3). all case paths are relative **to** `tests/`, remain inside it, **and** cannot escape through symlinks. expected reports follow CA-D-493.
- include positive/negative/exception/boundary coverage for every supported check **and** declared failure class; reusable fixture cases may cover multiple rules. the harness verifies the matrix against the independently resolved obligation inventory, **not** just the list of implemented checks.
