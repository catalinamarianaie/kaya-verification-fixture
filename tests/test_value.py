import unittest

from value import value


class ValueTest(unittest.TestCase):
    def test_authorized_patch(self):
        self.assertEqual(value(), 2)
