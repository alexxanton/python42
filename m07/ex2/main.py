from ex0.Card import Card
from ex2.EliteCard import EliteCard
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from typing import List


def get_methods(cls: type) -> List[str]:
    """Gets all the callable methods from a class"""
    return [m for m in dir(cls)
            if callable(getattr(cls, m)) and not m.startswith("__")]


def main() -> None:
    """Test multiple inheritance class"""
    print("\n=== DataDeck Ability System ===")
    print("\nEliteCard capabilities:")

    try:
        card = EliteCard(name="Arcane Warrior",
                         cost=5,
                         rarity="Legendary",
                         damage=5,
                         mana=8,
                         defense=3,
                         health=5,
                         combat="melee")

        print("- Card:", get_methods(Card))
        print("- Combatable:", get_methods(Combatable))
        print("- Magical:", get_methods(Magical))
        print(f"\nPlaying {card.name} ({card.card_type})")

        print("\nCombat phase:")
        print("Attack result:", card.attack("Enemy"))
        print("Defense result:", card.defend(5))

        print("\nMagic phase:")
        print(
            "Spell cast:", card.cast_spell("Fireball", ["Enemy1", "Enemy2"])
        )
        print("Mana channel:", card.channel_mana(3))
    except Exception as e:
        print("Error:", e)
    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
