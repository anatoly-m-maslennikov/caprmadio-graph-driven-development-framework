---
subjects:
  governs: "feature-boundary"
version: 15
updated_at: "2026-09-15 21:31:49 +0000"
---
# Install all FRAMEWORK_ENGINE Tools

INSTALL_TOOLS **must** provide installation of the selected FRAMEWORK_ENGINE Tool release under the applicable Operator selections **and** governing delivery bindings.

**all** of the following **must** hold:

- resolve runnable Tools **and** shared implementation dependencies from the selected canonical source; publish a digest-verified content-addressed release **and** a machine-readable current-release selection.
- resolve concrete source, release, launcher, **and** integration bindings from their authoritative declarations; do **not** redefine Scope Unit ownership **or** bindings **in** this Requirement.
- install registered stable launchers. install host Hook integrations **only** **when** selected by the Operator; absence of an unselected host integration **must not** block Tool installation.
- a selected Codex integration uses a shared dispatcher that resolves the current repository at invocation time, requires its local activation marker, **and** addresses its selected stable runtime-owned launcher. preserve unrelated host Hook groups **and** reject an unselected repository lookalike.
- installation remains mutation-free **unless** apply is explicitly authorized. preserve existing user-level Codex **and** Git Hook behavior, reject an unrelated hook-path override **before** mutation, **and** migrate **only** recognized prior CAPRMEDIO Hook Carriers.
- selected integration failure preserves **or** restores the previous valid release **and** managed integration state; report unavailable required host capabilities explicitly.
- persistent operational state remains **in** the Runtime State root; temporary execution state remains **in** the Temporary State root. no executable Framework dependency is installed into the Codex user directory.
- installed Tools remain runnable **without** importing their canonical source checkout.
- status distinguishes installed Hook Carriers from host activation **and** reports Operator-controlled trust **or** review still required by the host.
