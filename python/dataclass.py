'''
Raymond Hettinger - Dataclasses: The code generator to end all code generators - PyCon 2018
https://www.youtube.com/watch?v=T-TwcmT6Rcw
'''

from dataclasses import dataclass
from typing import NamedTuple

@dataclass
class Color1:
    # dataclasses are mutable
    hue: int
    saturation: float
    lightness: float = 0.5


class Color2(NamedTuple):
    # can be naturally unpacked
    hue: int
    saturation: float
    lightness: float = 0.5

