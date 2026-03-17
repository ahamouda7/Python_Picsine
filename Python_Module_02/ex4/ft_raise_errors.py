def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int, which_error: str) -> None:
    if which_error == "plant_name":
        try:
            if plant_name == "":
                raise ValueError("Plant name cannot be empty!")
            print(f"Plant '{plant_name}' is healthy!")
        except ValueError as e:
            print(f"Error: {e}")
    elif which_error == "water_level":
        try:
            if water_level < 1:
                raise ValueError(
                    f"Water level {water_level} is too low (min 1)"
                )
            if water_level > 10:
                raise ValueError(
                    f"Water level {water_level} is too high (max 10)"
                )
            print(f"Water level {water_level} is fine!")
        except ValueError as e:
            print(f"Error: {e}")
    else:
        try:
            if sunlight_hours < 2:
                raise ValueError(
                    f"Sunlight hours {sunlight_hours} is too low (min 2)"
                )
            if sunlight_hours > 12:
                raise ValueError(
                    f"Sunlight hours {sunlight_hours} is too high (max 12)"
                )
            print(f"Sunlight hours {sunlight_hours} is enough!")
        except ValueError as e:
            print(f"Error: {e}")


def test_plant_checks() -> None:
    print("Testing good values...")
    check_plant_health("tomato", 15, 0, "plant_name")
    print()

    print("Testing empty plant name...")
    check_plant_health("", 15, 0, "plant_name")
    print()

    print("Testing bad water level...")
    check_plant_health("tomato", 15, 0, "water_level")
    print()

    print("Testing bad sunlight hours...")
    check_plant_health("tomato", 15, 0, "sunlight_hours")


if __name__ == "__main__":
    print("=== Garden Plant Health Checker ===")

    print()
    test_plant_checks()
    print()

    print("All error raising tests completed!")
