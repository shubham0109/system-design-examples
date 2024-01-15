from collections import deque
from datetime import datetime

class MemCache:
    def __init__(self, seconds: int = None, eviction_policy = None):
        self.TTL = seconds
        self._cache = {}
        self.expiry_at = None
        self.eviction_policy = eviction_policy

    def _set_expiry(self):
        if self.TTL is not None:
            self.expiry_at = datetime.utcnow() + datetime(seconds=self.TTL)


    def __repr__(self):
        for key, value in self._cache.items():
            print("key: ", key, " value: ", value)

    def __str__(self):
        return str(self._cache)

    def put(self, key, value):
        hashed_key = self._get_hashed_value(key)

        removed_key = self.eviction_policy.eviction_policy(hashed_key, "put")
        if removed_key is not None:
            del self._cache[removed_key]

        self._cache[hashed_key] = value


    def get(self, key):
        hashed_key = self._get_hashed_value(key)
        
        if hashed_key not in self._cache.keys():
            return None
        else:
            self.eviction_policy.eviction_policy(hashed_key, "get")
            return self._cache.get(hashed_key)

    def clear(self):
        self.eviction_policy.eviction_policy(None, "clear")
        self._cache.clear()

    def delete(self, key):
        hashed_key = self._get_hashed_value(key)
        self.eviction_policy.eviction_policy(hashed_key, "delete")
        self._cache.pop(hashed_key, None)

    def _get_hashed_value(self, key):
       return hash(key)

     
