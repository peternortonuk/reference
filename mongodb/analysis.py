import json
import os

# location of json file
rel_path = r'data'
file = r'crimes_street_dates.json'
pathfile = os.path.join(os.path.dirname(__file__), rel_path, file)

# load into variable
with open(pathfile) as json_data:
    data = json.load(json_data)

import pdb; pdb.set_trace()
pass





