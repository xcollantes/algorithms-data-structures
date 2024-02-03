"""Intervew question about balance parenthesis give a string.

This solution also considers brackets, braces, and chevrons.
"""


def main():
    balanced = ["()", "no parens", "(amzn)", "{(msft)}",
                "(([this is text]))", "<html></html>"]
    unbalanced = ["(", "{", "))", "\}\}\}", "<<"]
    candidates = balanced + unbalanced
    for b in balanced:
        assert check_balance(b) is True, "Expected balanced but isn't."
    for u in unbalanced:
        assert check_balance(u) is False, "Expected unbalanced but is."


def check_balance(candidate: str) -> bool:
    """Return True if string is balanced, False otherwise."""
    if len(candidate) < 1:
        return True

    LEFT: list(str) = ["(", "[", "{", "<"]
    RIGHT: list(str) = [")", "]", "}", ">"]

    result: list(str) = []
    for ch in candidate:
        if ch in LEFT:
            result.append(ch)
        elif ch in RIGHT:
            if len(result) < 1:
                return False
            result.pop()

    if len(result) == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
