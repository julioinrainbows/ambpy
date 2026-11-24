# Interactive demo: a granular layer with jitter and Hann windows, saved in output/.
from pathlib import Path
from src.sample import Sample
from lib.effects.granular import simplegranular
from lib.effects.merge import merge
from lib.audioio import load_wav, save_wav
import random
import numpy as np


# Example -- Generates a granular texture from a WAV source.

root = Path(__file__).resolve().parents[1]

inputSource = str(input("Please insert the sample source: "))

inputOutput = str(input("Please insert the sample output source: "))

# Input is relative to the project root; enter only the output WAV filename.
path = root / inputSource

sample = load_wav(path=path)
# Separate destination: grains always read from the original audio.
result = Sample(np.zeros_like(sample.audio), sample.sr)

#120 grains per second of audio -- Distorted harmony
for i in range(int(sample.duration*120)):
    jitter = 0.25
    start = i/120

    ran = random.uniform(-jitter,jitter) if (start-jitter > 0 ) else random.uniform(0,jitter)

    # start is the destination time; read is the source time shifted by jitter.
    read = start + ran

    if read + 0.4 > sample.duration:
        break
    
    grain = simplegranular(
        sample=sample,
        start=read,
        duration=0.4,
        step=0.5,
    )

    pos = round(start* sample.sr)

    end = pos + len(grain.audio)
    if end > len(result.audio):
        break
    # Smooths the edges and applies the same window to all channels.
    window = np.hanning(len(grain.audio))[:, None]

    result.audio[pos:end] += grain.audio * window


# Attenuates only when the peak exceeds 0.95; does not boost quiet signals.
peak = np.max(np.abs(result.audio))
if peak > 0.95:
    result.audio *= 0.95 / peak

output_dir = root / "output"
output_dir.mkdir(exist_ok=True)
save_wav(result, output_dir / inputOutput)