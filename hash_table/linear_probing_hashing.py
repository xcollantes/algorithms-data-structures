"""Hashing with Linear Probing for hash collisions."""


def linear_probe_insert(items: list[int]) -> list:
    """If slot is occupied, check for +1 slot."""
    hash_table: list[int | None] = [None for _ in items]

    for item in items:
        hash_idx = item % len(hash_table)

        while :
            if hash_table[hash_idx]:
                # Go to next slot
                hash_idx += 1
            else:
                hash_table[hash_idx] = item

    return hash_table
