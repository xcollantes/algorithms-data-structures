"""Find number of digits in a given number."""

import math


def main():
    inputs: list(int, int) = [
        (1, 1),
        (1234, 4),
        (12, 2),
        (333333, 6),
        (123546789, 9),
    ]

    for num, places in inputs:
        print(num, "has", int(math.log10(num) + 1), "places")
        assert int(math.log10(num) + 1) == places


if __name__ == "__main__":
    main()
