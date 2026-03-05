
class SecurePlant:
    def __init__(self, name, height, age):
        self._name = name
        self._height = 0
        self._age = 0

        print(f"Plant created: {self._name}")

        self.set_height(height)
        self.set_age(age)

    def set_height(self, height):
        if height >= 0:
            self._height = height
            print(f"Height updated: {self._height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected\n")

    def set_age(self, age):
        if age >= 0:
            self._age = age
            print(f"Age updated: {self._age} days [OK]\n")
        else:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected\n")

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 25, 30)
    rose.set_height(-5)
    print(f"Current plant: {rose._name} ({rose.get_height()}cm, {rose.get_age()} days)")
