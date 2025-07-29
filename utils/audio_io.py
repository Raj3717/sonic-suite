import soundfile as sf
import librosa
import numpy as np

def load_audio(file_path, target_sr=16000):
    """Load an audio file and resample to target sampling rate."""
    try:
        audio, sr = librosa.load(file_path, sr=target_sr, mono=True)
        return audio, sr
    except Exception as e:
        raise AudioProcessingError(f"Failed to load audio {file_path}: {str(e)}")

def save_audio(file_path, audio, sr):
    """Save audio to file."""
    try:
        sf.write(file_path, audio, sr)
    except Exception as e:
        raise AudioProcessingError(f"Failed to save audio {file_path}: {str(e)}")