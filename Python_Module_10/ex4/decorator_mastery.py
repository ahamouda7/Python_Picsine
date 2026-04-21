from collections.abc import Callable
from typing import Any
import functools
import time


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")

        start = time.time()
        original_output = func(*args, **kwargs)
        end = time.time()
        duration = end - start
        print(f"Spell completed in {duration:.3f} seconds")

        return original_output
    return wrapper


def power_validator(min_power: int) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for arg in args:
                if isinstance(arg, int):
                    power = arg
            if power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            red = '\033[31m'
            yellow = '\033[93m'
            reset = '\033[0m'
            for n in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if n < max_attempts:
                        print(
                            f" {yellow}Warning:{reset} Spell failed, "
                            f"retrying... (attempt {n}/{max_attempts})"
                            )
            return (
                f" {red}Error:{reset} Spell casting failed "
                f"after {max_attempts} attempts"
                )
        return wrapper
    return decorator


@spell_timer
def fireball() -> str:
    time.sleep(0.1)
    return "Result: Fireball cast!"


@power_validator(min_power=10)
def is_valid_power(power: str, target: int) -> str:
    return f"{target} has a good power level ({power})"


@retry_spell(max_attempts=3)
def spell(power: int) -> str:
    int(power)
    green = '\033[32m'
    reset = '\033[0m'
    return f" {green}Success!{reset} The spell finally worked!"


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if (len(name) >= 3) and (name.replace(" ", "").isalpha()):
            return True
        return False

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    print("\nTesting spell timer...")
    print(fireball())

    print("\nTesting power validator...")
    red = '\033[31m'
    reset = '\033[0m'
    print(is_valid_power(20, "Fireball"))
    print(f" {red}Error:{reset}", is_valid_power(9, "Fireball"))

    print("\nTesting retrying spell...")
    print("Test 1: Valid power")
    print(spell(29))
    print("Test 2: Invalid power")
    print(spell("power"))

    print("\nTesting MageGuild...")
    mage = MageGuild()
    print(mage.validate_mage_name("Mage"))
    print(mage.validate_mage_name("Mage 29"))
    print(mage.cast_spell("Lightning", 15))
    print(mage.cast_spell("Fireball", 5))


if __name__ == "__main__":
    main()
