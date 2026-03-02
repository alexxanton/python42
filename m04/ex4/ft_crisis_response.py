def open_file(file: str, msg: str) -> None:
    """Attempts to read a file's content with secure meassures"""
    status = "Normal operations resumed"
    print(f"{msg}: Attempting access to '{file}'...")
    try:
        with open(file, "r") as f:
            print(f"SUCCESS: Archive recovered - ``{f.read()}''")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        status = "Crisis handled, system stable"
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        status = "Crisis handled, security maintained"
    finally:
        print(f"STATUS: {status}\n")


def main() -> None:
    """Executes the different tests"""
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    open_file("lost_archive.txt", "CRISIS ALERT")
    open_file("classified_vault.txt", "CRISIS ALERT")
    open_file("standard_archive.txt", "ROUTINE ACCESS")
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
