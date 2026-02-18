def open_file(file: str) -> None:
    print(f"Accessing Storage Vault: {file}")
    try:
        with open(file, "r") as f:
            print("Connection established...\n")
            print("RECOVERED DATA:")
            print(f.read())
        print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found.")

def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    open_file("ancient_fragment.txt")


if __name__ == "__main__":
    main()
