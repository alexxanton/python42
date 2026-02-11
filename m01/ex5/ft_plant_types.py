class Plant:
    """Represents a plant with a name, height and age."""
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self, info: str) -> None:
        """Prints the plant information."""
        print(f"{self.name} ({self.__class__.__name__}):",
              f"{self.height}cm, {self.age} days, {info}")


class Flower(Plant):
    """
    Represents a flower inheriting from plant and adds the color attribute.
    """
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """Simulates a flower blooming."""
        print(f"{self.name} is blooming beautifully!\n")

    def print_info(self) -> None:
        """Prints specific information about the flower."""
        self.get_info(f"{self.color} color")


class Tree(Plant):
    """
    Represents a tree inheriting from plant and adds the diameter attribute.
    """
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """Simulates a tree producing shade."""
        print("Oak provides 78 square meters of shade\n")

    def print_info(self) -> None:
        """Prints specific information about the tree."""
        self.get_info(f"{self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    """
    Represents a vegetable inheriting from plant and adds the harvest season
    and nutritonal values attributes.
    """
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def print_info(self) -> None:
        """Prints specific information about the vegetable."""
        nutrition = f"{self.name} is rich in {self.nutritional_value}"
        info = f"{self.harvest_season} harvest\n{nutrition}\n"
        self.get_info(info)


def main() -> None:
    """Tests the different classes and methods."""
    print("=== Garden Plant Types ===\n")
    rose = Flower("Rose", 10, 10, "red")
    rose.print_info()
    rose.bloom()
    orchid = Flower("Orchid", 10, 10, "pink")
    orchid.bloom()

    oak = Tree("Oak", 250, 200, 30)
    oak.print_info()
    oak.produce_shade()
    pine = Tree("Pine", 300, 600, 25)
    pine.produce_shade()

    tomato = Vegetable("Tomato", 13, 15, "summer", "vitamin c")
    tomato.print_info()
    potato = Vegetable("Potato", 7, 25, "summer", "vitamin c")
    potato.print_info()


if __name__ == "__main__":
    main()
