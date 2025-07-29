import matplotlib.pyplot as plt

def plot_waveform(audio, sr, title="Waveform", save_path=None):
    """Plot and optionally save audio waveform."""
    plt.figure(figsize=(10, 4))
    plt.plot(np.arange(len(audio)) / sr, audio)
    plt.title(title)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    if save_path:
        plt.savefig(save_path)
    plt.close()

def plot_spectrogram(audio, sr, title="Spectrogram", save_path=None):
    """Plot and optionally save Mel spectrogram."""
    S = librosa.feature.melspectrogram(y=audio, sr=sr)
    S_dB = librosa.power_to_db(S, ref=np.max)
    plt.figure(figsize=(10, 4))
    librosa.display.specshow(S_dB, sr=sr, x_axis="time", y_axis="mel")
    plt.colorbar(format="%+2.0f dB")
    plt.title(title)
    if save_path:
        plt.savefig(save_path)
    plt.close()