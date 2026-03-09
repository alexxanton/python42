from types import ModuleType
import alchemy
import alchemy.elements


def test_package_access(package: ModuleType, func_name: str) -> None:
    """Tries accessing packages that might not be imported"""
    package_name = package.__name__
    try:
        func = getattr(package, func_name)
        result = func()
        print(f"{package_name}.{func_name}():", result)
    except AttributeError:
        print(f"{package_name}.{func_name}(): AttributeError - not exposed")


def main() -> None:
    """Test importing from module access and package-level"""
    print("\n=== Sacred Scroll Mastery ===\n")
    print("Testing direct module access:")
    test_package_access(alchemy.elements, "create_fire")
    test_package_access(alchemy.elements, "create_water")
    test_package_access(alchemy.elements, "create_earth")
    test_package_access(alchemy.elements, "create_air")

    print("\nTesting package-level access (controlled by __init__.py):")
    test_package_access(alchemy, "create_fire")
    test_package_access(alchemy, "create_water")
    test_package_access(alchemy, "create_earth")
    test_package_access(alchemy, "create_air")

    print("\nPackage metadata:")
    print("Version:", alchemy.__version__)
    print("Author:", alchemy.__author__)


if __name__ == "__main__":
    main()
