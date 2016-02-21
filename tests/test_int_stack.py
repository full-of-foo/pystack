import unittest
from pystack.int_stack import dummy_function


class TestIntStack(unittest.TestCase):

    def test_that_one_can_test(self):
        self.assertEqual(dummy_function(), 1)
