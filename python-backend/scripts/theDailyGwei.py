import os
import re
import pandas as pd
import whisperpod as wp
from dotenv import load_dotenv


# Get the mogodb client, and set the database, and collection
client = wp.mongo.db.get_client()
database_name = "whisperPods"
collection_name = "thedailygwei"
db = client[database_name]
collection = db[collection_name]

# Get the libsyn podcast metadata
base_url = 'https://thedailygwei.libsyn.com/'
output_file = 'thedailygwei_metadata.json'
all_episodes = wp.request.metadata.scrape(base_url, output_file)

# Get the youtube video metadata
load_dotenv()
api_key = os.getenv('YOUTUBE_API')
playlist_id = 'PLIMWH1uKd3oE905uSUHdE5hd6e2UpADak'
output_file = 'thedailygwei_youtube_metadata.json'

video_data_list = wp.request.youtube.fetch_metadata(playlist_id, output_file, api_key)

# # Get the latest podcasts
# wp.request.requestPod.get_podcast(
#     "https://thedailygwei.libsyn.com/rss" , 
#     "thedailygwei",
#     "2020-10-01",
# )

# # TODO: Store mp3 to database?
# folder_path = "podcast/thedailygwei/2023"
# mp3_files = wp.utils.utils.find_mp3_files(folder_path)

# data = {
#     "Date": [],
#     "Episode Name": [],
#     "Podcast Name": [],
#     "Podcast Number": [],
#     "Subtitle": [],
#     "filename": [],
# }

# for file_path in mp3_files:
#     file = file_path.replace(f"{folder_path}\\", "")
#     # Extract components using regex
#     pattern = r"(\d{4}\.\d{2}\.\d{2}) (.+?) - (.+?) Refuel #(\d+) - (.+)\.mp3"
#     match = re.match(pattern, file)

#     if match:
#         date, episode_name, podcast_name, podcast_number, subtitle = match.groups()

#         # Append data to the dictionary
#         data["Date"].append(date)
#         data["Episode Name"].append(episode_name)
#         data["Podcast Name"].append(podcast_name)
#         data["Podcast Number"].append(int(podcast_number))
#         data["Subtitle"].append(subtitle)
#         data["filename"].append(file_path)

#     else:
#         print(f"Failed to extract components from the input string: {file}")

#     # Create a pandas DataFrame
#     df = pd.DataFrame(data)

#     # Convert the 'Date' column to datetime format and set it as the index
#     df['Date'] = pd.to_datetime(df['Date'], format='%Y.%m.%d')
#     df.set_index('Date', inplace=True)

#     print(df)

# import ipdb; ipdb.set_trace()

# transcript = wp.transcribe.transcribePod.whisper_podcast(df.iloc[0].filename)

# import ipdb; ipdb.set_trace()

# data['transcript'] = transcript
# post_id = collection.insert_one(data).inserted_id

# print(transcript['text'])