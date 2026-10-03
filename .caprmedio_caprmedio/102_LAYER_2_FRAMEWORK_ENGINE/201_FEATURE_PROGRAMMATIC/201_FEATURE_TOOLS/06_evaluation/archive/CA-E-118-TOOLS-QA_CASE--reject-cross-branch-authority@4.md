---
subjects:
  declared:
    continuant:
      - artifact-validation
    occurrent:
      - evaluation
version: 4
updated_at: 2026-08-23 17:53:53 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  evaluation_for:
    - CA-R-1137
---
# Reject cross branch authority

## Test case

**Fixture:** Point a tier-classified RMED child at a same-tier Atom in a sibling structural scope.

**Expected result:** Fail with the stable cross-branch-authority diagnostic and a non-zero exit.
