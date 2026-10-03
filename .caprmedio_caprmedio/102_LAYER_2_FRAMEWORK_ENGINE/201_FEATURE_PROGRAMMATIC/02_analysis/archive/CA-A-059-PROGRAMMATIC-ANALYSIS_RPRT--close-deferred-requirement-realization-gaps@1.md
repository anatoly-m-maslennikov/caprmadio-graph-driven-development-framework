---
subjects:
  declared:
    continuant:
      - programmatic-policy
    occurrent:
      - validation
version: 1
updated_at: 2026-08-23 18:16:51 +0400
relations:
  derived_from:
    - CA-A-058
---
# Close deferred PROGRAMMATIC Requirement realization gaps

## Scope and classification

CA-P-082 selected the 53 active Requirement IDs deferred by CA-A-058. Every
selected Requirement remains current authority. None was retired or merely
bounded because each still states a valid, distinct acceptance obligation.

The 53 obligations reduce to 38 direct Method boundaries only where the
Method's one independently replaceable procedure genuinely serves every
listed Requirement. The remaining boundaries are singular. No Evaluation
declares a Requirement relation: every Evaluation declares exactly one direct
`evaluation_for` relation to its Method and contains one executable
controlled-fixture acceptance case.

## Current realization matrix

| Requirement boundary | Method | Evaluation | Classification |
| --- | --- | --- | --- |
| CA-R-802 | CA-M-182 | CA-E-300 | one topology |
| CA-R-863 | CA-M-183 | CA-E-301 | one Finder |
| CA-R-864 | CA-M-184 | CA-E-302 | one Finder |
| CA-R-865 | CA-M-185 | CA-E-303 | one Doer |
| CA-R-866 | CA-M-186 | CA-E-304 | one Doer |
| CA-R-867 | CA-M-187 | CA-E-305 | one Doer |
| CA-R-868 | CA-M-188 | CA-E-306 | one lifecycle Doer |
| CA-R-869 | CA-M-189 | CA-E-307 | one lifecycle Doer |
| CA-R-870 | CA-M-190 | CA-E-308 | one lifecycle Doer |
| CA-R-1094 | CA-M-191 | CA-E-309 | one Initiative boundary |
| CA-R-1095 | CA-M-192 | CA-E-310 | one provenance boundary |
| CA-R-1096 | CA-M-193 | CA-E-311 | one MCP handoff |
| CA-R-1097, CA-R-1098 | CA-M-194 | CA-E-312 | one repeated Feature-registration procedure |
| CA-R-1099 | CA-M-195 | CA-E-313 | one Core Feature registration |
| CA-R-1100, CA-R-1101 | CA-M-196 | CA-E-314 | one repeated direct-APPS-unit registration procedure |
| CA-R-1102 | CA-M-197 | CA-E-315 | one Core unit registration |
| CA-R-1103 | CA-M-198 | CA-E-316 | one graph-viewing boundary |
| CA-R-1104 | CA-M-199 | CA-E-317 | one graph-context handoff boundary |
| CA-R-1120 | CA-M-200 | CA-E-318 | one bidirectional reconciliation boundary |
| CA-R-1122 | CA-M-201 | CA-E-319 | one portable-byte policy |
| CA-R-1123 | CA-M-202 | CA-E-320 | one routing-tree validation |
| CA-R-1124 | CA-M-203 | CA-E-321 | one script-to-Tool ownership rule |
| CA-R-1125 | CA-M-204 | CA-E-322 | one data-stage pipeline validation |
| CA-R-1127 | CA-M-205 | CA-E-323 | one Journal recovery boundary |
| CA-R-1128 | CA-M-206 | CA-E-324 | one journal-projection boundary |
| CA-R-1129, CA-R-1135 | CA-M-207 | CA-E-325 | one generic Artifact retrieval boundary |
| CA-R-1130, CA-R-1131 | CA-M-208 | CA-E-326 | one generic Artifact patch boundary |
| CA-R-1132, CA-R-1133, CA-R-1134 | CA-M-209 | CA-E-327 | one generic carrier construction-and-transition procedure |
| CA-R-1138, CA-R-1139, CA-R-1140 | CA-M-210 | CA-E-328 | one migration plan/apply/verify procedure |
| CA-R-1141, CA-R-1142 | CA-M-211 | CA-E-329 | one catalog materialization-and-currentness procedure |
| CA-R-1143 | CA-M-212 | CA-E-330 | one Project Settings patch boundary |
| CA-R-1144, CA-R-1145, CA-R-1146 | CA-M-213 | CA-E-331 | one external provenance capture/ingest/reconcile procedure |
| CA-R-1147 | CA-M-214 | CA-E-332 | one release-outcome record |
| CA-R-1148 | CA-M-215 | CA-E-333 | one accepted-deferred-Plan boundary |
| CA-R-1149 | CA-M-216 | CA-E-334 | one Extension-candidate extraction |
| CA-R-1150 | CA-M-217 | CA-E-335 | one Core Extension packaging boundary |
| CA-R-1151, CA-R-1152 | CA-M-218 | CA-E-336 | one source-resolution-and-installed-state procedure |
| CA-R-1153, CA-R-1154, CA-R-1155, CA-R-1156 | CA-M-219 | CA-E-337 | one repeated Tool-unit registration procedure |

## Coverage result

The matrix covers 53 of 53 scoped Requirements through 38 current Methods and
38 current Evaluations. Each scoped Requirement has exactly one direct
`method_for` owner, and every selected Method has exactly one direct
`evaluation_for` owner. The Methods and Evaluations are accepted realization
authority; they do not claim native implementation, runtime execution, or
passing test evidence.

All new carriers use the owning Scope Unit's canonical Method or Evaluation
location. Methods that realize Core Requirements carry the Core local-tier
filename token; the associated QA_CASE carriers remain Evaluation acceptance
cases. The direct relations are requirement-to-method and method-to-evaluation
only, with no duplicate or inverse ownership.

## Reopening conditions

Reopen CA-P-082 if a scoped Requirement changes, if any listed Method becomes
independently replaceable from its grouped boundary, if an Evaluation's
controlled-fixture case splits into independently executable cases, or if
BSEED relation, type, tier, or lifecycle authority changes.
