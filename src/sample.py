# In-memory audio: a (frames, channels) array and a sample rate in Hz.
from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray

@dataclass(eq=False)
class Sample:
    audio: NDArray[np.float64]
    sr: int

    @property
    # Number of audio frames, regardless of the channel count.
    def frames(self):
        return self.audio.shape[0]

    @property
    # Number of channels; requires a two-dimensional audio array.
    def channels(self):
        return self.audio.shape[1]

    @property
    # Duration in seconds.
    def duration(self):
        return self.frames/self.sr
