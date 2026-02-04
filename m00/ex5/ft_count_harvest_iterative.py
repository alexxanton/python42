def ft_count_harvest_iterative() -> None:
    days: int = int(input("Days until harvest: "))
    for x in range(days):
        print(f"Day {x + 1}")
    print("Harvest time!")

ft_count_harvest_iterative()
