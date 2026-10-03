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
version: 1
updated_at: 2026-08-26 04:35:53 +0400
autonomous_confidence_threshold: 98
relations: {}
---
# Compile Applicable Methodology from Three Source Layers

**when** CA-P-106 is Done, **then** the Assignee **must** define one deterministic mechanism for compiling the complete Applicable Methodology from Core Meta-Model, Installed Extensions, and Local Configuration.

## Scope

`(all active and draft Atoms, configurations, manifests, compilers, and evaluations that govern the three Applicable Methodology source Layers, Extension activation, replacement, priority, compatibility resolution, source frontiers, Projection currentness, deterministic ordering, GOVERNS, DEPENDS_ON, and subject- or process-scoped retrieval)`

## Definition of Done

the Task is **not done if** (the compiler reads any methodology source outside 000_APPLICABLE_MTHD_sources without an exact governed reference **or** it modifies 000_APPLICABLE_MTHD_sources **or** an inactive, replaced, incompatible, or lower-priority authority survives Local Configuration resolution **or** the same source frontier produces different ordered output **or** the generated carriers lack exact source and output digests **or** the compiler requires LLM inference **or** generated Applicable Methodology gains independent authority **or** deleting generated carriers prevents complete regeneration).

## Details

compile the complete Applicable Methodology into generated carriers under 00_APPLICABLE_METHODOLOGY while preserving its 000_APPLICABLE_MTHD_sources subfolder. preserve GOVERNS and DEPENDS_ON indexes in the output. subject- or process-scoped retrieval seeds from matching GOVERNS paths and adds DEPENDS_ON authority only through prerequisite closure. preserve an explicit extension boundary for later LLM assistance, but do not use it unless subsequent Evaluation evidence demonstrates insufficient mechanical retrieval quality.
