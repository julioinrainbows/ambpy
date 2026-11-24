import numpy as np
from src.sample import Sample

#Merge two audio samples into one.

#def inplacemerge(sourceSample: Sample, secondarySample: Sample)

#Merge two sounds into one.
def merge(sample1: Sample, sample2: Sample, * , mix: np.float64 = np.float64(1.0)):

    audio = sample1.audio.copy()
    size = min(len(audio), len(sample2.audio))

    audio[:size] = (
        audio[:size] * mix
        + sample2.audio[:size] * (1 - mix)
    )

    return Sample(audio,sample1.sr)