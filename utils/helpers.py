import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("SonicSuite")

class AudioProcessingError(Exception):
    """Custom exception for audio processing errors."""
    pass

def validate_audio_file(file_path):
    """Check if file is a valid audio format."""
    valid_extensions = {".wav", ".mp3", ".flac"}
    ext = os.path.splitext(file_path)[1].lower()
    if ext not in valid_extensions:
        raise AudioProcessingError(f"Unsupported file format: {ext}")

def seconds_to_hms(seconds):
    """Convert seconds to HH:MM:SS format."""
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    return f"{h:02d}:{m:02d}:{s:02d}"