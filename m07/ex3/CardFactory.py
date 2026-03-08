from abc import ABC, abstractmethod
from ex0.Card import Card
from typing import Any, Dict


class CardFactory(ABC):
    """Base class for card factories"""
    @abstractmethod
    def create_creature(self) -> Card:
        """Creates a creature card"""
        ...

    @abstractmethod
    def create_spell(self) -> Card:
        """Creates a spell card"""
        ...

    @abstractmethod
    def create_artifact(self) -> Card:
        """Creates an artifact card"""
        ...

    @abstractmethod
    def create_themed_deck(self, size: int) -> Dict[str, Any]:
        """Create a random themed deck"""
        ...

    @abstractmethod
    def get_supported_types(self) -> Dict[str, Any]:
        """Return all supported types"""
        ...
