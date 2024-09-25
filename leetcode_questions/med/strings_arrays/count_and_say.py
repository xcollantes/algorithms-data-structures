"""Run-length encoding (RLE) is a string compression method that works by
replacing consecutive identical characters (repeated 2 or more times) with the
concatenation of the character and the number marking the count of the
characters (length of the run).

For example, to compress the string "3322251" we
replace "33" with "23", replace "222" with "32", replace "5" with "15" and
replace "1" with "11". Thus the compressed string becomes "23321511".

Given a positive integer n, return the nth element of the count-and-say
sequence.
"""


def countAndSayIterative(n: int) -> str:
    """Iterative."""


def countAndSay(n: int) -> str:
    """Recursive."""
    print(f"Count and say: {n}")

    if n == 1:
        return "1"

    prev_result: int = countAndSay(n - 1)
    result: str = ""
    first_prev: str = prev_result[0]

    count: int = 1

    for i in range(1, len(prev_result)):
        if prev_result[i] == first_prev:
            count += 1
        else:
            # Append count
            result += str(count)
            result += str(first_prev)
            first_prev = prev_result[i]
            count = 1

    result += str(count)
    result += str(first_prev)

    print(f"result: {result}; prev {prev_result}; count: {count};")

    return result
