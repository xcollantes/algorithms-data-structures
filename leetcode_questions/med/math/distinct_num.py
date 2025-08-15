"""357. Count Numbers with Unique Digits

Medium

Given an integer n, return the count of all numbers with unique digits, x, where
0 <= x < 10n.


Example 1:

Input: n = 2
Output: 91
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100,
excluding 11,22,33,44,55,66,77,88,99


Example 2:

Input: n = 0
Output: 1


Constraints:
0 <= n <= 8
"""


def test_distinct_num():
    """pytest distinct_num.py"""
    assert distinct_num(2) == 91
    assert distinct_num(0) == 1
    assert distinct_num(4) == 5275
    assert distinct_num(1) == 10
    assert distinct_num(3) == 739


def distinct_num(n: int) -> int:
    # Special case: for n=0, only number 0 has unique digits in range [0, 1)
    if n == 0:
        return 1

    # For n=1: numbers 0-9 all have unique digits (10 total)
    # This covers all 1-digit numbers with unique digits
    total = 10
    
    # p tracks the number of ways to form numbers of current length
    # Starting with 9 because first digit can't be 0 (for multi-digit numbers)
    p = 9

    # Calculate numbers with unique digits for lengths 2, 3, ..., n
    for i in range(2, n + 1):
        # For i-digit numbers:
        # - First digit: 9 choices (1-9, can't be 0)
        # - Second digit: 9 choices (0-9 except first digit)
        # - Third digit: 8 choices (0-9 except first two digits)
        # - ...
        # - i-th digit: (11-i) choices
        
        # p currently holds ways to form (i-1)-digit numbers
        # Multiply by (11-i) to get ways to form i-digit numbers
        total += p * (11 - i)
        
        # Update p for next iteration: multiply by available choices for next position
        # (11-i) represents remaining digit choices after using (i-1) digits
        p *= 11 - i

    return total
