def ingredient_validation_test() -> None:
    """Tests ingredient validation"""
    from alchemy.grimoire import validate_ingredients
    print("\nTesting ingredient validation:")
    print('validate_ingredients("fire air"):',
          validate_ingredients("fire air"))
    print('validate_ingredients("dragon scales"):',
          validate_ingredients("dragon scales"))


def spell_recording_test() -> None:
    """Tests spell recording"""
    from alchemy.grimoire.spellbook import record_spell
    print("\nTesting spell recording with validation:")
    print('record_spell("Fireball", "fire air"):',
          record_spell("Fireball", "fire air"))
    print('record_spell("Dark Magic", "shadow"):',
          record_spell("Dark Magic", "shadow"))


def late_import_test() -> None:
    """Tests functions with late imports"""
    from alchemy.grimoire.spellbook import record_spell
    print("\nTesting late import technique:")
    print('record_spell("Lightning", "air"):',
          record_spell("Lightning", "air"))


def main() -> None:
    """Tests ingredient validation and late imports"""
    print("\n=== Circular Curse Breaking ===")
    ingredient_validation_test()
    spell_recording_test()
    late_import_test()
    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    main()
