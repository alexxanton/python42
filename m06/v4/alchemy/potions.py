def healing_potion() -> str:
    """Brew a healing potion with the power of fire and water"""
    from .elements import create_fire, create_water
    fire_result = create_fire()
    water_result = create_water()
    return f"Healing potion brewed with {fire_result} and {water_result}"


def strength_potion() -> str:
    """Brew a strength potion with the power of earth and fire"""
    from .elements import create_earth, create_fire
    earth_result = create_earth()
    fire_result = create_fire()
    return f"Strength potion brewed with {earth_result} and {fire_result}"


def invisibility_potion() -> str:
    """Brew an invisibility potion with the power of air and water"""
    from .elements import create_air, create_water
    air_result = create_air()
    water_result = create_water()
    return f"Invisibility potion brewed with {air_result} and {water_result}"


def wisdom_potion() -> str:
    """Brew a wisdom potion with the power of all elements"""
    from .elements import create_fire, create_water, create_earth, create_air
    fire_result = create_fire()
    water_result = create_water()
    earth_result = create_earth()
    air_result = create_air()
    return (
        "Wisdom potion brewed with all elements: "
        f"{fire_result}, {water_result}, {earth_result}, {air_result}"
    )
