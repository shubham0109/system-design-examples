from collections import deque, abc

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # Dictionary for key-value pairs
        self.order = deque(maxlen=capacity)  # Deque for maintaining order
        self.view = abc.MappingProxy(self.cache)  # Read-only dictionary view

    def __len__(self):
        return len(self.cache)

    def __getitem__(self, key):
        return self.view[key]  # Access cache through read-only view

    def get(self, key):
        try:
            # Move accessed element to front (Deque operation)
            self.order.remove(key)
            self.order.appendleft(key)
            return self.cache[key]
        except KeyError:
            return None

    def put(self, key, value):
        if key in self.cache:
            # Update entry position if existing (Deque operation)
            self.order.remove(key)
        else:
            if len(self) == self.capacity:
                # Evict LRU from deque (Deque operation)
                lru_key = self.order.pop()
                del self.cache[lru_key]

        # Store value and reference in dictionary (Dict operation)
        self.cache[key] = value
        self.order.appendleft(key)

    def remove(self, key):
        # Remove from both dictionary and deque (Dict & Deque operations)
        del self.cache[key]
        self.order.remove(key)

