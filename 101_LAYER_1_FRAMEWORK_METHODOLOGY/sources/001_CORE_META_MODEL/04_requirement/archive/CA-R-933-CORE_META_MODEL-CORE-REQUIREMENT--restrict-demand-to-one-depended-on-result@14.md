---
subjects:
  governs: "Atom/Content Role: Requirement/Type: Demand/Producer Result"
  depends_on:
    - "Consumer/Goal"
    - "Producer/Result"
version: 14
updated_at: 2026-09-06 01:45:12 +0400
relations:
  child_of:
    - CA-R-932
---
# Restrict Demand to one depended-on result

**every** Demand Atom **must** constrain **`=1`** Producer result on which its Consumer's accepted Goal depends.
