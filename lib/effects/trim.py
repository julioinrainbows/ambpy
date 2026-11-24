import numpy as np
from src.sample import Sample

def trim(sample: Sample,*,p1: float = 0.0, p2:float = 0.0)-> Sample:
    trimmedSample = sample.audio[round(p1):round(p2)]
    return Sample(trimmedSample,sample.sr)
