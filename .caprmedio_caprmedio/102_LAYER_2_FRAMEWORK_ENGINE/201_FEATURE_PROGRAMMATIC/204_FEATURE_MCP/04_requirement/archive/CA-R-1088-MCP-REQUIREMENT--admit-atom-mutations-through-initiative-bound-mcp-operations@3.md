---
subjects:
  - framework-engine-mcp
cce_version: cce_1
cce_form: obligation
version: 3
updated_at: 2026-08-23 15:46:20 +0400
---
# Admit Atom mutations through Initiative-bound MCP operations

Every mutation of a CAPRMEDIO Markdown Atom MUST enter through an authorized project-local MCP operation that delegates to the canonical Atom Tool. Search and read operations remain mutation-free. Create, update, move, archive, promote, upgrade, replacement, and every atomic or bulk composition of those operations MUST seal exactly one Initiative and stable action identity before mutation, validate the current project frontier, and carry that identity through durable provenance processing. The Initiative MUST retain a human-origin instruction reference: either its admitted Plan or Task Atom, or its ephemeral session task and human input. After the mutation succeeds and before acknowledging success, MCP MUST invoke `COMMIT_TRIGGER` and receive durable intake acknowledgment for the sealed action; intake failure leaves the action explicitly blocked or recoverable and MUST NOT be reported as successful admission.

An atomic operation selects exactly one Atom target. A bulk operation selects a finite target set of two or more Atom targets, freezes each target's identity, expected revision or digest, and canonical address before any write, and is all-or-nothing: if any target no longer satisfies its preconditions, it performs no target mutation and returns the exact per-target conflict result. A successful bulk operation neither widens nor silently replaces its sealed target set.

Multiple MCP service instances and sessions MAY operate concurrently. Every mutation of an existing Atom MUST carry its expected Atom Revision or carrier digest; a mismatch MUST reject that target rather than overwrite concurrent work. Promotion is an ordinary MCP mutation that validates its pre-promotion input and seals a new action; it MUST NOT require the future Git or Journal reconciliation of that same new action. A direct or otherwise unowned Atom write outside this gateway is unadmitted and cannot be represented as a normal governed MCP mutation.
