"""Heap example."""

import heapq


# Method 1: Using heapq (which implements a min heap) with negated values
def max_heap_using_heapq():
    """Demonstrate max heap using Python's heapq module with negated values."""
    # Initialize an empty max heap
    max_heap = []

    # Insert elements (negate values to turn min heap into max heap)
    values = [4, 1, 7, 3, 8, 5]
    for value in values:
        heapq.heappush(max_heap, -value)

    print("Max Heap using heapq:", [-x for x in max_heap])  # Display actual values

    # Extract maximum element
    max_value = -heapq.heappop(max_heap)
    print("Max value extracted:", max_value)
    print("Heap after extraction:", [-x for x in max_heap])

    # Heapify a list in-place
    values = [4, 1, 7, 3, 8, 5]
    negated = [-x for x in values]
    heapq.heapify(negated)
    print("Heapified array:", [-x for x in negated])


# Method 2: Custom Max Heap implementation
class MinHeap:
    """Custom implementation of a max heap."""

    def __init__(self):
        self.heap = [None]

    def push(self, value):
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        """Remove and return the maximum value from the heap."""
        if len(self.heap) <= 1:
            return None

        max_value = self.heap[1]
        # Move the last element to the root and remove the last element
        self.heap[1] = self.heap[-1]
        self.heap.pop()

        # Restore heap property
        if len(self.heap) > 1:
            self._sift_down(1)

        return max_value

    def peek(self):
        """Return the maximum value without removing it."""
        if len(self.heap) <= 1:
            return None
        return self.heap[1]

    def _sift_up(self, index):
        """Move a value up to its correct position."""
        parent = index // 2
        if index > 1 and self.heap[parent] < self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self._sift_up(parent)

    def _sift_down(self, index):
        """Move a value down to its correct position."""
        largest = index
        left = 2 * index
        right = 2 * index + 1

        # Find the largest among node and its children
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left

        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        # If the largest isn't the current node, swap and continue sifting down
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._sift_down(largest)

    @classmethod
    def heapify(cls, arr):
        """Create a max heap from an array."""
        heap = cls()
        heap.heap = [None] + arr.copy()

        # Start from the middle and sift down each node
        for i in range(len(heap.heap) // 2, 0, -1):
            heap._sift_down(i)

        return heap

    def __str__(self):
        """Return a string representation of the heap."""
        return str(self.heap[1:])


def demonstrate_custom_max_heap():
    """Show the custom MaxHeap implementation in action."""
    # Create an empty max heap and add elements
    heap = MinHeap()
    for value in [4, 1, 7, 3, 8, 5]:
        heap.push(value)

    print("Custom Max Heap:", heap)

    # Extract maximum element
    max_value = heap.pop()
    print("Max value extracted:", max_value)
    print("Heap after extraction:", heap)

    # Create a heap from an existing array
    values = [4, 1, 7, 3, 8, 5]
    heap = MinHeap.heapify(values)
    print("Heapified array:", heap)

    # Extract all elements in decreasing order
    sorted_values = []
    while heap.peek() is not None:
        sorted_values.append(heap.pop())
    print("Extracted in order:", sorted_values)


if __name__ == "__main__":
    print("=== Max Heap using heapq ===")
    max_heap_using_heapq()

    print("\n=== Custom Max Heap Implementation ===")
    demonstrate_custom_max_heap()
