from abc import ABC, abstractmethod


class Card(ABC):
    """Base class for cards"""
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        if not isinstance(name, str) or not name:
            raise ValueError("name must be a non-empty string")
        if not isinstance(cost, int) or cost < 0:
            raise ValueError("cost must be a non-negative integer")
        if not isinstance(rarity, str) or not rarity:
            raise ValueError("rarity must be a non-empty string")

        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        """Simulates a turn for a card game"""
        ...

    def get_card_info(self) -> dict:
        """Returns a dictionary with the card info"""
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity
        }

    def is_playable(self, available_mana: int) -> bool:
        """Validates mana quantity and checks if there's enough of it"""
        if not isinstance(available_mana, int) or available_mana < 0:
            raise ValueError("mana must be a non-negative integer")
        return available_mana > self.cost
