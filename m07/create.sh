for x in {0..4}; do
	mkdir ex"${x}"
	cd ex"${x}"
	case "$x" in

		0)
			touch __init__.py Card.py CreatureCard.py main.py
			;;
		1)
			touch  __init__.py SpellCard.py ArtifactCard.py Deck.py main.py
			;;
		2)
			touch __init__.py Combatable.py Magical.py EliteCard.py main.py
			;;
		3)
			touch __init__.py GameStrategy.py CardFactory.py AggressiveStrategy.py FantasyCardFactory.py GameEngine.py main.py
			;;
		4)
			touch __init__.py Rankable.py TournamentCard.py TournamentPlatform.py main.py
			;;
	esac
	cd ..
done
