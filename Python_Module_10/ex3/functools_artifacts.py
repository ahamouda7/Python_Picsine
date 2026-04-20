from collections.abc import Callable
from typing import List, Dict, Any
import functools
import operator


def spell_reducer(spells: List[int], operation: str) -> int:
    if not spells:
        return 0

    ops = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }
    if operation not in ops:
        raise ValueError("Unknown operation")

    return functools.reduce(ops[operation], spells)


def partial_enchanter(
        base_enchantment: Callable[[int, str, str], str]
        ) -> Dict[str, Callable]:
    encantment1 = functools.partial(base_enchantment, power=50, element="Fire")
    encantment2 = functools.partial(base_enchantment, power=50, element="Ice")
    encantment3 = functools.partial(base_enchantment, power=50, element="Air")
    return {"Fire": encantment1, "Ice": encantment2, "Air": encantment3}


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 2) + memoized_fibonacci(n - 1)


@functools.singledispatch
def spell(spell: Any) -> str:
    return f"unknown spell type"


def spell_dispatcher() -> Callable[[Any], str]:
    pass


def spell(power: int, element: str, target: str) -> str:
    return f"Firing {element} at {target} with {power} power!"


def main() -> None:
    print("\nTesting spell reducer...")
    red = '\033[31m'
    reset = '\033[0m'
    spells = [10, 20, 30, 40]
    try:
        print(f"Sum: {spell_reducer(spells, "add")}")
        print(f"Product: {spell_reducer(spells, "multiply")}")
        print(f"Max: {spell_reducer(spells, "max")}")
    except ValueError as e:
        print(f"{red}ERROR:{reset}", e)
        return

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")


if __name__ == "__main__":
    main()
