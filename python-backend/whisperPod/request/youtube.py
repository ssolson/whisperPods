import requests
import json
import os
import time
import re
from youtube_transcript_api import YouTubeTranscriptApi


def _get_video_ids(api_key, playlist_id):
    url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails&playlistId={playlist_id}&maxResults=50&key={api_key}"
    video_ids = []
    while url:
        response = requests.get(url)
        data = response.json()
        if 'items' not in data:
            print(
                f"Error: Status code {response.status_code}, Response data: {data}")
            break
        video_ids.extend([item['contentDetails']['videoId']
                         for item in data['items']])
        url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails&playlistId={playlist_id}&maxResults=50&pageToken={data['nextPageToken']}&key={api_key}" if 'nextPageToken' in data else None
    return video_ids


def extract_timestamps_links(description):
    timestamp_pattern = r"(\d{1,2}:\d{2})\s(.+?)(?:\n|$)"
    timestamps = re.findall(timestamp_pattern, description)

    extracted_data = []
    if timestamps:
        for i, (timestamp, section_name) in enumerate(timestamps):
            next_line_start = description.find(
                timestamp) + len(timestamp) + len(section_name)
            next_line_end = description.find('\n', next_line_start)
            next_line = description[next_line_start:next_line_end].strip()

            section_link = None
            if next_line.startswith("http"):
                section_link = next_line

            extracted_data.append({
                "timestamp": timestamp,
                "name": section_name,
                "link": section_link
            })
    else:

        link_pattern = r"(https?://[^\s]+)"
        links = re.findall(link_pattern, description)

        for link in links:
            extracted_data.append({
                "timestamp": None,
                "name": None,
                "link": link
            })

    return extracted_data


def _extract_chapters(description):
    pattern = r'((?:\d{1,2}:)?\d{1,2}:\d{2})\s+(.+)'
    matches = re.findall(pattern, description)
    chapters = [{'timestamp': timestamp, 'title': title.strip()}
                for timestamp, title in matches]
    return chapters


def get_video_data(api_key, video_id):
    url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails&id={video_id}&key={api_key}"
    response = requests.get(url)
    data = response.json()
    if 'items' not in data or len(data['items']) == 0:
        return None

    video = data['items'][0]
    snippet = video['snippet']

    chapters = extract_timestamps_links(snippet['description'])
    transcript = get_video_transcript(video_id)

    return {
        'id': video['id'],
        'title': snippet['title'],
        'description': snippet['description'],
        'publishedAt': snippet['publishedAt'],
        'chapters': chapters,
        'transcript': transcript
    }


def get_video_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
    except:
        return None
    else:
        return transcript


def fetch_metadata(playlist_id, output_file, api_key):

    # Load last checkpoint if it exists
    if os.path.exists(output_file):
        with open(output_file, 'r') as f:
            video_data_list = json.load(f)
            existing_video_ids = {video_data['id']
                                  for video_data in video_data_list}
    else:
        video_data_list = []
        existing_video_ids = set()

    video_ids = _get_video_ids(api_key, playlist_id)
    missing_video_ids = [
        video_id for video_id in video_ids if video_id not in existing_video_ids]

    for i, video_id in enumerate(missing_video_ids):
        video_data = get_video_data(api_key, video_id)

        if not video_data:
            print(f"Error: Failed to fetch data for video {video_id}")
            continue

        video_data['timestamps_links'] = extract_timestamps_links(
            video_data['description'])
        video_data_list.append(video_data)

        # Save the results every 5 requests
        if i % 5 == 0:
            with open(output_file, 'w') as f:
                json.dump(video_data_list, f)

        # Wait for 1-2 seconds before making another request
        print(f"Fetched data for video {video_id} ({video_data['title']})")
        time.sleep(1.5)

    # Save the final results
    with open(output_file, 'w') as f:
        json.dump(video_data_list, f)

    print("Completed fetching video metadata.")
    return video_data_list
