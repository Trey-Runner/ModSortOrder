import os
import requests
from dotenv import load_dotenv

load_dotenv()

APP_ID = 294100

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
