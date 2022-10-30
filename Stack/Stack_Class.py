class Empty(Exception):
    """Error attempting to access element from an empty Stack."""
    pass


class Stack:
    """Defining methods for Stacks."""

    def __init__(self):
        """Constructor to declare instance variable."""
        self._data = []  # Protected empty stack

    def __len__(self):  # Example of Method Overloading
        """Returns length of Stack."""
        return len(self._data)

    def push(self, foo):
        """Adds new items to Stack."""
        return self._data.append(foo)

    def pop(self):
        """Removes last element of the Stack(LIFO)."""
        if len(self._data) == 0:
            raise Empty('No values found.')
        else:
            return self._data.pop()

    def is_empty(self):
        """Check whether stack is empty or not."""
        return len(self._data) == 0

    def top(self):
        """Returns top(latest) element in Stack."""
        if len(self._data) == 0:
            raise Empty('No values found.')
        else:
            return self._data[-1]