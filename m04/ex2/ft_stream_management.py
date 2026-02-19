import sys


def ft_print(msg: str) -> None:
    """Prints a string to stdout"""
    sys.stdout.write(msg)
    sys.stdout.flush()


def ft_print_error(msg: str) -> None:
    """Prints a string to stderr"""
    sys.stderr.write(msg)
    sys.stderr.flush()


def ft_input(msg: str) -> str:
    """Gets a line from stdin"""
    ft_print(msg)
    for line in sys.stdin:
        if "\n" in line:
            break
    return line


def main() -> None:
    """Tests all the standard I/O streams functions"""
    ft_print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n\n")
    arch_id: str = ft_input("Input Stream active. Enter archivist ID: ")
    status: str = ft_input("Input Stream active. Enter status report: ")
    ft_print("\n")
    ft_print(f"[STANDARD] Archive status from {arch_id[:-1]}: {status[:-1]}\n")
    ft_print_error(
        "[ALERT] System diagnostic: Communication channels verified\n"
    )
    ft_print("[STANDARD] Data transmission complete\n")
    ft_print("\nThree-channel communication test successful.\n")


if __name__ == "__main__":
    main()
