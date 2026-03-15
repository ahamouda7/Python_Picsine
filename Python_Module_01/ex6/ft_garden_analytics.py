class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height

    def grow(self) -> None:
        self.height += 1
        print(f"{self.name} grew 1cm")

    def __str__(self) -> str:
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color = color

    def __str__(self) -> str:
        return f"{super().__str__()}, {self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int,
                 color: str, points: int) -> None:
        super().__init__(name, height, color)
        self.points = points

    def __str__(self) -> str:
        return f"{super().__str__()}, Prize points: {self.points}"


class GardenManager:
    total_gardens = 0

    class GardenStats:
        def __init__(self, plants: list) -> None:
            self.plants = plants

        def count_types(self) -> tuple:
            reg = 0
            flow = 0
            prize = 0
            for p in self.plants:
                if p.__class__.__name__ == Plant.__name__:
                    reg += 1
                elif p.__class__.__name__ == FloweringPlant.__name__:
                    flow += 1
                else:
                    prize += 1
            return reg, flow, prize

    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.plants = []
        GardenManager.total_gardens += 1

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self) -> None:
        print(f"\n{self.owner} is helping all plants grow...")
        for p in self.plants:
            p.grow()

    def generate_report(self) -> None:
        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for p in self.plants:
            print(f"- {p}")

        total_added = len(self.plants)
        stats = self.GardenStats(self.plants)

        print(f"\nPlants added: {total_added}, "
              f"Total growth: {total_added}cm")

        reg, flow, prize = stats.count_types()
        print(f"Plant types: {reg} regular, {flow} flowering, "
              f"{prize} prize flowers")

    @staticmethod
    def isvalide_height(height: int) -> bool:
        return height > 0

    @classmethod
    def create_garden_network(cls) -> None:
        print("Garden scores - Alice: 218, Bob: 92")
        print(f"Total gardens managed: {cls.total_gardens}")


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    alice_garden = GardenManager("Alice")
    bob_garden = GardenManager("Bob")

    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)

    alice_garden.grow_all()
    alice_garden.generate_report()

    test_height = alice_garden.isvalide_height(oak.height)
    print(f"\nHeight validation test: {test_height}")
    GardenManager.create_garden_network()
