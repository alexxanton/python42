from abc import ABC, abstractmethod
from typing import Any, Dict


class Combatable(ABC):
    """Interface for combat methods"""
    @abstractmethod
    def attack(self, target: Any) -> Dict[str, Any]:
        """Attacks a target"""
        ...

    @abstractmethod
    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        """Defends from an incoming attack"""
        ...

    @abstractmethod
    def get_combat_stats(self) -> Dict[str, Any]:
        """Get combat stats"""
        ...
