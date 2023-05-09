import json


def get_color(probability):
    if probability >= 0.9:
        return "\033[92m"  # Green
    elif probability >= 0.7:
        return "\033[93m"  # Yellow
    else:
        return "\033[91m"  # Red


def colored_segment(segment):
    words = segment["words"]
    colored_text = ""
    for word in words:
        color = get_color(word["probability"])
        colored_text += f"{color}{word['word']}\033[0m "
    return colored_text.strip()


file_path = "C:\\Users\\fuck\\Desktop\\cwcode\\whisper.pods\\whisperPods\\python-backend\\podcast\\thedailygwei\\2023\\output.json"

with open(file_path, 'r') as f:
    transcript_data = json.load(f)

segments = transcript_data["transcript"]["segments"]

parsed_transcript = ""

for segment in segments:
    start_time = segment["start"]
    end_time = segment["end"]
    text = colored_segment(segment)
    formatted_entry = f"[{start_time:.3f} --> {end_time:.3f}]  {text}\n"
    parsed_transcript += formatted_entry

print(parsed_transcript)


