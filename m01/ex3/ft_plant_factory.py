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

