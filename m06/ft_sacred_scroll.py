import alchemy


def test_package_access(func_name: str):
    try:
        func = getattr(alchemy, func_name)
        result = func()
        print(f"alchemy.{func_name}():", result)
    except AttributeError as e:
        print(f"alchemy.{func_name}():", e)


def main() -> None:
    """Test importing from module access and package-level"""
    print("\n=== Sacred Scroll Mastery ===\n")
    print("Testing direct module access:")
    print("alchemy.elements.create_fire():", alchemy.elements.create_fire())
    print("alchemy.elements.create_water():", alchemy.elements.create_water())
    print("alchemy.elements.create_earth():", alchemy.elements.create_earth())
    print("alchemy.elements.create_air():", alchemy.elements.create_air())

    print("\nTesting package-level access (controlled by __init__.py):")
    test_package_access("create_fire")
    test_package_access("create_water")
    test_package_access("create_earth")
    test_package_access("create_air")

    print("\nPackage metadata:")
    print("Version:", alchemy.__version__)
    print("Author:", alchemy.__author__)


if __name__ == "__main__":
    main()
