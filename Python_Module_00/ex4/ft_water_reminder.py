def ft_water_reminder():
    check = int(input("Days since last watering: "))
    if check > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")

ft_water_reminder()