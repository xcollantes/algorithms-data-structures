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

- **February 20, 1991:** Python 0.9.0, the first public release, emerges. It
  focuses on code readability and simplicity.

## Number Behavior and String Conversion

### int() Casting Limitations

The `int()` function can actually handle negative strings correctly, but it's important to understand its behavior with different input formats.

```python
# These work correctly
int("123")  # Returns 123
int("-123")  # Returns -123
int("+123")  # Returns 123

# These raise ValueError
int("12.34")  # ValueError: invalid literal for int() with base 10: '12.34'
int("abc")  # ValueError: invalid literal for int() with base 10: 'abc'
int("")  # ValueError: invalid literal for int() with base 10: ''
```

### isdigit() Function Limitations

The `isdigit()` method only returns `True` for strings that contain only digits (0-9). It does not recognize negative signs, decimal points, or other numeric characters.

```python
# These return True
"123".isdigit()  # True
"456".isdigit()  # True

# These return False
"-123".isdigit()  # False (contains minus sign)
"+123".isdigit()  # False (contains plus sign)
"12.34".isdigit()  # False (contains decimal point)
"abc".isdigit()  # False (contains letters)
"".isdigit()  # False (empty string)
"12³".isdigit()  # False (contains superscript)
```

### Alternative Methods for Number Validation

For more robust number validation, consider these alternatives:

```python
# Check if string can be converted to int (handles negatives)
def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

# Check if string can be converted to float (handles decimals and negatives)
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# Examples
is_integer("-123")  # True
is_integer("12.34")  # False
is_number("-123")  # True
is_number("12.34")  # True
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
