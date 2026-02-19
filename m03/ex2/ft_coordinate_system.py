import math


type Position = tuple[int, int, int]


def parse(pos: str) -> Position | None:
    """Parses the position string to get the coordinates"""
    try:
        parsed_pos = tuple([int(x) for x in pos.split(",")])
        return parsed_pos
    except ValueError as e:
        print("Error parsing coordinates:", e)
        print(f'Error details - Type: ValueError, Args: ("{e}")\n')
        return None


def calculate_distance(pos: Position, pos2: Position) -> float:
    """Gets the distance between two 3d objects"""
    x1, y1, z1 = pos
    x2, y2, z2 = pos2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)


def test_distance(pos: Position) -> None:
    """Executes the distance calculator and prints the output"""
    pos2 = (0, 0, 0)
    res = calculate_distance(pos, pos2)
    format_str = f"{res:.2f}" if res != int(res) else f"{res:.1f}"
    print(f"Distance between {pos2} and {pos}: {format_str}\n")


def simple_test(msg: str, pos: Position) -> None:
    """Executes a distance test without parsing"""
    print(msg, pos)
    test_distance(pos)


def parse_test(msg: str, pos_str: str) -> None:
    """Executes a distance test with parsing"""
    print(msg, f'"{pos_str}"')
    pos = parse(pos_str)

    if pos:
        print("Parsed position:", pos)
        test_distance(pos)


def unpacking_demo() -> None:
    """Demonstrates tuple unpacking"""
    packed = (3, 4, 0)
    x, y, z = packed
    print("Unpacking demonstration:")
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


def main() -> None:
    """Executes the tests and demonstrations"""
    print("=== Game Coordinate System ===\n")
    simple_test("Position created:", (10, 20, 5))
    parse_test("Parsing coordinates:", "3,4,0")
    parse_test("Parsing invalid coordinates:", "abc,def,ghi")
    unpacking_demo()


if __name__ == "__main__":
    main()
