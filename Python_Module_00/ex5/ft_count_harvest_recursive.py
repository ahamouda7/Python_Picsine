def ft_count_harvest_recursive():
    day = int(input("Days until harvest: "))
    def count_days(count = 1):
        if count > day:
            print("Harvest time!")
            return
        print(f"Day {count}")
        count_days(count + 1)
    count_days()

ft_count_harvest_recursive()