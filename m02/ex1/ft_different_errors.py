def garden_operations() -> None:
    try:
        print("Testing ValueError...")
        int("abc")
    except ValueError as e:
        print("Caught ValueError:", e, end="\n\n")

    try:
        print("Testing ZeroDivisionError...")
        1 / 0
    except ZeroDivisionError as e:
        print("Caught ZeroDivisionError:", e, end="\n\n")

    try:
        print("Testing FileNotFoundError...")
        f = open("missing.txt")
        f.close()
    except FileNotFoundError as e:
        print("Caught FileNotFoundError:", e, end="\n\n")

    try:
        print("Testing KeyError...")
        dictionary = {}
        dictionary["missing_plant"]
    except KeyError as e:
        print("Caught KeyError:", e, end="\n\n")

    try:
        print("Testing multiple errors together...")
        int("abc")
    except (ZeroDivisionError, ValueError):
        print("Caught an error, but program continues!\n")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("All error types tested successfully!")

test_error_types()
