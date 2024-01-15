from abc import ABC, abstractmethod
from collections import deque, defaultdict

class EvictionPolicy(ABC):
    
    @abstractmethod
    def is_full(self):
        raise NotImplementedError

    @abstractmethod
    def eviction_policy(self):
        raise NotImplementedError


class LRU_EvictionPolicy(EvictionPolicy):
    
    def __init__(self, maxsize: int = 128):
        self.MAX_SIZE = maxsize
        self.double_ll = deque()

    def is_full(self):
        return len (self.double_ll) == self.MAX_SIZE

    def eviction_policy(self, key, action: str = None):
        if action == "get":
            self.double_ll.remove(key)
            self.double_ll.appendleft(key)
            return key

        elif action == "put":
            if key in self.double_ll:
                self.double_ll.remove(key)
            
            removed_key = None
            if len(self.double_ll) == self.MAX_SIZE:
                removed_key = self.double_ll.pop()

            self.double_ll.appendleft(key)
            return removed_key

        elif action == "clear":
            self.double_ll.clear()
            return None

        elif action == "delete":
            self.double_ll.remove(key)
            return key

        else:
            return "No action given."


class LFU_EvictionPolicy(EvictionPolicy):
    
    def __init__(self, maxsize: int = 128):
        self.MAX_SIZE = maxsize
        self.frequency_map = defaultdict(int)

    def is_full(self):
        return len (self.frequency_map) == self.MAX_SIZE

    def eviction_policy(self, key, action: str = None):
        
        if action == "get":
            self.frequency_map[key] += 1
            return key

        elif action == "put":
            removed_key = None
            if len(self.frequency_map) == self.MAX_SIZE:
                removed_key = min(self.frequency_map.keys(), key=lambda k: self.frequency_map[k])
                del self.frequency_map[removed_key]

            self.frequency_map[key] += 1
            return removed_key

        elif action == "clear":
            self.frequency_map = defaultdict(int)
            return None

        elif action == "delete":
            del self.frequency_map[key]
            return key

        else:
            return "No action given."
