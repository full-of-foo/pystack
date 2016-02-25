from pystack.stack import IntStack

BAD_INT_STACK_VALUES = [1.0, 1j, "0", [], (), {}, None]


def build_int_stack(values=[1, 2]):
    stack = IntStack()
    stack._data = values
    return stack
