class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.__name = name
        self.__height = 0
        self.__age = 0

        print(f"Plant created: {self.__name}")

        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: int) -> None:
        if height >= 0:
            self.__height = height
            print(f"Height updated: {self.__height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected\n")

    def set_age(self, age: int) -> None:
        if age >= 0:
            self.__age = age
            print(f"Age updated: {self.__age} days [OK]\n")
        else:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected\n")

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 25, 30)
    rose.set_height(-5)
    print(f"Current plant: {rose._SecurePlant__name} "
          f"({rose.get_height()}cm, {rose.get_age()} days)")
