
class Plant:
    plants = []

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        Plant.plants.append(self)


rose = Plant("rose", 25, 30)
oak = Plant("oak", 200, 365)
cactus = Plant("cactus", 5, 90)
sunflower = Plant("sunflower", 80, 45)
fern = Plant("fern", 15, 120)

count = 0
if __name__ == "__main__":
    print("=== Plant Factory Output ===")

    for plant in Plant.plants:
        plant.name = plant.name.capitalize()
        print(f"Created: {plant.name} ({plant.height}cm, {plant.age} days)")
        count += 1

    print(f"\nTotal plants created: {count}")
