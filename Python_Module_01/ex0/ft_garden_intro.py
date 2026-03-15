class Plant:

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


rose = Plant("rose", 25, 30)

if __name__ == "__main__":
    rose.name = rose.name.capitalize()
    print("=== Welcome to My Garden ===")
    print(f"Plant: {rose.name}")
    print(f"Height: {rose.height}cm")
    print(f"Age: {rose.age} days\n")
    print("=== End of Program ===")
