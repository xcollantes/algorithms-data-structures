"""Calculate fibonacci sequence."""


def fibo(n: int) -> int:
    """Recursively calculate the nth term of fibo."""
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibo(n - 2) + fibo(n - 1)
