"""Pure D563 checks for hook-free ``ca`` Skill carrier admission."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest.mock import patch


RELEASE_ROOT = Path(__file__).resolve().parents[1]
if str(RELEASE_ROOT) not in sys.path:
    sys.path.insert(0, str(RELEASE_ROOT))

from release_contract import ReleaseContractError  # noqa: E402
from release_handoff import _assert_hook_free_skill_payload  # noqa: E402


class ReleaseSkillHookPayloadPureTests(unittest.TestCase):
    """No temporary carriers: inventory rows are mocked at the read boundary."""

    root = Path("/project")
    skill_root = root / "102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca"

    def _rows(self, *relative: str) -> list[Path]:
        return [self.skill_root / value for value in relative]

    def test_ordinary_skill_carriers_and_hook_prose_are_admitted(self) -> None:
        rows = self._rows("SKILL.md", "agents/openai.yaml", "references/hooks-guide.md")
        with patch("release_handoff._regular_files", return_value=rows):
            observed = _assert_hook_free_skill_payload(self.root, self.skill_root)
        self.assertEqual(observed, rows)

    def test_actual_hook_carriers_and_configurations_are_refused(self) -> None:
        for relative in ("hooks/pre-commit", ".git/hooks/pre-commit", ".pre-commit-config.yaml"):
            with self.subTest(relative=relative), patch(
                "release_handoff._regular_files", return_value=self._rows(relative)
            ):
                with self.assertRaises(ReleaseContractError) as raised:
                    _assert_hook_free_skill_payload(self.root, self.skill_root)
                self.assertEqual(raised.exception.code, "release-skill-hook-forbidden")


if __name__ == "__main__":
    unittest.main()
