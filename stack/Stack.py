"""Stack Implementation
"""

__author__ = "Xavier Collantes"


class Stack:
    def __init__(self):
        self.list = []

    def Push(self, item):
        """Add one item to the top of stack.

        item: Any value, any type.
        """
        self.list.append(item)

    def Pop(self):
        """Remove the top item.

        Returns: The top item.
        """
        # Alternativly use built-in pop()
        # return self.list.pop()
        top = self.list[len(self.list) - 1]
        self.list.remove(top)
        return top

    def IsEmpty(self):
        if self.list is not []:
            return True
        return False

    def Size(self):
        return len(self.list)

    def Push(self, item):
        self.list.append(item)

    def Peek(self):
        return self.list[len(self.list) - 1]
