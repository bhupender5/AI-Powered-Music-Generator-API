import numpy as np
from scipy.io.wavfile import write
import random
import os

sample_rate = 44100

# Simple notes frequencies
NOTES = {
    "C": 261.63,
    "D": 293.66,
    "E": 329.63,
    "F": 349.23,
    "G": 392.00,
    "A": 440.00,
    "B": 493.88
}

def generate_music(prompt):

    duration = 0.5
    melody = random.choices(list(NOTES.values()), k=8)

    audio = []

    for freq in melody:
        t = np.linspace(0, duration, int(sample_rate * duration), False)
        tone = np.sin(freq * t * 2 * np.pi)
        audio.extend(tone)

    audio = np.array(audio)

    os.makedirs("output", exist_ok=True)

    file_path = "output/generated_music.wav"

    write(file_path, sample_rate, audio.astype(np.float32))

    return file_path