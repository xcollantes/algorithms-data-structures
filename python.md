# Good to know concepts for Python

You should be well-versed in the programming language you're using; in this
case, Python3.

## What is Python

Python is an interpretive language which means the compiler will read the human
input language syntax and create machine code at runtime. This is opposed to a
compiled language which produces a binary file to run. But you can actually
create a binary file from the source code with the pycompiler library.

### Python 3.5

Python typing (PEP 484)

### Python 3.9

- You can specify the type such as `list[...]`, `set[...]`.
- In Python 3.8 or before, you have to import `from typing import List`.

### Python 3.10

Using `|` symbol for types

## PEP

Python 8: Style guide

Python 484: Typing hints

Python 20: Zen of Python

Python 257: Doc string conversions

- **February 20, 1991:** Python 0.9.0, the first public release, emerges. It
  focuses on code readability and simplicity.

## defaultdict

Same as the Python Dictionary but never returns `KeyError`.

Without `defaultdict`:

```python
my_dict = {"first": "name", "second": "age"}
my_dict["third"]  # KeyError
```

With `defaultdict`:

```python
from collections import defaultdict

my_dict = defaultdict(lambda: "Not found")
my_dict["first"] = "name"
my_dict["second"] = "age"

my_dict["third"]  # Returns "Not found"
```

## deque

Used for Stack data structure.

```python
from collections import deque

def reverse_words_deque(sentence: str) -> list[str]:
    """Use deque library."""
    stack: deque = deque(sentence.split(" "))

    result: list[str] = []
    while len(stack) > 0:
        result.append(stack.pop())

    print(result)
    return result
```

## Queue

Practically the same as deque except used for managing Threads.

Threads run within a Process.

```python
import queue
import threading
import time

q = queue.Queue()

def my_thread():
    while True:
        item = q.get()
        print(f"start: {item}")
        time.sleep(2)
        print(f"end: {item}")
        q.task_done()

t = threading.Thread(target=my_thread, daemon=True)
t.start()

for item in ["hello", 10, 99, 200]:
    q.put(item)

# Threads wait until all are done
q.join()
print("ALL DONE")
```

## max

Get maximum value in a data.

`key` can be given a function.

```python
a = {"a": 20, "b": 11, "c": 10, "d": 89}
max(a, key=a.get)
```

## sorted

`sorted()` will return a sorted function as opposed to `sort()` which returns
None and sorts in-place.

The `sorted()` function can also take `key=` which is a function that will be
applied to each iteration.

```python
t = [(3, 1), (3, 2), (1, 0)]
print(sorted(t))  # Prints [(1, 0), (3, 1), (3, 2)]

a = [3, 2, 1]
print(sorted(a))  # Prints [1, 2, 3]

o = {"a": 2, "c": 1, "b": 0}
print(sorted(o))  # Prints ["a", "b", "c"]
```

## enumerate

Takes an iterable and return an array of tuples with the first element as a
sequential number for each tuple.

```python
a = ['h', 'l', 'l', 'o']
[i for i in enumerate(a)]
# [(0, 'h'), (1, 'l'), (2, 'l'), (3, 'o')]
```

## Shallow vs Deep copy

Shallow creates a new instance in memory for one level deep only.

In this example, `list()` will create a shallow copy where the object is copied
non-recursively. For this use case, it works since the object is one dimension
anyway.

```python
a = [0, 1, 2, 3]
b = a
c = list(a)

a[0] = 9

print(a)  # [9, 1, 2, 3]
print(b)  # [9, 1, 2, 3]
print(c)  # [0, 1, 2, 3]
```

In this example, a shallow copy is created but the object is 2 dimensional so
the change in `a` also affects `c`.

```python
a = [[0, 1], [2, 3]]
b = a
c = list(a)

a[0][0] = 9

print(a)  # [[9, 1], [2, 3]]
print(b)  # [[9, 1], [2, 3]]
print(c)  # [[9, 1], [2, 3]]
```

Deep copy creates a new instance with recursive copy in memory.

```python
import copy

a = [[0, 1], [2, 3]]
b = a
c = copy.deepcopy(a)

a[0][0] = 9

print(a)  # [[9, 1], [2, 3]]
print(b)  # [[9, 1], [2, 3]]
print(c)  # [[0, 1], [2, 3]]
```
