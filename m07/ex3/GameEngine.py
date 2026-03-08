from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
from typing import Any, Dict
from pprint import pprint
from collections import Counter


class GameEngine:

    deck = {}

    def configure_engine(
        self, factory: CardFactory, strategy: GameStrategy
    ) -> None:
        self.deck = factory.create_themed_deck(50)
        print("Available types:")
        pprint(factory.get_supported_types())

    def simulate_turn(self) -> Dict[str, Any]:
        print("\nSimulating aggressive turn...")

        hand = dict(Counter(card.name for card in self.deck["deck"]))
        formatted = ", ".join(f"{name} ({count})" for name, count in hand.items())
        print(f"Hand: [{formatted}]")
        print("\nTurn execution:")
        print("Strategy:")
        return {}

    def get_engine_status(self) -> Dict[str, Any]:
        return {}
