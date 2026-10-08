from __future__ import annotations

import stat
import unittest
from unittest.mock import patch

import test_selected_atom_lifecycle as lifecycle_fixture
from lifecycle_intents import (
    LifecycleError,
    carrier_descriptor,
    create_atom_action,
    prepare_create_atom_revision,
    replace_atom_action,
)


class CompleteCarrierPreflightTest(unittest.TestCase):
    """Body admission must finish for the complete set before publication."""

    def setUp(self) -> None:
        self.fixture = lifecycle_fixture.SelectedAtomLifecycleTest(
            "test_authorized_create_uses_a_complete_carrier_and_rejects_occupied_destination"
        )
        self.fixture.setUp()
        self.addCleanup(self.fixture.tearDown)

    def _snapshot(self) -> dict[str, tuple[bytes, int]]:
        return {
            path.relative_to(self.fixture.root).as_posix(): (
                path.read_bytes(), stat.S_IMODE(path.stat().st_mode)
            )
            for path in self.fixture.root.rglob("*")
            if path.is_file()
        }

    def test_invalid_second_successor_is_rejected_before_any_publication(self) -> None:
        first = self.fixture._carrier("CA-R-103", "valid-first", "Valid first")
        second = self.fixture._carrier("CA-R-104", "invalid-second", "Invalid second")
        second["content"] = "# Summary\n\nInvalid second\n"
        parameters = {
            "predecessor": carrier_descriptor(self.fixture.root, "CA-R-100"),
            "successors": [first, second],
            "status_model": self.fixture._model(),
        }
        before = self._snapshot()

        with (
            patch("lifecycle_intents.prepare_create_atom_revision", wraps=prepare_create_atom_revision) as prepare,
            patch("lifecycle_intents.create_atom_revision", side_effect=AssertionError("publication crossed preflight")) as publish,
            patch("lifecycle_intents.archive_atom_revision", side_effect=AssertionError("archive crossed preflight")) as archive,
        ):
            with self.assertRaisesRegex(LifecycleError, "complete-carrier-invalid"):
                replace_atom_action(self.fixture.root, parameters, execute=True, authorized=True)

        self.assertEqual(2, prepare.call_count, "the valid first successor must pass admission")
        self.assertEqual(second["content"], prepare.call_args.args[3])
        publish.assert_not_called()
        archive.assert_not_called()
        self.assertEqual(before, self._snapshot())
        for successor in (first, second):
            self.assertFalse((self.fixture.root / successor["path"]).exists())
        self.assertFalse((self.fixture.requirements / "archive").exists())

    def test_invalid_create_body_is_rejected_before_preview_or_publication(self) -> None:
        carrier = self.fixture._carrier("CA-R-103", "invalid-create", "Invalid create")
        carrier["content"] = "# Summary\n\nInvalid create\n"
        before = self._snapshot()

        for execute in (False, True):
            with self.subTest(execute=execute), \
                    patch("lifecycle_intents.create_atom_revision", side_effect=AssertionError("publication crossed preflight")) as publish:
                with self.assertRaisesRegex(LifecycleError, "complete-carrier-invalid"):
                    create_atom_action(self.fixture.root, {"carrier": carrier}, execute=execute, authorized=True)
                publish.assert_not_called()
                self.assertEqual(before, self._snapshot())

    def test_replace_passes_bodies_to_both_full_set_preflight_boundaries(self) -> None:
        successors = [
            self.fixture._carrier("CA-R-103", "valid-first", "Valid first"),
            self.fixture._carrier("CA-R-104", "valid-second", "Valid second"),
        ]
        before = self._snapshot()
        with patch("lifecycle_intents.prepare_create_atom_revision", wraps=prepare_create_atom_revision) as prepare:
            result = replace_atom_action(
                self.fixture.root,
                {"predecessor": carrier_descriptor(self.fixture.root, "CA-R-100"),
                 "successors": successors, "status_model": self.fixture._model()},
                execute=False,
                authorized=True,
            )

        self.assertEqual("preview", result["outcome"])
        self.assertEqual(4, prepare.call_count)
        for call, successor in zip(prepare.call_args_list, successors * 2, strict=True):
            self.assertEqual((self.fixture.root, successor["path"], successor["frontmatter"], successor["content"]), call.args)
        self.assertEqual(before, self._snapshot())

    def test_create_passes_the_body_to_initial_preflight(self) -> None:
        carrier = self.fixture._carrier("CA-R-103", "valid-create", "Valid create")
        before = self._snapshot()
        with patch("lifecycle_intents.prepare_create_atom_revision", wraps=prepare_create_atom_revision) as prepare:
            result = create_atom_action(self.fixture.root, {"carrier": carrier}, execute=False, authorized=True)

        self.assertEqual("preview", result["outcome"])
        prepare.assert_called_once_with(self.fixture.root, carrier["path"], carrier["frontmatter"], carrier["content"])
        self.assertEqual(before, self._snapshot())


if __name__ == "__main__":
    unittest.main()
