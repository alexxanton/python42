def validate_ingredients(ingredients: str) -> str:
    """Validates if the ingredients in a string are valid"""
    valid_ingredients = ["fire", "water", "earth", "air"]
    for item in ingredients.split():
        if item not in valid_ingredients:
            return f"{ingredients} - INVALID"

    return f"{ingredients} - VALID"
