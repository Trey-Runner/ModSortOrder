import json
from steam_api import get_published_file_details
from sorter import sort_mods

with open("saved_mods.json", "r") as file:
    saved_mod_ids = json.load(file)

mods = get_published_file_details(saved_mod_ids)

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
