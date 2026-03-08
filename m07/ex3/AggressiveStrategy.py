from typing import Any, Dict


class AggressiveStrategy:
    def execute_turn(self, hand: list, battlefield: list) -> Dict[str, Any]:
        return {}

    def get_strategy_name(self) -> str:
        return ""

    def prioritize_targets(self, available_targets: list) -> list:
        return []
