"""Hashing with Linear Probing for hash collisions."""


def linear_probe_insert(items: list[int]) -> list:
    """If slot is occupied, check for +1 slot."""
    hash_table: list[int | None] = [None for _ in items]
    remaining_capacity = len(hash_table) - 1

    for item in items:
        hash_idx = item % len(hash_table)

        while remaining_capacity > 0:
            if hash_table[hash_idx] is not None:
                hash_table[hash_idx] = item
                remaining_capacity += 1
            else:
                hash_idx += 1

    return hash_table
