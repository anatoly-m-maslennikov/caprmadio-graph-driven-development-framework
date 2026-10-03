---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Applicable Methodology Compilation Validation"
  depends_on:
    - "Tool/COMPILE_APPLICABLE_METHODOLOGY"
    - "Applicable Methodology/Compilation Output"
version: 7
updated_at: "2026-09-15 19:28:04 +0400"
relations:
  evaluation_for:
    - CA-R-1240
    - CA-M-226
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Validate Conflict-Gated Deterministic Compilation

## Test case

the `COMPILE_APPLICABLE_METHODOLOGY` Evaluation **must not pass** **if** (dry-run mutates a Source **or** Output Carrier **or** dry-run omits a duplicate selected Atom identity, unresolved replacement, incompatible retained Candidate, unresolved priority, **or** output-path collision **or** apply accepts a stale, partial, missing, ambiguous, **or** mismatched Project Configuration approval **or** apply emits a non-RMEDO, Draft, archived, monolithic, **or** persistent-index Carrier **or** a projected Carrier is **not** byte-identical **to** its selected Source Carrier **or** a transaction failure leaves partial output **or** identical resolved Source Frontiers produce different output **or** removing generated output Carriers prevents complete regeneration).

## Sources

- [CA-R-1240 — Require Conflict-Gated Applicable Methodology Compilation](../04_requirement/CA-R-1240-COMPILE_APPLICABLE_METHODOLOGY-CORE-REQUIREMENT--require-conflict-gated-applicable-methodology-compilation.md)
