from typing import List


def light_spell_allowed_ingredients() -> List[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    # import inside function to avoid the circular import error
    from alchemy.grimoire.light_validator import validate_ingredients

    return (
        f"Spell recorded: {spell_name} ({validate_ingredients(ingredients)})"
        )
