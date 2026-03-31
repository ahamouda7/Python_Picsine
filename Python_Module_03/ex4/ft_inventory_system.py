import sys


def my_item(item: str) -> str:
    i = 0
    name = ""
    while i < len(item) and item[i] != ':':
        name += item[i]
        i += 1
    return name


def item_value(item: str) -> str:
    i = 0
    value = ""
    while i < len(item) and item[i] != ':':
        i += 1
    i += 1
    while i < len(item):
        value += item[i]
        i += 1
    return value


def isnumber(item: str) -> int:
    i = 0
    while i < len(item):
        if item[i] < '0' or item[i] > '9':
            return 0
        i += 1
    return 1


def isvalid(item: str, my_list: list[str]) -> int:
    i = 0
    if my_item(item) in my_list:
        return 2
    if item == my_item(item) or item == my_item(item) + ':':
        return 0
    while i < len(item) - 1:
        if item[i] == ':' and isnumber(item[(i + 1):]) == 0:
            return -1
        i += 1
    return 1


def valid_list() -> dict[str, str]:
    i = 1
    my_list: list[str] = []
    dictionary = {}
    while i < len(sys.argv):
        name = my_item(sys.argv[i])
        value = item_value(sys.argv[i])
        if isvalid(sys.argv[i], my_list) == 0:
            print(f"Error - invalid parameter '{sys.argv[i]}'")
        elif isvalid(sys.argv[i], my_list) == 2:
            print(f"Redundant item '{name}' - discarding")
        elif isvalid(sys.argv[i], my_list) == -1:
            print(f"Quantity error for '{name}': "
                  f"invalid literal for int() with base 10: '{value}'")
        else:
            dictionary[name] = value
            my_list.append(name)
        i += 1
    print(f"Got inventory: {dictionary}")
    print(f"Item list: {my_list}")
    return dictionary


def maxindex(dictionary: dict[str, str]) -> int:
    values = list(dictionary.values())
    ma = 0
    i = 1
    while i < len(dictionary):
        if int(values[i]) > int(values[ma]):
            ma = i
        i += 1
    return ma


def minindex(dictionary: dict[str, str]) -> int:
    values = list(dictionary.values())
    mi = 0
    i = 1
    while i < len(dictionary):
        if int(values[i]) < int(values[mi]):
            mi = i
        i += 1
    return mi


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    dictionary = valid_list()
    if len(dictionary) > 0:
        keys = list(dictionary.keys())
        values = list(dictionary.values())
        somme = 0
        for count in dictionary.values():
            somme += int(count)
        print(f"Total quantity of the {len(dictionary.keys())} items: {somme}")
        for k in dictionary.keys():
            v = int(dictionary[k])
            p = (v * 100) / somme
            print(f"Item {k} represents {round(p, 1)}%")
        ma = maxindex(dictionary)
        mi = minindex(dictionary)
        print(f"Item most abundant: {keys[ma]} with quantity {values[ma]}")
        print(f"Item most abundant: {keys[mi]} with quantity {values[mi]}")
    dictionary.update({"magic_item": "1"})
    print(f"Updated inventory: {dictionary}")
