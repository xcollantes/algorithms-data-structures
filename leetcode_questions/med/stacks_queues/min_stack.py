"""155. Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element
in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.  void push(int val) pushes the element
val onto the stack.  void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.  int getMin() retrieves the minimum
element in the stack.  You must implement a solution with O(1) time complexity
for each function.
"""

from collections import deque


class MinStack:
    def __init__(self) -> None:
        self.stack = deque()
        self.minVal = deque()

    def push(self, val: int) -> None:
        print(f"PUSH: {val}")

        if len(self.minVal) <= 0:
            self.minVal.append(val)
            print(f"NEW MINVAL: {self.minVal}")

        elif self.minVal[-1] >= val:
            self.minVal.append(val)
            print(f"NEW MINVAL: {self.minVal}")

        self.stack.append(val)

    def pop(self) -> int:
        p = self.stack.pop()

        if p == self.minVal[-1]:
            self.minVal.pop()
            print(f"NEW MINVAL: {self.minVal}")

        print(f"POPPPING {p}")

        return p

    def top(self) -> int:
        top = self.stack[-1]
        print(f"TOP: {top}")
        return top

    def getMin(self) -> int:
        print(f"RETURN MINVAL: {self.minVal}")
        return self.minVal[-1]

    def top(self) -> int:
        top = self.stack[-1]
        return top

    def getMin(self) -> int:
        return self.minVal[-1]

    def getMin(self) -> int:
        return self.minVal[-1]


# This solution technically should not work since you're popping the minstack at
# the same time as the value stack.
#
# class MinStack:
#     def __init__(self):
#         self.stack = []
#         self.min_stack = []

#     def push(self, val: int) -> None:
#         self.stack.append(val)

#         if self.min_stack:
#             val = min(self.min_stack[-1], val)

#         self.min_stack.append(val)

#     def pop(self) -> None:
#         self.stack.pop()
#         self.min_stack.pop()

#     def top(self) -> int:
#         return self.stack[-1]

#     def getMin(self) -> int:
#         return self.min_stack[-1]


def test_design_stack():
    """pytest min_stack.py"""
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    assert minStack.getMin() == -3
    minStack.pop()
    assert minStack.top() == 0
    assert minStack.getMin() == -2
