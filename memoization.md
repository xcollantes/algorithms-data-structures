# Memoization

Example: Fibonacci sequence `f(x) = f(x - 1) + f(x - 2); f(1) = 1; f(2) = 1`

```python
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
```

This solution without memoization will compute the same value multiple times
such as `fib(3)`, `fib(1)`, etc.

**With memoization:**

```python
memo: dict[int, int] = dict()

def fib(n, memo):
    if memo[n]:  # O(1)
        return memo[n]
    if n == 1 or n == 2:  # O(1)
        return 1
    else:
        memo[n] = fib(n - 1) + fib(n - 2)  # O(2n)
```

Without memoization time complexity: O(2n + 1) since you call `fib()` twice for
every `n` value.

With memoization time complexity: O(2n + 1) \* O(1) since each operation takes
O(1). This results to O(n) since we drop constants.

<https://www.youtube.com/watch?v=P8Xa2BitN3I>

<https://www.youtube.com/watch?v=vYquumk4nWw>
