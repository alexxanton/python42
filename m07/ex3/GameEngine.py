from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
from typing import Any, Dict


class GameEngine:
    def configure_engine(
        self, factory: CardFactory, strategy: GameStrategy
    ) -> None:
        pass

    def simulate_turn(self) -> Dict[str, Any]:
        return {}

    def get_engine_status(self) -> Dict[str, Any]:
        return {}
