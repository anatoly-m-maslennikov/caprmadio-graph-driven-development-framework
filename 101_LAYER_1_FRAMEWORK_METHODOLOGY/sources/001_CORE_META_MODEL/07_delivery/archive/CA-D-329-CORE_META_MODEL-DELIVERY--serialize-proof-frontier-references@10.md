---
subjects:
  governs: "Proof Carrier/Dependency Frontier"
  depends_on: []
version: 10
updated_at: "2026-09-10 20:54:39 +0400"
relations: {}
---
# Serialize Proof Frontier References

**every** proof Carrier **must** serialize its machine-readable dependency frontier as a YAML `proof_frontier_refs` list of exact versioned **or** digest-bound references. prose **must** be reserved for additional invalidation conditions that cannot be encoded **without** loss.
