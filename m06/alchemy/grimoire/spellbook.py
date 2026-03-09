def record_spell(spell_name: str, ingredients: str) -> str:
    """Returns a string with the spell name and its valuation result"""
    from alchemy.grimoire import validate_ingredients
    return (
        f"Spell recorded: {spell_name} ({validate_ingredients(ingredients)})"
    )
