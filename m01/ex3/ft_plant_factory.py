class Plant:
    def __init__(self, name: str, height: int, days: int):
        self.name = name
        self.height = height
        self.days = days
        self.get_info()

    def get_info(self) -> None:
        print(f"Created: {self.name} ({self.height}cm, {self.days} days)")


def get_len(plant_tuple: list[tuple[str, int, int]]) -> int:
    count = 0
    for x in plant_tuple:
        count += 1
    return count


if __name__ == "__main__":
    plant_tuple = [
            ("Rose", 25, 30),
            ("Oak", 200, 365),
            ("Cactus", 5, 90),
            ("Sunflower", 80, 45),
            ("Fern", 15, 120)
            ]

    count: int = get_len(plant_tuple)
    print("=== Plant Factory Output ===")
    plants: list[Plant] = [Plant(*plant) for plant in plant_tuple]
    print(f"\nTotal plants created: {count}")
