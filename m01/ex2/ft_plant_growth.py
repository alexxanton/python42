class Plant:
    def __init__(self, name, height, days):
        self.start_height = height
        self.name = name
        self.height = height
        self.days = days

    def grow(self):
        self.height += 1

    def age(self):
        self.days += 1

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.days} days old")
        if self.start_height < self.height:
            print(f"Growth this week: +{plant.height - plant.start_height}cm")

if __name__ == "__main__":
    plant = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    plant.get_info()
    for x in range(6):
        plant.grow()
        plant.age()
    print("=== Day 7 ===")
    plant.get_info()
