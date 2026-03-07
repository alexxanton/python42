from abc import ABC, abstractmethod


class Combatable(ABC):
    """Interface for combat methods"""
    @abstractmethod
    def attack(self, target) -> dict:
        """Attacks a target"""
        ...

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        """Defends from an incoming attack"""
        ...

    @abstractmethod
    def get_combat_stats(self) -> dict:
        """Get combat stats"""
        ...
