---
subjects:
  governs:
    continuant:
      - relation-model
  depends_on:
    continuant:
      - atom-boundary
cce_version: cce_1
cce_form: obligation
version: 12
updated_at: 2026-09-06 01:45:12 +0400
relations:
  child_of:
    - CAPRMEDIO-GOV-REQU-767-CORE_META_MODEL-CORE-REQUIREMENT--keep-active-prmedo-relations-within-active-authority
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-807-CORE_META_MODEL-REQUIREMENT--record-replacement-transitions-in-the-journal.md
---
# Record replacement transitions in the Journal

Replacement history **must** be recorded **only** **in** the authoritative Journal event that archives the predecessor. THE authoritative Journal event that archives the predecessor **must** name the explicit predecessor Atom ID **and** **`>=1`** already active successor Atom IDs. Active current-state Atom relations **must not** carry replacement history. Formal `replaced_by` **and** `replacement_of` relation realization **must** remain deferred, **and** **any** later replacement navigation **must** be derived from immutable Journal **and** archive history under separately admitted authority.
