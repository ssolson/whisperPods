import requests
import xml.etree.ElementTree as ET

url = "https://feeds.libsyn.com/310739/rss"
response = requests.get(url)

if response.status_code == 200:
    content = response.content
    root = ET.fromstring(content)

    # Example: Get the channel title
    channel_title = root.find("channel/title").text
    print(f"Channel title: {channel_title}")

    # Example: Get all item titles
    for item in root.findall("channel/item"):
        item_title = item.find("title").text
        print(f"Item title: {item_title}")
else:
    print(f"Failed to fetch the URL, status code: {response.status_code}")


import ipdb; ipdb.set_trace()