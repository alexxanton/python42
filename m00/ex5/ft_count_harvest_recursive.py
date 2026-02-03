def ft_count_harvest_recursive():
    def count(days, n):
        if n == 0:
            return
        print(n)
        count(days, n - 1)

    days = int(input("Days until harvest: "))
    count(days, days)

ft_count_harvest_recursive()
