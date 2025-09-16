"""Multiply two integers without using multiplication, division and bitwise
operators, and no loops."""


def multiply(a: int, b: int) -> int:

    if b == 0:
        return 0

    if b > 0:
        return a + multiply(a, b - 1)

    if b < 0:
        return -multiply(a, -b)


def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(1, 0) == 0
    assert multiply(-1, 2) == -2
    assert multiply(0, 0) == 0
