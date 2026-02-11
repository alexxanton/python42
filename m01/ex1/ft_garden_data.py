class Plant:
    """Represents a plant with a name, height and age."""
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def print_info(self) -> None:
        """Prints the plant information."""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main() -> None:
    """Displays the plants' attributes."""
    print("=== Garden Plant Registry ===")
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    rose.print_info()
    sunflower.print_info()
    cactus.print_info()


if __name__ == "__main__":
    main()
