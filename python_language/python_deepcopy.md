# How deepcopy and memory allocation works in Python

Shallow copy will create a new object with the same references to the original
object. The references reach one level deep only.

Deepcopy will create a new object with new references copying the values
recursively.

Allocation of memory space is related to the difference but in Python it's best
to think of the practical difference with copying nested values.

This difference only works in objects such as lists, dicts, and sets.

## Regular copy

- `B: list[Any] = A`

All references are the same.

```python
A = [[1, 1, 1], [2, 2, 2]]
B = A

A[0] = [3, 3, 3]  # First level change.
A[1][0] = 5       # Second level change.

# Changes at all levels are linked.
print(A)  # [[3, 3, 3], [5, 2, 2]]
print(B)  # [[3, 3, 3], [5, 2, 2]]
```

## Shallow copy

- `copy()`
- `copy.copy()`
- `B: list[Any] = A[:]`
- `list()`, `dict()`, `set()`

Use for large data objects to prevent duplications in memory.

If you edit one level deep, changes are independent.

```python
original_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = list(original_list)

# Edit one level deep.
original_list[2] = [5, 5, 5]

# The change is only one level deep.
print(original_list)  # [[1, 1, 1], [2, 2, 2], [5, 5, 5]]
print(new_list)       # [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
```

But if you change nested values, the changes are linked.

```python
original_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = list(original_list)

# Edit original nested value.
original_list[0][1] = 5

# Nested values are linked.
print(original_list)  # [[1, 5, 1], [2, 2, 2], [3, 3, 3]]
print(new_list)       # [[1, 5, 1], [2, 2, 2], [3, 3, 3]]
```

## Deepcopy

- `copy.deepcopy()`

Use when you want to keep both the original and new data.
