"""Hashing basic.

Use a simple Hash Function.

Time complexity: O(1) or constant time.
"""

import logging
from typing import Any


logging.basicConfig(level=logging.DEBUG, format="%(message)s")


def main():
    logging.info("Basic Hash Table")

    h = HashTable(10)
    h.print_table()
    h.insert(12, "Foo")
    h.insert(13, "bar")
    h.insert(14, "hello")
    h.print_table()
    h.remove(12)
    h.print_table()


class HashTable:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_table = [None] * capacity

    def insert(self, key: Any, data: Any):
        """Add node with data to hash table."""
        index = self.hash(key)
        self.hash_table[index] = [key, data]

    def remove(self, key: Any):
        """Take away a node in hash table."""
        index = self.hash(key)
        self.hash_table[index] = None

    def hash(self, key: Any) -> Any:
        """Simple hash function.

        Args:
            key (Any): User inputted key.

        Returns:
            Hash value used as index. In this case, a simple integer as index.
        """
        return key % self.capacity

    def print_table(self):
        print(self.hash_table)


if __name__ == "__main__":
    main()
