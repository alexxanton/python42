from typing import Callable, Dict, Any, TypedDict


class Vault(TypedDict):
    """Type class for vault dictionary"""
    store: Callable[[str, Any], None]
    recall: Callable[[str], Any]


def mage_counter() -> Callable[[], int]:
    """Returns a counter function"""
    count = 0

    def counter() -> int:
        """Returns a persistent value"""
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    """Returns an accumulator function"""
    power = initial_power

    def accumulate(n: int) -> int:
        """Accumulates to a persistent value"""
        nonlocal power
        power += n
        return power

    return accumulate


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    """Returns an enchantment with an applied type"""
    def enchantment(enchantment_name: str) -> str:
        """Combines the type and name and returns it"""
        return f"{enchantment_type} {enchantment_name}"
    return enchantment


def memory_vault() -> Vault:
    """Returns a dict with store and recall functions"""
    vault: Dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        """Store a value to a persistent dict"""
        vault[key] = value

    def recall(key: str) -> Any:
        """Recall a value from a persistent dict"""
        if key not in vault:
            return "Memory not found"
        return vault[key]

    return {"store": store, "recall": recall}


def main() -> None:
    """Execute all the scope tests"""
    print("\nTesting mage counter...")
    counter = mage_counter()
    for x in range(3):
        print(f"Call {x + 1}:", counter())

    print("\nTesting spell accumulator...")
    accumulate = spell_accumulator(0)
    for x in range(3):
        print(f"Call {x + 1}:", accumulate((x + 1) * 3))

    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))

    print("\nTesting memory vault...")
    vault = memory_vault()
    vault["store"]("num", 42)
    print("Stored value:", vault["recall"]("num"))
    print("Unknown value:", vault["recall"]("idk"))


if __name__ == "__main__":
    main()
