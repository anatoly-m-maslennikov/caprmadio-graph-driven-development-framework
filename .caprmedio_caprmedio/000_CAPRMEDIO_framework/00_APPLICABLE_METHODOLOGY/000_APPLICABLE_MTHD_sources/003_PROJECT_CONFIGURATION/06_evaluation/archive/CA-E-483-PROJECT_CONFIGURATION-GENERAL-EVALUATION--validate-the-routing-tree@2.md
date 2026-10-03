---
subjects:
  governs: "CAPRMEDIO Routing Tree"
  depends_on: []
version: 2
updated_at: "2026-09-17 15:07:45 +0000"
relations: {"evaluation_for":["CAPRMEDIO-GOV-REQU-333"]}
---
# Validate the routing tree

the Evaluation of the CAPRMEDIO Routing Tree registered under CAPRMEDIO-GOV-REQU-333 **must** reject a routing tree **when** **any** of the following is present:

- an invalid schema;
- an unknown target;
- ambiguous precedence;
- a duplicate route identity;
- an authority effect that is **not** explicitly declared.
