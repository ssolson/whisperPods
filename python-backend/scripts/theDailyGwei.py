import os
import re
import pandas as pd
# from pymongo.mongo_client import MongoClient
from whisperPod.mongo import db
from whisperPod.utils import utils

# Replace 'your_database' with the name of your database and 'your_collection' with the name of your collection
client = db.get_client()
# db = client.your_database
# collection = db.your_collection


folder_path = "podcast/thedailygwei/2023"
mp3_files = utils.find_mp3_files(folder_path)

data = {
    "Date": [],
    "Episode Name": [],
    "Podcast Name": [],
    "Podcast Number": [],
    "Subtitle": [],
    "filename": [],
}

for file_path in mp3_files:
    file = file_path.replace(f"{folder_path}\\", "")
    # Extract components using regex
    pattern = r"(\d{4}\.\d{2}\.\d{2}) (.+?) - (.+?) Refuel #(\d+) - (.+)\.mp3"
    match = re.match(pattern, file)

    if match:
        date, episode_name, podcast_name, podcast_number, subtitle = match.groups()

        # Append data to the dictionary
        data["Date"].append(date)
        data["Episode Name"].append(episode_name)
        data["Podcast Name"].append(podcast_name)
        data["Podcast Number"].append(int(podcast_number))
        data["Subtitle"].append(subtitle)
        data["filename"].append(file_path)

    else:
        print(f"Failed to extract components from the input string: {file}")

    # Create a pandas DataFrame
    df = pd.DataFrame(data)

    # Convert the 'Date' column to datetime format and set it as the index
    df['Date'] = pd.to_datetime(df['Date'], format='%Y.%m.%d')
    df.set_index('Date', inplace=True)

    print(df)

    import ipdb; ipdb.set_trace()

    transcript = whisper_podcast(df.iloc[0].filename)

    import ipdb; ipdb.set_trace()
    print(transcript['text'])