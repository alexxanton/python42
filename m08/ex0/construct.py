import os
import sys
import site


def display_warning() -> None:
    """Display a warning if the venv wasn't found"""
    print(
        "\nWARNING: You're in the global environment!",
        "The machines can see everything you install.\n",
        "To enter the construct, run:",
        "python -m venv matrix_env",
        "source matrix_env/bin/activate # On Unix",
        "matrix_env",
        "Scripts",
        "activate   # On Windows\n",
        "Then run this program again.",
        sep="\n"
    )


def display_success_msg() -> None:
    """Display a success message if the venv was found"""
    print(
        "\nSUCCESS: You're in an isolated environment!",
        "Safe to install packages without affecting",
        "the global system.",
        sep="\n"
    )


def main() -> None:
    """Checks if a virtual environment is active and displays info"""
    base_prefix = (
        getattr(sys, "base_prefix", None) or
        getattr(sys, "real_prefix", None) or
        sys.prefix
    )
    active = sys.prefix != base_prefix
    print("\nMATRIX STATUS:",
          "Welcome to the construct" if active else "You're still plugged in")
    print("\nCurrent Python:", sys.executable)
    venv_path = sys.prefix
    print("Virtual Environment:",
          os.path.basename(venv_path) if active else "None detected")
    if not active:
        display_warning()
        return
    print("Environment Path:", venv_path)
    display_success_msg()
    print("\nPackage installation path:", site.getsitepackages()[0])


if __name__ == "__main__":
    main()
