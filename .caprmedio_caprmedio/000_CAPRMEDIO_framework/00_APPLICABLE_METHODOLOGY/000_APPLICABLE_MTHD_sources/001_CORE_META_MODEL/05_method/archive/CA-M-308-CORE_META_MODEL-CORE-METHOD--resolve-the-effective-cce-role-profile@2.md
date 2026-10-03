---
subjects:
  governs: "CCE/Role Profile/resolution"
  depends_on:
    - "CCE/Role Profile"
    - "Atom/Content Role"
    - "Type"
    - "Atom/Claim"
version: 2
updated_at: "2026-09-22 18:51:52 +0400"
relations:
  child_of:
    - CA-M-307
  relates_to:
    - CA-M-309
    - CA-M-310
    - CA-M-311
    - CA-M-312
    - CA-M-313
    - CA-M-314
---
# Resolve the Effective CCE Role Profile

**to** resolve one effective CCE Role Profile for one Atom Claim, the Author **must** perform **all** of:

1. resolve the Atom's Content Role before selecting a profile.
2. **if** the Content Role is Plan, Requirement, Method, Evaluation, Delivery, **or** Operations, select the corresponding profile under CA-M-309 through CA-M-314.
3. apply an admitted Type profile **and** content-slot profile after the role profile; treat each narrower profile as a restriction **or** declared subordinate use, **not** as permission **to** change the role's primary contribution.
4. distinguish operators that express the primary Claim contribution from operators inside a condition, Definition of Done, input, result, failure, transition, representation, **or** another governed subordinate slot.
5. **if** the Content Role is Concern **or** Analysis, apply shared CCE **without** a role-specific profile.
6. **if** the Content Role is Implementation, return no registered CCE Role Profile **without** selecting a fallback profile **or** reporting role-profile conformance.
7. **if** the Content Role, Type, content slot, **or** applicable profile is unresolved, report the exact unresolved selection **and** do **not** report role-profile conformance.

the effective profile is derived from governed content classification. it is **not** another required Atom property.
