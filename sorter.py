def get_priority(mod_name):
    name = mod_name.lower()

    if "core" in name:
        return 0
    elif "royalty" in name or "ideology" in name or "biotech" in name or "anomaly" in name:
        return 1
    elif "framework" in name or "library" in name or "harmony" in name:
        return 2
    elif "hugs" in name or "xml extensions" in name:
        return 3
    elif "vanilla expanded" in name:
        return 4
    elif "faction" in name or "race" in name:
        return 5
    elif "weapon" in name or "armor" in name or "material" in name:
        return 6
    else:
        return 7


def sort_mods(mods):
    return sorted(mods, key=lambda mod: (get_priority(mod["title"]), mod["title"].lower()))
