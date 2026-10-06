---
subjects:
  governs: "Governed Artifact/Metadata/Carrier Reconciliation"
  depends_on:
    - "Governed Artifact/Metadata/Self-description"
    - "Governed Artifact/Metadata/Carrier Agreement"
    - "Artifact/Property"
    - "Carrier/Canonical Address"
cce_version: cce_1
cce_form: method
version: 1
updated_at: "2026-09-16 00:19:34 +0400"
relations: {}
---
# Reconcile Artifact Metadata and Carrier Address Atomically

**to** create, rename, **or** relocate a Governed Artifact, the Author **must** resolve its complete applicable Artifact/Metadata, compose its Carrier/Canonical Address from the same accepted values, parse that address back into address-encoded values, verify equality for **every** repeated Artifact/Property, **and** persist the embedded Metadata **and** Carrier change as one atomic governed change; **if** any value is missing, ambiguous, **or** unequal, the Author **must** stop without selecting one representation as authoritative over the other.
