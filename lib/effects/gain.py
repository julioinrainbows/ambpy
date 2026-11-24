import numpy as np
from src.sample import Sample


#A simple gain modulator.
def gain(sample: Sample ,gain: float,
    interval: tuple[float,float] | None = None ,
    *,inplace: bool = False) -> Sample | None:

    if interval is None:
        begin = 0
        end = len(sample.audio)
    else:
        begin = round(interval[0]*sample.sr)
        end = round(interval[1]*sample.sr)

    audio = sample.audio if inplace else sample.audio.copy()
    audio[begin:end] *= gain

    if inplace:
        return None

    return Sample(audio,sample.sr)
