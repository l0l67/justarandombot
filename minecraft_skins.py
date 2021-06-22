from lxml import html
import requests

base_url = "https://minecraft.tools/download-skin/"
player_name = "0"
def search(player_name):
    global data
    download_url = base_url + player_name
    data = requests.get(download_url).content
    data = bytes(data)
    return data