"""Actual flock exclusion and safe persistent carriers in retained Unit fixtures."""
from __future__ import annotations

import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

RELEASE_ROOT = Path(__file__).resolve().parents[1]
if str(RELEASE_ROOT) not in sys.path:
    sys.path.insert(0, str(RELEASE_ROOT))

from selector_publication_lock import (  # noqa: E402
    LOCK_RELATIVE, SelectorPublicationLockError, selector_publication_lock,
)


class SelectorPublicationLockTests(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp(prefix="selector-publication-lock-")).resolve()

    def test_persistent_same_inode_exclusion_and_release_after_body_error(self):
        with selector_publication_lock(self.root, timeout_seconds=0):
            inode = (self.root / LOCK_RELATIVE).stat().st_ino
            with self.assertRaises(SelectorPublicationLockError) as busy:
                with selector_publication_lock(self.root, timeout_seconds=0):
                    self.fail("second publication acquired ownership")
            self.assertEqual("selector-publication-lock-busy", busy.exception.code)
        with self.assertRaisesRegex(ValueError, "fixture body failed"):
            with selector_publication_lock(self.root, timeout_seconds=0):
                raise ValueError("fixture body failed")
        with selector_publication_lock(self.root, timeout_seconds=0):
            self.assertEqual(inode, (self.root / LOCK_RELATIVE).stat().st_ino)

    def test_real_separate_process_exclusion_and_os_release_without_unlink(self):
        program = (
            "import os, sys; sys.path.insert(0, sys.argv[1]); "
            "from selector_publication_lock import selector_publication_lock; "
            "lock = selector_publication_lock(sys.argv[2], timeout_seconds=0); "
            "lock.__enter__(); print('owned', flush=True); sys.stdin.readline(); os._exit(0)"
        )
        child = subprocess.Popen([sys.executable, "-c", program, str(RELEASE_ROOT), str(self.root)],
                                 stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                 text=True)
        try:
            self.assertEqual("owned\n", child.stdout.readline())
            with self.assertRaises(SelectorPublicationLockError):
                with selector_publication_lock(self.root, timeout_seconds=0):
                    self.fail("live child ownership was bypassed")
            # Exit without calling the context manager's cleanup: the OS owns
            # flock lifetime, not a PID stored in or deletion of the carrier.
            child.stdin.write("exit\n")
            child.stdin.flush()
            child.communicate(timeout=5)
            self.assertEqual(0, child.returncode)
            with selector_publication_lock(self.root, timeout_seconds=0):
                self.assertTrue((self.root / LOCK_RELATIVE).is_file())
        finally:
            if child.poll() is None:
                child.terminate()
                child.communicate(timeout=5)

    def _assert_replacement_does_not_split_process_ownership(self, replace_framework):
        holder_program = (
            "import os, sys; sys.path.insert(0, sys.argv[1]); "
            "from selector_publication_lock import selector_publication_lock; "
            "lock = selector_publication_lock(sys.argv[2], timeout_seconds=0); "
            "lock.__enter__(); print('owned', flush=True); sys.stdin.readline(); os._exit(0)"
        )
        contender_program = """
import sys
sys.path.insert(0, sys.argv[1])
from selector_publication_lock import SelectorPublicationLockError, selector_publication_lock
try:
    with selector_publication_lock(sys.argv[2], timeout_seconds=0):
        print('acquired')
except SelectorPublicationLockError as error:
    print(error.code)
"""
        holder = subprocess.Popen(
            [sys.executable, "-c", holder_program, str(RELEASE_ROOT), str(self.root)],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
        )
        try:
            self.assertEqual("owned\n", holder.stdout.readline())
            carrier = self.root / LOCK_RELATIVE
            if replace_framework:
                framework = carrier.parent
                original_inode = framework.stat().st_ino
                framework.rename(framework.with_name("framework-held"))
                framework.mkdir()
                self.assertNotEqual(original_inode, framework.stat().st_ino)
            else:
                original_inode = carrier.stat().st_ino
                replacement = carrier.with_name("replacement.lock")
                replacement.touch()
                os.replace(replacement, carrier)
                self.assertNotEqual(original_inode, carrier.stat().st_ino)
            command = [sys.executable, "-c", contender_program, str(RELEASE_ROOT), str(self.root)]
            contender = subprocess.run(command, capture_output=True, text=True, timeout=5)
            self.assertEqual(0, contender.returncode, contender.stderr)
            self.assertEqual("selector-publication-lock-busy\n", contender.stdout)
            # Both directory and file locks are released by process exit even
            # when the open carrier no longer has its original pathname.
            holder.stdin.write("exit\n")
            holder.stdin.flush()
            holder.communicate(timeout=5)
            self.assertEqual(0, holder.returncode)
            contender = subprocess.run(command, capture_output=True, text=True, timeout=5)
            self.assertEqual(0, contender.returncode, contender.stderr)
            self.assertEqual("acquired\n", contender.stdout)
        finally:
            if holder.poll() is None:
                holder.terminate()
                holder.communicate(timeout=5)

    def test_real_process_lockfile_replacement_cannot_split_ownership(self):
        self._assert_replacement_does_not_split_process_ownership(replace_framework=False)

    def test_real_process_framework_directory_replacement_cannot_split_ownership(self):
        self._assert_replacement_does_not_split_process_ownership(replace_framework=True)

    def test_changed_carrier_or_framework_refuses_successful_context_return(self):
        for replace_framework in (False, True):
            with self.subTest(replace_framework=replace_framework):
                with self.assertRaises(SelectorPublicationLockError) as changed:
                    with selector_publication_lock(self.root, timeout_seconds=0):
                        carrier = self.root / LOCK_RELATIVE
                        if replace_framework:
                            carrier.parent.rename(carrier.parent.with_name("framework-old"))
                            carrier.parent.mkdir()
                        else:
                            replacement = carrier.with_name("replacement.lock")
                            replacement.touch()
                            os.replace(replacement, carrier)
                self.assertEqual("selector-publication-lock-unsafe", changed.exception.code)
                with selector_publication_lock(self.root, timeout_seconds=0):
                    pass

    def test_unsupported_directory_flock_has_no_file_only_fallback(self):
        with mock.patch("selector_publication_lock.fcntl.flock", side_effect=OSError("unsupported")) as flock:
            with self.assertRaises(SelectorPublicationLockError) as unsupported:
                with selector_publication_lock(self.root, timeout_seconds=0):
                    self.fail("unsupported directory flock admitted ownership")
        self.assertEqual("selector-publication-lock-unavailable", unsupported.exception.code)
        self.assertEqual(1, flock.call_count)
        with selector_publication_lock(self.root, timeout_seconds=0):
            pass

    def test_rejects_symlinked_runtime_ancestor_or_lock_and_special_file(self):
        runtime = self.root / ".caprmedio_runtime"
        elsewhere = self.root / "unrelated"
        elsewhere.mkdir()
        runtime.symlink_to(elsewhere, target_is_directory=True)
        with self.assertRaises(SelectorPublicationLockError):
            with selector_publication_lock(self.root, timeout_seconds=0):
                pass
        self.assertEqual([], list(elsewhere.iterdir()))
        runtime.unlink()
        (self.root / LOCK_RELATIVE.parent).mkdir(parents=True)
        target = self.root / "other.lock"
        target.write_bytes(b"unrelated")
        carrier = self.root / LOCK_RELATIVE
        carrier.symlink_to(target)
        with self.assertRaises(SelectorPublicationLockError):
            with selector_publication_lock(self.root, timeout_seconds=0):
                pass
        self.assertEqual(b"unrelated", target.read_bytes())
        carrier.unlink()
        os.mkfifo(carrier)
        with self.assertRaises(SelectorPublicationLockError):
            with selector_publication_lock(self.root, timeout_seconds=0):
                pass

    def test_root_symlink_and_invalid_timeouts_refuse(self):
        alias = self.root / "alias"
        alias.symlink_to(self.root, target_is_directory=True)
        with self.assertRaises(SelectorPublicationLockError):
            with selector_publication_lock(alias, timeout_seconds=0):
                pass
        for timeout in (True, -1, 31, float("inf"), float("nan")):
            with self.subTest(timeout=timeout), self.assertRaises(SelectorPublicationLockError):
                with selector_publication_lock(self.root, timeout_seconds=timeout):
                    pass


if __name__ == "__main__":
    unittest.main()
