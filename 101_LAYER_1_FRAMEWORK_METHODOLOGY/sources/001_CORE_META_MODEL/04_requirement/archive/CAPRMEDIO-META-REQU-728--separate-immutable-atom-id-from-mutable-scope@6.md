---
subject_scopes:
  - artifact-model
version: 6
updated_at: 2026-08-21 04:43:43
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-098--scope-path-does-not-change-semantic-coordinates
    - CAPRMEDIO-META-REQU-128--separate-artifact-carrier-and-revision
---
# Separate immutable Atom ID from mutable scope

A role-classified Atom's stable Atom ID has the semantic components `<PREFIX>-<CONTENT_ROLE_LETTER>-<NUMBER>`. A role-classified draft has no assigned Atom ID; operator acceptance assigns exactly one value and canonically encodes it as the Carrier filename's immutable leading segment. The sole roleless Intent Atom uses its separately governed canonical identity. Once assigned, the Atom ID is independent of the Atom's mutable Carrier address, Structural scope, Tier, Summary, format, Revision, and all filename components outside the Atom-ID segment. A change to an identity-bearing semantic fact creates a successor Atom with a new Atom ID.
