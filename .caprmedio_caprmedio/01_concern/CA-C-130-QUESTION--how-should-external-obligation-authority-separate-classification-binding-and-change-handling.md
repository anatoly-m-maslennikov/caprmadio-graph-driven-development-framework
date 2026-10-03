---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Atom/Claim"
  depends_on:
    - "Atom/Content Role"
    - "Governance Origin"
    - "Artifact/Revision"
    - "Atom Change Classification"
    - "Lineage Impact Analysis"
    - "Action"
    - "Process"
priority: medium
version: 2
updated_at: "2026-09-20 23:49:39 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# How should external-obligation authority separate classification, binding, and change handling?

which existing authorities **or** separately identified Claims **must** own the external-obligation classification, accepted-source pin, consumed-Revision binding, **and** source-change disposition currently combined **in** CAPRMEDIO-META-REQU-100?

## evidence

the corrected source no longer derives Content Role from external Governance Origin. CA-R-1531 **and** CAPRMEDIO-META-REQU-113 determine contribution independently of origin; CAPRMEDIO-META-REQU-127 determines ownership. CA-D-393 **and** the admitted external Requirement/Method Types already rely on that distinction.

the source still combines pinned source version **or** digest, immutable consumed obligations, same-obligation Revision changes, different-obligation replacement, **and** lineage-impact disposition. CA-R-1432 **and** CA-R-807 already own general identity **and** replacement boundaries. the precise remaining external-specific acceptance **and** consumer-disposition responsibility is **not** established by moving **all** change-related wording into Operations.

## principle check

CA-M-002 requires reuse of existing authority; CA-M-005 rejects a duplicate external lifecycle; CA-M-006 requires coherent Content Role boundaries; CA-R-1490 requires preservation of source pins **and** lineage evidence. these Principles resolve the classification error but do **not** establish the exact reusable Action boundary **or** prove that the remaining conditions share one acceptance lifecycle under CA-R-1270.

## disposition

preserve the corrected source **and** its dependent authority while this split is unresolved. classify conditions by their actual contribution, reuse current identity authority, **and** preserve the applicable external source **and** every consumed Revision binding. do **not** invent an acceptance workflow, execution record, external Type, **or** new governing Entity merely **to** pass a role check. the legacy `scope-topology` Subject remains under CA-C-111's canonical-target review.
