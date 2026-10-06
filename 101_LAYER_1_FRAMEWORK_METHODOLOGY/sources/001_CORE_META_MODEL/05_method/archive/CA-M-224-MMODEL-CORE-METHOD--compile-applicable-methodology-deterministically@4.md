---
atom_id: CA-M-224
cce_version: cce_1
cce_form: method
subjects:
  governs:
    occurrent:
      - Applicable Methodology Compilation
  depends_on:
    continuant:
      - Applicable Methodology/Sources
      - Applicable Methodology
      - Applicable Methodology/Compilation Output
      - Local Configuration
version: 4
updated_at: 2026-08-27 21:13:36 +0400
relations: {}
---
# Compile Applicable Methodology Deterministically

to compile Applicable Methodology, the Compiler **must** perform all of:

1. read only the Source Layer Carriers under `.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/` that have an exact governed source reference.
2. confirm the ordered structural Source Layers as CORE_META_MODEL, INSTALLED_EXTENSIONS, and LOCAL_CONFIGURATION.
3. select only current active Atom revisions with Content Role in (REQUIREMENT, METHOD, EVALUATION, DELIVERY, OPS), and exclude every CONCERN, ANALYSIS, PLAN, IMPLEMENTATION, Draft, and archived revision.
4. include eligible Source Atom revisions from CORE_META_MODEL and LOCAL_CONFIGURATION only.
5. record INSTALLED_EXTENSIONS as an empty non-contributing structural Source Layer and include no Installed Extension Source Atom revision.
6. detect every duplicate selected Atom identity, unresolved replacement, incompatible retained Candidate, unresolved priority, and output-path collision.
7. calculate the source-frontier digest from the canonical UTF-8 JSON serialization of the ordered Source Layer, Atom ID, Atom revision, canonical relative Carrier path, and Carrier SHA-256 records for every eligible Candidate.
8. have the `COMPILE_APPLICABLE_METHODOLOGY` Tool dry-run report the complete deterministic conflict set and propose one deterministic Candidate resolution for each conflict.
9. apply a proposed resolution only **if** LOCAL_CONFIGURATION durably records one unambiguous Operator approval bound to that exact conflict and the exact source-frontier digest.
10. stop without producing or replacing Output **if** any approval is stale, partial, missing, ambiguous, or does not match the exact conflict and source-frontier digest.
11. never treat structural Source Layer order as permission to resolve a conflict and never modify a Source Atom.
12. stop without generating an Output **if** selection or resolution does not produce exactly one selected current revision for every retained Atom identity.
13. order selected Atom revisions by canonical role directory, Atom ID, and canonical relative Carrier path.
14. require CA-P-110 to implement and use the deterministic `COMPILE_APPLICABLE_METHODOLOGY` Tool with dry-run validation and staged atomic replacement of only generated RMEDO output directories.
15. map each selected Source Atom Carrier to `.caprmedio_framework/00_APPLICABLE_METHODOLOGY/<canonical role directory>/<source basename>`.
16. copy each Source Atom Carrier claim content and all source frontmatter unchanged, add only the projection mapping required by CA-R-1229, and treat that mapping as an explicit non-authoritative Projection declaration.
17. store no CAP or IMPLEMENTATION role directory, Draft, archive, monolithic JSON methodology, or precompiled Subject Index Carrier in the generated output tree.
18. preserve every Source Carrier unchanged, use no LLM inference, and reproduce the same generated Atom Carrier tree from the same resolved source frontier.
19. allow deletion of the generated RMEDO output directories and regenerate the complete tree from the source Layers without loss of authority.
