class ListNode:

        def __init__(

                self, key: int = 0, value: int = 0, next: ListNode = None, prev: ListNode = None
            ):
                self.key = key
                self.value = value
                self.next = next
                self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
            self.capacity = capacity
            self.hashmap = {}
            self.lru = ListNode()
            self.mru = ListNode(prev=self.lru)
            self.lru.next = self.mru

        # remove node from list
    def remove(self, node):
            node.prev.next = node.next
            node.next.prev = node.prev

        # insert at right
    def insert(self, node):
            node.next = self.mru
            node.prev = self.mru.prev
            self.mru.prev.next = node
            self.mru.prev = node

    def get(self, key: int) -> int:
        print("get", key)
        if key in self.hashmap:
                self.remove(self.hashmap[key])
                self.insert(self.hashmap[key])
                return self.hashmap[key].value
        return -1

    def put(self, key: int, value: int) -> None:
            print("put", key, value)
            if key in self.hashmap:
                self.remove(self.hashmap[key])
            self.hashmap[key] = ListNode(key, value)
            self.insert(self.hashmap[key])

            if len(self.hashmap) > self.capacity:
                temp = self.lru.next
                self.remove(temp)
                del self.hashmap[temp.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

