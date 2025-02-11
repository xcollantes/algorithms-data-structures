"""Sam Wang's solution."""

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.head = Node(-1, -1)
        self.tail = self.head
        self.dict = {}


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dict:
            self.renew(self.dict[key])
            return self.dict[key].value
        else:
            return -1


    def put(self, key, value):
        if key in self.dict:
            cur_node = self.dict[key]
            cur_node.value = value
            self.renew(cur_node)
        else:
            cur_node = Node(key, value)
            self.dict[key] = cur_node
            self.tail.next = cur_node
            cur_node.prev = self.tail
            self.tail = cur_node
            if self.size < self.capacity:
                self.size += 1
            else:
                to_delete = self.head.next
                to_delete.next.prev = to_delete.prev
                to_delete.prev.next = to_delete.next
                del self.dict[to_delete.key]
    def renew(self, entry):
        if entry != self.tail:
            entry.next.prev = entry.prev
            entry.prev.next = entry.next
            self.tail.next = entry
            entry.prev = self.tail
            self.tail = entry

    # def refresh(self):

    # def delete(self, key):



class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)