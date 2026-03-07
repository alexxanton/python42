from abc import ABC, abstractmethod
from typing import Any, Dict, List


class Magical(ABC):
    """Interface for magic methods"""
    @abstractmethod
    def cast_spell(
        self, spell_name: str, targets: List[Any]
    ) -> Dict[str, Any]:
        """Casts a spell that affects multiple targets"""
        ...

    @abstractmethod
    def channel_mana(self, amount: int) -> Dict[str, Any]:
        """Channel a certain amount of mana"""
        ...

    @abstractmethod
    def get_magic_stats(self) -> Dict[str, Any]:
        """Get magic stats"""
        ...
