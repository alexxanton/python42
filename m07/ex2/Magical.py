from abc import ABC, abstractmethod


class Magical(ABC):
    """Interface for magic methods"""
    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """Casts a spell that affects multiple targets"""
        ...

    @abstractmethod
    def channel_mana(self, amount: int) -> dict:
        """Channel a certain amount of mana"""
        ...

    @abstractmethod
    def get_magic_stats(self) -> dict:
        """Get magic stats"""
        ...
