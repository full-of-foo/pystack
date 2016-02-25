from pystack.exc import EmptyStackError


class Stack(object):
    """TODO - docstring"""

    def __init__(self):
        self._data = []

    def is_empty(self):
        return len(self._data) == 0

    def push(self, item):
        self._data.append(item)
        return item

    def pop(self):
        if self.is_empty():
            raise EmptyStackError()
        item = self._data[len(self._data) - 1]
        del self._data[len(self._data) - 1]
        return item


class IntStack(Stack):
    """TODO - docstring"""

    def push(self, item: int) -> int:
        if not isinstance(item, int):
            raise TypeError()
        return super().push(item)

    def pop(self) -> int:
        return super().pop()
