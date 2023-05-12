import whisper
import timeit
import sys
import json
import os.path
import os

print("Running...")

def whisper_podcast(filename, model="large-v2", chunk_length_s=30, word_timestamps=True):
    """
    Transcribes an audio file using the Whisper library.

    Parameters
    ----------
    filename : str
        The path to the audio file to transcribe.
    model : str, optional
        The name of the Whisper model to use for transcription. Defaults to "tiny.en".

    Returns
    -------
    str
        The transcribed text of the audio file.

    Example
    -------
    >>> whisper_podcast("/path/to/audio/file.mp3")
    'The transcribed text of the audio file.'
    """
    model = whisper.load_model(model)
    result = model.transcribe(filename, fp16=False, language='English', verbose=True, word_timestamps=True)

    return result


if __name__ == "__main__":
    filename = "C:\\Users\\fuck\\Desktop\\cwcode\\whisper.pods\\whisperPods\\python-backend\\podcast\\thedailygwei\\2023\\2023.04.26 EthStaker Knowledge Base, Market chat and more - The Daily Gwei Refuel #574 - Ethereum Updates.mp3"
    model = "large-v2"
    

    start_time = timeit.default_timer()
    transcript = whisper_podcast(filename, model)
    execution_time = timeit.default_timer() - start_time

    result = {
        "execution_time": execution_time,
        "transcript": transcript
    }

    output_filename = os.path.join(os.path.dirname(filename), "output.json")
    with open(output_filename, 'w') as outfile:
        json.dump(result, outfile)

    print(f"JSON output saved to {output_filename}")