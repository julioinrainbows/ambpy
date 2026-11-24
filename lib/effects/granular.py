# Single-grain extraction using linear interpolation, without windowing or overlap-add.
from typing import Literal, overload

import numpy as np
from src.sample import Sample

#A simple granular modulator.
def simplegranular(
    sample: Sample,
    *,
    start:float,
    duration:float = 0.05,
    step: float = 1.0
) -> Sample:
    
    count = round(duration*sample.sr)

    begin = start*sample.sr
    end = duration*sample.sr

    positions = begin + np.arange(count)*step

    if count < 1:
        raise ValueError("Error: Invalid interval provided for the grain syntesis.")
    if start < 0:
        raise ValueError("Error: Invalid start index.")
    if positions[-1] > len(sample.audio) - 1:
        raise ValueError("Error: length of the grain must not exceed the end of the sample data.")
    if step == 0:
        raise ValueError("Error: step must be greater than 0.")


    # Selects only the neighboring samples needed to interpolate each channel.
    first = int(np.floor(positions[0]))
    last = min(
        int(np.ceil(positions[-1])) + 1,
        len(sample.audio),
    )

    t = np.arange(first, last)

    grain = np.column_stack([
        np.interp(positions,
                    t,
                    sample.audio[first:last, channel])
        for channel in range(sample.channels)
    ])

    return Sample(grain,sample.sr)

