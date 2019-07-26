from itertools import chain
from more_itertools import collapse

# ==============================================================================
# list of lists
lst = [['aaaa', 'b', 'c'], ['x', 'y', 'z']]

iterator = chain.from_iterable(lst)
flatten = list(iterator)

print(flatten)


# ==============================================================================
# list of mixed types
lst = ['aaaa', 'b', 'c', ['x', 'y', 'z']]

iterator = chain.from_iterable(lst)
flatten = list(iterator)

print(flatten)


# ==============================================================================
# flatten lists only in list of mixed types

def flatten_list_of_lists(lst):
    for element in lst:
        if isinstance(element, list):
            for i in element:
                yield i
        if isinstance(element, str):
            yield element


lst = ['aaaa', 'b', 'c', ['xxx', 'y', 'z']]
iterator = flatten_list_of_lists(lst)
flatten = list(iterator)

print(flatten)


# ==============================================================================
# list of lists; using sum

lst = [['aaaa', 'b', 'c'], ['x', 'y', 'z']]
flatten = sum(lst, [])

print(flatten)


# ==============================================================================
# flatten using more-itertools.collapse

lst = ['aaaa', 'b', 'c', ['xxx', 'y', 'z']]
x = [i for i in collapse(lst)]  # not sure why list constructor doesnt work
print(x)

import pdb; pdb.set_trace()
pass
