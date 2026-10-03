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
version: 5
updated_at: 2026-08-27 20:26:51 +0400
autonomous_confidence_threshold: 99
relations: {}
---
# Define Deterministic Applicable Methodology Compilation

**when** CA-P-106 is Done, **then** the Assignee **must** define one deterministic CORE_META_MODEL-owned compilation authority that includes CORE_META_MODEL and LOCAL_CONFIGURATION as the only contributing Source Layers and retains INSTALLED_EXTENSIONS as an empty non-contributing structural Source Layer.

## Scope

`((all active and draft CORE_META_MODEL Atoms and Carriers that govern the Applicable Methodology compilation contract, deterministic ordering, output schemas, source and output digests, GOVERNS and DEPENDS_ON indexes, compilation Evaluations, and subject- or process-scoped retrieval) union (the exact INSTALLED_EXTENSIONS candidate-source manifests and LOCAL_CONFIGURATION selection, replacement, priority, and compatibility-resolution inputs referenced by that authority))`

## Definition of Done

the Task is **not done if** (any generic compilation authority is owned outside CORE_META_MODEL **or** LOCAL_CONFIGURATION owns any generic compilation rule instead of only Project-owned selection and resolution inputs **or** the three structural Source Layers are not CORE_META_MODEL, INSTALLED_EXTENSIONS, and LOCAL_CONFIGURATION in that order **or** the compilation contract can omit CORE_META_MODEL or LOCAL_CONFIGURATION **or** INSTALLED_EXTENSIONS contributes any Source Atom revision **or** it can retain inactive, replaced, incompatible, or lower-priority authority after Local Configuration resolution **or** it can read any methodology source outside 000_APPLICABLE_MTHD_sources without an exact governed reference **or** it can modify any source Layer **or** the same source frontier can produce different ordered output **or** the contract omits exact source and output digests **or** the compiler requires LLM inference **or** generated Applicable Methodology can gain independent authority **or** deleting generated carriers can prevent complete regeneration **or** this Task writes a final generated Applicable Methodology Carrier before CA-P-109 establishes its target).

## Details

place the generic compiler contract, deterministic ordering, output schemas, digest rules, GOVERNS and DEPENDS_ON indexes, and compilation Evaluations in CORE_META_MODEL without materializing final generated Carriers. treat INSTALLED_EXTENSIONS as an empty non-contributing structural Source Layer and LOCAL_CONFIGURATION as Project-owned selection and resolution inputs only. define subject- or process-scoped retrieval to seed from matching GOVERNS paths and add DEPENDS_ON authority only through prerequisite closure. preserve an explicit extension boundary for later LLM assistance, but do not use it unless subsequent Evaluation evidence demonstrates insufficient mechanical retrieval quality. defer the first final-carrier compilation to CA-P-110 after CA-P-109 establishes the target roots.

## Task Scope Resolution

the Assignee used CA-P-102 through CA-P-106 evidence and their accepted successors. CA-R-1224 selects CORE_META_MODEL followed by LOCAL_CONFIGURATION as the only contributing Source Layers. CA-R-1225 and CA-R-1221 establish that INSTALLED_EXTENSIONS is empty and contributes zero Candidates. CA-R-1226 defines the one-revision Project Customization boundary, and CA-R-1227 selects no local Tool, MCP, or App mode. [CA-P-107 compiler authority repair](../execution_evidence/CA-P-107-compiler-authority-repair.projection.json) records the retired invalid identities, globally unused successor identities, exact two-source semantics, and the required later mapping by CA-P-108 and CA-P-109.

## Completion Record

PASS. the previous CA-M-125, CA-M-126, CA-E-300, and CA-D-251 carriers were invalid because their identities were already issued elsewhere in the live carrier frontier; they are preserved as non-Atom invalid-identity archives. CA-M-224 defines the deterministic no-LLM algorithm with three structural layers and exactly two contributors. CA-M-225 defines mechanical Subject- and Process-scoped retrieval. CA-E-379 defines the falsifying compilation validation. CA-D-253 binds the source and output locations without creating them. the repaired authority remains in the old `.caprmedio` source area for CA-P-108 and CA-P-109 to map and migrate. No final Applicable Methodology Carrier was generated, no Source Layer Carrier was changed, and all Definition-of-Done conditions pass at 99 percent execution confidence.
