from pystack.exc import EmptyStackError


class Stack(object):
    """A list-based stack implementation.

    Attributes:
        _data (list): Private list maintaining stack elements
    """

    def __init__(self):
        """Initialises an empty stack."""
        self._data = []

    def is_empty(self):
        """Checks if the stack is empty.

        Returns:
            True if the stack is empty, False otherwise.
        """
        return len(self._data) == 0

    def push(self, item):
        """Pushes an item onto the stack.

        Returns:
            The pushed item.
        """
        self._data.append(item)
        return item

    def pop(self):
        """Removes and returns the item ontop of the stack.

        Returns:
            The last item added to the stack.
        Raises:
            EmptyStackError: given the an already empty stack.
        """
        if self.is_empty():
            raise EmptyStackError()
        item = self._data[len(self._data) - 1]
        del self._data[len(self._data) - 1]
        return item


class IntStack(Stack):
    """A list-based stack implementation for `int`s."""

    def push(self, item: int) -> int:
        """Pushes an `int` item onto the stack.

        Returns:
            The pushed `int`.
        Raises:
            TypeError: given the item is not an `int`.
        """
        if not isinstance(item, int):
            raise TypeError()
        return super().push(item)

    def pop(self) -> int:
        return super().pop()
