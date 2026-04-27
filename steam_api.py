import requests

def get_collection_mod_ids(collection_id):
    url = "https://api.steampowered.com/ISteamRemoteStorage/GetCollectionDetails/v1/"

    data = {
        "collectioncount": 1,
        "publishedfileids[0]": collection_id
    }

    response = requests.post(url, data=data)
    response.raise_for_status()

    collection = response.json()["response"]["collectiondetails"][0]

    mod_ids = []

    for child in collection["children"]:
        mod_ids.append(child["publishedfileid"])

    return mod_ids


def get_published_file_details(file_ids):
    url = "https://api.steampowered.com/ISteamRemoteStorage/GetPublishedFileDetails/v1/"

    data = {
        "itemcount": len(file_ids)
    }

    for index, file_id in enumerate(file_ids):
        data["publishedfileids[" + str(index) + "]"] = file_id

    response = requests.post(url, data=data)
    response.raise_for_status()

    return response.json()["response"]["publishedfiledetails"]
