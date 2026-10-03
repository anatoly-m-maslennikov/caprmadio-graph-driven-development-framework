"""Check report addresses and duplicate evidence, not semantic correctness."""
from __future__ import annotations

from typing import Any

from context_builder import body_section_texts


def _observation_sections(source: str) -> dict[str, str]:
    sections = body_section_texts(source)
    lines = source.splitlines(keepends=True)
    if lines and lines[0].strip() == '---':
        for end, line in enumerate(lines[1:], 1):
            if line.strip() == '---':
                sections['frontmatter'] = ''.join(lines[1:end])
                break
    return sections


def _validate_observations(check: dict[str, Any], sections: dict[str, str],
                           authorities: dict[str, str] | None) -> None:
    if 'positive_observations' not in check:
        if check.get('status') == 'passed':
            raise ValueError('passed check requires positive observations, not generic evidence alone')
        return
    observations = check['positive_observations']
    if not isinstance(observations, list):
        raise ValueError('invalid positive observations collection')
    if not observations:
        if check.get('status') == 'passed':
            raise ValueError('passed check requires positive observations, not generic evidence alone')
        return
    for observation in observations:
        if not isinstance(observation, dict):
            raise ValueError('invalid positive observation')
        location, excerpt = observation.get('location'), observation.get('excerpt')
        if not isinstance(location, str) or location not in sections:
            raise ValueError('positive observation names an unknown source section')
        if not isinstance(excerpt, str) or not excerpt.strip() or excerpt not in sections[location]:
            raise ValueError('positive observation excerpt is absent from its source section')
        authority, rule_excerpt = observation.get('authority'), observation.get('rule_excerpt')
        if (not isinstance(authority, str) or authority not in check.get('authority', [])
                or authorities is None or authority not in authorities):
            raise ValueError('positive observation needs a bound check authority')
        if (not isinstance(rule_excerpt, str) or not rule_excerpt.strip()
                or rule_excerpt not in authorities[authority]):
            raise ValueError('positive observation rule excerpt is absent from its authority')


def validate_report_quality(part: dict[str, Any], source: str, *,
                            authorities: dict[str, str] | None = None) -> None:
    """Reject contradictory explicit body addresses and identical findings.

    A missing-value observation is not expected to be a verbatim source quote.
    This guard validates body addresses for every finding, and exact excerpts
    only for violations. Other address schemes keep their existing checks.
    """
    sections = body_section_texts(source)
    observation_sections = (_observation_sections(source)
                            if part.get('evaluator') == 'properties' else sections)
    for check in part['checks']:
        if part.get('contract_version') in (5, 6):
            _validate_observations(check, observation_sections, authorities)
        seen = []
        for finding in check['findings']:
            if finding in seen:
                raise ValueError('duplicate finding record; group repeated occurrences or distinguish their evidence')
            seen.append(finding)
            if not finding['location'].startswith('body:'):
                continue
            location = finding['location']
            if location not in sections:
                raise ValueError('finding names an unknown body section address')
            if finding['kind'] == 'violation' and finding['excerpt'] not in sections[location]:
                raise ValueError('finding excerpt is absent from its claimed body section')
    if part.get('contract_version') == 5:
        for gap in part.get('coverage_gaps', []):
            if not isinstance(gap, dict):
                raise ValueError('invalid coverage gap')
            if gap.get('check_id') != 'subjects' or gap.get('kind') != 'unresolved_interpretation':
                continue
            subjects = next((check for check in part['checks'] if check['id'] == 'subjects'), None)
            if subjects is None:
                raise ValueError('Subject interpretation gap requires a Subjects check')
            mentions = subjects.get('subject_inventory', {}).get('mentions', [])
            if not any(mention.get('resolution') == 'unresolved' for mention in mentions):
                raise ValueError('Subject interpretation gap requires an unresolved mention; unread evidence is reviewer_incomplete')
