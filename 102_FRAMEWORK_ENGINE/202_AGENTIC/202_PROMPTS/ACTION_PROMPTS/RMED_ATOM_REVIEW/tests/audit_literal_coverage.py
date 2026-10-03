"""Read-only reviewer QA: flag unexamined literal anchors, not Atom defects.

A declared path is only a search hint. A hit may be a compound expression,
example or general use. The reviewer must interpret it; this helper never adds
Subjects or decides that a declaration is correct. Paraphrases still need QA.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from context_builder import body_section_texts, metadata  # noqa: E402
from review_evidence import literal_occurs  # noqa: E402


def audit(source: str, coherence: dict[str, Any]) -> list[dict[str, str]]:
    subjects = metadata(source).get('subjects', {})
    targets = subjects.get('depends_on', []) + [subjects.get('governs')]
    targets = sorted({target for target in targets if isinstance(target, str) and target})
    check = next(row for row in coherence['checks'] if row['id'] == 'subjects')
    mentions = check['subject_inventory']['mentions']
    unexamined = []
    for section, body in body_section_texts(source).items():
        aliases = (section, section.split(':', 2)[-1].lstrip('# '))
        for target in targets:
            if not literal_occurs(target, body):
                continue
            reviewed = any(mention['location'] in aliases
                and mention['excerpt'] in body
                and literal_occurs(target, mention['excerpt']) for mention in mentions)
            if not reviewed:
                unexamined.append({'section': section, 'literal_anchor': target})
    return unexamined
