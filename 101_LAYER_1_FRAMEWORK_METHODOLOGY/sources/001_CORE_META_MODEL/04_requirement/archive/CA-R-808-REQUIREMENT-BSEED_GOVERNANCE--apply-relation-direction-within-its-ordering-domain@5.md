---
subjects:
  - relation-model
  - atom-boundary
cce_version: cce_1
cce_form: obligation
version: 5
updated_at: 2026-08-23 11:32:10
relations:
  child_of:
    - CAPRMEDIO-GOV-REQU-767--keep-active-prmedo-relations-within-active-authority
---
# Apply relation direction within its ordering domain

EVERY declared relation MUST satisfy the target position and ordering domain registered for its relation family. Normative-authority relations MUST use the global-tier and authority hierarchy, temporal relations MUST use lifecycle succession, realization relations MUST use realization order, dependency relations MUST use dependency order, and every other admitted domain MUST use its own registered order. A universal upstream or downstream rule MUST NOT be inferred across different ordering domains, and an inverse-derived view MUST NOT create another declared edge.
