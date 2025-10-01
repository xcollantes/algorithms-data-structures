"""Fraction Addition

Medium

Given a string expression representing an expression of fraction addition and
subtraction, return the calculation result in string format.

The final result should be an irreducible fraction. If your final result is an
integer, change it to the format of a fraction that has a denominator 1. So in
this case, 2 should be converted to 2/1.
"""


def test_fraction_strings_simple():
    """pytest fraction_strings.py"""

    assert fraction_strings(
        ["2/6+2/6", "7/10+13/10", "1/8+1/9", "20/19+12/12", "1/1+2/2", "100/10+55/12"]
    ) == ["2/3", "2/1", "17/72", "39/19", "2/1", "175/12"]
    assert fraction_strings([]) == []


def fraction_strings(fractions: list[str]) -> list[str]:
    """
    n1
    /
    d1
    +
    n2
    /
    d2

    no negatives
    """

    res: list[str] = []

    # handle each calculation
    for calc in fractions:
        print(f"calc: {calc}")

        # split by + since only ever 2
        # doesn't work if more than 2
        frac1, frac2 = calc.split("+")
        print(f"    frac1: {frac1}")
        print(f"    frac2: {frac2}")

        # split by /
        # doesn't work if more than 2
        n1, d1 = frac1.split("/")
        n2, d2 = frac2.split("/")

        sum_den: int = int(d1)

        # get common denominator by multiply
        if d1 != d2:
            sum_den = int(d1) * int(d2)

            # equivalent of multiplying each side
            n1 = int(n1) * int(d2)
            n2 = int(n2) * int(d1)

            print(f"    new numerators: {n1} {n2}")

        # add numerators once denominator is common
        sum_num: int = int(n1) + int(n2)

        print(f"    unsimplified: {sum_num}/{sum_den}")

        # reduce
        # do not include 0 or 1.
        # negative for backwards to get greatest common simplification
        for i in range(min(sum_num, sum_den), 1, -1):

            print(
                f"i: {i} {sum_num / i} == {sum_num // i} AND {sum_den / i} == {sum_den // i}"
            )

            # if floor division and float division are the same, then exact
            # match
            if sum_num / i == sum_num // i and sum_den / i == sum_den // i:
                sum_num = sum_num // i
                sum_den = sum_den // i

                print(f"    new: {sum_num} / {sum_den}")

                # if you don't break, may get lower common factor.
                break

        res_element: str = f"{sum_num}/{sum_den}"

        print(f"    adding: {res_element}")
        res.append(res_element)

    # return ith list
    print(f"result: {res}")
    print()
    return res
