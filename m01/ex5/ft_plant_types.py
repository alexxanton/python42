class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self, info) -> None:
        print(f"{self.name} ({self.__class__.__name__}):",
              f"{self.height}cm, {self.age} days, {info}")


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!\n")

    def print_info(self) -> None:
        self.get_info(f"{self.color} color")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print("Oak provides 78 square meters of shade\n")

    def print_info(self) -> None:
        self.get_info(f"{self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def print_info(self) -> None:
        nutrition = f"{self.name} is rich in {self.nutritional_value}"
        info = f"{self.harvest_season} harvest\n{nutrition}\n"
        self.get_info(info)


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")
    rose = Flower("Rose", 10, 10, "red")
    rose.print_info()
    rose.bloom()
    orchid = Flower("Orchid", 10, 10, "pink")

    oak = Tree("Oak", 250, 200, 30)
    oak.print_info()
    oak.produce_shade()
    pine = Tree("Pine", 300, 600, 25)

    tomato = Vegetable("Tomato", 13, 15, "summer", "vitamin c")
    tomato.print_info()
