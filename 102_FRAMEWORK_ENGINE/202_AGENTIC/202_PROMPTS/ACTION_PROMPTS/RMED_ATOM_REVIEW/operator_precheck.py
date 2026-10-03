"""Conservative raw-rendering candidates, not a semantic CCE verdict.

The caller supplies the operator inventory from bound authority. Every exposed
unbolded occurrence must receive a reviewer disposition; quotations can be
literal examples. Fenced/inline code is excluded; ambiguous indentation stays
visible for reviewer classification rather than hiding list-continuation prose.
Summary is included. This is a conservative scanner, not a Markdown parser.
"""
from __future__ import annotations
import re
from context_builder import body_section_texts


def word_inventory(authority: str) -> list[str]:
    """Read the complete numbered registry, not arbitrary bold prose words."""
    rows = re.findall(r'^([1-9][0-9]*)\. [^:\n]+: (.+)$', authority, re.M)
    if [int(n) for n, _ in rows] != list(range(1, 10)):
        raise ValueError('operator authority needs its complete nine-category registry')
    values = []
    for _, row in rows:
        tokens = re.findall(r'\*\*([^*]+)\*\*', row)
        if not tokens:
            raise ValueError('empty operator registry category')
        values.extend(t for t in tokens if re.fullmatch(r'[a-z]+(?: [a-z]+)*', t))
    return values


def rendering_candidates(source: str, operators: list[str]) -> list[dict]:
    if not operators or any(not isinstance(v, str) or not v for v in operators):
        raise ValueError('explicit bound operator inventory required')
    pattern = re.compile(r'(?<![\w-])(?:' + '|'.join(
        re.escape(v) for v in sorted(set(operators), key=len, reverse=True)) + r')(?![\w-])', re.I)
    result = []
    for location, section in body_section_texts(source).items():
        visible = list(section)
        # Mask code and headings without shifting offsets.
        fence = None
        offset = 0
        for line in section.splitlines(keepends=True):
            marker = re.match(r'^\s{0,3}(`{3,}|~{3,})', line)
            masked = fence is not None or marker or re.match(r'^#{1,6}\s', line)
            if marker:
                token = marker.group(1)
                if fence is None:
                    fence = token
                elif token[0] == fence[0] and len(token) >= len(fence):
                    fence = None
            if masked:
                visible[offset:offset+len(line)] = ' ' * len(line)
            offset += len(line)
        prose = ''.join(visible)
        for match in re.finditer(r'(`+)(.*?)\1', prose, re.S):
            visible[match.start():match.end()] = ' ' * (match.end()-match.start())
        prose = ''.join(visible)
        bold_ranges = [(m.start(), m.end()) for m in re.finditer(r'\*\*[^\n]+?\*\*', prose)]
        for match in pattern.finditer(prose):
            if any(start <= match.start() and match.end() <= end for start, end in bold_ranges):
                continue
            result.append({'location': location, 'offset': match.start(), 'excerpt': match.group()})
    return result


def validate_operator_coverage(check: dict, source: str, operators: list[str]) -> None:
    """Require explicit classification before a CCE pass can cover this scan."""
    if check.get('status') != 'passed':
        return
    expected = rendering_candidates(source, operators)
    observed = check.get('operator_observations', [])
    if not isinstance(observed, list) or len(observed) != len(expected):
        raise ValueError('CCE pass lacks complete operator precheck coverage')
    for candidate, observation in zip(expected, observed, strict=True):
        if (not isinstance(observation, dict)
                or any(observation.get(k) != v for k,v in candidate.items())
                or observation.get('disposition') not in ('literal_example', 'non_operator_usage')
                or not isinstance(observation.get('reason'), str)
                or not observation['reason'].strip()):
            raise ValueError('CCE pass needs exact justified operator dispositions')
