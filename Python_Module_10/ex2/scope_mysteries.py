from collections.abc import Callable
from typing import Dict, Any


def mage_counter() -> Callable[[], int]:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    def wrapper(amount: int) -> int:
        nonlocal initial_power
        initial_power += amount
        return initial_power
    return wrapper


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def wrapper(item_name: str) -> str:
        return (f"{enchantment_type} {item_name}")
    return wrapper


def memory_vault() -> Dict[str, Callable[..., Any]]:
    vault = {}

    def store(key: str, value: Any) -> None:
        vault[key] = value

    def recall(key: str) -> Any:
        if key in vault:
            return vault[key]
        else:
            return "Memory not found"
    return {"store": store, "recall": recall}


def main() -> None:
    print("\nTesting mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    base = 100
    amount_1 = 20
    amount_2 = 30
    accumulator = spell_accumulator(base)
    print(f"Base {base}, add {amount_1}: {accumulator(amount_1)}")
    print(f"Base {base}, add {amount_2}: {accumulator(amount_2)}")

    print("\nTesting enchantment factory...")
    # Test 1
    factory = enchantment_factory("Flameling")
    print(factory("Sword"))
    # Test 2
    factory = enchantment_factory("Frozen")
    print(factory("Shield"))

    print("\nTesting memory vault...")
    vault = memory_vault()
    print("Store 'secret' = 42")
    vault["store"]("secret", 42)
    print(f"Recall 'secret': {vault['recall']('secret')}")
    # Test 1
    print(f"Recall 'unknown': {vault['recall']('unknown')}")


if __name__ == "__main__":
    main()
