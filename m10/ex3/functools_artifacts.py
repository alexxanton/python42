from functools import reduce, partial, lru_cache, singledispatch
import operator
from typing import List, Callable, Dict, Any


def spell_reducer(spells: List[int], operation: str) -> int:
    ops: Dict[str, Callable[[int, int], int]] = {
        "add": operator.add,
        "mul": operator.mul,
        "min": min,
        "max": max
    }

    if operation not in ops:
        raise ValueError(f"Unknown operation: '{operation}'")
    return int(reduce(ops[operation], spells))


def partial_enchanter(
    base_enchantment: Callable[[str, int, str], str]
) -> Dict[str, Callable[[str], str]]:
    return {
        "fire_enchant": partial(base_enchantment, "fire", 50),
        "ice_enchant": partial(base_enchantment, "ice", 50),
        "lightning_enchant": partial(base_enchantment, "lightning", 50)
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n must be >= 0")
    if n in (0, 1):
        return n
    return (memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2))


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def spell(s: Any) -> str:
        return f"{s}"

    @spell.register(int)
    def _(s: int) -> str:
        return f"Dealed {s} damage!"

    @spell.register(str)
    def _(s: str) -> str:
        return f"Casted {s} spell!"

    @spell.register(list)
    def _(s: List[Any]) -> str:
        return f"Spell hit {s}"

    return spell


def main() -> None:
    print("\nTesting spell reducer...")
    spells = [10, 20, 30, 40]
    try:
        print("Sum:", spell_reducer(spells, "add"))
        print("Product:", spell_reducer(spells, "mul"))
        print("Max:", spell_reducer(spells, "max"))
        print("Min:", spell_reducer(spells, "min"))
    except ValueError as e:
        print("Error:", e)

    print("\nTesting partial enchanter...")

    def base_enchantment(element: str, power: int, target: str) -> str:
        return f"{element} enchant {power} on {target}"

    enchantments = partial_enchanter(base_enchantment)
    print(enchantments["fire_enchant"]("sword"))
    print(enchantments["ice_enchant"]("shield"))
    print(enchantments["lightning_enchant"]("armor"))

    print("\nTesting memoized fibonacci...")
    try:
        print("Fib(10):", memoized_fibonacci(10))
        print("Fib(15):", memoized_fibonacci(15))
    except ValueError as e:
        print("Error:", e)

    print("\nTesting spell dispatcher...")
    spell = spell_dispatcher()
    print(spell(10))
    print(spell("fireball"))
    print(spell(["ogre", "cyclops", "slime"]))


if __name__ == "__main__":
    main()
