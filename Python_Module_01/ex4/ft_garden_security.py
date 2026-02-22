class SecurePlant:
    plant = []
    def __init__(self, name, height, age):
        self._name = name
        print(f"Plant created: {self._name}")
        self._height = self.set_height(height)
        self._age = self.set_age(age)
        SecurePlant.plant.append(self)

    def set_height(self, height):
        if height >= 0:
            self._height = height
            print(f"Height updated: {self._height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, age):
        if age >= 0:
            self._age = age
            print(f"Age updated: {self._age} days [OK]")
        else:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age


if __name__ == "__main__":
    # Matches the required output format exactly [cite: 225]
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 25, 30)
    p = SecurePlant.plant[-1]
    print()
    p.set_height(-5)
    print()
    print(f"Current plant: {p._name} ({p.get_height()}cm, {p.get_age()} days)")