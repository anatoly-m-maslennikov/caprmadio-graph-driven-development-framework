from __future__ import annotations

import os
import sys
import tempfile
import unittest
from pathlib import Path


TOOLS_ROOT = Path(__file__).resolve().parents[2]
if str(TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(TOOLS_ROOT))

from project_runtime import (  # noqa: E402
    RUNTIME_DIRECTORY,
    TEMPORARY_DIRECTORY,
    TemporaryBoundaryError,
    atomic_tempfile,
)


TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp" / "tests" / Path(__file__).stem
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)


class ProjectRuntimeTests(unittest.TestCase):
    def test_atomic_intermediate_is_owned_by_project_temporary_state(self) -> None:
        with tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True) as directory:
            repository = Path(directory)
            (repository / ".git").mkdir()
            destination = repository / "state" / "current.json"

            descriptor, temporary_name = atomic_tempfile(destination, "unit")
            temporary = Path(temporary_name)
            try:
                self.assertTrue(temporary.is_relative_to(repository / TEMPORARY_DIRECTORY / "unit" / "atomic"))
                self.assertFalse(temporary.is_relative_to(destination.parent))
                with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
                    handle.write("{}\n")
                os.replace(temporary, destination)
            finally:
                temporary.unlink(missing_ok=True)

            self.assertEqual(destination.read_text(encoding="utf-8"), "{}\n")
            self.assertEqual(RUNTIME_DIRECTORY.as_posix(), ".caprmedio_runtime")

    def test_owner_must_be_one_safe_path_component(self) -> None:
        with tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True) as directory:
            repository = Path(directory)
            (repository / ".git").mkdir()
            with self.assertRaises(TemporaryBoundaryError):
                atomic_tempfile(repository / "state.json", "../escape")


if __name__ == "__main__":
    unittest.main()
