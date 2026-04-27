# Gives each mod a priority number
# Lower number means the mod loads earlier
def get_priority(mod_name):
    name = mod_name.lower()

    # Base game and DLC content should be first
    if "core" in name:
        return 0
    elif "royalty" in name or "ideology" in name or "biotech" in name or "anomaly" in name:
        return 1

    # Frameworks and libraries should load before regular content mods
    elif "framework" in name or "library" in name or "harmony" in name:
        return 2

    # Common dependency/support mods
    elif "hugs" in name or "xml extensions" in name:
        return 3

    # Large mod groups usually load before small individual asset mods
    elif "vanilla expanded" in name:
        return 4

    # Gameplay expansion mods
    elif "faction" in name or "race" in name or "gene" in name:
        return 5

    # Smaller item or asset mods should load later
    elif "weapon" in name or "armor" in name or "material" in name or "item" in name:
        return 6

    # Unknown mods go near the bottom
    else:
        return 7


# Sorts mods by priority first, then alphabetically inside each group
def sort_mods(mods):
    return sorted(mods, key=lambda mod: (get_priority(mod["title"]), mod["title"].lower()))
