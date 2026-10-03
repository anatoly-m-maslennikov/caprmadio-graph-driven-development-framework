---
subjects:
  governs: "Scope Unit"
  depends_on:
    - "Atom/Claim"
    - "Atom/Local Tier"
    - "Methodology Source"
    - "Core Meta-Model"
    - "Extension"
    - "Project Configuration"
version: 13
updated_at: "2026-09-17 14:07:01 +0000"
relations:
  child_of:
    - CAPRMEDIO-REQU-033-REQUIREMENT--preserve-ancestor-core-authority-across-structural-levels
---
# Bound descendant specialization to its structural scope

applicable inherited authority **must** remain effective **in** a descendant Scope Unit **unless** that authority explicitly permits a specialization **and** the specialization stays within the permitted boundary.

- the specialization **must not** change the parent meaning outside its declared descendant scope.
- ancestor Core authority remains protected under CAPRMEDIO-REQU-033; a child declaration **or** an override label does **not** grant permission **to** weaken it.
- Extension **and** Project Configuration additions **must** also preserve Core Meta-Model authority at **every** Local Tier under CA-R-1375. changing the descendant's local rank **or** retaining unchanged Core Carrier bytes does **not** bypass that boundary.
