class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def print_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    rose = Plant("rose", 25, 30)
    sunflower = Plant("sunflower", 80, 45)
    cactus = Plant("cactus", 15, 120)
    rose.print_info()
    sunflower.print_info()
    cactus.print_info()
