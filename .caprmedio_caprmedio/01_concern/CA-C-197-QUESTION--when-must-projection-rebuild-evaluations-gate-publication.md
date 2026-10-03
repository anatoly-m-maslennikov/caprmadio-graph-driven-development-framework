---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Projection"
  depends_on:
    - "Action"
    - "Process"
    - "Artifact/Revision"
    - "Operator"
priority: medium
version: 1
updated_at: "2026-09-17 20:53:23 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# When must Projection rebuild Evaluations gate publication?

does the affected-Projection rebuild validate a candidate **before** publication, publish provisionally with rollback, **or** perform a separate post-publication verification?

## Evidence

R-1156 **and** M-255 require currentness **and** idempotence verification **after** publication. M-255 simultaneously says **not** **to** publish on a failed currentness **or** idempotence check. these statements leave the failure boundary unclear: a failed post-publication check cannot prevent an already completed publication. the complete affected dependency set, explicit approved outputs **and** unchanged frontier remain required.

## Principle check

DRY **and** coherence require one exact publication boundary, **not** conflicting implicit flows. Operator control prohibits unapproved effects; information preservation protects recoverable prior bytes **and** complete failure evidence. these Principles do **not** decide whether approval permits provisional publication, which candidate checks suffice, **or** what cross-output rollback the registered job requires.

## Disposition

preserve the current source Claims pending the exact candidate/publication/verification ownership map. do **not** guess rollback authority, publish a failed candidate as current, erase prior output, **or** silently remove the post-publication verification promise. retain complete dependency order, unchanged source frontier, exact approval, reproducibility **and** failure evidence. reuse C-141 for Action/Process extraction **and** C-117 for structural registration. no Projection is rebuilt here.

## Inspected source Revisions

- `CA-M-255@7`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-255-TOOLS-METHOD--rebuild-affected-projections.md`; SHA-256 `270f734328bf5a8983f8bb7cc7134574d82415beb79a0c14a3ffc9cf3c75166d`.
- `CA-R-1156@17`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/04_requirement/CA-R-1156-TOOLS-REQUIREMENT--define-the-projection-rebuild-tool-unit.md`; SHA-256 `5e386f42f33411c258bbf26c91411d48ee9b22485476f8af2ee26e3bb7f74645`.
- `CA-R-1061@10`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/04_requirement/CA-R-1061-TOOLS-REQUIREMENT--rebuild-one-programmatic-projection.md`; SHA-256 `c3643eda4f8de616b3f3a1f6a0cb930a14e0f216651e832c5eba9586f159d302`.
- `CA-R-1062@12`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/04_requirement/CA-R-1062-TOOLS-REQUIREMENT--validate-projection-currentness.md`; SHA-256 `35133ee5ffa0fd28cbebc671fc855ff92ffed5bd7a1d446b2ec2edce928505a2`.
- `CA-C-141@8`: `.caprmedio_caprmedio/01_concern/CA-C-141-QUESTION--which-derivation-rules-are-methods-rather-than-actions.md`; SHA-256 `bc248aba1e59bd04987afb35d6b8ba08c91b96b33a5fbdcd50536252d285f119`.
- `CA-C-117@1`: `.caprmedio_caprmedio/01_concern/CA-C-117-QUESTION--which-declarations-complete-the-authoritative-project-structure.md`; SHA-256 `18c58f8ab5fb4afaffe39137e0e0a54006d68bd45993b09d714e1cefea2a7846`.
- `CA-M-002@15`: `.caprmedio_caprmedio/05_method/CA-M-002-PRINCIPLE-METHOD--dry-don-t-repeat-yourself.md`; SHA-256 `943be84418b6f865e85d172845892c58187917d22dad56bb6103c5ded7cc6834`.
- `CA-M-005@8`: `.caprmedio_caprmedio/05_method/CA-M-005-PRINCIPLE-METHOD--add-complexity-only-when-necessary.md`; SHA-256 `cd4f3ec4fa61d979997600fbcdb2e96865da694ba1f49fcd391232b72664fd1b`.
- `CA-M-006@8`: `.caprmedio_caprmedio/05_method/CA-M-006-PRINCIPLE-METHOD--keep-the-whole-project-coherent.md`; SHA-256 `f34990465205ac3e655d83b1e3b5dcd66c8c93d2e5287cedbcb9dd38a432bd1f`.
- `CA-R-1490@1`: `.caprmedio_caprmedio/04_requirement/CA-R-1490-PRINCIPLE-REQUIREMENT--preserve-valuable-information.md`; SHA-256 `af65fc105597d5966efaa59d663d452dfa7d0376ad9ebe7bb2b521077ccafb65`.
