class GardenError(Exception):
    """Exception for general garden errors"""
    def __init__(self, message: str = "Gargen Error") -> None:
        Exception.__init__(self, message)


class PlantError(GardenError):
    """Exception for plant errors"""
    def __init__(self, message: str = "Plant Error") -> None:
        GardenError.__init__(self, message)


class WaterError(GardenError):
    """Exception for watering errors"""
    def __init__(self, message: str = "Water Error") -> None:
        GardenError.__init__(self, message)


class GardenManager:
    """Contains the plants and methods to take care of them"""
    def __init__(self) -> None:
        self.plants: list[tuple[str, int, int]] = []

    def add_plants(self, plants: list[tuple[str, int, int]]) -> None:
        """Adds plants to the plant list by checking if they're valid"""
        print("Adding plants to garden...")
        for plant in plants:
            try:
                if not plant[0]:
                    raise PlantError("Plant name cannot be empty!")
                self.plants.append(plant)
                print(f"Added {plant[0]} successfully")
            except PlantError as e:
                print(f"Error adding plant: {e}")

    def water_plants(self) -> None:
        """Simulates watering plants and handles errors"""
        print("\nWatering plants...")
        print("Opening watering system")
        try:
            for plant in self.plants:
                if not plant[0]:
                    raise WaterError("Can't water None")
                print(f"Watering {plant[0]} - success")
        except WaterError as e:
            print(f"Error adding plant: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plants_health(self) -> None:
        """Checks the health of a plant, displays errors for invalid values"""
        print("\nChecking plant health...")
        for plant, water, sun in self.plants:
            try:
                print(f"{plant}: healthy (water: {water}, sun: {sun})")
            except PlantError as e:
                print(f"Error adding plant: {e}")


def test_garden_management() -> None:
    plants = [
        ("tomato", 5, 8),
        ("lettuce", 15, 8),
        ("", 0, 0)
    ]
    print("=== Garden Management System ===\n")
    manager = GardenManager()
    manager.add_plants(plants)
    manager.water_plants()
    manager.check_plants_health()
    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
