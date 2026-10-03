---
subjects:
  governs: "DEPENDS_ON"
  depends_on:
    - "Subject"
    - "Atom/Subjects"
    - "Entity"
    - "Atom/Claim"
version: 11
updated_at: "2026-09-22 20:07:50 +0000"
relations: {}
---
# Reference Every Prerequisite Subject through DEPENDS_ON

**every** canonical Entity required by an Atom's Claim **without** governing that target **must** be referenced directly through DEPENDS_ON **in** the Atom's Subjects Property.
