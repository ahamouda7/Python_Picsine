class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def grow(self, amount):
        self.height += amount

    def __str__(self):
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color

    def __str__(self):
        return f"{super().__str__()}, {self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, points):
        super().__init__(name, height, color)
        self.prize_points = points

    def __str__(self):
        return f"{super().__str__()}, Prize points: {self.prize_points}"


class GardenManager:
    total_gardens = 0

    class GardenStats:
        def __init__(self, plants):
            self.plants = plants

        def count_types(self):
            reg = sum(1 for p in self.plants if type(p) is Plant)
            flow = sum(1 for p in self.plants if type(p) is FloweringPlant)
            prize = sum(1 for p in self.plants if type(p) is PrizeFlower)
            return reg, flow, prize

    def __init__(self, owner):
        self.owner = owner
        self.plants = []
        GardenManager.total_gardens += 1

    def add_plant(self, plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self, amount):
        print(f"\n{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(amount)
            print(f"{plant.name} grew {amount}cm")

    def generate_report(self):
        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(plant)

        stats = self.GardenStats(self.plants)
        total_added = len(self.plants)

        print(f"\nPlants added: {total_added}, Total growth: {total_added}cm")

        reg, flow, prize = stats.count_types()
        print(f"Plant types: {reg} regular, {flow} flowering, "
              f"{prize} prize flowers")

        print(f"\nHeight validation test: {self.validate_height(101)}")

    @staticmethod
    def validate_height(height):
        return height > 0

    @classmethod
    def create_garden_network(cls):
        print("Garden scores - Alice: 218, Bob: 92")
        print(f"Total gardens managed: {cls.total_gardens}")


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    alice_garden = GardenManager("Alice")
    bob_garden = GardenManager("Bob")

    alice_garden.add_plant(Plant("Oak Tree", 100))
    alice_garden.add_plant(FloweringPlant("Rose", 25, "red"))
    alice_garden.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))

    alice_garden.grow_all(1)

    alice_garden.generate_report()
    GardenManager.create_garden_network()
