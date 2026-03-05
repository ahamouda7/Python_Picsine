
class Plant:

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

class Flower(Plant):

	def __init__(self, name, height, age, color):
		super().__init__(name, height, age)
		self.color = color

	# def bloom():


class Tree(Plant):

	def __init__(self, name, height, age, trunk_diameter):
		super().__init__(name, height, age)
		self.trunk_diameter = trunk_diameter

	# def produce_shade():


class Vegetable(Plant):

	def __init__(self, name, height, age, harvest_season, nutritional_value):
		super().__init__(name, height, age)
		self.harvest_season = harvest_season
		self.nutritional_value = nutritional_value


rose = Flower("rose", 25, 30, "red")

if __name__ = "__main__":
	print(rose.color)