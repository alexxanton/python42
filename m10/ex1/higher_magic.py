def spell_combiner(spell1: callable, spell2: callable) -> callable:
    return lambda *args, **kwargs:  (
        spell1(*args, **kwargs),
        spell2(*args, **kwargs)
    )


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    return lambda *args, **kwargs: base_spell(*args, **kwargs) * multiplier


def conditional_caster(condition: callable, spell: callable) -> callable:
    pass


def spell_sequence(spells: list[callable]) -> callable:
    pass


def main() -> None:
    print("\nTesting spell combiner...")
    def fireball(creature: str) -> str:
        return f"Fireball hits {creature}"
    def heal(creature: str) -> str:
        return f"Heals {creature}"
    combined = spell_combiner(fireball, heal)
    print("Combined spell result: ", end="")
    effects = combined("Dragon")
    for i, item in enumerate(effects):
        print(item, end="")
        if i < len(effects) - 1:
            print(", ", end="")
    print()

    print("\nTesting power amplifier...")
    def power() ->  int:
        return 10
    amplified = power_amplifier(power, 3)
    print(f"Original: {power()}, Amplified: {amplified()}")

    print("\nTesting conditional caster...")
    conditional_caster(fireball, heal)

    print("\nTesting spell combiner...")
    spell_sequence([])


if __name__ == "__main__":
    main()
