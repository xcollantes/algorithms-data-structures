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

    assert fraction_strings(["2/6+2/6", "7/10+13/10", "1/8+1/9"]) == [
        "2/3",
        "2/1",
        "17/72",
    ]
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
        n1, d1 = frac1.split("/")
        n2, d2 = frac2.split("/")

        newden = d1

        # get common denominator by multiply
        if d1 != d2:
            newden = int(d1) * int(d2)

        print(f"    newden: {newden}")

        sumnum: int = int(n1) + int(n2)

        # reduce
        while

        

        # find


        res_element: str = f"{sumnum}/{newden}"

        print(f"    adding: {res_element}")
        res.append(res_element)


    # return ith list
    print(f"result: {res}")
    print()
    return res
