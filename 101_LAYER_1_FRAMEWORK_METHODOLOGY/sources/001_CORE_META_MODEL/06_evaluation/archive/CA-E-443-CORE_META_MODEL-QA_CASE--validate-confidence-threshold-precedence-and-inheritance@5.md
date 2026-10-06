---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Confidence Threshold/resolution validation"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
    - "Confidence Threshold"
    - "Autonomous Confidence Threshold"
    - "Operator"
    - "Hub Atom"
    - "Framework Instance Settings"
    - "Property"
    - "Concern"
    - "Carrier"
version: 5
updated_at: "2026-09-22 14:41:44 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"evaluation_for":["CA-R-1587","CA-R-1044","CA-R-1045","CA-R-1427","CA-R-1428","CA-M-271","CA-R-1591","CA-D-472","CA-D-278","CAPRMEDIO-META-REQU-144"]}
---
# Validate confidence-threshold precedence and inheritance

the confidence-threshold Evaluation **must** preserve CA-M-271 precedence **and** CA-R-1591 authorization gates.

- supply distinct valid values through Operator input, a Plan, nested Hubs, **and** Framework Instance Settings; omit sources successively **and** confirm nearest explicit source selection.
- scope direct input **to** one execution; retain the unrelated execution's setting.
- omit the inner Hub's file **or** confidence field while retaining a retry override: inherit confidence **without** copying it.
- supply a Hub file with explicit values: require the same Atom identity as its folder **and** its DoD; reject a separate Objective, `epic_overrides`, **or** a nearby unrelated file as an inherited source.
- use a current Plan Revision **without** taking values from its Archived copies; reject an ambiguous Bundle **or** invalid reached source **without** silent fallback.
- preserve an explicit override equal **to** the inherited value **after** the upstream source changes; an omitted override follows that change.
- accept permitted integer values including **=0**, **=87**, **=99**, **and** **=100**; reject out-of-range, non-integer, missing effective, **or** ambiguous values.
- confidence below the effective value requests Operator disposition; equal **or** greater confidence grants no additional authority.

report the selected source, context, expected value, **and** failed condition **without** mutating source values.
