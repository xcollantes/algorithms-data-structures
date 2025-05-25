"""Break up an integer into its digits with place values."""


import math


def test():
    assert sorted(deconstruct(3749)) == sorted([3000, 700, 40, 9])
    assert sorted(deconstruct(250)) == sorted([200, 50])
    assert sorted(deconstruct(1001)) == sorted([1000, 1])
    assert sorted(deconstruct(3749)) == sorted([3000, 700, 40, 9])
    assert sorted(deconstruct(0)) == []
    assert sorted(deconstruct(1000)) == sorted([1000])


def deconstruct(num: int) -> list[int]:
    if num == 0:
        return []

    result = []

    while num > 0:
        # Get the number of digits
        e = int(math.log10(num))

        # Calculate the place value (10^e)
        place_value = 10 ** e

        # Get the digit at this place value
        digit = num // place_value

        # Add the digit with its place value to result
        result.append(digit * place_value)

        # Remove the processed digit
        num -= digit * place_value

    return result
