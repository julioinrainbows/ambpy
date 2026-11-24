# WAV input/output: float64 arrays shaped (frames, channels), exported as PCM16.
from pathlib import Path

import numpy as np
import soundfile as sf

from src.sample import Sample

def load_wav(path: str | Path) -> Sample:
    # Reads all channels; mono audio also receives a channel dimension.
    audio, sr = sf.read(
        str(path),
        dtype="float64",
        always_2d=True
    )

    return Sample(
        audio = np.asarray(audio,dtype= np.float64),
        sr=int(sr)
    )

def save_wav(sample: Sample, path: str | Path) -> None:
    # Does not normalize: amplitudes outside the PCM range may be clipped.
    sf.write(
        str(path),
        sample.audio,
        sample.sr,
        format="WAV",
        subtype="PCM_16"
    )
