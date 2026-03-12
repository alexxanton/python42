from typing import Any, List, Dict


def artifact_sorter(
    artifacts: List[Dict[str, Any]]
) -> List[Dict[str, Any]]:
    """Sort the artifacts list with the power value"""
    return (
        sorted(artifacts, key=lambda artifact: artifact["power"], reverse=True)
    )


def power_filter(
    mages: List[Dict[str, Any]], min_power: int
) -> List[Dict[str, Any]]:
    """Filter mages power using min_power"""
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: List[str]) -> List[str]:
    """Transform spell names adding prefixes and suffixes"""
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Return mage statistics"""
    avg = sum(mage["power"] for mage in mages) / len(mages)
    return {
        "max_power": max(mages, key=lambda mage: mage["power"]),
        "min_power": min(mages, key=lambda mage: mage["power"]),
        "avg_power": avg
    }


def main() -> None:
    """Execute all functions to test lambda usage"""
    artifacts = [
        {"name": "Orb", "power": 85, "type": "Crystal"},
        {"name": "Ring", "power": 78, "type": "Chaos"},
        {"name": "Staff", "power": 92, "type": "Fire"}
    ]

    min_power = 80
    mages = [
        {"name": "Wizard", "power": 85, "type": "Ice"},
        {"name": "Witch", "power": 78, "type": "Poison"},
        {"name": "Mage", "power": 92, "type": "Fire"}
    ]

    spells = ["fireball", "heal", "shield"]

    print("\nTesting artifact sorter...")
    for i, artifact in enumerate(artifact_sorter(artifacts)):
        print(
            f"{artifact['type']} {artifact['name']} ({artifact['power']})",
            end=""
        )
        if i < len(artifacts) - 1:
            print(" comes before ", end="")
    print()

    print(f"\nTesting power filter... (min_power={min_power})")
    for i, mage in enumerate(power_filter(mages, min_power), 1):
        print(f"{i}: {mage['type']} {mage['name']} ({mage['power']})")

    print("\nTesting spell transformer...")
    for spell in spell_transformer(spells):
        print(spell, end=" ")
    print()

    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    max_mage = stats["max_power"]
    min_mage = stats["min_power"]
    print(
        "Max power: "
        f"{max_mage['type']} {max_mage['name']} ({max_mage['power']}) "
        "\nMin power: "
        f"{min_mage['type']} {min_mage['name']} ({min_mage['power']}) "
        "\nAvg power: "
        f"{stats['avg_power']:.1f}"
    )


if __name__ == "__main__":
    main()
