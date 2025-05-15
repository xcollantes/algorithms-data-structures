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

## Heap binary tree to array

![diagram](/heap/heap_array.png)

A heap can be expressed as a binary tree with the min or max at the root of the
tree.

The benefit of using an array avoids the overhead of a binary tree.

In array form, you can find the value give these formulas:

Left child of i: `2 * i`

Right child of i: `2 * i + 1`

Parent of i: `i // 2`

**Note:** It is cleaner for formulas if we start the array at 1 instead of 0.

### Examples

Given the image above, the left child of 15 is `= 2 * 3` where 3 is the array
index. So the left child is at index 6 where value is 12.

This works because the structure increases twice you move down the tree. In the
same way that traversing an array with two pointers: one at slow or +1 and one
at fast or +2, where when fast reaches the end of the array, slow will be at the
middle of the end or where fast is located.

So in the same way, since the tree is doubling at every level, the array is
filled up given the formulas with the ancestors of the tree as the array fills
up.
