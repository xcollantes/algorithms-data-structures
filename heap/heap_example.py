"""Heap example.

Without using heapq module.
"""

from typing import Any


class MinHeap:
    """

    Needed formulas:
        Where i is the index.

        parent = i // 2
        left_child = i * 2
        right_child = i * 2 + 1
    """

    def __init__(self) -> None:
        # Starting array at 1 for cleaner formulas.
        self.heap = [0]

        # If you needed a fixed heap:
        # self.heap = [0] * heap_size + 1

        self.size = 0

    def add(self, value: Any) -> None:
        """Add value to heap."""
        self.size += 1

        self.heap.append(value)

        # Use the end of the heap which is size.
        i = self.size
        parent = i // 2

        # As long as new element is smaller then the parent, exchange with
        # parent.
        while self.heap[i] < self.heap[parent] and i > 1:
            print(f"{self.heap[i]} < {self.heap[parent]} and {i} > 1")

            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]

            i = parent
            parent = i // 2  # Find new parent.

    def get_top(self) -> Any:
        """Peek top of heap."""
        # Heap starts at 1 to keep formulas which map the tree to array
        # cleaner.
        return self.heap[1]

    def pop(self) -> Any:
        """Remove and return top value."""

    def get_size(self) -> int:
        return self.size


# pytest


def test_heap():
    heap = MinHeap()
    heap.add(5)
    assert heap.get_top() == 5
    heap.add(2)
    assert heap.get_top() == 2
    heap.add(9)
    assert heap.get_top() == 2
    heap.add(0)
    assert heap.get_top() == 0
    heap.add(10)
    assert heap.get_top() == 0
    heap.add(4)
    assert heap.get_top() == 0
    heap.add(8)
    assert heap.get_top() == 0
