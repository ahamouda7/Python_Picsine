class Plant:
    plants = []
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        Plant.plants.append(self)

def grow(self):
    self.height += 6

def age(self):
    self.age += 6

def get_info(self):
    return f"{self.name}: {self.height}cm, {self.age} days old"

rose = Plant("rose", 25, 30)
sunflower = Plant("sunflower", 80, 45)
cactus = Plant("cactus", 15, 120)

i = 1
if __name__ == "__main__":
    for plant in Plant.plants:
        plant.name = plant.name.capitalize()
        print(f"Plant {i}:")
        print("=== Day 1 ===")
        print(get_info(plant))
        grow(plant)
        age(plant)
        print("=== Day 7 ===")
        print(get_info(plant))
        print()
        i += 1

