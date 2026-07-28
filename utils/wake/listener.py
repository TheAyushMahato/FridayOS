import numpy as np
import sounddevice as sd

from .config import SAMPLE_RATE
from .config import CHUNK_SIZE


class WakeListener:

    def __init__(self):

        self.stream = sd.InputStream(
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype="int16",
            blocksize=CHUNK_SIZE
        )

    def start(self):

        self.stream.start()

    def stop(self):

        self.stream.stop()

    def read(self):

        audio, overflow = self.stream.read(CHUNK_SIZE)

        audio = audio.flatten()

        return np.array(audio, dtype=np.int16)