class Plant:
    """Represents a plant with a name, height and age."""
    def __init__(self, name: str, height: int, days: int):
        self.start_height = height
        self.name = name
        self.height = height
        self.days = days

    def grow(self) -> None:
        """Makes the plant grow."""
        self.height += 1

    def age(self) -> None:
        """Makes the plant age."""
        self.days += 1

    def get_info(self) -> None:
        """Prints the plant information and checks if the plant has grown."""
        print(f"{self.name}: {self.height}cm, {self.days} days old")
        if self.start_height < self.height:
            print(f"Growth this week: +{self.height - self.start_height}cm")


def main() -> None:
    """Initializes a plant class and makes it grow over a simulated week."""
    plant = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    plant.get_info()
    for x in range(6):
        plant.grow()
        plant.age()
    print("=== Day 7 ===")
    plant.get_info()


if __name__ == "__main__":
    main()
