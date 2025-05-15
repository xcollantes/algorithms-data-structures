"""Heap using built-in function.

You provide your own array list of items. When you print out the array heap, the
order is of the heap formulas:

With i as the index:

left_child = i * 2
right_child = i * 2 + 1
parent = i // 2
"""

import heapq

heap = []


heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 4)
heapq.heappush(heap, 2)
heapq.heappush(heap, 1)
print(f"Min-heap property: smallest element is at position 0: {heap}")

print(f"heap as array: {heap}")

print(f"Popping the element at 0: {heapq.heappop(heap)}")
print(f"heap as array: {heap}")

a = [3, 4, 1, 22, 23, 11]
heapq.heapify(a)

print(f"List to heap: {a}")

print(f"Get N largest: {heapq.nlargest(2, a)}")

print(f"Get N smallest: {heapq.nsmallest(2, a)}")

priority_q = []

print("Priority queue with tuples")

heapq.heappush(priority_q, (2, "Medium priority"))
heapq.heappush(priority_q, (1, "Low priority"))
heapq.heappush(priority_q, (3, "High priority"))

print(f"priority queue: {priority_q}")

print("Process items in priority queue")

while priority_q:
    tag, content = heapq.heappop(priority_q)
    print(f"Priority queue: {tag}, {content}")
