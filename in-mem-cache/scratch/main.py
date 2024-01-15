from memcache import MemCache
from eviction_policy import LRU_EvictionPolicy

lru_eviction_policy = LRU_EvictionPolicy(maxsize=16)
cache = MemCache(eviction_policy=lru_eviction_policy)

cache.put("name", "shubham")
cache.put("age", 27)

print(cache.get("name"))
print(cache.get("age"))

print(cache.__repr__())
print(cache)
