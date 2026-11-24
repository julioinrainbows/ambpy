from src.sample import Sample
from lib.effects.fade import b3fade

import numpy as np


def concat(sample1:Sample,
           sample2:Sample,*,
           inplace=False,
           fade=False,
           fEnd: float =0.0,
           p1:float = 0.0,
           p2:float= 1.0) -> Sample | None:

    if sample1.channels != sample2.channels:
        raise ValueError("Both samples must have the same number of channels.")
    if len(sample1.audio) == 0 or  len(sample2.audio) == 0:
        raise ValueError("Neither sample can be empty.")


    c = Sample(np.concat((sample1.audio,sample2.audio),axis=0),sample1.sr)
    

    if fade:
        b3fade(c,(sample1.duration,sample1.duration+fEnd),inplace=True,p1=p1,p2=p2)
    if inplace:
        sample1.audio = c.audio
        return None

    return c
