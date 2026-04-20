from functools import lru_cache

@lru_cache(maxsize=None)
def fibonnaci(n):
    if n <= 1:
        return n

    return fibonnaci(n - 2) + fibonnaci(n - 1)

print(fibonnaci(5))
print(fibonnaci.cache_info())
fibonnaci.cache_clear()
print(fibonnaci(4))
print(fibonnaci.cache_info())
