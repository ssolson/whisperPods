
import json
import os
from pydub import AudioSegment

audio_path = "C:\\Users\\fuck\\Desktop\\cwcode\\whisper.pods\\whisperPods\\python-backend\\podcast\\thedailygwei\\2023\\2023.04.26 EthStaker Knowledge Base, Market chat and more - The Daily Gwei Refuel #574 - Ethereum Updates.mp3"
file_path = "C:\\Users\\fuck\\Desktop\\cwcode\\whisper.pods\\whisperPods\\python-backend\\podcast\\thedailygwei\\2023\\output.json"
buffer_time = 100  # Buffer time in milliseconds

with open(file_path, 'r') as f:
    transcript_data = json.load(f)

segments = transcript_data["transcript"]["segments"]

# Load audio file
audio_file = AudioSegment.from_mp3(audio_path)

# Create a folder for the segments
audio_filename = os.path.splitext(os.path.basename(audio_path))[0]
segments_folder = f"audio_segments_{audio_filename}"
os.makedirs(segments_folder, exist_ok=True)

# Process segments
for index, segment in enumerate(segments):
    start_time = segment["start"]
    end_time = segment["end"]
    
    # Add buffer time to the start and end times
    start_time_with_buffer = max(0, start_time * 1000)
    end_time_with_buffer = end_time * 1000 + buffer_time
    
    # Extract audio segment
    audio_segment = audio_file[start_time_with_buffer:end_time_with_buffer]
    
    # Export audio segment to the folder
    audio_segment.export(f"{segments_folder}/output_segment_{index}.mp3", format="mp3")

print("Process Complete!")