"""Fail-closed evidence for an explicitly declared dependent Subject.

This is an admission check, not a general-language Entity resolver.  It can
only corroborate an Entity already named exactly in an independently admitted
authority and directly used in that authority's substantive Markdown evidence.
"""
from __future__ import annotations

import re
from typing import Any

from context_builder import body_section_texts, metadata, prose


_RMEDO_ROLES = frozenset({"Requirement", "Method", "Evaluation", "Delivery", "Operations"})
_PROOF_FIELDS = frozenset({"entity", "authority", "excerpt"})
_UNSUPPORTED_CLAUSE = re.compile(
    r"\b(?:if|then|when|unless|until|otherwise|conditional|conditionally|example|examples|illustration|"
    r"illustrative|hypothetical|proposal|proposed|provisional|tentative|pending)\b",
    re.IGNORECASE,
)
_SECTION_HEADING = re.compile(r"^body:\d+:(#{1,6})\s+(.+?)\s*$")
_STRUCTURED_HEADINGS = frozenset({"summary", "scope", "claim", "details"})
_LEGACY_SUBJECT_LANES = frozenset({"continuant", "occurrent"})


def _text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _present_proof(mention: Any) -> dict[str, str] | None:
    if not isinstance(mention, dict):
        raise ValueError("declared Subject evidence needs a Subject mention")
    if "declared_subject_evidence" not in mention:
        return None
    proof = mention["declared_subject_evidence"]
    if not isinstance(proof, dict) or set(proof) != _PROOF_FIELDS:
        raise ValueError("invalid declared Subject evidence")
    if any(not _text(proof.get(field)) for field in _PROOF_FIELDS):
        raise ValueError("invalid declared Subject evidence")
    return {field: str(proof[field]).strip() for field in _PROOF_FIELDS}


def _validate_mention_binding(mention: dict[str, Any], proof: dict[str, str]) -> None:
    if mention.get("entity") != proof["entity"]:
        raise ValueError("declared Subject evidence needs the mention's exact Entity path")
    if mention.get("resolution_basis") != "meaning":
        raise ValueError("declared Subject evidence is semantic body evidence, not identity admission")
    if not _text(mention.get("rationale")):
        raise ValueError("declared Subject evidence needs the reviewer's semantic rationale")
    definitions = mention.get("definitions")
    if not isinstance(definitions, list) or not any(
        isinstance(row, dict) and row.get("authority") == proof["authority"]
        and row.get("excerpt") == proof["excerpt"] for row in definitions
    ):
        raise ValueError("declared Subject evidence must repeat one exact bound definition citation")


def _bound_raw(proof: dict[str, str], authorities: Any) -> str:
    if not isinstance(authorities, dict) or not _text(authorities.get(proof["authority"])):
        raise ValueError("declared Subject evidence needs a bound admitted authority")
    return str(authorities[proof["authority"]])


def _declared_values(value: Any) -> set[str]:
    """Read ordinary scalar/list Subject declarations without inference."""
    if _text(value):
        return {str(value)}
    if isinstance(value, list):
        return {item for item in value if _text(item)}
    return set()


def _declared_targets(subjects: Any, *, legacy_principle: bool) -> set[str]:
    """Return ordinary targets, plus trusted legacy continuant/occurrent lanes."""
    if not isinstance(subjects, dict):
        return set()
    targets = _declared_values(subjects.get("governs")) | _declared_values(subjects.get("depends_on"))
    if legacy_principle:
        for key in ("governs", "depends_on"):
            nested = subjects.get(key)
            if isinstance(nested, dict):
                for lane in _LEGACY_SUBJECT_LANES:
                    targets.update(_declared_values(nested.get(lane)))
    return targets


def _validate_authority(raw: str, entity: str, authority: str,
                        admitted_legacy_principles: frozenset[str]) -> None:
    props = metadata(raw)
    if not isinstance(props, dict):
        raise ValueError("declared Subject authority metadata is invalid")
    legacy_principle = authority in admitted_legacy_principles
    if not legacy_principle:
        if str(props.get("status", "")).casefold() != "active":
            raise ValueError("declared Subject authority must be Active RMEDO")
        if props.get("content_role") not in _RMEDO_ROLES:
            raise ValueError("declared Subject authority must be Active RMEDO")
    if entity not in _declared_targets(props.get("subjects"), legacy_principle=legacy_principle):
        raise ValueError("declared Subject authority must explicitly declare the exact Entity path")


def _normalized(value: str) -> str:
    return " ".join(value.split())


def _admitted_claim_section(raw: str, excerpt: str) -> str:
    """Return the one accepted Claim section containing this exact quotation.

    A legacy title may supply its leading unsectioned assertion, including when
    later subheadings introduce supporting material. This never admits those
    later sections. Structured carriers supply proof only from ``## Claim``.
    """
    sections = body_section_texts(raw)
    headings: list[tuple[str, int, str]] = []
    for address in sections:
        match = _SECTION_HEADING.fullmatch(address)
        if match is not None:
            headings.append((address, len(match[1]), match[2].casefold()))
    candidates = [address for address, section in sections.items()
                  if excerpt in prose(section)]
    if len(candidates) != 1:
        raise ValueError("declared Subject evidence needs one unambiguous asserted Claim context")
    candidate = candidates[0]
    titles = [address for address, depth, _ in headings if depth == 1]
    if len(titles) == 1 and candidate == titles[0]:
        title = next(name for address, _, name in headings if address == titles[0])
        has_structured_claim = any(depth == 2 and name in ('scope', 'claim')
                                   for _, depth, name in headings)
        # A structured Summary/preamble or explicitly hypothetical title is not
        # Claim authority. Later headings cannot expand the admitted region.
        if (title not in _STRUCTURED_HEADINGS and not has_structured_claim
                and not _UNSUPPORTED_CLAUSE.search(title)):
            return sections[candidate]
    claims = [address for address, depth, name in headings if depth == 2 and name == "claim"]
    structured = all(depth == 1 or (depth == 2 and name in _STRUCTURED_HEADINGS)
                     for _, depth, name in headings)
    if structured and len(titles) == 1 and len(claims) == 1 and candidate == claims[0]:
        return sections[candidate]
    raise ValueError("declared Subject evidence needs an unconditional asserted Claim context")


def _is_complete_claim_clause(section: str, excerpt: str) -> bool:
    """Accept one complete direct Claim paragraph or direct top-level bullet."""
    paragraphs = [paragraph.strip() for paragraph in re.split(r"\n\s*\n", prose(section))
                  if paragraph.strip()]
    containing = [paragraph for paragraph in paragraphs if excerpt in paragraph]
    if len(containing) == 1 and not re.match(r"^\s*[-*+]\s+", containing[0]):
        return _normalized(containing[0]) == _normalized(excerpt)
    lines = section.splitlines()
    direct = [line for line in lines if re.match(r"^[-*+]\s+", line) and excerpt in line]
    if len(direct) != 1 or _normalized(re.sub(r"^[-*+]\s+", "", direct[0])) != _normalized(excerpt):
        return False
    index = lines.index(direct[0])
    for following in lines[index + 1:]:
        if not following.strip() or re.match(r"^[-*+]\s+|^#{1,6}\s", following):
            return True
        # Markdown's indented and lazy continuations both belong to the same
        # bullet. A one-line quotation must not crop either form.
        return False
    return True


def _validate_body_clause(raw: str, proof: dict[str, str]) -> None:
    excerpt = proof["excerpt"]
    section = _admitted_claim_section(raw, excerpt)
    if not _is_complete_claim_clause(section, excerpt):
        raise ValueError("declared Subject evidence needs one complete asserted Claim paragraph or direct Claim bullet")
    if len(excerpt.split()) < 4:
        raise ValueError("declared Subject evidence needs a substantive body quotation")
    if _UNSUPPORTED_CLAUSE.search(excerpt):
        raise ValueError("conditional, hypothetical, or example source clause is not declared Subject authority")


def validate_declared_subject_evidence(mention: Any, authorities: Any, *,
                                       candidate_source: str | None = None,
                                       admitted_legacy_principles: frozenset[str] = frozenset()) -> bool:
    """Validate one optional explicit-dependency proof, or return ``False``.

    ``authorities`` is intentionally the caller's already admitted and bound
    authority map.  A source whose bytes are the evaluation candidate is
    rejected even if it is also present in that map: a candidate cannot admit
    its own Subject mapping.
    """
    proof = _present_proof(mention)
    if proof is None:
        return False
    _validate_mention_binding(mention, proof)
    raw = _bound_raw(proof, authorities)
    if candidate_source is not None and raw == candidate_source:
        raise ValueError("evaluation candidate cannot self-admit declared Subject evidence")
    _validate_authority(raw, proof["entity"], proof["authority"], admitted_legacy_principles)
    _validate_body_clause(raw, proof)
    return True
