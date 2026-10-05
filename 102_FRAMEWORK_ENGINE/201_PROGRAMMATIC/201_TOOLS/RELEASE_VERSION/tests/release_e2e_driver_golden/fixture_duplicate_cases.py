import unittest


class Duplicate(unittest.TestCase):
    def test_same(self):
        self.assertTrue(True)


def load_tests(loader, tests, pattern):
    return unittest.TestSuite([Duplicate("test_same"), Duplicate("test_same")])
