from ex0.CreatureCard import CreatureCard


def main() -> None:
    """Tests the card system"""
    print("\n=== DataDeck Card Foundation ===")
    print("\nTesting Abstract Base Class Design:")
    game_state = {"mana": 8}

    try:
        card = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
        target = "Goblin Warrior"

        print("\nCreatureCard Info:")
        print(card.get_card_info())
    except ValueError as e:
        print("Card creation error:", e)
        return

    try:
        print(
            f"\nPlaying {card.name} with {game_state['mana']} mana available:"
        )
        is_playable = card.is_playable(game_state["mana"])
        print("Playable:", is_playable)
        if is_playable:
            game_state.update(card.play(game_state))
            print("Play result:", game_state)

        print(f"\n{card.name} attacks {target}:")
        print("Attack result:", card.attack_target(target))

        print(f"\nTesting insufficient mana ({game_state['mana']} available):")
        print("Playable:", card.is_playable(game_state["mana"]))
    except ValueError as e:
        print("Game logic error:", e)

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
