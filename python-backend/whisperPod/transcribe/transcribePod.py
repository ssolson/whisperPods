import whisper
from transformers import WhisperForConditionalGeneration, WhisperProcessor
import torchaudio

def whisper_podcast(filename, model="tiny.en"):
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
    return model.transcribe(filename, fp16=False, language='English', verbose=True)


def custom_whisper_podcast(filename, model_path):

    # Load the model and processor
    model = WhisperForConditionalGeneration.from_pretrained(model_path)
    processor = WhisperProcessor.from_pretrained(model_path)

    # Load the audio file
    waveform, rate = torchaudio.load(filename)

    # Convert the waveform into features using the processor
    features = processor(waveform, sampling_rate=rate, return_tensors="pt")
    
    # Apply the model
    model.to(features.input_values.device)  # Ensure the model is on the same device as the features
    with torch.no_grad():
        logits = model(input_values=features.input_values, attention_mask=features.attention_mask).logits

    # Retrieve the predicted token ids from the logits
    predicted_ids = torch.argmax(logits, dim=-1)

    # Convert the token ids back into text
    transcription = processor.decode(predicted_ids[0])

    return transcription
