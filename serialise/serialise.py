'''
https://realpython.com/python-json/
'''

import pandas as pd
import json, pickle
from pprint import pprint


def serialise(obj):
    representation = {
        'class': obj.__class__.__name__,
        'args': [obj.values.tolist(), obj.index.tolist()],
    }
    return representation

def deserialise(representation):
    if representation['class'] == 'Series':
        return pd.Series(*representation['args'])


# ==============================================================================
import pdb; pdb.set_trace()

# this is a python specific object type; and won't serialise directly
obj = pd.Series([10, 11, 12], index=['2018-01-01', '2018-02-01', '2018-03-01'])

# =====================================
# serialise then convert to json
rr = serialise(obj)
pprint(rr)
jj1 = json.dumps(rr)

# or encode directly by passing the function
jj2 = json.dumps(obj=obj, default=serialise)

# pickle can serialise python objects directly
pk1 = pickle.dumps(rr)
pk2 = pickle.dumps(obj)
pprint(jj2)
print()

# =====================================
# take the json and deserialise it
rr = json.loads(jj1)
pprint(rr)
obj1 = deserialise(rr)

# or decode directly by passing the function
obj2 = json.loads(jj1, object_hook=deserialise)
print(obj2)

