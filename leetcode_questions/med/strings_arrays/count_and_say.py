"""38. Count and Say

Run-length encoding (RLE) is a string compression method that works by
replacing consecutive identical characters (repeated 2 or more times) with the
concatenation of the character and the number marking the count of the
characters (length of the run).

For example, to compress the string "3322251" we
replace "33" with "23", replace "222" with "32", replace "5" with "15" and
replace "1" with "11". Thus the compressed string becomes "23321511".

Given a positive integer n, return the nth element of the count-and-say
sequence.

The confusing part is that you have to perform the RLE on the result of the
previous function call.
"""


def countAndSayIterative(n: int) -> str:
    """Iterative."""


def countAndSay(n: int) -> str:
    """Recursive."""
    print(f"Count and say: {n}")

    if n == 1:
        return "1"

    # Returns the RLE
    # n acts as another layer of performing the RLE.
    prev_rle: str = countAndSay(n - 1)
    current_rle: str = ""
    count: int = 1

    prev_rle_char: str = prev_rle[0]
    for i in range(1, len(prev_rle)):
        print(f"i: {i}; prev_rle_char: {prev_rle_char}; prev_rle[i]: {prev_rle[i]}")
        if prev_rle[i] == prev_rle_char:
            print(f"Equals: {prev_rle[i]} == {prev_rle_char}")
            count += 1
        else:
            # Append count
            current_rle += str(count) + str(prev_rle_char)
            prev_rle_char = prev_rle[i]
            count = 1

    current_rle += str(count) + str(prev_rle_char)

    print(f"current_rle: {current_rle}; prev {prev_rle}; count: {count};")

    return current_rle
