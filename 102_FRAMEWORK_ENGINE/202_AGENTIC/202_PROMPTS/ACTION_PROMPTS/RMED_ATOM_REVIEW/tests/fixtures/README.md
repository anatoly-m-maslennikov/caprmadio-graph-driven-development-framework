# Synthetic review corpus

These are fixtures, not authority or real Project Atoms. Their mock universe admits:
Widget; its Color, Size, and Status Properties; Color value Blue; Size value Large;
Status values Active and Queued; Operator. The fixture Operator registry contains Fixture Operator.
DEMO's admitted Standard Global Tier is 11. Requirement and Delivery are admitted
Content Roles and same-named Types. No secret or external input is needed.

The expected judgments are in cases.json, never in the candidate Atom body.
The lists name minimum required failed checks, not an instruction to suppress
additional evidenced failures. Empty lists describe semantic-positive examples
under this synthetic context and still require evidence for every real run check.
Mechanical body outcomes are separately tested through the actual checker.
`required_blocked_checks` records dependent checks which cannot be completed
without a missing physical Property. A missing Scope is a Properties defect,
not a second semantic defect in every check that depends on that section.

Replay each carrier with evaluate_atom.prompt.md and the stated fixture context.
Compare actual findings with the expected judgments; retain the exact model,
prompt/source bindings, findings, and mismatches. Do not fabricate such a replay
from these expectations. Automated tests establish carrier/contract behavior,
not model-level semantic accuracy.

Additional Subject-coverage cases place an Operator mention only in Summary,
Details, or a Details table, and omit that Entity from DEPENDS_ON. Two more add
an unrelated Operator dependency and repeat GOVERNS as a dependency. Every case
must fail subjects for the stated reason, independently of any other finding.
The positive cases include independently mentioned Widget and qualified values;
the path's component Terms are not independently added as Entities.

For a blinded coherence replay, run `tests/prepare_semantic_replay.py NEW_RUN_DIR`.
It verifies current baseline digests, binds explicit synthetic definitions and
Principle applicability, freezes the current prompt, and shuffles carriers into
numbered packets. Give reviewers only `context.json` and their assigned
`packets/NNNN.json`; keep `private-expectations.json` separate. Test candidates
are bound input data, not definition authority. Have reviewers write actual
contract-4 coherence records in `results/NNNN.json`, then run
`tests/compare_semantic_replay.py RUN_DIR`. That comparison validates admission
and expected minimum checks; independently adjudicate all additional findings
and the evidence itself. Do not infer semantic correctness from JSON admission.
