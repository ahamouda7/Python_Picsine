from collections.abc import Callable
from typing import List


def spell1(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def spell2(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def is_it_safe(target: str, power: int) -> bool:
    friends = ["Arthur", "Merlin", "Gandalf"]
    return (power < 100) and (target not in friends)


def spell_combiner(
    spell1: Callable[[str, int], str],
    spell2: Callable[[str, int], str]
) -> Callable[[str, int], tuple[str, str]]:
    def wrapper(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return wrapper


def power_amplifier(
    base_spell: Callable[[str, int], str],
    multiplier: int
) -> Callable[[str, int], str]:
    def wrapper(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return wrapper


def conditional_caster(
    condition: Callable[[str, int], bool],
    spell: Callable[[str, int], str]
) -> Callable[[str, int], str]:
    def wrapper(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"
    return wrapper


def spell_sequence(
    spells: list[Callable[[str, int], str]]
) -> Callable[[str, int], List[str]]:
    def wrapper(target: str, power: int) -> List[str]:
        spells_list = []
        for s in spells:
            spells_list.append(s(target, power))
        return spells_list
    return wrapper


def main() -> None:
    print("\nTesting spell combiner...")
    spells = spell_combiner(spell1, spell2)
    print(f"Result: {spells('target', 29)}")

    print("\nTesting power amplifier...")
    new_spell = power_amplifier(spell1, 3)
    print(f"Result: {new_spell('target', 29)}")

    print("\nTesting conditional caster...")
    is_true = conditional_caster(is_it_safe, spell2)
    print(f"Result: {is_true('target', 100)}")

    print("\nTesting spell sequence...")
    sequence = spell_sequence([spell1, spell2])
    print(f"Result: {sequence('target', 29)}")


if __name__ == "__main__":
    main()
