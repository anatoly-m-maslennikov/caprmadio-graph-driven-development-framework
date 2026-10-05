---
atom_id: CA-D-573
content_role: Delivery
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-05 09:08:00 +0400"
subjects:
  governs: "Tool/RELEASE_VERSION/Approved rollback retention settings"
  depends_on: [Tool, Framework Instance Settings, Manifest, Image, Container, Permission]
relations:
  delivery_for: [CA-R-1879, CA-R-1880, CA-M-333]
---
# Summary

Serialize approved Release rollback retention

## Scope

The closed rollback-retention condition read from the authoritative Framework Instance Settings sealed by D566's `framework_settings_digest`.

## Claim

Release Version **must** read exactly one optional `[release_version.rollback_retention]` table from the locally reopened authoritative Framework Instance Settings whose bytes match the sealed D566 `framework_settings_digest`; the table has exactly `condition` and `required_image_digests`, where `condition` is exactly `retain_prior` or `until_verified_promotion` and `required_image_digests` is an ordered, duplicate-free list of exact lowercase immutable SHA-256 image digests.

## Details

Missing, unknown, malformed, duplicate, digest-mismatched, or stale settings/table members mean retention is unknown and no image removal is permitted. There is no implicit default, caller approval flag, mutable tag, new registry, selector rewrite, or automatic deletion. `retain_prior` retains N. A historical saved prior selector is release evidence only and is not a required rollback reference or a release-of-retention record.

`until_verified_promotion` permits consideration of only exact non-forced removal of the selected prior-image digest after actual successful terminal suite, candidate-image, and observed-promotion verification records each bind the same sealed candidate manifest identity and digest; failed, blocked, pending, incomplete, or differently bound records never satisfy this condition. The reopened matching settings list must not require that old digest, and inspection must prove no running or stopped container or other required old-image reference uses it. Any unavailable, mismatched, uncertain, or incomplete check retains the image with a truthful blocked or pending outcome. This serialization supplies the approved condition consumed by CA-R-1880 and CA-O-169; it does not authorize image execution, permission escalation, settings mutation, source admission, Journal recording, or removal itself.
