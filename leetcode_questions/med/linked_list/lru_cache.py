"""146. LRU Cache

Medium

Design a data structure that follows the constraints of a Least Recently Used
(LRU) cache.

Implement the LRUCache class:

`LRUCache(int capacity)` Initialize the LRU cache with positive size capacity.

`int get(int key)` Return the value of the key if the key exists, otherwise return -1.

`void put(int key, int value)` Update the value of the key if the key exists.
Otherwise, add the key-value pair to the cache. If the number of keys exceeds
the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.


Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4


Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.
"""


class Node:
    """Bi-directional node."""

    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value

        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0

        # Key to Node will make accessing fast since no need to iterate through the linked list.
        # Essential since we will be rewiring the pointers between the nodes.
        self.cache: dict[int, Node] = {}

        # Actual values are self.head + 1 node.
        # Head of linked list is Least Recently Used node.
        self.head = Node(-1, 1)

        self.tail = self.head

    def get(self, key: int) -> int:
        print(f"GET: {key} from {self.cache.keys()}")

        if self.cache.get(key, None):
            # Mark the node value as accessed.
            self.move_used(self.cache[key])

            print(f"    Found {self.cache[key].value}")

            return self.cache[key].value
        else:
            print(f"    Not found")

            return -1

    def put(self, key: int, value: int) -> None:
        print(f"PUT: {key} {value}")

        # check if exists
        if key in self.cache:
            curr_node: Node = self.cache[key]
            curr_node.value = value

            self.move_used(curr_node)

        else:

            new_node: Node = Node(key, value)
            self.cache[key] = new_node

            self.tail.next = new_node

            new_node.prev = self.tail
            self.tail = new_node

            print(f"Added to cache hashmap {self.cache.keys()}")

            # If cache is full: Evict least used.
            # It's possible to be over the capacity with the last addition.
            if len(self.cache) > self.capacity:
                print(f"Capacity reached on {self.cache.keys()}")

                del_node: Node = self.head.next
                new_head: Node = del_node.next

                new_head.prev = del_node.prev

                self.head.next = new_head
                new_head.prev = self.head

                print(f"Deleted node from cache and node deleted: {del_node.key}")
                del self.cache[del_node.key]

    def move_used(self, curr_node: Node) -> None:
        """Take recently accessed node and move to the end.

        End of the linked list is recently used.
        So front of linked list is Least Recently Used.
        """
        if curr_node == self.tail:
            return

        next_node: Node = curr_node.next
        prev_node: Node = curr_node.prev

        # Rearrange pointers to skip current node.
        next_node.prev = curr_node.prev
        prev_node.next = curr_node.next

        # Move recently used node to end.
        self.tail.next = curr_node

        curr_node.prev = self.tail

        self.tail = curr_node

    def peek(self):
        curr = self.head
        while curr:
            print(f"{curr.key} -> ", end="")
            curr = curr.next
        print()


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
