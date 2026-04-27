import requests

# Gets every mod ID inside a Steam Workshop collection
def get_collection_mod_ids(collection_id):
    url = "https://api.steampowered.com/ISteamRemoteStorage/GetCollectionDetails/v1/"

    # Steam expects the number of collections first
    # Then each collection ID as publishedfileids[0], publishedfileids[1], etc.
    data = {
        "collectioncount": 1,
        "publishedfileids[0]": collection_id
    }

    # Sends the request to Steam
    response = requests.post(url, data=data)
    response.raise_for_status()

    # Converts Steam's response into Python dictionary/list data
    result = response.json()["response"]["collectiondetails"][0]

    # If the collection is invalid, private, deleted, or empty, stop clearly
    if "children" not in result:
        return []

    mod_ids = []

    # Each child is one mod inside the collection
    for child in result["children"]:
        mod_ids.append(child["publishedfileid"])

    return mod_ids


# Gets details like title/name for each Workshop mod ID
def get_published_file_details(file_ids):
    url = "https://api.steampowered.com/ISteamRemoteStorage/GetPublishedFileDetails/v1/"

    # Steam requires itemcount to match the number of IDs being requested
    data = {
        "itemcount": len(file_ids)
    }

    # Adds every mod ID to the request using Steam's required format
    for index, file_id in enumerate(file_ids):
        data["publishedfileids[" + str(index) + "]"] = file_id

    # Sends the request to Steam
    response = requests.post(url, data=data)
    response.raise_for_status()

    # Returns the list of mod detail dictionaries
    return response.json()["response"]["publishedfiledetails"]
