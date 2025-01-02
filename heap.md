# Heaps

Heaps are priority queues which can do:

- Add element in `O(log n)`
- Remove min element in `O(log n)`
- Find element `O(1)`

Min can be interchanged to max so either a min heap or max heap.

## When to use

Heaps are good for finding the min or max of a collection of data.

Potentially can improve time complexity from `O(n**2)` to `O(n * log n)`. Using
naive methods you would iterate the number of elements and another set of times
for each element or `O(n**2)`.

Heap will split the problem into a binary tree so the time complexity goes to
`O(n * log n)` since you iterate once per element but then each subsequent
iteration is split from the original iteration method.
h