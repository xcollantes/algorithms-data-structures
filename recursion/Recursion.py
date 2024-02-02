"""Recursion Practice
"""

__author__ = "Xavier Collantes"


def main():
    print("Reverse a string: %s" % reverse("hello world"))
    print("Factorial: %s" % fact(5))
    print("Sum of parts: %s" % sum_digits(4321))


def reverse(x):
    if len(x) == 1:
        return x
    else:
        return x[-1] + reverse(x[: len(x) - 1])


def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n - 1)


def sum_digits(n):
    if len(str(n)) == 1:
        return n
    else:
        return sum_digits(n // 10) + (n % 10)  # Use classic division


if __name__ == "__main__":
    main()
