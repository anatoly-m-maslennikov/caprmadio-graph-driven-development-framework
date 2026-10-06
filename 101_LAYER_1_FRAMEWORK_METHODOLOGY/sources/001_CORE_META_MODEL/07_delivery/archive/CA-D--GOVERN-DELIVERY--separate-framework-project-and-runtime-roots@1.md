---
cce_version: cce_1
cce_form: delivery
subjects:
  governs:
    continuant:
      - CAPRMEDIO Carrier/Ownership Root
  depends_on:
    continuant:
      - CAPRMEDIO Carrier/Ownership Class
version: 1
updated_at: 2026-08-26 04:35:53 +0400
relations: {}
---
# Separate Framework, Project, and Runtime Roots

the Delivery authority **must** place Framework-owned persistent Carriers under `.caprmedio_framework/`, Project-owned persistent Carriers under `.caprmedio_project/`, and ephemeral Runtime State under `.caprmedio_runtime/`.
