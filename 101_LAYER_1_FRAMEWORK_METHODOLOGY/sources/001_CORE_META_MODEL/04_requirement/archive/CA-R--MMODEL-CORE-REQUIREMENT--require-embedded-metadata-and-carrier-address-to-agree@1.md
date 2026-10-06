---
subjects:
  governs: "Governed Artifact/Metadata/Carrier Agreement"
  depends_on:
    - "Governed Artifact/Metadata/Self-description"
    - "Artifact/Property"
    - "Carrier/Canonical Address"
cce_version: cce_1
cce_form: requirement
version: 1
updated_at: "2026-09-16 00:19:34 +0400"
relations: {}
---
# Require Embedded Metadata and Carrier Address to Agree

**for every** Artifact/Property encoded both **in** a Governed Artifact's embedded Metadata **and** **in** its Carrier/Canonical Address, the two resolved values **must** be equal; a missing required value **or** mismatch **must** invalidate the Artifact **and must not** be resolved by silently preferring either representation.
