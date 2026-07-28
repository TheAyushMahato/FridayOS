import tempfile
import sounddevice as sd
import soundfile as sf

from faster_whisper import WhisperModel

print("Loading Whisper Model...")

model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)

print("Whisper Ready.")


def listen(duration=8):

    samplerate = 16000

    print("\n🎤 Listening...")

    audio = sd.rec(
        int(duration * samplerate),
        samplerate=samplerate,
        channels=1,
        dtype="float32"
    )

    sd.wait()

    with tempfile.NamedTemporaryFile(
        suffix=".wav",
        delete=False
    ) as file:

        sf.write(
            file.name,
            audio,
            samplerate
        )

        segments, _ = model.transcribe(
            file.name,
            beam_size=1,
            vad_filter=True,
            vad_parameters=dict(
                min_silence_duration_ms=500
            )
        )

    text = ""

    for segment in segments:
        text += segment.text + " "

    text = text.strip()

    print(f"\nYou said: {text}")

    return text