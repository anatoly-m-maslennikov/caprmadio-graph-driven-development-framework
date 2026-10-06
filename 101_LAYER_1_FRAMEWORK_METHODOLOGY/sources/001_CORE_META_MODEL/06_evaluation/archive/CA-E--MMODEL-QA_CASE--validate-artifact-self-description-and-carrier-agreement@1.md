---
subjects:
  governs: "Governed Artifact/Metadata Validation"
  depends_on:
    - "Governed Artifact/Metadata/Self-description"
    - "Governed Artifact/Metadata/Carrier Agreement"
    - "Artifact/Property"
    - "Carrier/Canonical Address"
cce_version: cce_1
cce_form: evaluation
version: 1
updated_at: "2026-09-16 00:19:34 +0400"
relations: {}
---
# Validate Artifact Self-Description and Carrier Agreement

## Claim checked

a Governed Artifact is independently interpretable from its own authoritative Carrier **and** its complete applicable embedded Metadata agrees with its Carrier/Canonical Address.

## Test case

**for every** registered Governed Artifact Type **and** authoritative Carrier format, create a valid fixture containing complete explicit applicable Metadata, including values otherwise derivable from its filename, placement, **or** registered defaults. parse the Carrier without using its filename **or** placement as input **and** recover every applicable Artifact/Property. separately compare each repeated value with the value parsed from the actual Carrier/Canonical Address. **then** omit each required Property in turn, omit a default-valued Property, change each address-encoded value independently in embedded Metadata **and** in the Carrier address, **and** move the Carrier without reconciling its embedded Metadata.

## Acceptance criteria

the complete fixture resolves one value for every applicable Artifact/Property **and** all repeated values agree. every omitted Property, unresolved value, mismatch, **or** unreconciled move fails with the exact Artifact, Property, embedded value, **and** address-derived value identified.

## Failure disposition

record a Concern naming the affected Governed Artifact, Carrier, Artifact/Property, **and** failed completeness **or** agreement condition.
