cap = 2
Q = 2
Queries = [["PUT", 1, 2], ["GET", 1]]

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, cap):
        self.capacity = cap
        self.cache = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
    
    def add(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head
        
    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.add(node)
        return node.value

    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
        newNode = Node(key, value)
        self.add(newNode)
        self.cache[key] = newNode
        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self.remove(lru)
            del self.cache[lru.key]

# Run queries
s = LRUCache(cap)
for query in Queries:
    if query[0] == "PUT":
        s.put(query[1], query[2])
    elif query[0] == "GET":
        print(s.get(query[1]))