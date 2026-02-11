class SecurePlant:
    """Represents a plant with a name, height and age."""
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.__height = height
        self.__age = age

    def __is_valid(self, value: int, operation: str) -> bool:
        """Checks if the operation is  valid."""
        if value < 0:
            print("\nInvalid operation attempted:",
                  f"{operation} {value}cm [REJECTED]")
            print(f"Security: Negative {operation} rejected")
            return False
        return True

    @property
    def height(self) -> int:
        """Get the height of the plant."""
        return self.__height

    @property
    def age(self) -> int:
        """Get the age of the plant."""
        return self.__age

    @height.setter
    def height(self, value: int) -> None:
        """Set the height of the plant."""
        if self.__is_valid(value, "height"):
            self.__height = value
            print(f"Height updated: {self.height}cm [OK]")

    @age.setter
    def age(self, value: int) -> None:
        """Set the age of the plant."""
        if self.__is_valid(value, "age"):
            self.__age = value
            print(f"Age updated: {self.age} days [OK]")


def main() -> None:
    """Tests if the encapsulation system works."""
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 25, 30)
    print(f"Plant created: {rose.name}")
    rose.height = 25
    rose.age = 30
    rose.height = -5
    print(f"\nCurrent plant: {rose.name} ({rose.height}cm, {rose.age} days)")


if __name__ == "__main__":
    main()
