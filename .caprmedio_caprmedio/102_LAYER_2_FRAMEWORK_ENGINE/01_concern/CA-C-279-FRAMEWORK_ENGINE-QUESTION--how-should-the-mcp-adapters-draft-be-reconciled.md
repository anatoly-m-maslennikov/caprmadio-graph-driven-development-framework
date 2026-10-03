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
updated_at: "2026-09-23 19:20:45 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-D-049", "CA-M-159", "CA-M-166", "CA-R-1111", "CA-R-1116", "CA-R-1117", "CA-R-1118", "CA-R-1119"]}
---
# Summary

How should the MCP adapters draft be reconciled?

## Claim

how should the identified Draft Atom be reconciled **with** active authority **and** Project Principles **without** losing useful information **or** promoting it?

### Draft under review

- prior Carrier, now archived: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/07_delivery/archive/CA-D--DELIVERY-FR_ENGN--provide-versioned-mcp-adapter-surfaces@1.md`.
- inspected SHA-256: `3a3f3e8624c315bd24cff8c6e7ffc429ca5362faf2e3aeec0f820596e5443ee7`.
- review point: 70 of 79; campaign `draft-review-8afeac79`.

### Prior review finding

> **Revise/split** — Place MCP-specific residual carrier contract in MCP; reuse active negotiation, request-bound and result Requirements.
>
> Basis: `CA-R-1111`, `CA-R-1116`, `CA-R-1117`, `CA-R-1119`; I7,I8. Reviewer confidence: 99%.

### Active authority cited by the review

- `CA-R-1111@10`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP/04_requirement/CA-R-1111-MCP-REQUIREMENT--delegate-mcp-calls-to-canonical-tools.md`; SHA-256 `f3bd57e26ac8d6c2e457fb40a5119a173f03f16ec1dc572931755bbb2c9f33a4`.
- `CA-R-1116@8`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP/04_requirement/CA-R-1116-MCP-REQUIREMENT--negotiate-supported-mcp-protocol-capabilities.md`; SHA-256 `41fc42ad57bb56bd54c3ab649cf8e021033abdb1138099a0038e59646f6b5a4b`.
- `CA-R-1117@8`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP/04_requirement/CA-R-1117-MCP-REQUIREMENT--bound-and-control-mcp-requests.md`; SHA-256 `f9e9ac3f9730660aeeba7ba01f843c0c852d560bf19c63532b9d551f566e119a`.
- `CA-R-1119@8`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP/04_requirement/CA-R-1119-MCP-REQUIREMENT--return-stable-model-readable-mcp-results.md`; SHA-256 `1663002b0f30f8f4f4c5187e2caf633b8f3ce13e58029daa72ff2071d7b5df7c`.

### Principles to apply

- [CA-M-002](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-002-PRINCIPLE-METHOD--dry-don-t-repeat-yourself.md).
- [CA-M-005](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-005-PRINCIPLE-METHOD--add-complexity-only-when-necessary.md).
- [CA-M-006](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-006-PRINCIPLE-METHOD--keep-the-whole-project-coherent.md).
- [CA-R-1490](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/04_requirement/CA-R-1490-PRINCIPLE-REQUIREMENT--preserve-valuable-information.md).
- [CA-E-001](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/06_evaluation/CA-E-001-PRINCIPLE-EVALUATION--make-governed-commitments-and-results-checkable.md).

### Resolution

resolved for the approved group-12 repair. the Operator accepted the corrections **and** required the canonical Scope Unit spelling FRAMEWORK_ENGINE.

MCP owns its remaining adapter publication. CA-R-1111 **and** CA-R-1116 through CA-R-1119 retain delegation, negotiation, bounded requests, authorization, **and** result behavior. the replacement uses the exact Scope Unit name FRAMEWORK_ENGINE **and** does **not** adopt a protocol version from the legacy reference links.

#### Replacement Drafts

- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP/07_delivery/drafts/CA-D--MCP-DELIVERY--publish-versioned-mcp-adapter-declarations.md`; Version 1; SHA-256 `31cfc2e1f4da8740a44dbb02da39768ae530ac64f5d53a8c1e6aec9c60c63d9e`.

#### Preservation and boundary

- exact prior Draft: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/07_delivery/archive/CA-D--DELIVERY-FR_ENGN--provide-versioned-mcp-adapter-surfaces@1.md`; Version 1; SHA-256 `3a3f3e8624c315bd24cff8c6e7ffc429ca5362faf2e3aeec0f820596e5443ee7`.
- new Summaries start new Draft identities under CA-R-1464; no Atom IDs are allocated **and** nothing is promoted.
- active Principles favor existing authority over duplication, preserve valuable prior content, **and** require explicit role, scope, **and** evidence boundaries. independent Claims are separated under CA-R-918 **and** the R/D profiles CA-M-310 **and** CA-M-313.
- original Drafts **and** prior Question Revisions remain byte-for-byte recoverable. historical review findings are preserved as history, **not** unresolved current decisions.
- no active authority, implementation, runtime, configuration, installed release, Hook, **or** Projection is changed. the replacement Drafts do **not** claim implementation conformance.

#### Active authority checked

- `CA-D-049@6`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP/07_delivery/CA-D-049-MCP-DELIVERY--bind-mcp-delivery-place.md`; SHA-256 `ccb4221676336035e51607b534e47234b6ad777c92ea413b03e6c46d8ea56f23`.
- `CA-M-159@9`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-159-PROGRAMMATIC-CORE-METHOD--define-typed-contracts-at-replaceable-technical-boundaries.md`; SHA-256 `21454fcd4f401ce9b49f7a1576744953c66e19eefa2ab1735ffb994dc2b15b20`.
- `CA-M-166@11`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-166-PROGRAMMATIC-CORE-METHOD--preserve-declared-interface-compatibility-boundaries.md`; SHA-256 `14497a272a2c9c45c2d585603236eabe4d9487c802b000f01f77d65a24ff3a0e`.
- `CA-R-1111@10`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP/04_requirement/CA-R-1111-MCP-REQUIREMENT--delegate-mcp-calls-to-canonical-tools.md`; SHA-256 `f3bd57e26ac8d6c2e457fb40a5119a173f03f16ec1dc572931755bbb2c9f33a4`.
- `CA-R-1116@8`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP/04_requirement/CA-R-1116-MCP-REQUIREMENT--negotiate-supported-mcp-protocol-capabilities.md`; SHA-256 `41fc42ad57bb56bd54c3ab649cf8e021033abdb1138099a0038e59646f6b5a4b`.
- `CA-R-1117@8`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP/04_requirement/CA-R-1117-MCP-REQUIREMENT--bound-and-control-mcp-requests.md`; SHA-256 `f9e9ac3f9730660aeeba7ba01f843c0c852d560bf19c63532b9d551f566e119a`.
- `CA-R-1118@8`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP/04_requirement/CA-R-1118-MCP-REQUIREMENT--enforce-least-authority-and-secret-boundaries.md`; SHA-256 `82d59e479f842f88999db966ca6796d90dc272b0ca58cc032a99cbfd68308d3c`.
- `CA-R-1119@8`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP/04_requirement/CA-R-1119-MCP-REQUIREMENT--return-stable-model-readable-mcp-results.md`; SHA-256 `1663002b0f30f8f4f4c5187e2caf633b8f3ce13e58029daa72ff2071d7b5df7c`.
