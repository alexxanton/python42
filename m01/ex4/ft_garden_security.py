class SecurePlant:
    def __init__(self, name, height, age):
        self.name = name
        self.__height = height
        self.__age = age

    def __is_valid(self, value, operation) -> bool:
        if value < 0:
            print("\nInvalid operation attempted:",
                  f"{operation} {value}cm [REJECTED]")
            print(f"Security: Negative {operation} rejected")
            return False
        else:
            return True

    def get_height(self) -> None:
        return self.height

    def get_age(self) -> None:
        return self.age

    def set_height(self, value) -> None:
        if self.__is_valid(value, "height"):
            self.height = value
            print(f"Height updated: {self.height}cm [OK]")

    def set_age(self, value) -> None:
        if self.__is_valid(value, "age"):
            self.age = value
            print(f"Age updated: {self.age} days [OK]")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    p = SecurePlant("p", 1, 1)
    p.set_height(25)
    p.set_age(30)
    p.set_height(-5)
