def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> str:
    """Checks if the values are valid"""
    if not plant_name:
        raise ValueError("Plant name cannot be empty!")

    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")

    if sunlight_hours > 12:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is too high (max 12)"
        )
    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")

    return f"Plant '{plant_name}' is healthy!"


def execute_test(plant_name: str, water_level: int,
                 sunlight_hours: int) -> None:
    """Executes the checker and catches any exception that may occur"""
    try:
        result = check_plant_health(plant_name, water_level, sunlight_hours)
        print(result, "\n")
    except ValueError as e:
        print(f"Error: {e}\n")


def test_plant_checks() -> None:
    """Executes the tests"""
    print("=== Garden Plant Health Checker ===\n")
    print("Testing good values...")
    execute_test("tomato", 5, 5)
    print("Testing empty plant name...")
    execute_test("", 5, 5)
    print("Testing bad water level...")
    execute_test("potato", 15, 5)
    print("Testing bad sunlight hours...")
    execute_test("eggplant", 5, 0)
    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
