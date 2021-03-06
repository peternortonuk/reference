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
from typing import NamedTuple, List

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
# demonstrates the post_init; which runs after the auto __init__
# shows use of default factory function
# and an example of ordering

RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()

@dataclass(order=True)  # we can make comparisons between objects
class PlayingCard:
    # init=False means the field isnt initialised; it's done by the post_init below
    # repr=False means only rank and suit are shown
    sort_index: int = field(init=False, repr=False)
    rank: str
    suit: str

    def __post_init__(self):
        # calculate a scalar index for any card
        # and set the value of the field
        self.sort_index = RANKS.index(self.rank) * len(SUITS) + SUITS.index(self.suit)


def make_french_deck():
    return [PlayingCard(r, s) for s in SUITS for r in RANKS]

@dataclass
class Deck:
    cards: List[PlayingCard] = field(default_factory=make_french_deck)

y = Deck()
print(y)
print(y.cards[4])
print(y.cards[4].sort_index)

# because we set order=True and it actually uses the sort_index field
print(y.cards[4] > y.cards[5], '\n')

# compare with
print(sorted(make_french_deck()), '\n')


# ==============================================================
# inheritance with post_init

@dataclass
class Base:
    x: float
    y: float
    z: float = field(init=False)

    def __post_init__(self):
        print('Called!')
        self.z = self.x + self.y

@dataclass
class Child(Base):
    a: int

    def __post_init__(self):
        super().__post_init__()


obj = Child(a=0, x=1.5, y=2.5)
print(obj)

pass