from src.sample import Sample
from typing import Literal

import numpy as np

#Cubic Bezier fade with custom control points.
def b3fade(
    sample: Sample,
    interval: tuple[float, float],
    *,
    mode: Literal["in", "out"] = "in",
    inplace: bool = False,
    p1: float = 0.0,
    p2: float = 1.0,
) -> Sample | None:
    begin, end = interval
    duration = len(sample.audio) / sample.sr

    if not 0 <= begin < end <= duration:
        raise ValueError("Invalid interval")

    if not (np.isfinite(p1) and np.isfinite(p2)):
        raise ValueError("Control points must be finite")

    audio = sample.audio if inplace else sample.audio.copy()

    t = np.arange(len(audio)) / sample.sr

    u = np.clip((t - begin) / (end - begin), 0.0, 1.0)

    envelope = (
        3.0 * (1.0 - u) ** 2 * u * p1
        + 3.0 * (1.0 - u) * u**2 * p2
        + u**3
    )

    if mode == "out":
        envelope = 1.0 - envelope
    if audio.ndim == 1:
        audio *= envelope
    else:
        audio *= envelope[:, None]

    if inplace:
        return None

    return Sample(audio=audio, sr=sample.sr)


#Linear fade-in or fade-out.
def b2fade(
    sample: Sample,
    interval: tuple[float, float],
    *,
    mode: Literal["in", "out"] = "in",
    inplace: bool = False,
) -> Sample | None:
    begin, end = interval
    duration = len(sample.audio) / sample.sr

    if not 0 <= begin < end <= duration:
        raise ValueError("Invalid Interval")

    audio = sample.audio if inplace else sample.audio.copy()
    t = np.arange(len(audio)) / sample.sr

    levels = [0.0, 1.0] if mode == "in" else [1.0, 0.0]
    envelope = np.interp(t, [begin, end], levels)
    
    audio *= envelope[:, None]

    if inplace:
        return None

    return Sample(audio, sample.sr)
