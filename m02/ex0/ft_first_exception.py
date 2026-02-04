def check_temperature(temp_str: str) -> int | None:
    try:
        temp: int = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None

    if temp > 40:
        print(f"Error: {temp_str}°C is too hot for plants (max 40°C)")
        return None
    if temp < 0:
        print(f"Error: {temp_str}°C is too cold for plants (min 0°C)")
        return None
    return temp


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===\n")
    for x in ["25", "abc", "100", "-50"]:
        print(f"Testing temperature: {x}")
        if check_temperature(x):
            print(f"Temperature {x}°C is perfect for plants!")
        print()
    print("All tests completed - program didn't crash!")

test_temperature_input()
