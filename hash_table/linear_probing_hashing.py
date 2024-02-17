"""Hashing with Linear Probing for hash collisions."""

import logging
from basic_hashing import HashTable
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

    logging.info("Linear probing Hash Table")
    linear = LinearProbe(10)
    linear.print_table()
    linear.insert(12, "Foo")
    linear.insert(13, "bar")
    linear.insert(14, "hello")
    logging.info("introduce conflict")
    linear.insert(12, "conflict")
    linear.print_table()
    linear.remove(12)
    linear.print_table()


class LinkedListNode:
    """Doubly Linked List."""

    def __init__(self, value: Any,
                 prev_node=None,
                 next_node=None) -> None:
        self.prev_node = prev_node
        self.value = value
        self.next_node = next_node


class LinearProbe(HashTable):

    # Override
    def insert(self, key: Any, data: Any):
        index = self.hash(key)

        max_probing: int = 0
        while self.hash_table[index] is not None and max_probing < self.capacity:
            index += 1
            max_probing += 1

        self.hash_table[index] = [key, data]


if __name__ == "__main__":
    main()
