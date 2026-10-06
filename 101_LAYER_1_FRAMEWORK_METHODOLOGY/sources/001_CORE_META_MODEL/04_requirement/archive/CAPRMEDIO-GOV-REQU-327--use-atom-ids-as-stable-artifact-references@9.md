---
subject_scopes:
  - relation-model
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a01cb6-4ee4-7553-b68d-0823dda35094
version: 9
updated_at: 2026-08-22 04:00:55
relations:
  child_of:
    - CAPRMEDIO-META-REQU-122
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
    - CA-R-888
---
# Use Atom IDs as stable Artifact references

Every ordinary relation target to an identified role-classified Atom must use the target's exact Atom ID `<PROJECT_PREFIX>-<CONTENT_ROLE_LETTER>-<NUMBER>`, derived from the immutable leading segment of its canonical Carrier filename. A relation target to Intent uses its canonical Carrier stem `CA-intent`. Mutable filename components are not part of the reference. A draft has no Atom ID and may be addressed only by its complete current filename stem as a provisional draft locator; every draft rename must update its incoming provisional references in the same governed change.

The resolver must distinguish Atom-ID references from provisional draft locators, resolve exactly one current Carrier under `.caprmedio`, and reject an ambiguous, missing, duplicated, or mismatched reference. Directory location and mutable filename components outside the Atom-ID segment are not part of an identified Atom's stable reference, so a governed Carrier rename or move preserves incoming Atom-ID relations.
