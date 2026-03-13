def mage_counter() -> callable:
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> callable:
    power = 0

    def accumulate(n: int):
        nonlocal power
        power += n
        return power

    return accumulate


def enchantment_factory(enchantment_type: str) -> callable:
    pass


def memory_vault() -> dict[str, callable]:
    pass


def main() -> None:
    print("\nTesting mage counter...")
    counter = mage_counter()
    print(counter())
    print(counter())
    print(counter())

    print("\nTesting spell accumulator...")
    accumulate = spell_accumulator(0)
    print(accumulate(3))
    print(accumulate(3))
    print(accumulate(3))

    print("\nTesting enchantment factory...")
    print("\nTesting memory vault...")


if __name__ == "__main__":
    main()
