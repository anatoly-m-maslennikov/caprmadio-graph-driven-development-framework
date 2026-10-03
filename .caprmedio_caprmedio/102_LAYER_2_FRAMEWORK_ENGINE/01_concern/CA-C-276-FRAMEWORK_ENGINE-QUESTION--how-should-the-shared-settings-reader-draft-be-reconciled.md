---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Atom"
  depends_on:
    - "Atom/Claim"
    - "Artifact/Revision"
    - "Project"
    - "Operator"
priority: medium
version: 3
updated_at: "2026-09-23 19:08:49 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-D-364", "CA-D-365", "CA-M-284"]}
---
# Summary

How should the Shared Settings Reader draft be reconciled?

## Claim

how should the identified Draft Atom be reconciled **with** active authority **and** Project Principles **without** losing useful information **or** promoting it?

### Draft under review

- prior Carrier, now archived: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/07_delivery/archive/CA-D--DELIVERY-FR_ENGN--provide-one-centralized-validated-settings-reader@2.md`.
- inspected SHA-256: `28828f9cc214a427bdb2809c4009f2a05341ce54e1447b9377c7a11ae01e928d`.
- review point: 67 of 79; campaign `draft-review-8afeac79`.

### Prior review finding

> **Retire** — Old path and Projection/mutation model contradict the current Reader and authoritative Settings Carrier.
>
> Basis: `CA-M-284`, `CA-D-364`, `CA-D-365`; I7. Reviewer confidence: 99%.

### Active authority cited by the review

- `CA-M-284@11`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-284-PROGRAMMATIC-CORE-METHOD--read-engine-settings-through-one-shared-boundary.md`; SHA-256 `690b9f8716d649e8d27a7e63ff0129455d6de14f9cf3fd30a7173cf25f9dc049`.
- `CA-D-364@6`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-364-CORE_META_MODEL-DELIVERY--bind-project-settings-to-its-authoritative-toml-carrier.md`; SHA-256 `5d2d615155201df76cae3c7ae218dbb34e152e5a52eec9867bf9a6ebb0c3c270`.
- `CA-D-365@8`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-365-CORE_META_MODEL-DELIVERY--bind-project-settings-revisions-to-journal-receipts.md`; SHA-256 `e4072704bab06ff5ed4c067c3ef871017896666e2f1be126e34ab43edc164100`.

### Principles to apply

- [CA-M-002](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-002-PRINCIPLE-METHOD--dry-don-t-repeat-yourself.md).
- [CA-M-005](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-005-PRINCIPLE-METHOD--add-complexity-only-when-necessary.md).
- [CA-M-006](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-006-PRINCIPLE-METHOD--keep-the-whole-project-coherent.md).
- [CA-R-1490](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/04_requirement/CA-R-1490-PRINCIPLE-REQUIREMENT--preserve-valuable-information.md).
- [CA-E-001](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/06_evaluation/CA-E-001-PRINCIPLE-EVALUATION--make-governed-commitments-and-results-checkable.md).

### Resolution

resolved for the approved group-11 repair. the Operator placed Python-specific details **in** PROGRAMMATIC. the old Engine Draft is archived; **any** replacement remains Draft **and** unpromoted.

- exact prior Draft: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/07_delivery/archive/CA-D--DELIVERY-FR_ENGN--provide-one-centralized-validated-settings-reader@2.md`; Version 2; SHA-256 `28828f9cc214a427bdb2809c4009f2a05341ce54e1447b9377c7a11ae01e928d`.

retired **without** replacement. CA-M-284 already supplies the shared read-only validated Settings Reader **and** immutable derived snapshot. CA-D-364 owns the authoritative Project Settings TOML location; CA-D-365 binds its Revision evidence. the legacy `.caprmedio/` path **and** claim that Project Settings is a Projection are obsolete. Settings changes target their authoritative Carrier, **not** a regenerated Settings Projection. no Reader Implementation was changed.

- DRY **and** coherence favor existing authority over repeated rules. the narrower replacements carry one independently replaceable Delivery contribution under CA-R-918 **and** CA-M-313.
- changed Summaries start new Draft identities at Version 1 under CA-R-1464; no Atom IDs are allocated **and** no authoritative promotion occurs.
- historical Engine placement remains **only** **in** the preserved archive **and** this review record. new technical proposals declare PROGRAMMATIC as their owning **and** target Scope Unit.
- prior Questions **and** Drafts are preserved byte-for-byte. cited review findings remain historical evidence, **not** unresolved current decisions.
- this repair changes no active Method, settings file, technical configuration, Tool, runtime, installed release, **or** Projection. it does **not** claim that those implementations already satisfy the Drafts.

#### Active authority checked

- `CA-D-364@6`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-364-CORE_META_MODEL-DELIVERY--bind-project-settings-to-its-authoritative-toml-carrier.md`; SHA-256 `5d2d615155201df76cae3c7ae218dbb34e152e5a52eec9867bf9a6ebb0c3c270`.
- `CA-D-365@8`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-365-CORE_META_MODEL-DELIVERY--bind-project-settings-revisions-to-journal-receipts.md`; SHA-256 `e4072704bab06ff5ed4c067c3ef871017896666e2f1be126e34ab43edc164100`.
- `CA-M-284@11`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-284-PROGRAMMATIC-CORE-METHOD--read-engine-settings-through-one-shared-boundary.md`; SHA-256 `690b9f8716d649e8d27a7e63ff0129455d6de14f9cf3fd30a7173cf25f9dc049`.
