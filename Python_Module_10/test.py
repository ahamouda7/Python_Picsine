# Test 1:

# import functools
# import operator

# @functools.lru_cache(maxsize=None)
# def fibonnaci(n):
#     if n <= 1:
#         return n

#     return fibonnaci(n - 2) + fibonnaci(n - 1)

# print(fibonnaci(5))
# print(fibonnaci.cache_info())
# fibonnaci.cache_clear()
# print(fibonnaci(4))
# print(fibonnaci.cache_info())

# # print(functools.reduce(operator.add, [1, 2, 3, 4]))


# Test 2:

import functools
from collections.abc import Callable

def echo_magic(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        
        # Let the real function do its work
        original_output = func(*args, **kwargs)
        
        # The wrapper mutates the result!
        return f"{original_output} ... {original_output} ... (echo)"
    def wrapper1(*args, **kwargs):
        
        # Let the real function do its work
        original_output = func(*args, **kwargs)
        
        # The wrapper mutates the result!
        return f"... {original_output} ... (echo)"
        
    return wrapper1

@echo_magic
def shout_spell(word: str) -> str:
    return f"Force Push: {word}!"

# We call the spell, but the decorator intercepts and modifies the return value
# a = echo_magic(shout_spell)
print(shout_spell("AWAY"))

# OUTPUT:
# Force Push: AWAY! ... Force Push: AWAY! ... (echo)
