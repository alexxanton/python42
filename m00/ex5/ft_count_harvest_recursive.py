def ft_count_harvest_recursive() -> None:
    def count(current: int, days: int) -> None:
        if current > days:
            print("Harvest time!")
            return
        print(f"Day {current}")
        count(current + 1, days)

    days: int = int(input("Days until harvest: "))
    count(1, days)

ft_count_harvest_recursive()
