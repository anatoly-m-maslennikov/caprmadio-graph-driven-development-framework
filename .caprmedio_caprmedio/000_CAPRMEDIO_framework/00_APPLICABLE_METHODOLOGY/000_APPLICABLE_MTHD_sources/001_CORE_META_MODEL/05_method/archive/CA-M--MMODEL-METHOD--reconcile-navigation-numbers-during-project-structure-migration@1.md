---
subjects:
  governs: "Project Structure"
  depends_on:
    - "Scope Unit"
    - "Scope Unit/Navigational Order Number"
    - "Directory Carrier/Numeric Prefix"
    - "Carrier"
cce_version: cce_1
cce_form: method
version: 1
updated_at: "2026-09-16 21:56:43 +0000"
relations:
  relates_to:
    - CA-R-1484
    - CA-D-297
    - CA-D-299
    - CA-D-300
    - CA-D-445
---
# Reconcile Navigation Numbers During Project Structure Migration

**to** prepare a Project Structure candidate from an accepted Scope Unit inventory, the Author **must** reconcile **every** unit's Navigational Order Number with its existing Carrier evidence: decode the number from a real authority **or** Delivery Directory Carrier **when** the default numbered convention applies; compare all decoded values with each other **and** with the selected candidate value; preserve matching existing numbers without renumbering the Carriers; **and** record the exact Carrier paths and decoding rule used. **when** an admitted native Carrier layout has no encoded number, the Author **must** obtain the candidate value from accepted creation-order evidence **or** an explicit Operator selection **without** requiring a folder rename. **if** the evidence is absent, ambiguous, **or** contradictory, the Author **must** leave the inventory value unresolved, block candidate completion, **and** request a decision instead of using a parent's prefix, lexical sorting, filesystem timestamps, **or** a guessed chronology. the completed Project Structure declaration owns the selected value; a folder name remains a checked Carrier rendering **or** migration observation, **not** a second structural authority.
