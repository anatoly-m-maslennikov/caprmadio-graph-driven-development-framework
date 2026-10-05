import unittest


class Success(unittest.TestCase):
    def test_success(self):
        self.assertEqual(2 + 2, 4)
