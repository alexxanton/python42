from abc import ABC, abstractmethod
from ex0.Card import Card
from typing import Any, Dict, List


class GameStrategy(ABC):
    @abstractmethod
    def execute_turn(
        self, hand: List[Card], battlefield: List[Any]
    ) -> Dict[str, Any]:
        """Executes a turn based on the strategy type"""
        ...

    @abstractmethod
    def get_strategy_name(self) -> str:
        """Get strategy class name"""
        ...

    @abstractmethod
    def prioritize_targets(self, available_targets: List[Any]) -> List[Any]:
        """Select targets with high priority"""
        ...
