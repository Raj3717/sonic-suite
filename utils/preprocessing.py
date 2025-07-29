def normalize_audio(audio):
    """Normalize audio amplitude to [-1, 1]."""
    return audio / np.max(np.abs(audio))

def trim_silence(audio, top_db=20):
    """Trim silence from audio using librosa."""
    return librosa.effects.trim(audio, top_db=top_db)[0]

def resample_audio(audio, orig_sr, target_sr):
    """Resample audio to target sampling rate."""
    return librosa.resample(audio, orig_sr=orig_sr, target_sr=target_sr)