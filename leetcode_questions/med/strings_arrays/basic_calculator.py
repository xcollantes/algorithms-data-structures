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
    curr: int = 0
    op: str = "+"
    stack = deque()

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
                stack.append(stack.pop() // curr)

            op = e
            curr = 0

    return sum(stack)
