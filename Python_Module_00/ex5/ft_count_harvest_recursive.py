
def ft_count_harvest_recursive() -> None:
    day = int(input("Days until harvest: "))

    def count_days(count: int = 1) -> None:
        if count > day:
            print("Harvest time!")
            return
        print(f"Day {count}")
        count_days(count + 1)

    count_days()
