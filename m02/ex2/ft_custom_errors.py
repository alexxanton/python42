class GardenError(Exception):
    def __init__(self, message="Gargen Error"):
        Exception.__init__(self, message)


class PlantError(GardenError):
    def __init__(self, message="Plant Error"):
        Exception.__init__(self, message)


class WaterError(GardenError):
    def __init__(self, message):
        Exception.__init__(message)

def test_custom_exceptions():
    print("=== Custom Garden Errors Demo ===")

    try:
        raise PlantError
    except PlantError(""):
        print()

test_custom_exceptions()
