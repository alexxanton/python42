from typing import Any, Dict
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    """Card class with tournament capabilities"""

    card_type = "tournament"

    def __init__(
        self, name: str, card_id: str, cost: int, rarity: str
    ) -> None:
        super().__init__(name, cost, rarity)

        if not isinstance(card_id, str) or not card_id:
            raise ValueError("card_id must be a non-empty string")

        self.card_id = card_id
        self.rating = 1000
        self.wins = 0
        self.losses = 0

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        return self.play_base(game_state, "Strike enemies")

    def attack(self, target: Any) -> Dict[str, Any]:
        return {
            "attacker": self.name,
            "target": str(target)
        }

    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        if not isinstance(incoming_damage, int) or incoming_damage < 0:
            raise ValueError(
                "incoming_damage must be a non-negative integer"
            )

        return {"defender": self.name}

    def get_combat_stats(self) -> Dict[str, Any]:
        return {}

    # Rankable
    def update_wins(self, wins: int = 1) -> None:
        if not isinstance(wins, int) or wins < 0:
            raise ValueError("wins must be a non-negative integer")
        self.wins += wins
        self.rating += wins * 10

    def update_losses(self, losses: int = 1) -> None:
        if not isinstance(losses, int) or losses < 0:
            raise ValueError("losses must be a non-negative integer")
        self.losses += losses
        self.rating -= losses * 10

    def get_rank_info(self) -> Dict[str, Any]:
        return {
            "interfaces": [c.__name__ for c in self.__class__.__bases__],
            "rating": self.rating,
            "record": f"{self.wins}-{self.losses}",
        }

    def calculate_rating(self) -> int:
        return self.rating

    def get_tournament_stats(self) -> Dict[str, Any]:
        return {
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses
        }
