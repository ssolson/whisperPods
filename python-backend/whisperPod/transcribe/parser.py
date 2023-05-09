import json
import os

file_path = "C:\\Users\\fuck\\Desktop\\cwcode\\whisper.pods\\whisperPods\\python-backend\\podcast\\thedailygwei\\2023\\output.json"

with open(file_path, 'r') as f:
    transcript_data = json.load(f)

segments = transcript_data["transcript"]["segments"]

parsed_transcript = {}

for segment in segments:
    start_time = segment["start"]
    end_time = segment["end"]
    text = segment["text"]
    formatted_entry = {
        "start": "{:.3f}".format(start_time),
        "end": "{:.3f}".format(end_time),
        "text": text
    }
    parsed_transcript[len(parsed_transcript)] = formatted_entry

output_filename = os.path.join(os.path.dirname(file_path), "trainingScript.json")
with open(output_filename, 'w') as outfile:
    json.dump(parsed_transcript, outfile)