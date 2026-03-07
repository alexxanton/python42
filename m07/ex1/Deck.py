from ex0.Card import Card
import random


class Deck:
    """Holds the cards and contains methods to use them"""
    cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        """Add a card to the deck"""
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        """Remove a card from the deck if it exists"""
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        """Shuffle the cards list"""
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        """Removes the last card from the deck and returns it"""
        if not self.cards:
            raise ValueError("empty deck")
        return self.cards.pop()

    def get_deck_stats(self) -> dict:
        """Displays deck stats"""
        creatures = [c for c in self.cards if c.card_type == "Creature"]
        spells = [c for c in self.cards if c.card_type == "Spell"]
        artifacts = [c for c in self.cards if c.card_type == "Artifact"]
        total = sum([c.cost for c in self.cards])
        count = len(self.cards)
        avg = total / count if count > 0 else 0.0

        return {
            "total_cards": len(self.cards),
            "creatures": len(creatures),
            "spells": len(spells),
            "artifacts": len(artifacts),
            "avg_cost": round(avg, 1),
        }
