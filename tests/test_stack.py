import unittest
from pystack.stack import IntStack
from pystack.exc import EmptyStackError
from tests.fixtures import BAD_INT_STACK_VALUES, build_int_stack


class TestIntStack(unittest.TestCase):
    """Test cases for the `IntStack` implementation.

    Fixtures:
        stack (IntStack): a populated `IntStack` instance
        emptyStack (IntStack): an empty `IntStack` instance
    """

    def setUp(self):
        self.stack = build_int_stack()
        self.emptyStack = build_int_stack([])

    def test_init(self):
        self.assertEqual(len(IntStack()._data), 0)

    def test_is_empty(self):
        self.assertTrue(self.emptyStack.is_empty())
        self.assertFalse(self.stack.is_empty())

    def test_cannot_push_other_types(self):
        [self.assertRaises(TypeError, self.stack.push, v) for v in BAD_INT_STACK_VALUES]

    def test_cannot_pop_when_empty(self):
        self.assertRaises(EmptyStackError, self.emptyStack.pop)

    def test_postioning_with_push(self):
        self.assertEqual(self.stack.push(3), 3)
        self.assertEqual(self.stack._data[-1:][0], 3)

        self.assertEqual(self.stack.push(4), 4)
        self.assertEqual(self.stack._data[-1:][0], 4)
        self.assertEqual(self.stack._data[-2:][0], 3)

    def test_postioning_with_pop(self):
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack._data[-1:][0], 1)

        self.assertEqual(self.stack.pop(), 1)
        self.assertEqual(len(self.stack._data), 0)
