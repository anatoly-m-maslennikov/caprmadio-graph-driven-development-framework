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
version: 2
updated_at: 2026-08-26 16:23:41 +0400
autonomous_confidence_threshold: 98
relations: {}
---
# Define Deterministic Applicable Methodology Compilation

**when** CA-P-106 is Done, **then** the Assignee **must** define one deterministic compilation authority that always includes CORE_META_MODEL and applies the exact Installed Extension selection and resolution stated by LOCAL_CONFIGURATION.

## Scope

`(all active and draft Atoms, configurations, manifests, compilers, and evaluations that govern the three Applicable Methodology source Layers, Extension activation, replacement, priority, compatibility resolution, source frontiers, Projection currentness, deterministic ordering, GOVERNS, DEPENDS_ON, and subject- or process-scoped retrieval)`

## Definition of Done

the Task is **not done if** (the compilation contract can omit CORE_META_MODEL **or** it can admit an Installed Extension not selected by LOCAL_CONFIGURATION **or** it can retain inactive, replaced, incompatible, or lower-priority authority after Local Configuration resolution **or** it can read any methodology source outside 000_APPLICABLE_MTHD_sources without an exact governed reference **or** it can modify any source Layer **or** the same source frontier can produce different ordered output **or** the contract omits exact source and output digests **or** the compiler requires LLM inference **or** generated Applicable Methodology can gain independent authority **or** deleting generated carriers can prevent complete regeneration **or** this Task writes a final generated Applicable Methodology Carrier before CA-P-109 establishes its target).

## Details

define the compiler contract, deterministic ordering, output schemas, digest rules, GOVERNS and DEPENDS_ON indexes, and compilation Evaluations without materializing final generated Carriers. define subject- or process-scoped retrieval to seed from matching GOVERNS paths and add DEPENDS_ON authority only through prerequisite closure. preserve an explicit extension boundary for later LLM assistance, but do not use it unless subsequent Evaluation evidence demonstrates insufficient mechanical retrieval quality. defer the first final-carrier compilation to CA-P-110 after CA-P-109 establishes the target roots.
