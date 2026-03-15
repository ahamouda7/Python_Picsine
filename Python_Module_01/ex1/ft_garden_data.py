class Plant:
    plants = []

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        Plant.plants.append(self)


rose = Plant("rose", 25, 30)
sunflower = Plant("sunflower", 80, 45)
cactus = Plant("cactus", 15, 120)

if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    for plant in Plant.plants:
        print(f"{plant.name}: {plant.height}cm, {plant.age} days old")
