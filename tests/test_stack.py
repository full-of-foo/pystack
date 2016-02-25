import unittest
from pystack.stack import IntStack
from pystack.exc import EmptyStackError


class TestIntStack(unittest.TestCase):

    def test_init(self):
        self.assertEqual(len(IntStack()._data), 0)

    def test_is_empty(self):
        stack = IntStack()
        self.assertTrue(stack.is_empty())
        stack.push(1)
        self.assertFalse(stack.is_empty())

    def test_cannot_push_other_types(self):
        stack = IntStack()
        for val in [1.0, 1j, "0", [], (), {}]:
            self.assertRaises(TypeError, stack.push, val)

    def test_cannot_pop_when_empty(self):
        self.assertRaises(EmptyStackError, IntStack().pop)

    def test_postioning_with_push(self):
        stack = IntStack()
        self.assertEqual(stack.push(1), 1)
        self.assertEqual(stack._data[-1:][0], 1)

        self.assertEqual(stack.push(2), 2)
        self.assertEqual(stack._data[-1:][0], 2)
        self.assertEqual(stack._data[-2:][0], 1)

    def test_postioning_with_push(self):
        stack = IntStack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack._data[-1:][0], 1)

        self.assertEqual(stack.pop(), 1)
        self.assertEqual(len(IntStack()._data), 0)
