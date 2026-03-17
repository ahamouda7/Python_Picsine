class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def garden_errors(which_error: str, age: int, days: int) -> None:
    if which_error == "Plant":
        try:
            if age > 3:
                raise PlantError("The tomato plant is wilting!")
            print("The tomato plant is fine.")
        except PlantError as e:
            print(f"Caught PlantError: {e}")
    elif which_error == "Water":
        try:
            if days > 2:
                raise WaterError("Not enough water in the tank!")
            print("Enough water, plant is fine.")
        except WaterError as e:
            print(f"Caught WaterError: {e}")
    else:
        try:
            if age > 3:
                raise PlantError("The tomato plant is wilting!")
        except GardenError as e:
            print(f"Caught a garden error: {e}")

        try:
            if days > 2:
                raise WaterError("Not enough water in the tank!")
        except GardenError as e:
            print(f"Caught a garden error: {e}")


def test_custom_errors() -> None:
    print("Testing PlantError...")
    garden_errors("Plant", 6, 3)
    print()

    print("Testing WaterError...")
    garden_errors("Water", 6, 3)
    print()

    print("Testing catching all garden errors...")
    garden_errors("all", 6, 3)


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")

    print()
    test_custom_errors()
    print()

    print("All custom error types work correctly!")
