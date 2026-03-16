import operator
from functools import reduce, partial, lru_cache, singledispatch


def spell_reducer(spells: list[int], operation: str) -> int:
    pass


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    pass


def memoized_fibonacci(n: int) -> int:
    pass


def spell_dispatcher() -> callable:
    pass


def main() -> None:
    print("\nTesting spell reducer...")
    print("\nTesting partial enchanter...")
    print("\nTesting memoized fibonacci...")
    print("\nTesting spell dispatcher...")


if __name__ == "__main__":
    main()
