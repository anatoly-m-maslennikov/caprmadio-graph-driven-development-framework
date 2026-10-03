---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Tool"
  depends_on:
    - "Projection"
    - "Scope Unit"
    - "Atom/Content Role: Requirement/Type: Demand"
priority: medium
version: 2
updated_at: "2026-09-17 19:03:48 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Which owner retains the TOOLS-to-MCP supply obligation?

should R-1096's supplier obligation become a consumer-owned Demand, remain a PROGRAMMATIC composition Requirement, **or** be absorbed by existing authority **without** losing coverage?

## Evidence

R-1096 requires TOOLS **to** supply active immediate Tool units **and** invocation information, then requires MCP projection, exclusion, invalid-input reporting, **and** delegation. MCP R-1106 through R-1112 cover discovery, contract completeness, projection cardinality, disabled/removed units, fail-closed publication, delegation, **and** preserved behavior. their overlap does **not** by itself establish who owns the supplier commitment. R-1111 also admits direct Finder/dry-run execution while reserving particular mutation for authorized MCP delegation; an unconditional independent-execution rewrite would erase that distinction.

## Principle check

DRY favors existing child authority for equivalent requirements. coherence requires an exact current owner **and** target; information preservation protects the supplier obligation **and** permission limits. none of these authorizes inventing a Scope-Unit dependency graph **or** deleting unmatched supply responsibility.

## Disposition

preserve R-1096 pending an exact clause-to-owner map. do **not** label a required projection outcome O merely because execution is mentioned. reuse existing MCP Requirements **where** equivalent; retain any distinct supplier obligation under its admitted relational Type **and** explicit target **before** retiring duplicate clauses. no Tool interface, Scope Unit declaration, **or** MCP behavior changes here.

## Inspected source Revisions

- `CA-R-1096@8`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/04_requirement/CA-R-1096-PROGRAMMATIC-REQUIREMENT--supply-active-tools-to-mcp.md`; SHA-256 `87b6fc4a22835d5d4f8557da8b247dd16fc03e2ef662e3e117854bfad7218fde`.
- `CA-R-1106@8`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP/04_requirement/CA-R-1106-MCP-REQUIREMENT--discover-active-tool-units.md`; SHA-256 `4f5307657cd5bfffdf940ee6394b2a87dc91a54d9816dc246c305d0f05dfc987`.
- `CA-R-1107@9`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP/04_requirement/CA-R-1107-MCP-REQUIREMENT--require-complete-tool-invocation-contracts.md`; SHA-256 `0ffeed71691af63a1b75aa6cf33c7ac4164729e44bc162a34b3819021fb2bef4`.
- `CA-R-1108@8`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP/04_requirement/CA-R-1108-MCP-REQUIREMENT--project-one-mcp-tool-per-active-tool.md`; SHA-256 `6da41d36d1e0b4f2e6ae190da4c64a8c9dbb89d9638836e8ab019dc407055d27`.
- `CA-R-1109@8`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP/04_requirement/CA-R-1109-MCP-REQUIREMENT--reconcile-disabled-and-removed-tools.md`; SHA-256 `e7506b554ba053fe39f822b24c5377c54ff733c50985d3fb0e6924db7c810bd4`.
- `CA-R-1110@8`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP/04_requirement/CA-R-1110-MCP-REQUIREMENT--fail-closed-on-invalid-tool-projections.md`; SHA-256 `e8da0517cab4819370e6781195b650903004665597eaff6f0954fcad76ff1640`.
- `CA-R-1111@10`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP/04_requirement/CA-R-1111-MCP-REQUIREMENT--delegate-mcp-calls-to-canonical-tools.md`; SHA-256 `f3bd57e26ac8d6c2e457fb40a5119a173f03f16ec1dc572931755bbb2c9f33a4`.
- `CA-R-1112@9`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP/04_requirement/CA-R-1112-MCP-REQUIREMENT--preserve-tool-contracts-and-authority.md`; SHA-256 `73f0b4576cce80d6f742d72d79fae1fd6a85d3dc8aff2ae787612fdd76775da0`.
- `CA-M-002@15`: `.caprmedio_caprmedio/05_method/CA-M-002-PRINCIPLE-METHOD--dry-don-t-repeat-yourself.md`; SHA-256 `943be84418b6f865e85d172845892c58187917d22dad56bb6103c5ded7cc6834`.
- `CA-M-005@8`: `.caprmedio_caprmedio/05_method/CA-M-005-PRINCIPLE-METHOD--add-complexity-only-when-necessary.md`; SHA-256 `cd4f3ec4fa61d979997600fbcdb2e96865da694ba1f49fcd391232b72664fd1b`.
- `CA-M-006@8`: `.caprmedio_caprmedio/05_method/CA-M-006-PRINCIPLE-METHOD--keep-the-whole-project-coherent.md`; SHA-256 `f34990465205ac3e655d83b1e3b5dcd66c8c93d2e5287cedbcb9dd38a432bd1f`.
- `CA-R-1490@1`: `.caprmedio_caprmedio/04_requirement/CA-R-1490-PRINCIPLE-REQUIREMENT--preserve-valuable-information.md`; SHA-256 `af65fc105597d5966efaa59d663d452dfa7d0376ad9ebe7bb2b521077ccafb65`.

## Tool-frontier Method consumer

M-193 combines enumeration/validation/atomic publication with later call delegation. these are distinct operational entry contexts, **not** a proved single linear Process. preserve completeness, no code-inferred meaning, stable endpoint identity, invalid-Tool diagnostics, unchanged delegation, **and** retained earlier bytes on refresh failure. R-1110 prohibits presenting that retained frontier as current; M-193 now explicitly reuses this boundary. resolve separate Action responsibilities **and** shared criteria **before** a gap-free O replacement.

## Additional inspected source Revisions

- `CA-M-193@9`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-193-PROGRAMMATIC-METHOD--supply-the-active-tool-frontier-to-mcp.md`; SHA-256 `028bbbdc73e09a749f5f15797d19d3adba5540f731f7eabc6399dcd2338e9c97`.
- `CA-R-1096@9`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/04_requirement/CA-R-1096-PROGRAMMATIC-REQUIREMENT--supply-active-tools-to-mcp.md`; SHA-256 `91b3c104cbeecbe850514baf0a45ae39c55c689f40fef4a25c42b673e374c44d`.
- `CA-R-1110@8`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP/04_requirement/CA-R-1110-MCP-REQUIREMENT--fail-closed-on-invalid-tool-projections.md`; SHA-256 `e8da0517cab4819370e6781195b650903004665597eaff6f0954fcad76ff1640`.
- `CA-R-1453@4`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1453-CORE_META_MODEL-CORE-REQUIREMENT--define-process.md`; SHA-256 `ef8aef1fb7a2193b3647e4de316069b2dfa2f0fd4009178421fd61d886356db4`.
