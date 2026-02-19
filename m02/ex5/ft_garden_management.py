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


class SunlightError(GardenError):
    """Exception for sunlight errors"""
    def __init__(self, message: str = "Sunlight Error") -> None:
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

    def check_plant_health(self, plant: tuple[str, int, int]) -> None:
        """Checks if the values are valid"""
        plant_name, water_level, sunlight_hours = plant
        if not plant_name:
            raise PlantError("Plant name cannot be empty!")

        if water_level > 10:
            raise WaterError(f"Water level {water_level} is too high (max 10)")
        if water_level < 1:
            raise WaterError(f"Water level {water_level} is too low (min 1)")

        if sunlight_hours > 12:
            raise SunlightError(
                f"Sunlight hours {sunlight_hours} is too high (max 12)"
            )
        if sunlight_hours < 2:
            raise SunlightError(
                f"Sunlight hours {sunlight_hours} is too low (min 2)"
            )

    def check_plants(self) -> None:
        """Checks the health of a plant, displays errors for invalid values"""
        print("\nChecking plant health...")
        for plant, water, sun in self.plants:
            try:
                self.check_plant_health((plant, water, sun))
                print(f"{plant}: healthy (water: {water}, sun: {sun})")
            except (PlantError, WaterError, SunlightError) as e:
                print(f"Error: {e}")

    def error_recovery(self) -> None:
        print("\nTesting error recovery...")
        try:
            raise GardenError("Not enough water in tank")
        except GardenError as e:
            print("Caught GardenError:", e)
        finally:
            print("System recovered and continuing...")


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
    manager.check_plants()
    manager.error_recovery()
    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
