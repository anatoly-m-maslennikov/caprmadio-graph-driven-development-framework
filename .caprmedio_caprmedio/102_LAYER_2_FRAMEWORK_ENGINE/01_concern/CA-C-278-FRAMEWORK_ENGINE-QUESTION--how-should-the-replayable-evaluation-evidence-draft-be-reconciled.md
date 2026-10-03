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
relations: {"relates_to": ["CA-D-250", "CA-D-437", "CA-E-455", "CA-M-285", "CA-R-1490", "CAPRMEDIO-META-REQU-097", "CAPRMEDIO-META-REQU-158"]}
---
# Summary

How should the Replayable Evaluation evidence draft be reconciled?

## Claim

how should the identified Draft Atom be reconciled **with** active authority **and** Project Principles **without** losing useful information **or** promoting it?

### Draft under review

- prior Carrier, now archived: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/07_delivery/archive/CA-D--DELIVERY-FR_ENGN--provide-replayable-software-evaluation-evidence@2.md`.
- inspected SHA-256: `170ffa256f642978e77e028c9e3376c2c99c84aa4ace896baa9c3a1de4af983e`.
- review point: 69 of 79; campaign `draft-review-8afeac79`.

### Prior review finding

> **Revise/split** — Retain record encoding/placement only; reference selected evaluation technique and evidence rules; use valuable-information retention.
>
> Basis: `CA-M-285`, `CA-D-250`, `CA-R-1490`; I7,I8. Reviewer confidence: 98%.

### Active authority cited by the review

- `CA-M-285@9`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-285-PROGRAMMATIC-CORE-METHOD--select-software-evaluation-techniques-by-failure-mode.md`; SHA-256 `ab57a74d62e1a75aa1a7c56c2e2b0659ecdfdb88b722c729c6fd208ae8af47c2`.
- `CA-D-250@9`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/07_delivery/CA-D-250-PROGRAMMATIC-CORE-DELIVERY--provide-programmatic-software-carriers.md`; SHA-256 `0631b4211c0973f6f622e3a3b7ca956f17c67e2d442d3149958ff0f7c7d32520`.
- `CA-R-1490@1`: `.caprmedio_caprmedio/04_requirement/CA-R-1490-PRINCIPLE-REQUIREMENT--preserve-valuable-information.md`; SHA-256 `af65fc105597d5966efaa59d663d452dfa7d0376ad9ebe7bb2b521077ccafb65`.

### Principles to apply

- [CA-M-002](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-002-PRINCIPLE-METHOD--dry-don-t-repeat-yourself.md).
- [CA-M-005](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-005-PRINCIPLE-METHOD--add-complexity-only-when-necessary.md).
- [CA-M-006](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-006-PRINCIPLE-METHOD--keep-the-whole-project-coherent.md).
- [CA-R-1490](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/04_requirement/CA-R-1490-PRINCIPLE-REQUIREMENT--preserve-valuable-information.md).
- [CA-E-001](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/06_evaluation/CA-E-001-PRINCIPLE-EVALUATION--make-governed-commitments-and-results-checkable.md).

### Resolution

resolved for the approved group-11 repair. the Operator placed Python-specific details **in** PROGRAMMATIC. the old Engine Draft is archived; **any** replacement remains Draft **and** unpromoted.

- replacement Draft: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/07_delivery/drafts/CA-D--PROGRAMMATIC-DELIVERY--deliver-replayable-software-evaluation-records.md`; Version 1; SHA-256 `312917feddce4e00236a1311bb822589b518ccd039124dac95422386b2cc1ad6`.
- exact prior Draft: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/07_delivery/archive/CA-D--DELIVERY-FR_ENGN--provide-replayable-software-evaluation-evidence@2.md`; Version 2; SHA-256 `170ffa256f642978e77e028c9e3376c2c99c84aa4ace896baa9c3a1de4af983e`.

Evaluation technique selection remains **in** CA-M-285; separate check results remain governed by CA-E-455. the replacement keeps the evidence-record content **and** placement boundary. valuable information replaces the obsolete reusable-only retention filter under CA-R-1490. retained references **must not** depend **only** on disposable output, **and** the records do **not** become another Journal.

- DRY **and** coherence favor existing authority over repeated rules. the narrower replacements carry one independently replaceable Delivery contribution under CA-R-918 **and** CA-M-313.
- changed Summaries start new Draft identities at Version 1 under CA-R-1464; no Atom IDs are allocated **and** no authoritative promotion occurs.
- historical Engine placement remains **only** **in** the preserved archive **and** this review record. new technical proposals declare PROGRAMMATIC as their owning **and** target Scope Unit.
- prior Questions **and** Drafts are preserved byte-for-byte. cited review findings remain historical evidence, **not** unresolved current decisions.
- this repair changes no active Method, settings file, technical configuration, Tool, runtime, installed release, **or** Projection. it does **not** claim that those implementations already satisfy the Drafts.

#### Active authority checked

- `CA-D-250@9`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/07_delivery/CA-D-250-PROGRAMMATIC-CORE-DELIVERY--provide-programmatic-software-carriers.md`; SHA-256 `0631b4211c0973f6f622e3a3b7ca956f17c67e2d442d3149958ff0f7c7d32520`.
- `CA-D-437@8`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/07_delivery/CA-D-437-PROGRAMMATIC-CORE-DELIVERY--materialize-the-project-temporary-boundary.md`; SHA-256 `6f36d43c22e9da8d595bdb80666aaad96d99412aec2e964c5cf698f2e79666d0`.
- `CA-E-455@8`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-455-PROGRAMMATIC-CORE-EVAL_APPROACH--evaluate-changed-python-targets-under-one-configuration.md`; SHA-256 `1f4947fe6e008b1c5bc67425b9b77708505635f243144a4fcb22644f3d48e76a`.
- `CA-M-285@9`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-285-PROGRAMMATIC-CORE-METHOD--select-software-evaluation-techniques-by-failure-mode.md`; SHA-256 `ab57a74d62e1a75aa1a7c56c2e2b0659ecdfdb88b722c729c6fd208ae8af47c2`.
- `CA-R-1490@1`: `.caprmedio_caprmedio/04_requirement/CA-R-1490-PRINCIPLE-REQUIREMENT--preserve-valuable-information.md`; SHA-256 `af65fc105597d5966efaa59d663d452dfa7d0376ad9ebe7bb2b521077ccafb65`.
- `CAPRMEDIO-META-REQU-097@15`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CAPRMEDIO-META-REQU-097-CORE_META_MODEL-CORE-REQUIREMENT--requirement-keep-provenance-separate-from-evidence.md`; SHA-256 `8604de6d53fe8b7ecfd4ca1ea68b4fad76128d624b949b76a0d989577bfd4c04`.
- `CAPRMEDIO-META-REQU-158@13`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CAPRMEDIO-META-REQU-158-CORE_META_MODEL-CORE-REQUIREMENT--use-one-project-journal-for-governed-provenance.md`; SHA-256 `d9d05e7eb7c57d770f802812b365559f908a071e9d99fe7b6ccaf10b40b06d31`.
