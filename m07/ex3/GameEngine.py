from ex0.Card import Card
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
from typing import Any, Dict, List
from pprint import pprint
from collections import Counter


class GameEngine:
    """Simulates turns for a card game"""
    def __init__(self) -> None:
        self.deck: List[Card] = []
        self.strategy: GameStrategy | None = None
        self.battlefield: List[Any] = ["spell", "enemy player", "creature"]
        self.turns = 0
        self.total_dmg = 0

    def configure_engine(
        self, factory: CardFactory, strategy: GameStrategy
    ) -> None:
        """Configures the engine by creating a deck with a strategy"""
        if not isinstance(factory, CardFactory):
            raise ValueError("factory must be an instance of CardFactory")
        if not isinstance(strategy, GameStrategy):
            raise ValueError("strategy must be an instance of GameStrategy")

        self.deck = factory.create_themed_deck(50)["deck"]
        self.strategy = strategy
        print("Available types:")
        pprint(factory.get_supported_types())

    def simulate_turn(self) -> Dict[str, Any]:
        """Simulates a turn"""
        if self.strategy is None:
            raise ValueError("strategy must be selected before using engine")

        print("\nSimulating aggressive turn...")
        hand = dict(Counter(card.name for card in self.deck))
        formatted = ", ".join(
            f"{name} ({count})" for name, count in hand.items()
        )
        print(f"Hand: [{formatted}]")
        print("\nTurn execution:")
        print("Strategy:", self.strategy.get_strategy_name())
        self.turns += 1
        turn = self.strategy.execute_turn(self.deck, self.battlefield)
        self.total_dmg += turn["damage_dealt"]
        return turn

    def get_engine_status(self) -> Dict[str, Any]:
        """Get engine status"""
        if self.strategy is None:
            raise ValueError("strategy must be selected before using engine")

        return {
            "turns_simulated": self.turns,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": self.total_dmg,
            "cards_created": len(self.deck),
        }
