class Plant:
    plants: list['Plant'] = []

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.agee = age
        Plant.plants.append(self)

    def grow(self) -> None:
        self.height += 6

    def age(self) -> None:
        self.agee += 6

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.agee} days old"


rose = Plant("rose", 25, 30)
sunflower = Plant("sunflower", 80, 45)
cactus = Plant("cactus", 15, 120)

if __name__ == "__main__":
    i = 1
    for p in Plant.plants:
        if i > 1:
            print()
        print(f"Plant [{i}]:")
        print("=== Day 1 ===")
        p.name = p.name.capitalize()
        print(p.get_info())

        p.grow()
        p.age()

        print("=== Day 7 ===")
        print(p.get_info())
        i += 1
