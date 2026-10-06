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
version: 9
updated_at: 2026-08-29 02:40:41 +0400
relations:
  child_of:
    - CAPRMEDIO-GOV-REQU-767--keep-active-prmedo-relations-within-active-authority
---
# Apply relation direction within its ordering domain

**every** declared relation **must** satisfy the target position **and** ordering domain registered for its relation family. Normative-authority relations **must** use the global-tier **and** authority hierarchy, temporal relations **must** use lifecycle succession, realization relations **must** use realization order, dependency relations **must** use dependency order, **and** **every** other admitted domain **must** use its own registered order. A universal upstream **or** downstream rule **must not** be inferred across different ordering domains, **and** an inverse-derived view **must not** create another declared edge.
