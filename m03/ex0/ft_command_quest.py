import sys


def main() -> None:
    """Prints the program name and its arguments"""
    count: int = 1
    print("=== Command Quest ===")
    if len(sys.argv) == 1:
        print("No arguments provided!")
    print("Program name:", sys.argv[0])
    for arg in sys.argv[1:]:
        print(f"Argument {count}: {arg}")
        count += 1
    print("Total arguments:", count)


if __name__ == "__main__":
    main()
