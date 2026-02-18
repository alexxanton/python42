class GardenError(Exception):
    """Exception for general garden errors"""
    def __init__(self, message: str = "Gargen Error"):
        Exception.__init__(self, message)


class PlantError(GardenError):
    """Exception for plant errors"""
    def __init__(self, message: str = "Plant Error"):
        GardenError.__init__(self, message)


class WaterError(GardenError):
    """Exception for watering errors"""
    def __init__(self, message: str = "Water Error"):
        GardenError.__init__(self, message)


def test_custom_exceptions() -> None:
    """Tests the custom exceptions"""
    print("=== Custom Garden Errors Demo ===\n")

    try:
        print("Testing PlantError...")
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print("Caught PlantError:", e)
        print()

    try:
        print("Testing WaterError...")
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print("Caught WaterError:", e)
        print()

    try:
        print("Testing catching all garden errors...")
        raise GardenError("The tomato plant is wilting!")
    except GardenError as e:
        print("Caught a garden error:", e)

    try:
        raise GardenError("Not enough water in the tank!")
    except GardenError as e:
        print("Caught a garden error:", e)
        print()

    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_exceptions()
