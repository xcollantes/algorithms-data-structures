# Map

Performs function for each element of iterable.

```python
def myfunc(a):
    return len(a)

mylist = ["hello", "word", "a"]
x = map(myfunc, mylist)

# Result in x.
for e in x:
    print(e)
```

Using length as key using `len()`:

```python
mylist = ["hello", "word", "a"]

# Result in x.
x = map(len, mylist)

for e in x:
    print(e)

# 5
# 4
# 1
```
