class Node:
    def __init__(self,key,val):
        self.key,self.val = key,val
        self.prev,self.next = None,None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {} #cache
        self.left,self.right = Node(0,0), Node(0,0)
        self.left.next,self.right.prev = self.right,self.left
    
    def remove(self,key):
        p,n = self.map[key].prev, self.map[key].next
        p.next,n.prev = n,p
        self.map[key].prev, self.map[key].next = None,None
        return
    
    def insert(self,key):
        p = self.right.prev
        p.next = self.map[key]
        self.right.prev = self.map[key]
        self.map[key].prev, self.map[key].next = p, self.right
        return
    
    def insert_node(self,key,value):
        node= Node(key,value)
        self.map[key] = node
        p = self.right.prev
        p.next,self.right.prev = node,node
        node.prev,node.next = p,self.right
        return

    def get(self, key: int) -> int:
        if key in self.map:
            self.remove(key)
            self.insert(key)
            return self.map[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(key)
            del self.map[key]
        if len(self.map)>=self.cap:
            lru = self.left.next
            self.remove(lru.key)
            del self.map[lru.key]
        self.insert_node(key,value)
        return

