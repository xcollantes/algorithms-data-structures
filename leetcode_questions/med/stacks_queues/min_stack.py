"""155. Min Stack

Medium

Design a stack that supports push, pop, top, and retrieving the minimum element
in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

Constraints:

-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.
"""


class MinStack:
    def __init__(self) -> None:
        self.mins = []
        self.values = []

    def push(self, val: int) -> None:
        if self.mins:
            self.mins.append(min(self.getMin(), val))
        self.mins.append(val)

        print(f"push: {val} m: {self.mins} v: {self.values}")

    def pop(self) -> int:
        # We keep a parallel mins stack which has a value for every entry in the
        # value stack.
        # This way, we can pop no matter what and still have the min. Think of
        # it like snapshots: for every value element, we have a min element
        # corresponding to the value element.
        #
        # Alternatively, we can keep a min stack which checks if the next value
        # is the same value being popped.
        p = self.values.pop()
        m = self.mins.pop()

        print(f"pop: v: {p} m: {m}")
        return p

    def top(self) -> int:
        return self.values[-1]

    def getMin(self) -> int:
        return self.mins[-1]


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
