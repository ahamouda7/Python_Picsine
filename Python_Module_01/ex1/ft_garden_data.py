class Plant:
    plants = []
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        Plant.plants.append(self)

print("=== Garden Plant Registry ===")


rose = Plant("rose", 25, 30)
sunflower = Plant("sunflower", 80, 45)
cactus = Plant("cactus", 15, 120)

# plants = [rose, sunflower, cactus]

if __name__ == "__main__":
    for plant in Plant.plants:
        print(f"{plant.name}: {plant.height}cm, {plant.age} days old")