def water_plants(plant_list: list[str | None]) -> None:
    try:
        print("Opening watering system")
        for plant in plant_list:
            if not plant:
                raise ValueError
            print("Watering", plant)
    except ValueError:
        print("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    plants: list[str | None] = ["tomato", "lettuce", "carrots"]
    plants_with_error: list[str | None] = ["tomato", None]
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    water_plants(plants)
    print("Watering completed successfully!")
    print("\nTesting with error...")
    water_plants(plants_with_error)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
