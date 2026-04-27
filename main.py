from steam_api import get_collection_mod_ids, get_published_file_details
from sorter import sort_mods

# Asks the user for a Steam Workshop collection ID
collection_id = input("Enter RimWorld Steam collection ID: ")

# Gets all mod IDs inside the collection
mod_ids = get_collection_mod_ids(collection_id)

# Tests to see if the collection is empty or not
print("DEBUG mod_ids:", mod_ids)

# Stops if the collection is private, empty, deleted, or invalid
if len(mod_ids) == 0:
    print("No mods found. The collection may be private, empty, deleted, or the ID may be wrong.")
else:
    # Gets title and Steam details for each mod
    mods = get_published_file_details(mod_ids)

    clean_mods = []

    # Keeps only valid mods that Steam successfully returned
    for mod in mods:
        if mod.get("result") == 1 and "title" in mod and "publishedfileid" in mod:
            clean_mods.append({
                "id": mod["publishedfileid"],
                "title": mod["title"]
            })

    # Stops if all returned mods were invalid, deleted, hidden, or missing titles
    if len(clean_mods) == 0:
        print("No valid mod details found.")
    else:
        # Sorts mods using the custom load order rules
        sorted_mods = sort_mods(clean_mods)

        # Displays the final sorted mod load order
        print("RimWorld Mod Load Order")
        print("-----------------------")

        for index, mod in enumerate(sorted_mods, start=1):
            print(str(index) + ". " + mod["title"] + " (" + mod["id"] + ")")
