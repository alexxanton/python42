def water_plants(plant_list: list[str | None]) -> None:
    """Simulates watering plants, and if there's no plant it raises an error"""
    try:
        print("Opening watering system")
        for plant in plant_list:
            if not plant:
                raise ValueError(f"Cannot water {plant} - invalid plant!")
            print("Watering", plant)
    except ValueError as e:
        print("Error:", e)
        raise
    finally:
        print("Closing watering system (cleanup)")


def execute_test(plant_list: list[str | None]) -> None:
    """Tries to execute the water_plants function"""
    try:
        water_plants(plant_list)
        print("Watering completed successfully!")
    except ValueError:
        print("\nCleanup always happens, even with errors!")


def test_watering_system() -> None:
    """Creates a list with plants and another with an empty plant to test"""
    plants: list[str | None] = ["tomato", "lettuce", "carrots"]
    plants_with_error: list[str | None] = ["tomato", None]
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    execute_test(plants)
    print("\nTesting with error...")
    execute_test(plants_with_error)


if __name__ == "__main__":
    test_watering_system()
