from typing import Callable, Optional, Set


def exec_func(
    func: Callable[[], str],
    options: Optional[Set[str]] = None
) -> None:
    """
    Executes the function given as a parameter and contains some
    options to print specific things like module
    """
    func_name = func.__name__
    if options is None:
        options = set()
    if "print" in options:
        module_name = func.__module__
        if "advanced" in module_name:
            module_name = module_name.replace(".advanced", "")
        if "basic" in module_name:
            module_name = module_name.replace(".basic", "")
        print(f"{module_name}.", end="")
    print(f"{func_name}():", func())


def absolute_imports() -> None:
    from alchemy.transmutation import basic
    print("\nTesting Absolute Imports (from basic.py):")
    exec_func(basic.lead_to_gold)
    exec_func(basic.stone_to_gem)


def relative_imports() -> None:
    from alchemy.transmutation import advanced
    print("\nTesting Relative Imports (from advanced.py):")
    exec_func(advanced.philosophers_stone)
    exec_func(advanced.elixir_of_life)


def package_access() -> None:
    import alchemy.transmutation
    print("\nTesting Package Access:")
    exec_func(alchemy.transmutation.lead_to_gold, {"print"})
    exec_func(alchemy.transmutation.philosophers_stone, {"print"})


def main() -> None:
    print("\n=== Pathway Debate Mastery ===")
    absolute_imports()
    relative_imports()
    package_access()
    print("\nBoth pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    main()
