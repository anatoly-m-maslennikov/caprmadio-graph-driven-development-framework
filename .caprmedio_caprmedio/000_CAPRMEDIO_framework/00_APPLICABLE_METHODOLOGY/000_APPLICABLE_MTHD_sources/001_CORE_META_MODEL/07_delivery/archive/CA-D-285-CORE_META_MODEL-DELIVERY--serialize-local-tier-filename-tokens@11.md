---
subjects:
  governs: "Atom/Local Tier/Filename Token"
  depends_on:
    - "Atom"
    - "Atom/Local Tier"
    - "Atom/Local Tier: Standard"
    - "Change Content Roles"
    - "Implementation"
    - "Artifact/Carrier"
version: 11
updated_at: "2026-09-22 14:41:44 +0000"
relations: {"delivery_for": ["CA-R-1566"]}
---
# Serialize Local Tier Filename Tokens

subject **to** the role-tier restrictions under CA-R-1566, an ordinary Atom filename **must** serialize Principle as `PRINCIPLE`, Core as `CORE`, General as `GENERAL`, **and** the default Standard Local Tier by omitting the Local Tier segment at the registered descriptor position **after** its identity **and** current Scope owner. `PRINCIPLE` is admitted **only** for a Project-scoped Atom; `STD`, `STANDARD`, `DETAIL`, **and** combined tier segments **must not** be serialized. the external Project Goal's registered tierless grammar **must** be recognized **before** applying the ordinary omitted-Standard default; a tier token **must not** replace **or** alter the registered identity, owner, target, **or** sequence grammar of a Goal **or** Plan.
