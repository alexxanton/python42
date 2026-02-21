def open_file(file: str) -> None:
    """Attempts to read a file and print its contents"""
    print("Initiating secure vault access...")
    try:
        with open(file, "r") as f:
            print("Vault connection established with failsafe protocols\n")
            print("SECURE EXTRACTION:")
            print(f.read())
        print("\nSECURE PRESERVATION:")
    except FileNotFoundError:
        print("ERROR: Storage vault not found.")


def main() -> None:
    """Executes the function to open files"""
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    open_file("classified_data.txt")


if __name__ == "__main__":
    main()
