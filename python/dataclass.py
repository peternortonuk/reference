'''
Raymond Hettinger - Dataclasses: The code generator to end all code generators - PyCon 2018
https://www.youtube.com/watch?v=T-TwcmT6Rcw

https://docs.python.org/3/library/dataclasses.html
https://www.python.org/dev/peps/pep-0557/


field specifier supports the following:
    default: Default value of the field
    default_factory: Function that returns the initial value of the field
    init: Use field in .__init__() method? (Default is True.)
    repr: Use field in repr of the object? (Default is True.)
    compare: Include the field in comparisons? (Default is True.)
    hash: Include the field when calculating hash()? (Default is to use the same as for compare.)
    metadata: A mapping with information about the field

'''

from dataclasses import dataclass, field, fields
from typing import NamedTuple

# ==============================================================
# compare dataclass and NamedTuple

@dataclass(frozen=True)
class Color1:
    # dataclasses are mutable unless frozen explicitly
    hue: int
    saturation: float
    lightness: float = field(default=0.5)  # another way to express default


class Color2(NamedTuple):
    # can be naturally unpacked
    hue: int
    saturation: float
    lightness: float = 0.5

# ==============================================================
# dataclasses support inheritance
# and metadata

@dataclass
class Position:
    name: str
    lon: float = field(metadata={'unit': 'degrees'})
    lat: float = field(metadata={'unit': 'degrees'})

@dataclass
class Capital(Position):
    country: str


x = Capital('Oslo', 10.8, 59.9, 'Norway')
print(x.name, x.lon, x.lat, '\n')

print(fields(x))
print(fields(Position)[2].name)
print(fields(Position)[2].metadata['unit'], '\n')


# ==============================================================
# the decorator writes the __init__
# but what if you want to append a task after initialisation

RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()

@dataclass(order=True)
class PlayingCard:
    sort_index: int = field(init=False, repr=False)
    rank: str
    suit: str

    def __post_init__(self):
        self.sort_index = (RANKS.index(self.rank) * len(SUITS)
                           + SUITS.index(self.suit))


pass