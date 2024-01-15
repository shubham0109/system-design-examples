from functools import lru_cache

@lru_cache(maxsize=20)
def steps_to(stair):
    if stair == 1:
        return 1
    elif stair == 2:
        return 2
    elif stair == 3:
        return 4
    else:
        return steps_to(stair-1) + steps_to(stair-2) + steps_to(stair-3) 


print(steps_to(30))
print(steps_to.cache_info())
