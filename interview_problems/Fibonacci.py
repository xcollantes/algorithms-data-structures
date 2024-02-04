from typing import List


def main():
    print(fib_rec(10))
    print(fib_iter(10))


def fib_memo(n: int) -> int:
    pass


def fib_iter(n: int) -> int:
    a = 0
    b = 1
    for i in range(n):
        temp = b
        b = a + b
        a = temp

    return a


def fib_rec(n: int) -> int:
    if n == 1 or n == 0:
        return n
    else:
        return fib_rec(n - 2) + fib_rec(n - 1)


if __name__ == "__main__":
    main()
