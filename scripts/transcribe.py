import sys
import whisper
from pydub import AudioSegment
import tempfile
import os

def transcribe_audio(audio_path):
    """
    Transcribe audio file using local Whisper model
    """
    # Load Whisper model (options: tiny, base, small, medium, large)
    model = whisper.load_model("base")

    # Convert audio to WAV format if not already
    audio = AudioSegment.from_file(audio_path)
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_wav:
        audio.export(temp_wav.name, format="wav")

        # Transcribe
        result = model.transcribe(temp_wav.name)

    os.unlink(temp_wav.name)
    return result["text"]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python transcribe.py <audio_file_path>")
        sys.exit(1)
    
    transcript = transcribe_audio(sys.argv[1])
    print(transcript)

    # Save transcript
    os.makedirs("outputs", exist_ok=True)
    with open("outputs/transcript.txt", "w", encoding="utf-8") as f:
        f.write(transcript)
