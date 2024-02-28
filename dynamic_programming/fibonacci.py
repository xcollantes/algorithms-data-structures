"""Calculate fibonacci sequence."""


def fibo(n: int) -> int:
    """Recursively calculate the nth term of fibo."""
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibo(n - 2) + fibo(n - 1)


memo = {}


def fibo_dp(n: int) -> int:
    """Return the nth term of fibo using Dynamic Programming.

    Notice the amount of time taken to run the DP version compared to the
    regular version.
    """
    if n == 0:
        return 0
    if n == 1:
        return 1

    if n in memo:
        return memo[n]

    # Save the input and calculation result
    memo[n] = fibo_dp(n - 1) + fibo_dp(n - 2)
    return memo[n]
