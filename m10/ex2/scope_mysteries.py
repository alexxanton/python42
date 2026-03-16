from typing import Callable, Dict, Any


def mage_counter() -> Callable[[], int]:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    power = 0

    def accumulate(n: int) -> int:
        nonlocal power
        power += n
        return power

    return accumulate


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def enchantment(enchantment_name: str) -> str:
        return f"{enchantment_type} {enchantment_name}"
    return enchantment


def memory_vault() -> Dict[str, Callable[[], None]]:
    vault: Dict[str, callable]

    def store(key: str, value: Any) -> Dict[str, Any]:
        vault[key] = value

    def recall(key: str) -> Any:
        if key not in vault:
            return ""
        return vault[key]

    return {"store": store, "recall": recall,}


def main() -> None:
    print("\nTesting mage counter...")
    counter = mage_counter()
    for x in range(3):
        print(f"Call {x + 1}:", counter())

    print("\nTesting spell accumulator...")
    accumulate = spell_accumulator(1)
    for x in range(3):
        print(f"Call {x + 1}:", accumulate(x + 1 * 3))

    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))
    print("\nTesting memory vault...")


if __name__ == "__main__":
    main()
