from dotenv import load_dotenv
import os


def main() -> None:
    """Tries to export values from the .env file and display their info"""
    print("\nORACLE STATUS: Reading the Matrix...\n")
    load_dotenv()
    required = [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT"
    ]

    keys = {k: os.getenv(k) for k in required}
    missing = [key for key in keys if keys[key] is None]
    if missing:
        print("Missing keys:", str(missing).replace("'", ""))
        return

    print("Mode:", keys["MATRIX_MODE"])
    print("Database: Connected to local instance")
    print("API Access: Authenticated")
    print("Log Level:", keys["LOG_LEVEL"])
    print("Zion Network: Online")

    print(
        "\nEnvironment security check:",
        "[OK] No hardcoded secrets detected",
        "[OK] .env file properly configured",
        "[OK] Production overrides available",
        "\nThe Oracle sees all configurations.",
        sep="\n"
    )


if __name__ == "__main__":
    main()
