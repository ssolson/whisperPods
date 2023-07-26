import ipdb
import os
import re
import json
import pandas as pd
import whisperpod as wp
from dotenv import load_dotenv
from datetime import datetime


# Get the current working directory
current_directory = os.getcwd()


# Get the mogodb client, and set the database, and collection
client = wp.mongo.db.get_client()
database_name = "whisperPods"
collection_name = "thedailygwei"
db = client[database_name]
collection = db[collection_name]

# Get the libsyn podcast metadata
base_url = 'https://thedailygwei.libsyn.com/'
podcast_output_file = 'scripts/thedailygwei_metadata.json'
podcast_outfile_absolute_path = os.path.join(
    current_directory, podcast_output_file)
# Request Data and save to file
all_episodes = wp.request.metadata.scrape(
    base_url, podcast_outfile_absolute_path
)

# Load podcast metadata file
if os.path.exists(podcast_outfile_absolute_path):
    with open(podcast_outfile_absolute_path, 'r') as f:
        podcast_metadata = json.load(f)

# Get the youtube video metadata
load_dotenv()
api_key = os.getenv('YOUTUBE_API')
playlist_id = 'PLIMWH1uKd3oE905uSUHdE5hd6e2UpADak'
youtube_output_file = 'scripts/thedailygwei_youtube_metadata.json'
youtube_outfile_absolute_path = os.path.join(
    current_directory, youtube_output_file)

# Get the youtube video metadata
video_data_list = wp.request.youtube.fetch_metadata(
    playlist_id, youtube_outfile_absolute_path, api_key)

if os.path.exists(youtube_outfile_absolute_path):
    with open(youtube_outfile_absolute_path, 'r') as f:
        youtube_metadata = json.load(f)


# Iterate through each item in the metadata list
for item in youtube_metadata:
    # Extract timestamps and links
    timestamps_links = wp.request.youtube.extract_timestamps_links(
        item['description'])

    # Append the extracted data to the item
    item['chapters'] = timestamps_links
    try:
        del item['timestamps_links']
    except:
        pass

    # ipdb.set_trace()

# Write the updated metadata to the file
with open(youtube_outfile_absolute_path, 'w') as f:
    json.dump(youtube_metadata, f)


df_podcast = pd.DataFrame(podcast_metadata)
df_podcast['release_date'] = pd.to_datetime(
    df_podcast['release_date']
)

# Drop AMA and Drive Thru episodes
df_podcast = df_podcast[~df_podcast['item_title'].str.contains(
    "The Daily Gwei AMA Series")]
df_podcast = df_podcast[~df_podcast['item_title'].str.contains(
    "The Daily Gwei Drive Thru")]

# Episode Number from title
df_podcast['episode'] = df_podcast['item_title'].str.extract(
    r'#(\d+)(?:\s|\u200B|$)').astype('int')

# Episode Number from slug
df_podcast['slug_num'] = df_podcast['item_slug'].str.extract(
    'refuel-(\d+)').astype('int')
# NOTE 1: Libsyn is missing episode 20. 
# NOTE 2: Ep 26 Slug is Ep 20 but return 26;

# Youtube ID
pattern = r"(?<=youtu.be/)([^&#?/\s\"]*)"
df_podcast['youtube_id'] = df_podcast['item_body'].str.extract(pattern)

# Set the index to the episode number
df_podcast = df_podcast.set_index('episode')

# Create a dataframe from the youtube metadata
df_youtube = pd.DataFrame(youtube_metadata)

# Convert the publishedAt column to datetime
df_youtube['publishedAt'] = pd.to_datetime(
    df_youtube['publishedAt']
)

# Rename YouTube dataframe columns by adding 'yt_' prefix
df_youtube = df_youtube.add_prefix('yt_')

# Drop Yearly Recap
df_youtube = df_youtube[df_youtube['yt_id'] != 'eRaDjLsUDss']

# Episode Number
df_youtube['episode'] = df_youtube['yt_title'].str.extract(
    r'#(\d+)(?:[\s\u200B]*|$)'
).astype('int')


df_youtube = df_youtube.set_index('episode')

# Find missing episodes
all_episodes_set = set(range(1, 579))
podcast_set = set(df_podcast.index.values)
youtube_set = set(df_youtube.index.values)

podcast_missing = all_episodes_set - podcast_set
youtube_missing = all_episodes_set - youtube_set

for ep in youtube_missing:
    ep_id = df_podcast.loc[ep].youtube_id
    missing_ep = wp.request.youtube.get_video_data(api_key, ep_id)


# Combine the dataframes
combined_df = df_podcast.merge(
    df_youtube, left_index=True, right_index=True, suffixes=('_podcast', '_youtube'), how='outer')

# Delete redundant or unneeded columns
del combined_df['item_body_short']
del combined_df['item_body']
del combined_df['web_image_content_id']
del combined_df['player']
del combined_df['extra_content']
del combined_df['display_download_link']
del combined_df['premium_state']

# Replace NaT values with None
combined_df = combined_df.replace({pd.NaT: None})

# Create a new column 'episode' from the index
combined_df['index'] = combined_df.index

# Create a new column 'episode' from the index
combined_df['episode'] = combined_df.index

# Write combined_df to a JSON file
combined_df.to_json('scripts/combined_df.json',
                    orient='records', date_format='iso')

ipdb.set_trace()

# Delete all existing documents in the collection
collection.delete_many({})

# Convert the combined_df DataFrame to a list of dictionaries
data = combined_df.to_dict(orient='records')

# Insert the list of dictionaries into the MongoDB collection
collection.insert_many(data)


ipdb.set_trace()


# import ipdb; ipdb.set_trace()

# transcript = wp.transcribe.transcribePod.whisper_podcast(df.iloc[0].filename)

# data['transcript'] = transcript
# print(transcript['text'])
