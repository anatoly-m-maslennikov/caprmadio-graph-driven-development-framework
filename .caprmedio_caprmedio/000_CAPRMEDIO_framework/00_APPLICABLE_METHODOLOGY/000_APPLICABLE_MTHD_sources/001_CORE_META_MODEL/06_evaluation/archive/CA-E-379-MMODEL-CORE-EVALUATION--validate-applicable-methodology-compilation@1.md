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
version: 1
updated_at: 2026-08-27 20:26:51 +0400
relations: {}
---
# Validate Applicable Methodology Compilation

the Applicable Methodology Compilation Validation **must not pass** if (a Source Carrier is read outside the exact governed source references under `000_APPLICABLE_MTHD_sources` **or** the structural Source Layers are not CORE_META_MODEL, INSTALLED_EXTENSIONS, and LOCAL_CONFIGURATION in that order **or** CORE_META_MODEL or LOCAL_CONFIGURATION is omitted **or** INSTALLED_EXTENSIONS is not empty and non-contributing **or** an inactive, replaced, incompatible, or lower-priority Source Atom revision is retained **or** Local Configuration resolution is ambiguous **or** the same source frontier produces different ordered output **or** either required digest is absent or irreproducible **or** either Subject Index is incomplete or references an Atom revision outside the output manifest **or** compilation uses LLM inference **or** compilation changes a Source Carrier **or** the Output claims independent authority **or** deleting generated Output prevents complete regeneration).
