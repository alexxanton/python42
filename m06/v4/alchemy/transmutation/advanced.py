from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone() -> str:
    """Create the Philosopher's stone by using alchemy and magic potions"""
    return (
        f"Philosopher’s stone created using {lead_to_gold()} "
        f"and {healing_potion()}"
    )


def elixir_of_life() -> str:
    """Drink the elixir of life, how did you get it???"""
    return "Elixir of life: eternal youth achieved!"
