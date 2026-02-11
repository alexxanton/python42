class SecurePlant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.__height = height
        self.__age = age

    def __is_valid(self, value: int, operation: str) -> bool:
        if value < 0:
            print("\nInvalid operation attempted:",
                  f"{operation} {value}cm [REJECTED]")
            print(f"Security: Negative {operation} rejected")
            return False
        else:
            return True

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age

    def set_height(self, value: int) -> None:
        if self.__is_valid(value, "height"):
            self.height = value
            print(f"Height updated: {self.height}cm [OK]")

    def set_age(self, value: int) -> None:
        if self.__is_valid(value, "age"):
            self.age = value
            print(f"Age updated: {self.age} days [OK]")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    p = SecurePlant("p", 1, 1)
    p.set_height(25)
    p.set_age(30)
    p.set_height(-5)
