


import os
import json

# Set the path to your audio sample folder
audio_folder = "C:\\Users\\fuck\\Desktop\\cwcode\\whisper.pods\\whisperPods\\python-backend\\whisperpod\\transcribe\\audio_segments_2023.04.26 EthStaker Knowledge Base, Market chat and more - The Daily Gwei Refuel #574 - Ethereum Updates"


# Load the transcript data from the JSON file
with open("transcript.json", "r") as f:
    transcript_data = json.load(f)

# Get the segments and the number of segments
segments = transcript_data["transcript"]["segments"]
num_segments = len(segments)

# Create an empty list to store the formatted entries
formatted_entries = []

# Loop through all the segments
for i, segment in enumerate(segments):
    text = segment["text"]
    audio_filename = f"output_segment_{i}.mp3"  # generate the audio filename for the segment
    audio_path = os.path.join(audio_folder, audio_filename)  # generate the audio path for the segment
    formatted_entry = {
        "text": text,
        "audio_path": audio_path
    }
    formatted_entries.append(formatted_entry)

# Write the formatted entries to a JSON file
with open("formatted_data.json", "w") as f:
    json.dump(formatted_entries, f)


# Create an empty dictionary to store the mappings
audio_and_text = {}

# Loop through all the audio files in the folder
for file in os.listdir(audio_folder):
    # Only consider files with .mp3 extension, change as per your requirements
    if file.endswith(".mp3"):
        # Extract the filename without extension
        file_name = os.path.splitext(file)[0]
        # Set the text string for the audio sample
        text_string = "Your text for file " + file_name
        # Add the mapping to the dictionary
        audio_to_text[file_name] = text_string

# Write the dictionary to a JSON file
with open("audio_to_text.json", "w") as outfile:
    json.dump(audio_to_text, outfile)