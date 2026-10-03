---
atom_id: CA-P-107
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - Applicable Methodology
    occurrent:
      - Applicable Methodology Compilation
  depends_on:
    occurrent:
      - CA-P-106
version: 3
updated_at: 2026-08-26 16:48:17 +0400
autonomous_confidence_threshold: 98
relations: {}
---
# Define Deterministic Applicable Methodology Compilation

**when** CA-P-106 is Done, **then** the Assignee **must** define one deterministic CORE_META_MODEL-owned compilation authority that always includes CORE_META_MODEL and applies the exact Installed Extension selection and resolution stated by LOCAL_CONFIGURATION.

## Scope

`((all active and draft CORE_META_MODEL Atoms and Carriers that govern the Applicable Methodology compilation contract, deterministic ordering, output schemas, source and output digests, GOVERNS and DEPENDS_ON indexes, compilation Evaluations, and subject- or process-scoped retrieval) union (the exact INSTALLED_EXTENSIONS candidate-source manifests and LOCAL_CONFIGURATION selection, replacement, priority, and compatibility-resolution inputs referenced by that authority))`

## Definition of Done

the Task is **not done if** (any generic compilation authority is owned outside CORE_META_MODEL **or** LOCAL_CONFIGURATION owns any generic compilation rule instead of only Project-owned selection and resolution inputs **or** the compilation contract can omit CORE_META_MODEL **or** it can admit an Installed Extension not selected by LOCAL_CONFIGURATION **or** it can retain inactive, replaced, incompatible, or lower-priority authority after Local Configuration resolution **or** it can read any methodology source outside 000_APPLICABLE_MTHD_sources without an exact governed reference **or** it can modify any source Layer **or** the same source frontier can produce different ordered output **or** the contract omits exact source and output digests **or** the compiler requires LLM inference **or** generated Applicable Methodology can gain independent authority **or** deleting generated carriers can prevent complete regeneration **or** this Task writes a final generated Applicable Methodology Carrier before CA-P-109 establishes its target).

## Details

place the generic compiler contract, deterministic ordering, output schemas, digest rules, GOVERNS and DEPENDS_ON indexes, and compilation Evaluations in CORE_META_MODEL without materializing final generated Carriers. treat INSTALLED_EXTENSIONS as immutable candidate-source inputs and LOCAL_CONFIGURATION as Project-owned selection and resolution inputs only. define subject- or process-scoped retrieval to seed from matching GOVERNS paths and add DEPENDS_ON authority only through prerequisite closure. preserve an explicit extension boundary for later LLM assistance, but do not use it unless subsequent Evaluation evidence demonstrates insufficient mechanical retrieval quality. defer the first final-carrier compilation to CA-P-110 after CA-P-109 establishes the target roots.
