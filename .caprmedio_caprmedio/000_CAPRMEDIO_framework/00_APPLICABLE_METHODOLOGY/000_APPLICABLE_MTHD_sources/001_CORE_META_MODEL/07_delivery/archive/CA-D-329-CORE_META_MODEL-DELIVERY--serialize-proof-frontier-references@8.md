---
atom_id: CA-D-329
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Proof Carrier/Dependency Frontier"
  depends_on: []
version: 8
updated_at: "2026-09-10 20:54:39 +0400"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Serialize Proof Frontier References

**every** proof Carrier **must** serialize its machine-readable dependency frontier as a YAML `proof_frontier_refs` list of exact versioned **or** digest-bound references. prose **must** be reserved for additional invalidation conditions that cannot be encoded **without** loss.
