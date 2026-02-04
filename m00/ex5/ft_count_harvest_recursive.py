def ft_count_harvest_recursive() -> None:
    def count(current, days) -> None:
        if current > days:
            print("Harvest time!")
            return
        print(f"Day {current}")
        count(current + 1, days)

    days = int(input("Days until harvest: "))
    count(1, days)

ft_count_harvest_recursive()
