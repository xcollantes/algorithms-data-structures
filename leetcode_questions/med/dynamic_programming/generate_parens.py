"""22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of
well-formed parentheses.
"""


def generateParenthesis(n: int) -> list[str]:
    # Initialize an empty list to store the resulting combinations of parentheses
    result = []

    # Define the initial counts of left and right parentheses used
    # Start with a queue (stack in this case, as we use pop from the end) for breadth-first exploration
    left = right = 0  # Start with 0 left '(' and 0 right ')' parentheses used
    q = [
        (left, right, "")
    ]  # Each element in the queue contains (count of left, count of right, current string)

    # Use a while loop to explore all valid combinations
    while q:
        # Extract the current state from the queue
        left, right, s = q.pop()  # Retrieve the top of the stack

        # If the current string `s` has reached the required length (2 * n), it is a valid result
        if len(s) == 2 * n:
            result.append(s)  # Add the valid combination to the result list

        # If there are remaining left parentheses to add, append one and push the state to the stack
        if left < n:
            q.append((left + 1, right, s + "("))

        # If there are more left parentheses in the string than right ones, a ')' can be added
        # This ensures that the parentheses sequence remains valid
        if right < left:
            q.append((left, right + 1, s + ")"))

    # Once all valid combinations have been explored and added to `result`, return it
    return result
