import reference.pandas as pd
obj = pd.Series([10, 11, 12], index=['2018-01-01', '2018-02-01', '2018-03-01'])

def serialize(obj):
    representation = {
        'class': obj.__class__.name__,
        'args': [obj.values, obj.index],
    }

def deserialize(representation):
    if representation['class'] == 'pd.Series':
        return pd.Series(*representation['args'])