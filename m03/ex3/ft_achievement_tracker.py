def get_all(players: dict) -> set:
    """Get all achievements"""
    achievements = set()
    for name in players:
        achievements = achievements.union(players[name])
    return achievements


def get_unique(players: dict, unique_name: str) -> set:
    """Gets the achievements that only the specified player has"""
    unique = players[unique_name]
    names = [name for name in players if name != unique_name]
    others = set()
    for name in names:
        others = others.union(players[name])
    unique = unique.difference(others)
    return unique


def get_common(players: dict) -> set:
    """Get achievements owned by every player"""
    names = [name for name in players]
    common = players[names[0]]
    for name in names[1:]:
        common = common.intersection(players[name])
    return common


def get_rarest(players: dict) -> set:
    """Get achievements owned by just one player"""
    rarest = set()
    for name in players:
        rarest = rarest.union(get_unique(players, name))
    return rarest


def get_common_vs(players: dict, name1: str, name2: str) -> set:
    """Get achievements owned by both the specified players"""
    return players[name1].intersection(players[name2])


def main() -> None:
    """Executes all the achievement trackers"""
    players = {
        "alice": {"first_kill", "level_10", "treasure_hunter", "speed_demon"},
        "bob": {"first_kill", "level_10", "boss_slayer", "collector"},
        "charlie": {"level_10", "treasure_hunter", "boss_slayer",
                    "perfectionist"}
    }
    print("=== Achievement Tracker System ===\n")
    for name in players:
        print(f"Player {name} achievements: {players[name]}")
    print("\n=== Achievement Analytics ===")
    print("All unique achievements:", get_all(players))
    print("Total unique achievements:", len(get_all(players)))
    print("\nCommon to all players:", get_common(players))
    print("Rare achievements (1 player):", get_rarest(players))
    print("\nAlice vs Bob common:", get_common_vs(players, "alice", "bob"))
    print("Alice unique:", get_unique(players, "alice"))
    print("Bob unique:", get_unique(players, "bob"))


if __name__ == "__main__":
    main()
