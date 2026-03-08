from abc import ABC, abstractmethod
from typing import Any, Dict


class Rankable(ABC):
    """Interface with ranking capabilities"""
    @abstractmethod
    def calculate_rating(self) -> int:
        """Calculates the rating"""
        ...

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """Update wins counter"""
        ...

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        """Update losses counter"""
        ...

    @abstractmethod
    def get_rank_info(self) -> Dict[str, Any]:
        """Get ranking info"""
        ...
