---
atom_id: CA-E-517
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
author: Anatoly Maslennikov
status: Active
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Tool/VALIDATE_ATOMS"
  depends_on:
    - "Tool"
    - "Operator"
    - "Artifact/Revision"
    - "Evaluation"
version: 3
updated_at: "2026-09-24 13:59:55 +0000"
relations:
  evaluation_for:
    - CA-D-491
    - CA-D-492
    - CA-D-493
    - CA-R-1623
---
# Summary

Check Atom validator isolation and repeatability

## Claim

the `VALIDATE_ATOMS` isolation check **must** reject unbounded, mutating, **or** misleading execution.

- compare fixture-tree fingerprints **before** **and** **after** valid, invalid, incomplete, **and** error runs; require no writes, temporary files, repairs, **or** Journal mutations by the Tool.
- exercise symlink escapes, unauthorized roots, protected files, executable YAML tags, malicious-looking Markdown, resource-limit exhaustion, **and** unreadable inputs; require safe, explicit outcomes **without** executing content **or** disclosing protected bytes.
- add, remove, **or** change a relevant input during assessment: require incomplete currentness rather than mixed-Revision success.
- repeat against identical inputs **and** definition bindings: require identical findings, coverage, **and** result, apart from declared Run identifiers **and** timestamps.
- check the input/output schemas **and** exit-code mapping under CA-D-492 **and** CA-D-493, including invalid request **and** no-target cases.
- run the end-to-end fixture cases through a separate invocation of the real delivered command. isolate **every** case from live Project Atoms **and** from previous cases; fixture setup belongs **to** the test harness, **not** the validator.
- compare input-tree bytes **before** **and** **after** the command, including invalid **and** multi-error cases. mock external effects **only** at their boundaries; do **not** replace core validation behavior with a test double.

- discover an in-bound candidate whose carried selection values exclude it. permit **only** the reads needed **to** decide membership; require an exclusion reason, no validation outcomes for that candidate, **and** unchanged target counts. reference-context reads remain distinct from selected-target coverage.
- expose a protected file **or** an escaping symlink through candidate discovery **before** selection is known. require boundary enforcement **before** content reads; caller-supplied roots **must not** grant additional permission.
