---
subjects:
  governs: "Framework Instance Settings/Authoritative Carrier/Content"
  depends_on:
    - "Framework Instance Settings"
    - "Operator"
    - "Framework Instance Settings/interaction/reporting mode"
version: 8
updated_at: "2026-09-11 19:51:42 +0400"
relations:
  child_of:
    - CA-D-361
  relates_to:
    - CAPRMEDIO-GOV-REQU-294
    - CAPRMEDIO-META-REQU-675
---
# Serialize Interaction Reporting Mode

an explicit instance reporting default **in** the Framework Instance Settings TOML Carrier **must** use `reporting_mode` **in** the `[interaction]` section, using an allowed value governed by CAPRMEDIO-GOV-REQU-294.
