class Plant:
    def __init__(self, name, height, days):
        self.name = name
        self.height = height
        self.days = days
        self.get_info()

    def get_info(self):
        print(f"Created: {self.name} ({self.height}cm, {self.days} days)")


def get_len(plant_tupple) -> int:
    count = 0
    for x in plant_tupple:
        count += 1
    return count


if __name__ == "__main__":
    plant_tupple = [
            ("Rose", 25, 30),
            ("Oak", 200, 365),
            ("Cactus", 5, 90),
            ("Sunflower", 80, 45),
            ("Fern", 15, 120)
            ]

    count: int = get_len(plant_tupple)
    plants = [None] * count
    print("=== Plant Factory Output ===")
    for x in range(count):
        plants[x] = Plant(*plant_tupple[x])
    print(f"\nTotal plants created: {count}")
