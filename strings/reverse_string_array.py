"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
"""


def main():
    s1 = [1, 2, 3, 4, 5, 6, 7]
    reverse(s1)
    print(s1)
    assert s1 == [7, 6, 5, 4, 3, 2, 1]

    s2 = [1, 2, 3, 4, 5, 6, 7, 8]
    reverse(s2)
    print(s2)
    assert s2 == [8, 7, 6, 5, 4, 3, 2, 1]

    s3 = ["h", "e", "l", "l", "o"]
    reverse(s3)
    print(s3)
    assert s3 == ["o", "l", "l", "e", "h"]

    s4 = ["H", "a", "n", "n", "a", "h"]
    reverse(s4)
    print(s4)
    assert s4 == ["h", "a", "n", "n", "a", "H"]


def reverse(s: list[any]) -> None:
    """Inplace reverse array."""
    ep: int = len(s) - 1
    for fp in range(len(s) // 2):
        # print("fp: ", s[fp], " ep:", s[ep])
        s[fp], s[ep] = s[ep], s[fp]   # Pythonic way
        ep -= 1
        print(s)


if __name__ == "__main__":
    main()
