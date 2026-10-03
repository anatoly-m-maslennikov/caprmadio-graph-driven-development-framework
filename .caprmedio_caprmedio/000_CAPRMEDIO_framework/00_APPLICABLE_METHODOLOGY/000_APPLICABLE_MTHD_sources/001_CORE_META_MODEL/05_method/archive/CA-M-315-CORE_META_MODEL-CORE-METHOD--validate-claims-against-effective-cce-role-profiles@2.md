---
subjects:
  governs: "CCE/Role Profile/validation"
  depends_on:
    - "CCE/Role Profile"
    - "CCE Operator"
    - "Atom/Claim"
    - "Atom/Content Role"
    - "Type"
version: 2
updated_at: "2026-09-22 18:51:52 +0400"
relations:
  child_of:
    - CA-M-307
    - CA-M-308
  relates_to:
    - CA-M-113
    - CA-M-229
    - CA-M-234
---
# Validate Claims against Effective CCE Role Profiles

**to** validate one Atom Claim against its effective CCE Role Profile, the Validator **must** perform **all** of:

1. resolve the effective profile under CA-M-308 **without** inferring a different Content Role from the wording under review.
2. identify the Claim's primary contribution, every subordinate content slot, **and** every registered CCE Operator occurrence.
3. verify that the primary contribution matches the resolved role profile **and** that every narrower Type **or** content-slot contribution remains within its admitted boundary.
4. verify that every CCE Operator use is permitted for its exact primary **or** subordinate context **and** has explicit logical scope.
5. reject a primary contribution owned by another Content Role even **when** every individual CCE Operator is present **in** the global registry.
6. for Concern **or** Analysis, validate shared CCE **and** their governed Content Role meaning **without** requiring a role-specific profile.
7. for Implementation content, report that no CCE Role Profile is registered; do **not** apply another role's profile **or** report role-profile conformance.
8. report every mismatch by Content Role, Type, content slot, primary contribution, **and** Operator occurrence. do **not** rewrite the source Claim **or** report conformance while one required classification remains unresolved.

global CCE Operator registration is necessary but insufficient for role-profile conformance.
