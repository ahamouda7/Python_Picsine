class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.agee = age

    def grow(self):
        self.height += 6

    def age(self):
        self.agee += 6

    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.agee} days old"


rose = Plant("rose", 25, 30)

if __name__ == "__main__":
    rose.name = rose.name.capitalize()
    print("=== Day 1 ===")
    print(rose.get_info())

    rose.grow()
    rose.age()

    print("=== Day 7 ===")
    print(rose.get_info())
