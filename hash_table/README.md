# Hashing

A Hash Table is a way to store data after being processed by a Hash Function.
The Hash Table will contain data with a Key and Value pair.

Hash collision: When a Hash Function creates duplicate Keys and a conflict is
created where that Key is stored.

Resolve Hash collisions by choosing a technique: - resolve by "chaining" -
resolve through "open addressing" - linear/quadratic probing - double hashing

Chaining: When a collision is found, store the new data using a Doubly Linked
List.

![Hash
chaining](https://cdn.programiz.com/sites/tutorial2program/files/Hash-3_1.png)

Open addressing: Instead of storing multiple values in one slot in the Hash
Table, each slot has one value or left NULL. Use either Linear probing or Double
Hashing.

Linear probing: If conflict is found, place value in next slot.

```python
i = some index
m = some mod
hash_function(key, value) = (hash_function_prime(key) + i) % m
```

If there is a conflict at i + 1, then check i + 2, and so on. The value will be
placed until an open slot if found in a linear iteration.

Downfall of Linear addressing: If a cluster of slots are occupied, then the
whole cluster must be iterated on.

Quadratic probing: Checks for an open slot like Linear probing but instead of +1
for increments, each increment is larger.

Double hashing: If a collision is found, use another hash function to find next
slot.
