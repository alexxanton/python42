from alchemy.elements import create_fire, create_earth


def lead_to_gold() -> str:
    """Transform lead to gold using the poer of alchemy and fire"""
    return f"Lead transmuted to gold using {create_fire()}"


def stone_to_gem() -> str:
    """Combine alchemy and magic to transform a petty stone into a gem"""
    return f"Stone transmuted to gem using {create_earth()}"
