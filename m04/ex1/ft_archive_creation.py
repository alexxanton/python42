def write_file(file: str, lines: list[str]) -> None:
    """Create a file and write into it"""
    print(f"Initializing new storage unit: {file}")
    with open(file, "w") as f:
        print("Storage unit created successfully...\n")
        print("Inscribing preservation data...")
        for line in lines:
            print(line)
            f.write(f"{line}\n")
    print("\nData inscription complete. Storage unit sealed.")
    print(f"Archive '{file}' ready for long-term preservation.")


def main() -> None:
    """Executes the function to open files"""
    lines = [
        "[ENTRY 001] New quantum algorithm discovered",
        "[ENTRY 002] Efficiency increased by 347%",
        "[ENTRY 003] Archived by Data Archivist trainee"
    ]
    print("=== CYBER ARCHIVES- PRESERVATION SYSTEM ===\n")
    write_file("new_discovery.txt", lines)


if __name__ == "__main__":
    main()
