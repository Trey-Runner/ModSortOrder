from steam_api import get_collection_mod_ids, get_published_file_details
from sorter import sort_mods

collection_id = input("Enter RimWorld Steam collection ID: ")

mod_ids = get_collection_mod_ids(collection_id)
mods = get_published_file_details(mod_ids)

clean_mods = []

for mod in mods:
    clean_mods.append({
        "id": mod["publishedfileid"],
        "title": mod["title"]
    })

sorted_mods = sort_mods(clean_mods)

print("RimWorld Mod Load Order")
print("-----------------------")

for index, mod in enumerate(sorted_mods, start=1):
    print(str(index) + ". " + mod["title"] + " (" + mod["id"] + ")")
