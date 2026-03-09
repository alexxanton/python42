from typing import Callable, Optional, Mapping, Set


def exec_func(
    func: Callable[[], str],
    options: Optional[Set[str]] = None,
    namespace: Optional[Mapping[str, object]] = None
) -> None:
    """
    Executes the function given as a parameter and contains some
    options to print specific things like module name or alias
    """
    try:
        func_name = func.__name__
        if options is None:
            options = set()
        if "print" in options:
            print(f"{func.__module__}.", end="")
        if "alias" in options and namespace is not None:
            for name, value in namespace.items():
                if value is func:
                    func_name = name
                    break
        print(f"{func_name}():", func())
    except AttributeError:
        pass


def full_module_import() -> None:
    """Imports full module and executes a function"""
    import alchemy.elements
    print("\nMethod 1 - Full module import:")
    exec_func(alchemy.elements.create_fire, {"print"})


def specific_function_import() -> None:
    """Imports a specific function from a module and uses it"""
    print("\nMethod 2 - Specific function import:")
    from alchemy.elements import create_water
    exec_func(create_water)


def aliased_import() -> None:
    """Imports a function and creates and alias for it"""
    print("\nMethod 3 - Aliased import:")
    from alchemy.potions import healing_potion as heal
    exec_func(heal, {"alias"}, locals())


def multiple_imports() -> None:
    """Imports multiple functions from different modules and uses them"""
    from alchemy.elements import create_fire, create_earth
    from alchemy.potions import strength_potion
    print("\nMethod 4 - Multiple imports:")
    exec_func(create_earth)
    exec_func(create_fire)
    exec_func(strength_potion)


def main() -> None:
    """Tests all the import styles"""
    print("\n=== Import Transmutation Mastery ===")
    full_module_import()
    specific_function_import()
    aliased_import()
    multiple_imports()
    print("\nAll import transmutation methods mastered!")


if __name__ == "__main__":
    main()
