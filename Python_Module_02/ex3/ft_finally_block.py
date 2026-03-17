class PlantNotFound(Exception):
    pass


def water_plants(plant_list: list[str]) -> None:
    my_plants = ["tomato", "lettuce", "carrots"]
    try:
        i = 0
        while i < len(plant_list):
            j = 0
            while j < len(my_plants):
                if plant_list[i] == my_plants[j]:
                    print(f"Watering {plant_list[i]}")
                    break
                j += 1
            if j == len(my_plants):
                raise PlantNotFound("Cannot water None - invalid plant!")
            i += 1
        print("Watering completed successfully!")
    except PlantNotFound as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    correct_plant_list = ["tomato", "lettuce", "carrots"]
    wrong_plant_list = ["tomato", "oak", "carrots"]

    print("Testing normal watering...")
    print("Opening watering system")
    water_plants(correct_plant_list)
    print()

    print("Testing with error...")
    print("Opening watering system")
    water_plants(wrong_plant_list)


if __name__ == "__main__":
    print("=== Garden Watering System ===")

    print()
    test_watering_system()
    print()

    print("Cleanup always happens, even with errors!")
