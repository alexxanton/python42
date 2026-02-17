import sys


def parse_args() -> dict:
    inventory = dict()
    for arg in sys.argv[1:]:
        if not ":" in arg:
            return {}
        item = arg.split(":")
        try:
            inventory.update({item[0]: int(item[1])})
        except ValueError:
            return {}
    return inventory


def categorize(inventory: dict) -> tuple[dict, dict]:
    treshold = 4
    moderate = dict()
    scarce = dict()
    for item, qty in inventory.items():
        if qty >= treshold:
            moderate[item] = qty
        else:
            scarce[item] = qty
    return moderate, scarce


def main() -> None:
    inventory = parse_args()
    if not inventory:
        return

    items = len(inventory)
    total = 0
    for x in inventory.values():
        total += x
    max_item = max(inventory, key=inventory.get)
    min_item = min(inventory, key=inventory.get)
    moderate, scarce = categorize(inventory)
    restock = [item for item, qty in inventory.items() if qty <= 1]

    print("=== Inventory System Analysis ===")
    print("Total items in inventory:", total)
    print("Unique item types:", items)
    print("\n=== Current Inventory ===")
    for item, qty in inventory.items():
        print(f"{item}: {qty} units ({qty / total * 100:.1f}%)")
    print("\n=== Inventory Statistics ===")
    print(f"Most abundant: {max_item} ({inventory[max_item]} units)")
    print(f"Least abundant: {min_item} ({inventory[min_item]} units)")
    print("\n=== Item Categories ===")
    print("Moderate:", moderate)
    print("Scarce:", scarce)
    print("\n=== Management Suggestions ===")
    print("Restock needed:", restock)
    print("\n=== Dictionary Properties Demo ===")
    print("Dictionary keys:", list(inventory.keys()))
    print("Dictionary values:", list(inventory.values()))
    print("Sample lookup - 'sword' in inventory:", "sword" in inventory)


if __name__ == "__main__":
    main()
