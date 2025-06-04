"""22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of
well-formed parentheses.
"""


def generateParenthesis(n: int) -> list[str]:
    result = []

    # Define the initial counts of left and right parentheses used.
    # Start with a queue (stack in this case, as we use pop from the end) for
    # breadth-first exploration.
    left = 0
    right = 0

    # Start with 0 left '(' and 0 right ')' parentheses used.
    q = [
        (left, right, "")
    ]  # Each element in the queue contains (count of left, count of right, current string).

    # Use a while loop to explore all valid combinations.
    # Using BFS, the latest element will be popped off and examined.
    while q:
        print(f"LEFT: {left}; RIGHT: {right}; s: {s}")

        # Popping off the stack is like reverting up the tree.
        left, right, s = q.pop()

        # If the current string `s` has reached the required length (2 * n), it
        # is a valid result.
        if len(s) == 2 * n:
            print(f"    append result s: {s}")
            result.append(s)

        # If there are remaining left parentheses to add, append one and push
        # the state to the stack.
        #
        # n is technically HALF of the complete string but MAX of the left
        # parens.
        if left < n:
            left_add = (left + 1, right, s + "(")
            print(f"    new left: {left_add}")
            q.append(left_add)

        # If there are more left parentheses in the string than right ones, a ')' can be added
        # This ensures that the parentheses sequence remains valid
        if right < left:
            right_add = (left, right + 1, s + ")")
            print(f"    new right: {right_add}")
            q.append(right_add)

    # Once all valid combinations have been explored and added to `result`, return it
    return result


from leetcode_questions.utils.models.leetcode_data_models import (
    Difficulty,
    Metadata,
    Tags,
)

__metadata__ = Metadata(
    tags=[Tags.DYNAMIC_PROGRAMMING, Tags.STRING],
    difficulty=Difficulty.MEDIUM,
)
