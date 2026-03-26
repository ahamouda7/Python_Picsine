import math


class InvalidSyntax(Exception):
    pass


def length(user_input: list) -> int:
    len = 0
    for i in user_input:
        len += 1
    print(len)
    return len


def get_player_pos() -> tuple:
    error = 1
    while error == 1:
        try:
            user_input = tuple(input("Enter new coordinates as floats "
                                     "in format 'x,y,z': ").split(","))
            if length(user_input) != 3:
                raise InvalidSyntax()
            cord_list = []
            for cord in user_input:
                cord_list.append(float(cord.strip()))
            coordinates = tuple(cord_list)
            error = 0
        except ValueError:
            for cord in user_input:
                try:
                    float(cord)
                except ValueError:
                    print(f"Error on parameter '{cord}': "
                          "could not convert string to float: '{cord}'")
                    error = 1
                    break
        except InvalidSyntax:
            print("Invalid syntax")
    return coordinates


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print()

    coordinates = get_player_pos()
    print("Get a first set of coordinates")
    print(f"Got a first tuple: {coordinates}")
    print(f"It includes: X={coordinates[0]}, "
          f"Y={coordinates[1]}, Z={coordinates[2]}")
    print(f"Distance to center: {round(math.sqrt(
        coordinates[0] ** 2
        + coordinates[1] ** 2
        + coordinates[2] ** 2), 4)}")
    print()

    print("Get a second set of coordinates")
    coordinates_2 = get_player_pos()
    print(f"Distance to center: {round(math.sqrt(
        (coordinates_2[0] - coordinates[0]) ** 2
        + (coordinates_2[1] - coordinates[1]) ** 2
        + (coordinates_2[2] - coordinates[2]) ** 2), 4)}")
