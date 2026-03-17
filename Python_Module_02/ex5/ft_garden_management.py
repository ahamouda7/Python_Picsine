class GardenError(Exception):
    pass


class PlantNotFound(GardenError):
    pass


class ValueError(GardenError):
    pass


class GardenManager:
    def __init__(self, name: str, water: int, sun: int) -> None:
        self.name = name
        self.water = water
        self.sun = sun

    def add_plant(self) -> None:
        self.check_plant_health("plant_name", 1)

    def water_plants(plant_list: list[str]) -> None:
        my_plants = ["tomato", "lettuce", "carrots"]
        try:
            i = 0
            while i < len(plant_list):
                j = 0
                while j < len(my_plants):
                    if plant_list[i] == my_plants[j]:
                        print(f"Watering {plant_list[i]} - success")
                        break
                    j += 1
                if j == len(my_plants):
                    raise PlantNotFound("Cannot water None - invalid plant!")
                i += 1
        except PlantNotFound as e:
            print(f"Error: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, which_error: str, days: int) -> None:
        if which_error == "plant_name":
            try:
                if self.name == "":
                    raise ValueError("Plant name cannot be empty!")
                print(f"Added {self.name} successfully")
            except ValueError as e:
                print(f"Error adding plant: {e}")

        elif which_error == "health":
            try:
                if self.water < 1:
                    raise ValueError(
                        f"Water level {self.water} is too low (min 1)"
                    )
                if self.water > 10:
                    raise ValueError(
                        f"Water level {self.water} is too high (max 10)"
                    )
            except ValueError as e:
                print(f"Error checking {self.name}: {e}")

            try:
                if self.sun < 2:
                    raise ValueError(
                        f"Sunlight hours {self.sun} is too low (min 2)"
                    )
                if self.sun > 12:
                    raise ValueError(
                        f"Sunlight hours {self.sun} is too high (max 12)"
                    )
                if self.water < 1 and self.sun > 10:
                    print(f"{self.name}: healthy "
                          f"(water: {self.water}, sun: {self.sun})")
            except ValueError as e:
                print(f"Error checking {self.name}: {e}")

        else:
            try:
                if days > 2:
                    raise GardenError("Not enough water in the tank!")
                print("Enough water, plant is fine.")
            except GardenError as e:
                print(f"Caught GardenError: {e}")
                print("System recovered and continuing...")


tomato = GardenManager("tomato", 5, 8)
lettuce = GardenManager("lettuce", 15, 8)
carrots = GardenManager("", 7, 8)


def test_garden_management() -> None:
    print("Adding plants to garden...")
    tomato.add_plant()
    lettuce.add_plant()
    carrots.add_plant()
    print()

    print("Watering plants...")
    print("Opening watering system")
    GardenManager.water_plants([tomato.name, lettuce.name])
    print()

    print("Checking plant health...")
    tomato.check_plant_health("health", 1)
    lettuce.check_plant_health("health", 1)
    print()

    print("Testing error recovery...")
    tomato.check_plant_health("tank_water", 3)


if __name__ == "__main__":
    print("=== Garden Management System ===")

    print()
    test_garden_management()
    print()

    print("Garden management system test complete!")
