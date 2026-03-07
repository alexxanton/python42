from abc import ABC, abstractmethod
from typing import Any, Dict


class Card(ABC):

    card_type = ""

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
    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        """Simulates a turn for a card game"""
        ...

    def get_card_info(self) -> Dict[str, Any]:
        """Returns a Dict[str, Any]ionary with the card info"""
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity
        }

    def is_playable(self, available_mana: int) -> bool:
        """Validates mana quantity and checks if there's enough of it"""
        if not isinstance(available_mana, int) or available_mana < 0:
            raise ValueError("mana must be a non-negative integer")
        return available_mana >= self.cost

    def play_base(
        self, game_state: Dict[str, Any], effect: str
    ) -> Dict[str, Any]:
        """Base for the abstract method 'play'"""
        if "mana" not in game_state:
            raise KeyError("mana not in game_state")

        if not self.is_playable(game_state["mana"]):
            return {
                "card_played": None,
                "mana_used": 0,
                "effect": None
            }

        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "mana": game_state["mana"] - self.cost,
            "effect": effect
        }
