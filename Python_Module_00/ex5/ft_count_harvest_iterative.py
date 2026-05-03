def ft_count_harvest_iterative() -> None:
    day = int(input("Days until harvest: "))
    count = 1
    while (count <= day):
        print(f"Day {count}")
        count += 1
    print("Harvest time!")
