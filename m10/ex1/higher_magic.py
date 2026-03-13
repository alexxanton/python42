from typing import Callable, Any, Tuple, List


CallStr = Callable[[Any], str]
TupleCall = Callable[[Any], Tuple[str, str]]
CallInt = Callable[[Any], int]
CallBool = Callable[[], bool]


def spell_combiner(spell1: CallStr, spell2: CallStr) -> TupleCall:
    """Returns two combined functions"""
    return lambda *args, **kwargs:  (
        spell1(*args, **kwargs),
        spell2(*args, **kwargs)
    )


def power_amplifier(base_spell: CallInt, multiplier: int) -> CallInt:
    """Amplifies a function by multiplying it"""
    return lambda *args, **kwargs: base_spell(*args, **kwargs) * multiplier


def conditional_caster(condition: CallBool, spell: CallStr) -> CallStr:
    """Returns the value of a function if the condition is true"""
    return (
        lambda *args, **kwargs: spell(*args, **kwargs)
        if condition() else "Spell fizzled"
    )


def spell_sequence(spells: List[CallStr]) -> List[CallStr]:
    """Makes a sequence of functions with a shared parameter"""
    return (
        lambda *args, **kwargs: [spell(*args, **kwargs) for spell in spells]
    )


def main() -> None:
    """Tests all the function magic"""
    def fireball(creature: str) -> str:
        """Simulate a fireball hitting a creature"""
        return f"Fireball hits {creature}"

    def heal(creature: str) -> str:
        """Simulate healing a creature"""
        return f"Potion heals {creature}"

    def power() -> int:
        """Returns a value representing power"""
        return 10

    print("\nTesting spell combiner...")
    combined = spell_combiner(fireball, heal)
    print("Combined spell result: ", end="")
    effects = combined("Dragon")
    for i, item in enumerate(effects):
        print(item, end="")
        if i < len(effects) - 1:
            print(", ", end="")
    print()

    print("\nTesting power amplifier...")
    amplified = power_amplifier(power, 3)
    print(f"Original: {power()}, Amplified: {amplified()}")

    print("\nTesting conditional caster...")
    caster = conditional_caster(lambda: True, fireball)
    print(caster("Dragon"))

    print("\nTesting spell combiner...")
    spells = spell_sequence([fireball, heal])
    print(spells("Dragon"))


if __name__ == "__main__":
    main()
