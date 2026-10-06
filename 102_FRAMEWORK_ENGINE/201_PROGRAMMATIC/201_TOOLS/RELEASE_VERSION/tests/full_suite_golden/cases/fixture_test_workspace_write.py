from pathlib import Path
import unittest


class WorkspaceWriteTests(unittest.TestCase):
    def test_workspace_is_read_only(self):
        workspace = Path.cwd()
        with self.assertRaises(OSError):
            (workspace / "must-not-be-written.txt").write_text("forbidden", encoding="utf-8")
