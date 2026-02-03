def ft_harvest_total():
    total = 0
    for x in [1, 2, 3]:
        total += int(input(f"Day {x} harvest: "))
    print(f"Total harvest: {total}")

ft_harvest_total()
