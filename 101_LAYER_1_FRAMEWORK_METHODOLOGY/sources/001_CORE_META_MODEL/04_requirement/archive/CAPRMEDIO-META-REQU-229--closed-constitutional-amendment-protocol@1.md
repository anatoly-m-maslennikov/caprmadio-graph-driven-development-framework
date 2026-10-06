---
subject_scope: authority
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMEDIO-META-REQU-210--closed-constitutional-amendment-protocol
  - type: relates_to
    targets:
      - CAPRMEDIO-META-REQU-199--exploration-mode-defers-artifact-creation
      - CAPRMEDIO-META-REQU-200--meta-eligibility-rule
      - CAPRMEDIO-META-REQU-204--forward-change-propagation
      - CAPRMEDIO-META-REQU-207--bounded-recursive-self-hosting
      - CAPRMEDIO-META-REQU-228--optional-thin-maintained-views
---

# Requirement — Close every constitutional amendment

Every semantic change to META follows one closed amendment sequence:

1. explore without changing governed truth;
2. obtain explicit operator acceptance for one primary claim;
3. map affected authority, layers, handoffs, views, methods, implementations,
   and evaluation;
4. verify META eligibility and acyclic layer placement;
5. classify the authority change and commit either a same-ID revision or a
   successor with a new identity;
6. archive only predecessors that are fully replaced;
7. complete the revision-bound lineage-impact review forward through affected
   descendants;
8. refresh every enabled maintained Specification required by the applicable
   gate; and
9. verify the resulting authority and downstream fixed point.

A failed or ambiguous step leaves the amendment incomplete and cannot claim a
new fixed point. Git preserves each committed authority revision; lineage
analysis records the disposition of every affected branch.

## Rationale

The successor removes obsolete Evergreen terminology while preserving a
replayable governance-of-governance boundary.
