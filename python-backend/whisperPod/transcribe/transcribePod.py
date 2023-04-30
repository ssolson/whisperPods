import whisper


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
