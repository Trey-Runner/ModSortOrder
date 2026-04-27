import requests

# Gets every mod ID inside a Steam Workshop collection
def get_collection_mod_ids(collection_id):
    url = "https://api.steampowered.com/ISteamRemoteStorage/GetCollectionDetails/v1/"

    # Steam requires the number of collections being requested
    data = {
        "collectioncount": 1,
        "publishedfileids[0]": collection_id
    }

    # Sends request to Steam
    response = requests.post(url, data=data)

    # Stops the program if the Steam request completely fails
    response.raise_for_status()

    # Converts Steam's JSON response into Python data
    data = response.json()

    # Safety check in case Steam returns an unexpected response
    if "response" not in data or "collectiondetails" not in data["response"]:
        return []

    collection_list = data["response"]["collectiondetails"]

    # Safety check in case the collection does not exist or is private
    if len(collection_list) == 0:
        return []

    result = collection_list[0]

    # Safety check in case the collection has no mods inside it
    if "children" not in result:
        return []

    mod_ids = []

    # Each child inside the collection is a Workshop mod
    for child in result["children"]:
        if "publishedfileid" in child:
            mod_ids.append(child["publishedfileid"])

    return mod_ids


# Gets Steam Workshop details for each mod ID
def get_published_file_details(file_ids):
    url = "https://api.steampowered.com/ISteamRemoteStorage/GetPublishedFileDetails/v1/"

    # Safety check to avoid calling Steam with an empty list
    if len(file_ids) == 0:
        return []

    # Steam requires itemcount to match the number of IDs
    data = {
        "itemcount": len(file_ids)
    }

    # Adds each mod ID using Steam's required format
    for index, file_id in enumerate(file_ids):
        data["publishedfileids[" + str(index) + "]"] = file_id

    # Sends request to Steam
    response = requests.post(url, data=data)

    # Stops the program if the Steam request completely fails
    response.raise_for_status()

    # Converts response into Python data
    data = response.json()

    # Safety check in case Steam returns an unexpected response
    if "response" not in data or "publishedfiledetails" not in data["response"]:
        return []

    return data["response"]["publishedfiledetails"]
