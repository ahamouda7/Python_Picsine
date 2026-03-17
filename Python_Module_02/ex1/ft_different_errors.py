def garden_operations() -> None:
    try:
        21 / 0
    except Exception:
        print("Caught an error, but program continues!")


def test_error_types() -> None:
    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    print()

    print("Testing ZeroDivisionError...")
    try:
        29 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    print()

    print("Testing FileNotFoundError...")
    try:
        open("missing.txt")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    print()

    print("Testing KeyError...")
    try:
        dic = {"rose": 25, "sunflower": 80, "cactus": 15}
        print(dic["oak"])
    except KeyError:
        print("Caught KeyError: Missing plant 'oak'")
    print()

    print("Testing multiple errors together...")
    garden_operations()


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")

    print()
    test_error_types()
    print()

    print("All error types tested successfully!")
