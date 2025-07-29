# sonic-suite
sonic-suite is a comprehensive Python package for audio processing, offering a modular suite of tools for tasks such as text transcription, background noise reduction, multi-speaker detection, text-to-speech synthesis, emotion detection, language identification, audio effects, speaker identification, and music analysis. Built with scalability and ease of use in mind, sonic-suite is ideal for developers, researchers, and audio enthusiasts.

# Features
- **Text Transcription**: Convert speech to text using state-of-the-art models like Whisper.
- **Noise Reduction**: Remove background noise from audio for clearer sound.
- **Multi-Speaker Detection**: Identify and separate multiple speakers in audio (diarization).
- **Text-to-Speech (TTS)**: Synthesize natural-sounding speech from text.
- **Emotion Detection**: Analyze audio to detect speaker emotions (e.g., happy, sad).
- **Language Identification**: Detect the spoken language in audio files.
- **Audio Effects**: Apply creative effects like reverb, pitch shifting, or time stretching.
- **Speaker Identification**: Recognize specific speakers using voice embeddings.
- **Music Analysis**: Perform beat detection, tempo estimation, and instrument separation.
- **Pipeline Support**: Chain multiple processing steps for seamless workflows.

# Installation
Clone the Repository:
git clone https://github.com/<your-username>/SonicSuite.git
cd SonicSuite

Create a Virtual Environment (recommended):
python -m venv venv
source venv/bin/activate

Install Dependencies:
pip install -r requirements.txt

# Usage
sonic-suite provides a modular API and a pipeline for combining multiple audio processing tasks. Below are some examples:

Example 1: Transcribe Audio
```python
from sonicsuite.transcription import Transcriber

transcriber = Transcriber(model="openai/whisper-base")
text = transcriber.transcribe("data/sample1.wav")
print("Transcription:", text)
```
Example 2: Denoise and Transcribe
```python
from sonicsuite.core import AudioPipeline

pipeline = AudioPipeline(noise_reduction=True, transcription=True)
result = pipeline.process(input_path="data/sample1.wav")
print("Transcription:", result.transcription)
```
Example 3: Apply Audio Effects
```python
from sonicsuite.audio_effects import AudioEffects

effects = AudioEffects()
output = effects.apply_reverb(input_path="data/sample1.wav", output_path="output/reverbed.wav")
```
# Contributing
We welcome contributions! To contribute:

Fork the repository.
Create a new branch.
Make your changes and commit.
Push to your branch.
Open a pull request.

# Contact
For questions or feedback, open an issue on GitHub or reach out to the maintainers at rajkrishan13@gmail.com.
