class Plant:

    def __init__(self, name, height, age):
        self.name = name.capitalize()
        self.height = height
        self.age = age


class Flower(Plant):

    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        print(f"{self.name} (Flower): {self.height}cm, "
              f"{self.age} days, {self.color} color")

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):

    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        print(f"{self.name} (Tree): {self.height}cm, "
              f"{self.age} days, {self.trunk_diameter}cm diameter")

    def produce_shade(self):
        radius = self.trunk_diameter / 10
        shade_area = int(3.14 * (radius ** 2))
        print(f"{self.name} provides {shade_area} square meters of shade")


class Vegetable(Plant):

    def __init__(self, name, height, age, harvest_season,
                 nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        print(f"{self.name} (Vegetable): {self.height}cm, "
              f"{self.age} days, {self.harvest_season} harvest")
        print(f"{self.name} is rich in {nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")

    rose = Flower("Rose", 25, 30, "red")
    rose.bloom()
    print()

    tulip = Flower("Tulip", 15, 14, "yellow")
    tulip.bloom()
    print()

    oak = Tree("Oak", 500, 1825, 50)
    oak.produce_shade()
    print()

    pine = Tree("Pine", 800, 3650, 40)
    pine.produce_shade()
    print()

    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    print()

    carrot = Vegetable("Carrot", 10, 60, "fall", "vitamin A")
