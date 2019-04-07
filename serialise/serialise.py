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

# this is python specific object type
obj = pd.Series([10, 11, 12], index=['2018-01-01', '2018-02-01', '2018-03-01'])

# serialise it and convert to json
rr = serialise(obj)
pprint(rr)
jj = json.dumps(rr)
pk1 = pickle.dumps(rr)
pk2 = pickle.dumps(obj)  # pickle can serialise python objects directly
pprint(jj)
print()

# take the json and deserialise
rr = json.loads(jj)
pprint(rr)
obj = deserialise(rr)
print(obj)

