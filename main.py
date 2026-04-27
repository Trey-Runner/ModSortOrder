from steam_api import get_collection_mod_ids, get_published_file_details
from sorter import sort_mods

# User enters the Steam Workshop collection ID
collection_id = input("Enter RimWorld Steam collection ID: ")

# Pulls all mod IDs from that collection
mod_ids = get_collection_mod_ids(collection_id)

# Stops if Steam does not return any mods
if len(mod_ids) == 0:
    print("No mods found. The collection may be private, empty, deleted, or the ID may be wrong.")
else:
    # Gets each mod's Steam Workshop details
    mods = get_published_file_details(mod_ids)

    clean_mods = []

    # Keeps only the information needed for sorting/display
    for mod in mods:
        clean_mods.append({
            "id": mod["publishedfileid"],
            "title": mod["title"]
        })

    # Sorts the list based on custom priority rules
    sorted_mods = sort_mods(clean_mods)

    # Displays final sorted load order
    print("RimWorld Mod Load Order")
    print("-----------------------")

    for index, mod in enumerate(sorted_mods, start=1):
        print(str(index) + ". " + mod["title"] + " (" + mod["id"] + ")")
