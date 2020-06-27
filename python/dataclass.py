'''
Raymond Hettinger - Dataclasses: The code generator to end all code generators - PyCon 2018
https://www.youtube.com/watch?v=T-TwcmT6Rcw

https://docs.python.org/3/library/dataclasses.html
https://www.python.org/dev/peps/pep-0557/
'''

from dataclasses import dataclass, field
from typing import NamedTuple

@dataclass
class Color1:
    # dataclasses are mutable
    hue: int
    saturation: float
    lightness: float = field(default=0.5)  # another way to express default


class Color2(NamedTuple):
    # can be naturally unpacked
    hue: int
    saturation: float
    lightness: float = 0.5

