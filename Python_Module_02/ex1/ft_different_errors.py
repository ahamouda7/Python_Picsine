def garden_operations(which_error: str) -> None:
    if which_error == "Value":
        try:
            int("abc")
        except ValueError:
            print("Caught ValueError: invalid literal for int()")
    elif which_error == "ZeroDiv":
        try:
            29 / 0
        except ZeroDivisionError:
            print("Caught ZeroDivisionError: division by zero")
    elif which_error == "File":
        try:
            open("missing.txt")
        except FileNotFoundError:
            print("Caught FileNotFoundError: No such file 'missing.txt'")
    elif which_error == "Key":
        try:
            dic = {"rose": 25, "sunflower": 80, "cactus": 15}
            print(dic["oak"])
        except KeyError:
            print("Caught KeyError: Missing plant 'oak'")
    else:
        try:
            21 / 0
        except Exception:
            print("Caught an error, but program continues!")


def test_error_types() -> None:
    print("Testing ValueError...")
    garden_operations("Value")
    print()

    print("Testing ZeroDivisionError...")
    garden_operations("ZeroDiv")
    print()

    print("Testing FileNotFoundError...")
    garden_operations("File")
    print()

    print("Testing KeyError...")
    garden_operations("Key")
    print()

    print("Testing multiple errors together...")
    garden_operations("Multiple")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")

    print()
    test_error_types()
    print()

    print("All error types tested successfully!")
