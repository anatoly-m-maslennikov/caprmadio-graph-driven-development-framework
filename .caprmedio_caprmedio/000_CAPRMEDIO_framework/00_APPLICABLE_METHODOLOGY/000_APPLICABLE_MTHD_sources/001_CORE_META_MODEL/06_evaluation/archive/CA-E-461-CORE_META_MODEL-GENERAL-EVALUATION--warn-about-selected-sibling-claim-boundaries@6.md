---
subjects:
  governs: "Atom/Claim"
  depends_on:
    - "Atom"
    - "Atom/Content Role: Evaluation"
    - "Scope Unit"
    - "Atom/Claim/Target Scope Unit"
version: 6
updated_at: "2026-09-22 17:59:17 +0000"
relations: {}
---
# Warn About Selected-sibling Claim Boundaries

**when** **`=1`** Atom Claim concerns **only** **`>=2`** selected sibling Scope Units **and** does **not** apply **to** their containing Scope Unit as a whole, the Evaluation **must** report a non-blocking boundary warning for review; that restriction alone **must not** make the Atom invalid **or** trigger automatic rejection, splitting, **or** retargeting **to** their parent.
