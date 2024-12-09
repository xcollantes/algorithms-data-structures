# Dictionaries

Also known as hashes in other languages.

## Creating dictionaries

```python
a_dict = {}
a_dict = dict()
```

## Accessing and editing

```python
a_dict = {"Third": 12, "Second": 10, "First": 5}

a_dict["First"]  # By key.

# Access with default if key not found.
a_dict.get("First", "default value")

# Useful for counting.
values_list = ["Red", "Blue", "Red", "Yellow"]

a_dict_counts = {}
for color in values_list:
    a_dict_counts[color] = a_dict_counts.get(color, 0) + 1
```

## Sorting

Sort entire dictionary. Return entire dictionary.

```python
a_dict = {"Third": 12, "Second": 10, "First": 5}

# item[1] since item is one iteration of a_dict.items().
s = sorted(a_dict.items(), key=lambda item: item[1])

# Since above returns list of tuples, change back it dict.
# {"First": 5, "Second": 10, "Third": 12}
s = dict(s)

print(s)
```

Sort by value. Return sorted keys.

```python
a_dict = {"Third": 12, "Second": 10, "First": 5}

# Performs `a_dict.get()` for each element in `a_dict`.
s = sorted(a_dict, key=a_dict.get)

# ["First", "Second", "Third"]
print(s)
```

Sort by keys. Return entire dictionary.

```python
a_dict = {"Third": 12, "Second": 10, "First": 5}

# If you iterate on `a_dict`, keys are iterated.
s = sorted(a_dict)

# ["First", "Second", "Third"]
print(s)
```

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
