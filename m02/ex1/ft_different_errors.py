def garden_operations(error: str) -> None:
    """Tries all the exceptions"""
    if error == "ValueError":
        print("Testing ValueError...")
        int("abc")

    if error == "ZeroDivisionError":
        print("Testing ZeroDivisionError...")
        1 / 0

    if error == "FileNotFoundError":
        print("Testing FileNotFoundError...")
        f = open("missing.txt")
        f.close()

    if error == "KeyError":
        print("Testing KeyError...")
        dictionary = {}
        dictionary["missing_plant"]

    if error == "multiple":
        print("Testing multiple errors together...")
        int("abc")


def test_error_types() -> None:
    """Executes the garden operations to test the exceptions"""
    print("=== Garden Error Types Demo ===\n")
    try:
        garden_operations("ValueError")
    except ValueError as e:
        print(f"Caught ValueError: {e}\n")

    try:
        garden_operations("ZeroDivisionError")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}\n")

    try:
        garden_operations("FileNotFoundError")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}\n")

    try:
        garden_operations("KeyError")
    except KeyError as e:
        print(f"Caught KeyError: {e}\n")

    try:
        garden_operations("multiple")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!\n")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
