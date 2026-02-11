class Plant:
    """Represents a plant with a name, height and age."""
    def __init__(self, name: str, height: int, days: int):
        self.name = name
        self.height = height
        self.days = days

    def get_info(self) -> None:
        """Prints the plant information."""
        print(f"Created: {self.name} ({self.height}cm, {self.days} days)")


def main() -> None:
    """
    Creates instances of the plant class within an array and displays the info.
    """
    count: int = 0
    plant_tuple: list[tuple[str, int, int]] = [
            ("Rose", 25, 30),
            ("Oak", 200, 365),
            ("Cactus", 5, 90),
            ("Sunflower", 80, 45),
            ("Fern", 15, 120)
            ]

    print("=== Plant Factory Output ===")
    plants: list[Plant] = [Plant(*plant) for plant in plant_tuple]
    for plant in plants:
        plant.get_info()
        count += 1
    print(f"\nTotal plants created: {count}")


if __name__ == "__main__":
    main()
