"""227. Basic Calculator II

Solved Medium Topics Companies Given a string s which represents an expression,
evaluate this expression and return its value.

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate
results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings
as mathematical expressions, such as eval().
"""

from collections import deque


def basic_calculator(s: str) -> int:
    # Track current number built up per digit.
    # This is done by adding each digit multiplied by 10 which represents the
    # next digit place.
    curr: int = 0
    op: str = "+"
    stack = deque()

    # Append "+" to the string since we need an operator to trigger the last
    # operation.
    for e in s + "+":
        if e.isdigit():
            curr = (curr * 10) + int(e)

        elif e in "+-*/":
            if op == "+":
                stack.append(curr)
            elif op == "-":
                stack.append(-curr)
            elif op == "*":
                stack.append(stack.pop() * curr)
            elif op == "/":
                # Using Python floor division to round to lower integer.
                stack.append(stack.pop() // curr)

            # Reset the operator to the current operator after using the
            # previous operator.
            op = e
            # Reset the current number since we just used the number.
            curr = 0

    return sum(stack)
