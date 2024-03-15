"""
Given a string s which represents an expression, evaluate this expression and return its value.

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings
as mathematical expressions, such as eval().

https://leetcode.com/problems/basic-calculator-ii/description
"""

from collections import deque
import logging


def string_eval(s: str) -> int:
    """Return value of evaluated string.

    Naive brute-force approach.
    """
    num = 0
    sum_stack = deque()
    operator = "+"

    for ch in s + "+":  # Add plus sign since we're adding all numbers in end
        logging.info(ch)

        if ch.isdigit():
            # Multiply by 10 since the current character is part of a number
            num = (num * 10) + int(ch)

        elif ch in "*+-/":
            logging.info("Found operator: %s", ch)

            if operator == "*":
                sum_stack.append(sum_stack.pop() * num)
            elif operator == "+":
                sum_stack.append(num)
            elif operator == "-":
                sum_stack.append(-num)
            elif operator == "/":
                sum_stack.append(sum_stack.pop() // num)  # Integer division

            # Clear the digit since we're no longer iterating on a number
            num = 0

            # Set the operator to the current character which is an operator
            operator = ch

    return sum(sum_stack)
