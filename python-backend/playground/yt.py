import requests
import json
import os
import time
import re

api_key = 'AIzaSyAyDyGW67h0yohWU33Q9oiNOWDCYxIZ9zc'
playlist_id = 'PLIMWH1uKd3oE905uSUHdE5hd6e2UpADak'

output_file = 'thedailygwei_youtube_metadata.json'

def get_video_ids(api_key, playlist_id):
    url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails&playlistId={playlist_id}&maxResults=50&key={api_key}"
    video_ids = []
    while url:
        response = requests.get(url)
        data = response.json()
        if 'items' not in data:
            print(f"Error: Status code {response.status_code}, Response data: {data}")
            break
        video_ids.extend([item['contentDetails']['videoId'] for item in data['items']])
        url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails&playlistId={playlist_id}&maxResults=50&pageToken={data['nextPageToken']}&key={api_key}" if 'nextPageToken' in data else None
    return video_ids

def extract_chapters(description):
    pattern = r'((?:\d{1,2}:)?\d{1,2}:\d{2})\s+(.+)'
    matches = re.findall(pattern, description)
    chapters = [{'timestamp': timestamp, 'title': title.strip()} for timestamp, title in matches]
    return chapters

def get_video_data(api_key, video_id):
    url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails&id={video_id}&key={api_key}"
    response = requests.get(url)
    data = response.json()
    if 'items' not in data or len(data['items']) == 0:
        return None
    try: 
        video = data['items'][0]
    except:
        import ipdb; ipdb.set_trace()
    snippet = video['snippet']

    chapters = extract_chapters(snippet['description'])
    return {
        'id': video['id'],
        'title': snippet['title'],
        'description': snippet['description'],
        'publishedAt': snippet['publishedAt'],
        'chapters': chapters
    }

# Load last checkpoint if it exists
if os.path.exists(output_file):
    with open(output_file, 'r') as f:
        video_data_list = json.load(f)
        last_video_id = video_data_list[-1]['id']
else:
    video_data_list = []
    last_video_id = None

video_ids = get_video_ids(api_key, playlist_id)
start_index = video_ids.index(last_video_id) + 1 if last_video_id in video_ids else 0

for i, video_id in enumerate(video_ids[start_index:], start=start_index):
    video_data = get_video_data(api_key, video_id)

    if not video_data:
        print(f"Error: Failed to fetch data for video {video_id}")
        continue
    video_data_list.append(video_data)

    # Save the results every 5 requests
    with open(output_file, 'w') as f:
        json.dump(video_data_list, f)

    # Wait for 1-2 seconds before making another request
    print(f"Fetched data for video {video_id} ({video_data['title']})")
    time.sleep(1.5)

# Save the final results
with open(output_file, 'w') as f:
    json.dump(video_data_list, f)

print("Completed fetching video metadata.")