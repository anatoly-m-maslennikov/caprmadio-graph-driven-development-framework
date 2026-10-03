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
relations: {"relates_to": ["CA-D-250", "CA-E-394", "CA-E-397", "CA-M-159", "CA-M-166", "CA-M-281", "CA-M-286"]}
---
# Summary

How should the Boundary schemas draft be reconciled?

## Claim

how should the identified Draft Atom be reconciled **with** active authority **and** Project Principles **without** losing useful information **or** promoting it?

### Draft under review

- prior Carrier, now archived: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/07_delivery/archive/CA-D--DELIVERY-FR_ENGN--provide-explicit-validated-boundary-schemas@2.md`.
- inspected SHA-256: `081f8379d2a71a91b227c270566a791780dda12d4f1521154752bfae2c63b820`.
- review point: 66 of 79; campaign `draft-review-8afeac79`.

### Prior review finding

> **Revise/split** — Reference Pydantic selection and typed-boundary Methods; keep only public schema/version serialization in Delivery.
>
> Basis: `CA-M-286`, `CA-M-159`, `CA-D-250`; I7,I8. Reviewer confidence: 99%.

### Active authority cited by the review

- `CA-M-286@8`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-286-PROGRAMMATIC-CORE-METHOD--validate-untrusted-structured-data-with-pydantic.md`; SHA-256 `70fd46681fe112c2ce926c38572ccc22b8f41d95644e852a7cf8241433f64a16`.
- `CA-M-159@9`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-159-PROGRAMMATIC-CORE-METHOD--define-typed-contracts-at-replaceable-technical-boundaries.md`; SHA-256 `21454fcd4f401ce9b49f7a1576744953c66e19eefa2ab1735ffb994dc2b15b20`.
- `CA-D-250@9`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/07_delivery/CA-D-250-PROGRAMMATIC-CORE-DELIVERY--provide-programmatic-software-carriers.md`; SHA-256 `0631b4211c0973f6f622e3a3b7ca956f17c67e2d442d3149958ff0f7c7d32520`.

### Principles to apply

- [CA-M-002](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-002-PRINCIPLE-METHOD--dry-don-t-repeat-yourself.md).
- [CA-M-005](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-005-PRINCIPLE-METHOD--add-complexity-only-when-necessary.md).
- [CA-M-006](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-006-PRINCIPLE-METHOD--keep-the-whole-project-coherent.md).
- [CA-R-1490](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/04_requirement/CA-R-1490-PRINCIPLE-REQUIREMENT--preserve-valuable-information.md).
- [CA-E-001](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/06_evaluation/CA-E-001-PRINCIPLE-EVALUATION--make-governed-commitments-and-results-checkable.md).

### Resolution

resolved for the approved group-11 repair. the Operator placed Python-specific details **in** PROGRAMMATIC. the old Engine Draft is archived; **any** replacement remains Draft **and** unpromoted.

- replacement Draft: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/07_delivery/drafts/CA-D--PROGRAMMATIC-DELIVERY--publish-version-bound-machine-boundary-schemas.md`; Version 1; SHA-256 `04e2853cf52d1aab4dff451f9859d2a2c78f0e2ad121e33abe1aaedca9145c68`.
- exact prior Draft: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/07_delivery/archive/CA-D--DELIVERY-FR_ENGN--provide-explicit-validated-boundary-schemas@2.md`; Version 2; SHA-256 `081f8379d2a71a91b227c270566a791780dda12d4f1521154752bfae2c63b820`.

typed-interface design belongs **to** CA-M-159; Pydantic selection, strictness, extra-field handling, **and** typed-core separation belong **to** CA-M-286. the replacement keeps the consumed JSON Schema publication **and** version/serialization binding **without** requiring Pydantic throughout the core **or** inventing a supported version. compatibility remains governed by CA-M-166.

- DRY **and** coherence favor existing authority over repeated rules. the narrower replacements carry one independently replaceable Delivery contribution under CA-R-918 **and** CA-M-313.
- changed Summaries start new Draft identities at Version 1 under CA-R-1464; no Atom IDs are allocated **and** no authoritative promotion occurs.
- historical Engine placement remains **only** **in** the preserved archive **and** this review record. new technical proposals declare PROGRAMMATIC as their owning **and** target Scope Unit.
- prior Questions **and** Drafts are preserved byte-for-byte. cited review findings remain historical evidence, **not** unresolved current decisions.
- this repair changes no active Method, settings file, technical configuration, Tool, runtime, installed release, **or** Projection. it does **not** claim that those implementations already satisfy the Drafts.

#### Active authority checked

- `CA-D-250@9`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/07_delivery/CA-D-250-PROGRAMMATIC-CORE-DELIVERY--provide-programmatic-software-carriers.md`; SHA-256 `0631b4211c0973f6f622e3a3b7ca956f17c67e2d442d3149958ff0f7c7d32520`.
- `CA-E-394@7`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-394-PROGRAMMATIC-CORE-EVAL_APPROACH--evaluate-pydantic-boundary-contracts.md`; SHA-256 `d36770e7729db7dc773e3685d7845ba719e39c7786f9e46b29c0e9698c354696`.
- `CA-E-397@6`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-397-PROGRAMMATIC-CORE-EVAL_APPROACH--verify-machine-contract-compatibility.md`; SHA-256 `83e6fdeaafee27ba27f9a665aa6788fa3881bba8a224fa912defefa2628f41c6`.
- `CA-M-159@9`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-159-PROGRAMMATIC-CORE-METHOD--define-typed-contracts-at-replaceable-technical-boundaries.md`; SHA-256 `21454fcd4f401ce9b49f7a1576744953c66e19eefa2ab1735ffb994dc2b15b20`.
- `CA-M-166@11`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-166-PROGRAMMATIC-CORE-METHOD--preserve-declared-interface-compatibility-boundaries.md`; SHA-256 `14497a272a2c9c45c2d585603236eabe4d9487c802b000f01f77d65a24ff3a0e`.
- `CA-M-281@11`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-281-PROGRAMMATIC-CORE-METHOD--declare-one-python-and-software-configuration-boundary.md`; SHA-256 `e825a96f745f0b9e73b795c01b076ce8e4a5e7815784f4910e2889595baa6441`.
- `CA-M-286@8`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-286-PROGRAMMATIC-CORE-METHOD--validate-untrusted-structured-data-with-pydantic.md`; SHA-256 `70fd46681fe112c2ce926c38572ccc22b8f41d95644e852a7cf8241433f64a16`.
