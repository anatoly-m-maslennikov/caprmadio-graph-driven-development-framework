---
atom_id: CA-E-379
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    occurrent:
      - Applicable Methodology Compilation Validation
  depends_on:
    continuant:
      - Applicable Methodology
      - Applicable Methodology/Sources
      - Applicable Methodology/Compilation Output
version: 3
updated_at: 2026-08-27 21:13:36 +0400
relations: {}
---
# Validate Applicable Methodology Compilation

the Applicable Methodology Compilation Validation **must not pass** if (a Source Carrier is read outside the exact governed source references under `000_APPLICABLE_MTHD_sources` **or** the structural Source Layers are not CORE_META_MODEL, INSTALLED_EXTENSIONS, and LOCAL_CONFIGURATION in that order **or** CORE_META_MODEL or LOCAL_CONFIGURATION is omitted **or** INSTALLED_EXTENSIONS is not empty and non-contributing **or** a selected Carrier has Content Role outside (REQUIREMENT, METHOD, EVALUATION, DELIVERY, OPS) **or** a selected Carrier is a CONCERN, ANALYSIS, PLAN, IMPLEMENTATION, Draft, or archived revision **or** the dry-run conflict report omits a duplicate selected Atom identity, unresolved replacement, incompatible retained Candidate, unresolved priority, or output-path collision **or** any conflict is resolved without one durable unambiguous Operator approval in LOCAL_CONFIGURATION bound to the exact conflict and source-frontier digest **or** any approval is stale, partial, missing, ambiguous, or mismatched **or** structural Source Layer order resolves a conflict **or** a projected Carrier lacks exactly the projection mapping required by CA-R-1229 **or** that mapping does not resolve to its Source Carrier under `000_APPLICABLE_MTHD_sources` **or** the projected Carrier differs from its Source Carrier after removing projection metadata **or** a projected Carrier is treated as authoritative **or** a persistent Subject Index Carrier or monolithic JSON methodology exists **or** compilation uses LLM inference **or** compilation changes a Source Carrier **or** the same resolved source frontier produces different generated Atom Carrier trees **or** deleting generated RMEDO output directories prevents complete regeneration).
