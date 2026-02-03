def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    units = {
            "packets": f"{quantity} packets available",
            "grams": f"{quantity} grams total",
            "area": f"covers {quantity} square meters"
            }
    print(f"{seed_type.capitalize()} seeds: {units[unit]}")

ft_seed_inventory("lettuce", 13, "area")
