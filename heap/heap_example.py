"""Heap example.

Without using heapq module.
"""

class Heap:
    def __init__(self) -> None:
        self.size = 0
        self._heap = []

    def add(self, value: any) -> None:
        self._heap.append(value)
        self.size += 1
        self._heapify(len(self._heap) - 1)

        while index > 0 and self._heap[index] < self.heap[self.parent(index)]