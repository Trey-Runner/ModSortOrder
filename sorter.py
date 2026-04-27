# Gives each mod a priority number
# Lower number = loads earlier
def get_priority(mod_name):
    name = mod_name.lower()

    # Base game and official DLCs should be first
    if "core" in name:
        return 0
    elif "royalty" in name or "ideology" in name or "biotech" in name or "anomaly" in name:
        return 1

    # Frameworks and libraries should load before content mods
    elif "framework" in name or "library" in name or "harmony" in name:
        return 2

    # Common support mods
    elif "hugs" in name or "xml extensions" in name:
        return 3

    # Large mod series should usually come before small asset mods
    elif "vanilla expanded" in name:
        return 4

    # Gameplay/content categories
    elif "faction" in name or "race" in name:
        return 5

    # Smaller single-item or asset-style mods load later
    elif "weapon" in name or "armor" in name or "material" in name:
        return 6

    # Anything unknown goes near the bottom
    else:
        return 7


# Sorts first by priority, then alphabetically inside each priority group
def sort_mods(mods):
    return sorted(mods, key=lambda mod: (get_priority(mod["title"]), mod["title"].lower()))
